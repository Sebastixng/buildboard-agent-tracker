# dashboard.py - BuildBoard Project Dashboard (A3H LLC)

import streamlit as st
import pandas as pd
import pyodbc
import sys
import os
import openai
from dotenv import load_dotenv

# ─────────────────────────────────────────────────────────────
# Load environment variables from .env
# ─────────────────────────────────────────────────────────────
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# ─────────────────────────────────────────────────────────────
# Add backend utils path and import DB functions
# ─────────────────────────────────────────────────────────────
sys.path.append(os.path.abspath("../../backend/utils"))
from db_writer import add_log_entry, update_status

# ─────────────────────────────────────────────────────────────
# Database read connection
# ─────────────────────────────────────────────────────────────
def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=BuildBoard;'
        'Trusted_Connection=yes;'
    )

def load_projects():
    conn = get_connection()
    df = pd.read_sql("SELECT ProjectID, Title, Niche, Status, CreatedAt FROM Projects", conn)
    conn.close()
    return df

def load_project_logs(project_id):
    conn = get_connection()
    df = pd.read_sql(f"""
        SELECT CreatedAt, Entry
        FROM Logs
        WHERE ProjectID = {int(project_id)}
        ORDER BY CreatedAt ASC
    """, conn)
    conn.close()
    return df

def summarize_logs(logs_text):
    prompt = f"""Summarize the following project progress notes for a product manager. Focus on what was built, what tools were used, and what decisions were made:\n\n{logs_text}"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message["content"].strip()

# ─────────────────────────────────────────────────────────────
# Streamlit UI
# ─────────────────────────────────────────────────────────────
st.set_page_config(page_title="BuildBoard Dashboard", layout="wide")
st.title("📊 BuildBoard Project Dashboard")

project_df = load_projects()
statuses = ["All"] + sorted(project_df["Status"].unique())
selected_status = st.selectbox("Filter by Status", statuses)

if selected_status != "All":
    project_df = project_df[project_df["Status"] == selected_status]

st.dataframe(project_df[["ProjectID", "Title", "Niche", "Status", "CreatedAt"]], use_container_width=True)

st.markdown("---")
selected_id = st.selectbox("📁 View Logs for Project ID", project_df["ProjectID"].tolist())

logs_df = load_project_logs(selected_id)

st.markdown(f"### 📝 Logs for Project ID {selected_id}")
for row in logs_df.itertuples():
    st.markdown(f"**{row.CreatedAt.strftime('%Y-%m-%d %H:%M')}**  \n{row.Entry}")
    st.markdown("---")

# ➕ Add new manual log entry
with st.expander("➕ Add New Log Entry"):
    log_note = st.text_area("Log Entry")
    if st.button("Add Log to Selected Project"):
        if log_note.strip():
            add_log_entry(int(selected_id), log_note.strip())
            st.success("✅ Log entry added.")
        else:
            st.warning("Please enter a log note.")

# 🧠 GPT-based log summarization
if st.button("🧠 Summarize Logs with GPT"):
    logs_text = "\n".join(
        f"{row.CreatedAt.strftime('%Y-%m-%d')}: {row.Entry}"
        for row in logs_df.itertuples()
    )
    summary = summarize_logs(logs_text)
    st.markdown("### 📋 GPT Summary")
    st.success(summary)

    if st.button("📌 Save This Summary to Logs"):
        add_log_entry(int(selected_id), summary)
        st.success("✅ Summary saved to logs.")
