from telegram.ext import Application
from telegram.request import HTTPXRequest

from app.bot.handlers import register_handlers
from app.core.config import TELEGRAM_TOKEN


def main():
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN is not set in .env")

    request = HTTPXRequest(
        connect_timeout=30.0,
        read_timeout=30.0,
        write_timeout=30.0,
        pool_timeout=30.0,
    )

    application = (
        Application.builder()
        .token(TELEGRAM_TOKEN)
        .request(request)
        .build()
    )

    register_handlers(application)

    print("Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()