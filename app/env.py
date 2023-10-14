import os

DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "p4ssw0rd")
DB_HOST = os.getenv("DB_HOST", "172.0.4.2")
DB_PORT = os.getenv("DB_PORT", "3006")
DATABASE = os.getenv("DATABASE", "project-time-manager")

GIT = os.getenv("GIT_URL", "https://github.com")
PHPMYADMIN = os.getenv("PHPMYADMIN_URL", "https://www.phpmyadmin.net/")
