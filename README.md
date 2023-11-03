## Project Time Manager

The goal is to create a database for documenting the time spent on projects.
➔ Who did what, when, and to what extent for which project?

Key Features:

- Recording data on which employee was involved in which project and for how long.
- Assigning specific projects to project categories (e.g., Training Project, Database Project, Research Project, etc.).
- Associating projects with specific customers.
- Categorizing individual activities (e.g., Customer Consultation, Software Development, Software Testing, Documentation) with respective hourly rates (e.g., simple → €50/h, medium → €75/h, complex → €100/h, etc.).
- Assigning each employee to a department.
- Associating a fixed salary with each employee.

The model should support the following analyses:

- Total time spent on each project.
- Total project costs.
- Percentage contribution of each department to a project.


## Solution
It is necessary to document some assumptions to build a satisfying solution.

1. This model has been designed to fulfill specific requirements rather than being developed for real-world use cases.
2. Information can only be added, not modified.
3. There will be no database migration

### Entity Relationship Diagram
<br>

![SVG-Bild](https://raw.githubusercontent.com/CarlKuhligk/WHZ-Project-Time-Manger/main/doc/ERD%20-%20Simple.drawio.svg)

#### phpMyAdmin View
![SVG-Bild](https://raw.githubusercontent.com/CarlKuhligk/WHZ-Project-Time-Manger/main/doc/tAXTvzDYnj.png)

#### Chen Notation

![SVG-Bild](https://raw.githubusercontent.com/CarlKuhligk/WHZ-Project-Time-Manger/main/doc/ERD%20Chen.drawio.svg)

### Dataprocessing
An interface allows the user to create new records.
The interface supports the user by displaying already existing information.
Errors during creation are displayed in the interface.

The project analysis is performed with simple sql commands. [Here you can see these commands](https://github.com/CarlKuhligk/WHZ-Project-Time-Manger/blob/main/app/database/query.py).

The webinterface is created with flask. The diagrams are created with pltoly. The python database interaction is realized with sqlalchemy. phpMyAdmin is used to see what is going on in the database.

![web ui](https://raw.githubusercontent.com/CarlKuhligk/WHZ-Project-Time-Manger/main/doc/gdjIC7iQB7.png)

### Demo

[Interface](https://whz-db-project.kuhligk.de/)


[phpMyAdmin](https://whz-db-inspect.kuhligk.de/) (read only)
- host: mariadb
- user: spectator
- no password