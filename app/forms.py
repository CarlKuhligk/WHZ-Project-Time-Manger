from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    IntegerField,
    SelectField,
    TimeField,
)
from wtforms.validators import InputRequired


class NewActivityTypeForm(FlaskForm):
    name = StringField("Name:", validators=[InputRequired()])
    salary = IntegerField("Salary:", validators=[InputRequired()])
    submit = SubmitField("Submit")


class NewEmployeeForm(FlaskForm):
    name = StringField("Name:", validators=[InputRequired()])
    salary = IntegerField("Salary:", validators=[InputRequired()])
    department = SelectField("Department", validators=[InputRequired()])
    submit = SubmitField("Submit")


class NewCustomerForm(FlaskForm):
    name = StringField("Name:")
    submit = SubmitField("Submit")


class NewProjectForm(FlaskForm):
    name = StringField("Name:", validators=[InputRequired()])
    customer = SelectField("Customer:", validators=[InputRequired()])
    category = SelectField("Category:", validators=[InputRequired()])
    submit = SubmitField("Submit")


class NewActivityForm(FlaskForm):
    employee = SelectField("Employee:", validators=[InputRequired()])
    project = SelectField("Project:", validators=[InputRequired()])
    activity_type = SelectField("Type:", validators=[InputRequired()])
    category = SelectField("Category:", validators=[InputRequired()])
    start = TimeField("Start Time:", validators=[InputRequired()])
    end = TimeField("End Time:", validators=[InputRequired()])
    submit = SubmitField("Submit")
