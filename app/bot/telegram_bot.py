from telegram.ext import Application

from app.bot.handlers import register_handlers
from app.core.config import TELEGRAM_TOKEN


def main():
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN is not set in .env")

    application = Application.builder().token(TELEGRAM_TOKEN).build()

    register_handlers(application)

    print("Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()
