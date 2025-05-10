# db_writer.py – A3H LLC Database Writer for BuildBoard

import pyodbc

def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;DATABASE=BuildBoard;Trusted_Connection=yes;'
    )

def add_project(title, niche, description, status="Idea"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC spA3H_AddProject ?, ?, ?, ?", title, niche, description, status)
    conn.commit()
    conn.close()
    print(f"[✅] Added project: {title}")

def add_log_entry(project_id, entry):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC spA3H_AddLogEntry ?, ?", project_id, entry)
    conn.commit()
    conn.close()
    print(f"[📝] Added log to project ID {project_id}")

def update_status(project_id, new_status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC spA3H_UpdateProjectStatus ?, ?", project_id, new_status)
    conn.commit()
    conn.close()
    print(f"[🔄] Updated project ID {project_id} to status '{new_status}'")
