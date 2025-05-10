# buildboard_ui.py - A3H LLC BuildBoard Streamlit App (Cloud-Ready)

import streamlit as st
import pandas as pd
import pyodbc
import os
from datetime import datetime

# ✅ Direct import (relative path works on Streamlit Cloud)
from backend.utils.db_writer import add_project, add_log_entry

# ─────────────────────────────────────────────────────────────
# Database connection (for reads)
# ─────────────────────────────────────────────────────────────
def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'  # May need updating for hosted SQL or public preview
        'DATABASE=BuildBoard;'
        'Trusted_Connection=yes;'
    )

def load_projects():
    conn = get_connection()
    df = pd.read_sql("SELECT ProjectID, Title, Status FROM Projects ORDER BY CreatedAt DESC", conn)
    conn.close()
    return df

def get_project_overview(project_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC spA3H_GetProjectOverview ?", int(project_id))
    row = cursor.fetchone()
    conn.close()
    return row

# ─────────────────────────────────────────────────────────────
# Streamlit UI
# ─────────────────────────────────────────────────────────────

st.set_page_config(page_title="BuildBoard by A3H LLC", layout="centered")
st.title("🛠️ BuildBoard - A3H Project Tracker")

# Section: New Project Form
with st.expander("➕ Add New Project"):
    with st.form("new_project_form"):
        title = st.text_input("Project Title")
        niche = st.text_input("Niche (e.g., AI Tool, Medical, Retail)")
        description = st.text_area("Description")
        status = st.selectbox("Status", ["Idea", "In Progress", "Paused", "Done"], index=0)
        submitted = st.form_submit_button("Add Project")
        if submitted and title:
            add_project(title, niche, description, status)
            st.success("✅ Project added! Refresh the page to see it listed.")

# Section: Project Selector
st.subheader("📋 Select a Project to View")
projects = load_projects()

if not projects.empty:
    project_options = [f"{row.Title} (ID: {row.ProjectID})" for row in projects.itertuples()]
    selected_index = st.selectbox("Select a Project", range(len(project_options)), format_func=lambda x: project_options[x])
    selected_id = int(projects.iloc[selected_index]["ProjectID"])

    # Display Project Overview
    overview = get_project_overview(selected_id)
    st.markdown(f"### 🧾 {overview.Title}")
    st.write(f"**Status:** {overview.Status}")
    st.write(f"**Niche:** {overview.Niche}")
    st.write(f"**Created:** {overview.CreatedAt.strftime('%Y-%m-%d')}")
    st.write("**Latest Log Entry:**")
    st.info(overview.LatestLog or "No logs yet.")

    # Add new log
    st.markdown("### 📝 Add New Log Entry")
    log_text = st.text_area("Progress Note")
    if st.button("Save Log Entry"):
        if log_text.strip():
            add_log_entry(selected_id, log_text.strip())
            st.success("✅ Log entry saved. Refresh to see the update.")
        else:
            st.warning("Please enter some log text.")
else:
    st.info("No projects yet. Add one above to get started.")
