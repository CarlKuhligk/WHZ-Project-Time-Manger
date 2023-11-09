import pandas as pd
from database.session import db
import plotly.graph_objects as go
import json
import plotly
import database.query as querry

custom_colormap = [
    "#7EA9E0",
    "#D87EE0",
    "#7EE0BB",
    "#E0BE7E",
    "#ABE07E",
    "#B87BE0",
    "#7BC7E0",
    "#E07C7C",
    "#D3E07B",
    "#E04F7B",
    #
    "#0B6DE0",
    "#E02816",
    "#E09816",
    "#00DBE0",
    "#0BC06C",
    "#E00BB3",
    "#8F01E0",
    "#E03400",
    "#3FE016",
    "#BAE00B",
    #
    "#93FF01",
    "#01FFB0",
    "#C800FE",
    "#FF5301",
    "#2F00FF",
    "#FF0400",
    "#FFC000",
    "#FF01DB",
    "#FFFF00",
    "#33FF57",
]


def create_dataframe(data, columns, dtypes):
    df = pd.DataFrame(data, columns=columns)
    df = df.astype({column: dtype for column, dtype in zip(columns, dtypes)})
    return df


def get_total_time_cost_group_by_department_df():
    total_time_cost_group_by_department = db.session.execute(
        querry.total_time_cost_group_by_department
    ).all()

    return create_dataframe(
        total_time_cost_group_by_department,
        ["Department", "Time", "Amount"],
        [str, float, float],
    )


def get_total_time_cost_group_by_employee_df():
    total_time_cost_group_by_employee = db.session.execute(
        querry.total_time_cost_group_by_employee
    ).all()
    return create_dataframe(
        total_time_cost_group_by_employee,
        ["Employee", "Time", "Amount"],
        [str, float, float],
    )


def get_total_time_cost_group_by_category_df():
    total_time_cost_group_by_category = db.session.execute(
        querry.total_time_cost_group_by_category
    ).all()

    return create_dataframe(
        total_time_cost_group_by_category,
        ["Category", "Time", "Amount"],
        [str, float, float],
    )


def get_summary_chats_as_html():
    department_df = get_total_time_cost_group_by_department_df()
    employee_df = get_total_time_cost_group_by_employee_df()
    category_df = get_total_time_cost_group_by_category_df()

    fig_1 = go.Figure()
    fig_1.add_trace(
        go.Pie(
            labels=department_df["Department"],
            values=department_df["Amount"],
            name="Department",
            textinfo="percent+label",
            customdata=department_df["Time"],
            marker=dict(colors=custom_colormap[:10]),
        )
    )
    fig_1.add_annotation(
        dict(text="Departments", x=0.5, y=1.3, font_size=20, showarrow=False),
    )

    fig_2 = go.Figure()
    fig_2.add_trace(
        go.Pie(
            labels=employee_df["Employee"],
            values=employee_df["Amount"],
            name="Employee",
            textinfo="percent+label",
            customdata=employee_df["Time"],
            marker=dict(colors=custom_colormap[10:20]),
        )
    )
    fig_2.add_annotation(
        dict(text="Employes", x=0.5, y=1.3, font_size=20, showarrow=False)
    )

    fig_3 = go.Figure()
    fig_3.add_trace(
        go.Pie(
            labels=category_df["Category"],
            values=category_df["Amount"],
            name="Category",
            textinfo="percent+label",
            customdata=category_df["Time"],
            marker=dict(colors=custom_colormap[20:]),
        )
    )
    fig_3.add_annotation(
        dict(text="Categories", x=0.5, y=1.3, font_size=20, showarrow=False)
    )

    fig_1.update_traces(
        hovertemplate="%{label}: %{percent} <br> Amount: %{value:.2f} € <br> Time: %{customdata:.2f} h",
    )
    fig_2.update_traces(
        hovertemplate="%{label}: %{percent} <br> Amount: %{value:.2f} € <br> Time: %{customdata:.2f} h",
    )
    fig_3.update_traces(
        hovertemplate="%{label}: %{percent} <br> Amount: %{value:.2f} € <br> Time: %{customdata:.2f} h",
    )

    return [
        json.dumps(fig_1, cls=plotly.utils.PlotlyJSONEncoder),
        json.dumps(fig_2, cls=plotly.utils.PlotlyJSONEncoder),
        json.dumps(fig_3, cls=plotly.utils.PlotlyJSONEncoder),
    ]


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
    columns = ["Project", "Employee", "Time", "Amount", "Type"]
    return create_dataframe(
        project_time_cost_group_by_employee,
        columns,
        [str, str, float, float, str],
    )


