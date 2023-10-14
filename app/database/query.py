from sqlalchemy import text

project_time_cost_group_by_department = text(
    """
        SELECT
            Project.name AS project_name,
            Department.name,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) / 3600) AS time,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) * ActivityCategory.rate / 3600) AS cost
        FROM
            Project
        LEFT JOIN Activity ON Project.id = Activity.project_id
        LEFT JOIN Employee ON Activity.employee_id = Employee.id
        LEFT JOIN Department on Employee.department_id = Department.id
        LEFT JOIN ActivityType ON Activity.type_id = ActivityType.id
        LEFT JOIN ActivityCategory ON ActivityType.activity_category_id = ActivityCategory.id
        GROUP BY Project.name, Department.name;
"""
)

project_time_cost_group_by_employee = text(
    """
        SELECT
            Project.name AS project_name,
            Employee.name AS employee_name,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) / 3600) AS time,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) * ActivityCategory.rate / 3600) AS cost,
            ActivityType.name AS activity_type
        FROM
            Project
        LEFT JOIN Activity ON Project.id = Activity.project_id
        LEFT JOIN Employee ON Activity.employee_id = Employee.id
        LEFT JOIN ActivityType ON Activity.type_id = ActivityType.id
        LEFT JOIN ActivityCategory ON ActivityType.activity_category_id = ActivityCategory.id
        GROUP BY Project.name, Employee.name, ActivityType.name;
"""
)

total_time_cost_group_by_department = text(
    """
        SELECT
            Department.name AS name,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) / 3600) AS time,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) * ActivityCategory.rate / 3600) AS cost
        FROM
            Activity
        LEFT JOIN Employee ON Activity.employee_id = Employee.id
        LEFT JOIN Department on Employee.department_id = Department.id
        LEFT JOIN ActivityType ON Activity.type_id = ActivityType.id
        LEFT JOIN ActivityCategory ON ActivityType.activity_category_id = ActivityCategory.id
        GROUP BY Department.name;
"""
)

total_time_cost_group_by_employee = text(
    """
        SELECT
            Employee.name AS name,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) / 3600) AS time,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) * ActivityCategory.rate / 3600) AS cost
        FROM
            Activity
        LEFT JOIN Employee ON Activity.employee_id = Employee.id
        LEFT JOIN ActivityType ON Activity.type_id = ActivityType.id
        LEFT JOIN ActivityCategory ON ActivityType.activity_category_id = ActivityCategory.id
        GROUP BY Employee.name;
"""
)

total_time_cost_group_by_category = text(
    """
        SELECT
            ActivityType.name,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) / 3600) AS time,
            SUM(TIMESTAMPDIFF(SECOND, Activity.start_time, Activity.end_time) * ActivityCategory.rate / 3600) AS costs
        FROM
            Activity
        LEFT JOIN ActivityType ON Activity.type_id = ActivityType.id
        LEFT JOIN ActivityCategory ON ActivityType.activity_category_id = ActivityCategory.id
        GROUP BY
            ActivityType.name;
"""
)
