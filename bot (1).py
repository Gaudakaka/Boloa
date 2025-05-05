# bot.py
# შენს ბოტის ლოგიკა ჩასვი აქ
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("გამარჯობა! ბოტი მუშაობს.")

if __name__ == "__main__":
    app = ApplicationBuilder().token("TOKEN_HERE").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
