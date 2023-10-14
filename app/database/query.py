from sqlalchemy import text

project_time_cost_group_by_department = text(
    """
        SELECT
            Project.name AS project_name,
            Employee.department,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) / 3600) AS time,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) * ActivityType.salary / 3600) AS cost
        FROM
            Project
        JOIN Activity ON Project.id = Activity.project_id
        JOIN Employee ON Activity.employee_id = Employee.id
        JOIN ActivityType ON Activity.type_id = ActivityType.id
        GROUP BY Project.name, Employee.department;
"""
)

project_time_cost_group_by_employee = text(
    """
        SELECT
            Project.name AS project_name,
            Employee.name AS employee_name,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) / 3600) AS time,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) * ActivityType.salary / 3600) AS cost
        FROM
            Project
        JOIN Activity ON Project.id = Activity.project_id
        JOIN Employee ON Activity.employee_id = Employee.id
        JOIN ActivityType ON Activity.type_id = ActivityType.id
        GROUP BY Project.name, Employee.name;
"""
)

total_time_cost_group_by_department = text(
    """
        SELECT
            Employee.department AS name,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) / 3600) AS time,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) * ActivityType.salary / 3600) AS cost
        FROM
            Activity
        JOIN Employee ON Activity.employee_id = Employee.id
        JOIN ActivityType ON Activity.type_id = ActivityType.id
        GROUP BY Employee.department;
"""
)

total_time_cost_group_by_employee = text(
    """
        SELECT
            Employee.name AS name,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) / 3600) AS time,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) * ActivityType.salary / 3600) AS cost
        FROM
            Activity
        JOIN Employee ON Activity.employee_id = Employee.id
        JOIN ActivityType ON Activity.type_id = ActivityType.id
        GROUP BY Employee.name;
"""
)

total_time_cost_group_by_category = text(
    """
        SELECT
            Activity.category,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) / 3600) AS required_time,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) * ActivityType.salary / 3600) AS costs
        FROM
            Activity
        JOIN ActivityType ON Activity.type_id = ActivityType.id
        GROUP BY
            Activity.category;
"""
)