def format_number(n):
    if n < 1000:
        return f"{n:.2f}"
    elif n < 1_000_000:
        return f"{n / 1_000:.2f}k"
    elif n < 1_000_000_000:
        return f"{n / 1_000_000:.2f}M"
    else:
        return f"{n / 1_000_000_000:.2f}B"


def get_project_chats_as_html():
    department_df = get_project_time_cost_group_by_department_df()
    department_grouped = department_df.groupby("Project")
    employee_dt = get_project_time_cost_group_by_employee_df()
    employee_grouped = employee_dt.groupby("Project")

    project_names = list(department_grouped.groups.keys())
    charts = []

    for project_name in project_names:
        department_data = department_grouped.get_group(project_name)
        employee_data = employee_grouped.get_group(project_name)

        department_data = department_data.dropna()
        if department_data.empty:
            continue

        fig_1 = go.Figure()
        fig_1.add_trace(
            go.Pie(
                labels=department_data["Department"],
                values=department_data["Amount"],
                name="Department",
                textinfo="percent+label",
                customdata=department_data["Time"],
                hole=0.3,
                marker=dict(colors=custom_colormap[:10]),
            )
        )
        fig_1.update_xaxes(title_text="Departments")
        fig_1.update_traces(
            hovertemplate="%{label}<br>Amount: %{value:.2f}: €<br>Time: %{customdata:.2f} h"
        )

        fig_1.add_annotation(
            dict(
                text=f"""{format_number(sum(department_data["Amount"]))} €""",
                x=0.5,
                y=0.5,
                font_size=18,
                showarrow=False,
            )
        )

        fig_1.add_annotation(
            dict(
                text=f"Grouped by Department",
                x=0.5,
                y=1.2,
                font_size=20,
                showarrow=False,
            )
        )

        employee_grouped_types = employee_data.groupby("Type")
        activity_type_names = list(employee_grouped_types.groups.keys())

        fig_2 = go.Figure()

        category_colors = custom_colormap[20:]

        for i, activity_type_name in enumerate(activity_type_names):
            chart_data = employee_grouped_types.get_group(activity_type_name)
            color = category_colors[i]

            fig_2.add_trace(
                go.Bar(
                    name=activity_type_name,
                    x=chart_data["Employee"].values,
                    y=chart_data["Amount"].values,
                    customdata=chart_data["Time"],
                    marker_color=color,
                )
            )

        fig_2.update_xaxes(title_text="Employee")
        fig_2.update_yaxes(title_text="Service Fee")
        fig_2.update_traces(
            hovertemplate="Amount: %{value:.2f}: €<br>Time: %{customdata:.2f} h",
        )
        fig_2.update_layout(barmode="stack")

        fig_2.add_annotation(
            dict(
                text="Grouped by Employee",
                xref="paper",
                yref="paper",
                x=0.5,
                y=1.2,
                font_size=20,
                showarrow=False,
            )
        )

        charts.append(
            [
                project_name,
                json.dumps(fig_1, cls=plotly.utils.PlotlyJSONEncoder),
                json.dumps(fig_2, cls=plotly.utils.PlotlyJSONEncoder),
            ]
        )
    return charts
