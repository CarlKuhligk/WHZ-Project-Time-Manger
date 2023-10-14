from flask import Flask, render_template, flash, globals
from database.session import db
from typing import TypeVar
from datetime import datetime, timedelta

from chart_builder import get_summary_chats_as_html, get_project_chats_as_html
import forms
import database.models as models
import env

app = Flask(__name__)
app.config["SECRET_KEY"] = "r8qXr7igeahMWRCNJnR7"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"mariadb+mariadbconnector://{env.DB_USER}:{env.DB_PASSWORD}@{env.DB_HOST}:{env.DB_PORT}/{env.DATABASE}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["GIT"] = env.GIT
app.config["PHPMYADMIN"] = env.PHPMYADMIN
db.init_app(app)

with app.app_context():
    db.create_all()

R = TypeVar


def add_object(type, **kwargs):
    try:
        new_object = type(**kwargs)
        db.session.add(new_object)
        db.session.commit()
    except Exception as e:
        flash({"title": "Error!", "details": e, "category": "danger"})
    else:
        flash({"title": "Succsess!", "details": "", "category": "success"})


@app.route("/")
def index():
    return render_template(
        "index.html",
        summary_chart=get_summary_chats_as_html(),
        project_chats=get_project_chats_as_html(),
    )


@app.route("/create_activity_type", methods=["GET", "POST"])
def add_activity_type():
    form: forms.NewActivityTypeForm = forms.NewActivityTypeForm()
    if form.is_submitted():
        add_object(models.ActivityType, name=form.name.data, salary=form.salary.data)
    return render_template("add_activity_type.html", form=form)


@app.route("/create_employee", methods=["GET", "POST"])
def add_employee():
    form: forms.NewEmployeeForm = forms.NewEmployeeForm()
    form.department.choices = [department.name for department in models.Department]
    if form.is_submitted():
        add_object(
            models.Employee,
            name=form.name.data,
            salary=form.salary.data,
            department=form.department.data,
        )
    return render_template("add_employee.html", form=form)


@app.route("/create_customer", methods=["GET", "POST"])
def add_customer():
    form: forms.NewCustomerForm = forms.NewCustomerForm()
    if form.is_submitted():
        add_object(
            models.Customer,
            name=form.name.data,
        )
    return render_template("add_customer.html", form=form)


@app.route("/create_project", methods=["GET", "POST"])
def add_project():
    form: forms.NewProjectForm = forms.NewProjectForm()
    customers = db.session.query(models.Customer).all()
    form.customer.choices = [customer.name for customer in customers]
    form.category.choices = [category.name for category in models.ProjectCategory]
    if form.is_submitted():
        add_object(
            models.Project,
            name=form.name.data,
            category=form.category.data,
            customer_id=[
                customer.id
                for customer in customers
                if customer.name == form.customer.data
            ][0],
        )
    return render_template("add_project.html", form=form)


@app.route("/create_activity", methods=["GET", "POST"])
def add_activity():
    employes = db.session.query(models.Employee).all()
    projects = db.session.query(models.Project).all()
    activity_types = db.session.query(models.ActivityType).all()

    form: forms.NewActivityForm = forms.NewActivityForm()
    form.employee.choices = [employee.name for employee in employes]
    form.project.choices = [project.name for project in projects]
    form.activity_type.choices = [
        f"{activity_type.name} ({activity_type.salary}€/h)"
        for activity_type in activity_types
    ]
    form.category.choices = [
        activity_category.name for activity_category in models.ActivityCategory
    ]
    if form.is_submitted():
        current_date = datetime.now().date()
        start_time = datetime.combine(current_date, form.start.data)
        end_time = datetime.combine(current_date, form.end.data)
        if form.end.data < form.start.data:
            end_time += timedelta(days=1)

        add_object(
            models.Activity,
            employee_id=[
                employee.id
                for employee in employes
                if employee.name == form.employee.data
            ][0],
            project_id=[
                project.id for project in projects if project.name == form.project.data
            ][0],
            category=form.category.data,
            type_id=[
                activity_type.id
                for activity_type in activity_types
                if activity_type.name == form.activity_type.data.split(" (")[0]
            ][0],
            start_time=start_time,
            end_time=end_time,
        )

    return render_template("add_activity.html", form=form)


if __name__ == "__main__":
    print("stating server")
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
