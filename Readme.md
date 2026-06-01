# Telegram Bot

## Run locally
pip install -r requirements.txt
python bot.py

## Run with Docker
docker build -t prometheus-bot .
docker run -e BOT_TOKEN=YOUR_TOKEN prometheus-bot