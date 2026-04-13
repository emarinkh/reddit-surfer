reddit-surfer

an AI-powered social media intelligence tool that automatically monitors Reddit for trending discussions, analyzes them using a local AI, and queues content for LinkedIn publishing -all running locally on your machine with zero cloud costs. Scrapes live posts from multiple subreddits using Reddit's public API Analyzes trends using a locally hosted LLM (Llama 3.2 via Ollama) Stores all data in a SQLite database with two tables — a Trend Buffer and a Scheduling Queue Displays results on a Flask web dashboard Runs automatically daily via a cron job

Tech stack: Python, SQLite, Flask, Ollama, Llama 3.2, HTML/Jinja2, Linux cron
