# BuildBoard - A3H LLC Project Tracker

BuildBoard is a modular, local-first project tracker designed for developers, startups, and builders to brainstorm, log, and summarize product development — powered by SQL Server, Streamlit, and optional GPT integration.

## 🚀 Features

* Add, edit, and track projects with status and niche
* Log all progress entries into SQL
* View full logs and summaries in a dashboard
* Use GPT to summarize project progress
* Works locally, no cloud dependency

## 📁 Folder Structure

```
BuildBoard/
├── backend/
│   └── utils/
│       └── db_writer.py
├── config/
│   └── .env
├── frontend/
│   └── streamlit/
│       ├── buildboard_ui.py
│       └── dashboard.py
├── launch_ui.bat
├── launch_dashboard.bat
```

## 🧠 Requirements

* Python 3.10+
* SQL Server (Local or Networked)
* Python packages:

  ```bash
  pip install streamlit pyodbc openai python-dotenv
  ```

## ⚙️ Setup

1. Clone this repo or unzip the folder
2. Update your `.env` file in `config/` with your OpenAI key
3. Run the SQL script in `backend/database/init.sql` to create your DB
4. Double-click `launch_ui.bat` and `launch_dashboard.bat` to start

## 🧠 GPT Summarization

* Enabled in `dashboard.py`
* Press "🧠 Summarize Logs" to create natural-language summaries

## ✅ Testing

Manually verify using:

* Add a project in `buildboard_ui.py`
* Log progress entries
* View and summarize in `dashboard.py`
* Check SQL tables `Projects` and `Logs`

## ☁️ Deploy Options

* [Streamlit Cloud](https://streamlit.io/cloud)
* [Hugging Face Spaces](https://huggingface.co/spaces)
* GitHub with Docker or Azure App Service

## 📝 License

MIT — Copyright © A3H LLC
