import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

BOOK = "My favorite book is '1984' by George Orwell."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Use /book")

async def book(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(BOOK)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("book", book))

app.run_polling()

