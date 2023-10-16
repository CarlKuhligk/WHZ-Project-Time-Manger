import pandas as pd
from database.session import db
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import database.query as querry


def create_dataframe(data, columns, dtypes):
    df = pd.DataFrame(data, columns=columns)
    df = df.astype({column: dtype for column, dtype in zip(columns, dtypes)})
    return df


def get_total_time_cost_group_by_department_df():
    total_time_cost_group_by_department = db.session.execute(
        querry.total_time_cost_group_by_department
    )
    columns = ["Department", "Time", "Amount"]
    return create_dataframe(
        total_time_cost_group_by_department,
        columns,
        [str, float, float],
    )


def get_total_time_cost_group_by_employee_df():
    total_time_cost_group_by_employee = db.session.execute(
        querry.total_time_cost_group_by_employee
    )
    columns = ["Employee", "Time", "Amount"]
    return create_dataframe(
        total_time_cost_group_by_employee,
        columns,
        [str, float, float],
    )


def get_total_time_cost_group_by_category_df():
    total_time_cost_group_by_category = db.session.execute(
        querry.total_time_cost_group_by_category
    )
    columns = ["Category", "Time", "Amount"]
    return create_dataframe(
        total_time_cost_group_by_category,
        columns,
        [str, float, float],
    )


def get_summary_chats_as_html():
    department_df = get_total_time_cost_group_by_department_df()
    employee_df = get_total_time_cost_group_by_employee_df()
    category_df = get_total_time_cost_group_by_category_df()

    fig = make_subplots(
        rows=1,
        cols=3,
        specs=[[{"type": "domain"}, {"type": "domain"}, {"type": "domain"}]],
    )
    fig.add_trace(
        go.Pie(
            labels=department_df["Department"],
            values=department_df["Amount"],
            name="Department",
            customdata=department_df["Time"],
        ),
        1,
        1,
    )
    fig.add_trace(
        go.Pie(
            labels=employee_df["Employee"],
            values=employee_df["Amount"],
            name="Employee",
            customdata=department_df["Time"],
        ),
        1,
        2,
    )
    fig.add_trace(
        go.Pie(
            labels=category_df["Category"],
            values=category_df["Amount"],
            name="Category",
            customdata=department_df["Time"],
        ),
        1,
        3,
    )
    fig.update_traces(
        hovertemplate="%{label}: %{percent} <br> Amount: %{value:.2f} € <br> Time: %{customdata:.2f} h",
    )
    fig.update_layout(
        title_text="",
        annotations=[
            dict(text="Departments", x=0.075, y=1.3, font_size=20, showarrow=False),
            dict(text="Employes", x=0.5, y=1.3, font_size=20, showarrow=False),
            dict(text="Categories", x=0.9, y=1.3, font_size=20, showarrow=False),
        ],
    )

    return fig.to_html(full_html=False)


def get_project_time_cost_group_by_department_df():
    project_time_group_by_department = db.session.execute(
        querry.project_time_cost_group_by_department
    )
    columns = ["Project", "Department", "Time", "Amount"]
    return create_dataframe(
        project_time_group_by_department,
        columns,
        [str, str, float, float],
    )


def get_project_time_cost_group_by_employee_df():
    project_time_cost_group_by_employee = db.session.execute(
        querry.project_time_cost_group_by_employee
    )
    columns = ["Project", "Employee", "Time", "Amount"]
    return create_dataframe(
        project_time_cost_group_by_employee,
        columns,
        [str, str, float, float],
    )


def get_project_chats_as_html():
    department_df = get_project_time_cost_group_by_department_df()
    department_grouped = department_df.groupby("Project")
    employee_dt = get_project_time_cost_group_by_employee_df()
    employee_grouped = employee_dt.groupby("Project")
    project_names = list(department_grouped.groups.keys())
    charts = []

    for project in project_names:
        department_data = department_grouped.get_group(project)
        employee_data = employee_grouped.get_group(project)

        fig = make_subplots(
            rows=1,
            cols=2,
            specs=[[{"type": "domain"}, {"type": "domain"}]],
        )
        fig.add_trace(
            go.Pie(
                labels=department_data["Department"],
                values=department_data["Amount"],
                name="Department",
                customdata=department_data["Time"],
            ),
            1,
            1,
        )
        fig.add_trace(
            go.Pie(
                labels=employee_data["Employee"],
                values=employee_data["Amount"],
                name="Employee",
                customdata=employee_data["Time"],
            ),
            1,
            2,
        )
        fig.update_traces(
            hovertemplate="%{label}: %{percent} <br> Amount: %{value:.2f}: € <br> Time: %{customdata:.2f} h",
        )
        charts.append([project, fig.to_html(full_html=False)])
    return charts
