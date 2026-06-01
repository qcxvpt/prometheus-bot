# Prometheus Bot 🤖

Telegram bot that returns information about a favorite book and demonstrates CI/CD pipeline with Docker and GitHub Actions.

---

## 📌 Features

- Telegram bot using Python (python-telegram-bot)
- `/start` command — greeting message
- `/book` command — returns favorite book info
- Dockerized application
- CI/CD pipeline with GitHub Actions
- Automated Docker build and push to Docker Hub

---

## 📚 Bot Functionality

The bot responds to:

### /start

### /book

---

## 🚀 Run locally

### 1. Clone repository
```bash
git clone https://github.com/qcxvpt/prometheus-bot.git
cd prometheus-bot
pip install -r requirements.txt
export BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
python main.py
docker build -t prometheus-bot .
docker run -e BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN" prometheus-bot
docker run -e BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN" prometheus-bot
