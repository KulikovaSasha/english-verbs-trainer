from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, MessageHandler, filters

from app.crud.user import get_or_create_user
from app.database.db import SessionLocal
from app.services.trainer import check_training_answer, get_training_task

from app.services.stats import get_user_stats
from app.services.progress import get_user_level_progress

active_tasks = {}


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I am your English Verbs Trainer bot.\n\n"
        "Commands:\n"
        "/start - start the bot\n"
        "/help - show help\n"
        "/train - start training"
        "/score - show your score"
        "/progress - show level progress"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Use these commands:\n"
        "/start - start the bot\n"
        "/help - show help\n"
        "/train - get a training task\n\n"
        "Answer format:\n"
        "went, gone"
        "/score - show your score"
        "/progress - show level progress"
    )


async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_user = update.effective_user
    db = SessionLocal()

    try:
        user = get_or_create_user(
            db=db,
            telegram_id=str(telegram_user.id),
            username=telegram_user.username,
        )

        stats = get_user_stats(db, user.id)

        message = (
            f"📊 Your statistics\n\n"
            f"Total answers: {stats['total_answers']}\n"
            f"Correct answers: {stats['correct_answers']}\n"
            f"Wrong answers: {stats['wrong_answers']}\n"
            f"Accuracy: {stats['accuracy']}%\n"
        )

        if stats["hard_verbs"]:
            message += "\nHard verbs:\n"
            for verb in stats["hard_verbs"]:
                message += (
                    f"- {verb['base_form']} ({verb['translation']}) — "
                    f"correct: {verb['correct_count']}, wrong: {verb['wrong_count']}\n"
                )

        await update.message.reply_text(message)

    finally:
        db.close()

async def score_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_user = update.effective_user
    db = SessionLocal()

    try:
        user = get_or_create_user(
            db=db,
            telegram_id=str(telegram_user.id),
            username=telegram_user.username,
        )

        await update.message.reply_text(
            f"🏆 Your score: {user.score}"
        )
    finally:
        db.close()

async def progress_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_user = update.effective_user
    db = SessionLocal()

    try:
        user = get_or_create_user(
            db=db,
            telegram_id=str(telegram_user.id),
            username=telegram_user.username,
        )

        level = "A0"
        if context.args:
            level = context.args[0].upper()

        progress = get_user_level_progress(db, user.id, level)

        await update.message.reply_text(
            f"📘 Progress for level {progress['level']}\n\n"
            f"Learned verbs: {progress['learned_verbs']} / {progress['total_verbs']}\n"
            f"Progress: {progress['progress_percent']}%"
        )
    finally:
        db.close()


async def train_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_user = update.effective_user
    db = SessionLocal()

    try:
        user = get_or_create_user(
            db=db,
            telegram_id=str(telegram_user.id),
            username=telegram_user.username,
        )

        task = get_training_task(db)

        if task is None:
            await update.message.reply_text("No verbs available.")
            return

        active_tasks[telegram_user.id] = {
            "user_id": user.id,
            "verb_id": task["verb_id"],
        }

        await update.message.reply_text(
            f"Training started!\n\n"
            f"Verb: {task['base_form']}\n"
            f"Translation: {task['translation']}\n"
            f"Level: {task['level']}\n\n"
            f"Send your answer in this format:\n"
            f"went, gone"
        )
    finally:
        db.close()


async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_user = update.effective_user
    message_text = update.message.text.strip()

    if telegram_user.id not in active_tasks:
        await update.message.reply_text("Please use /train first.")
        return

    parts = [part.strip() for part in message_text.split(",")]

    if len(parts) != 2:
        await update.message.reply_text(
            "Please send your answer in this format:\n"
            "went, gone"
        )
        return

    past_simple, past_participle = parts

    task_data = active_tasks[telegram_user.id]

    db = SessionLocal()

    try:
        result = check_training_answer(
            db=db,
            user_id=task_data["user_id"],
            verb_id=task_data["verb_id"],
            past_simple=past_simple,
            past_participle=past_participle,
        )

        if result is None:
            await update.message.reply_text("Verb not found.")
            return

        if result["is_correct"]:
            await update.message.reply_text("Correct! ✅")
        else:
            await update.message.reply_text(
                "Incorrect. ❌\n"
                f"Correct answer: "
                f"{result['correct_past_simple']}, {result['correct_past_participle']}"
            )

        del active_tasks[telegram_user.id]
    finally:
        db.close()


def register_handlers(application):
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("train", train_command))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_answer)
    )
    application.add_handler(CommandHandler("stats", stats_command))
    application.add_handler(CommandHandler("score", score_command))
    application.add_handler(CommandHandler("progress", progress_command))
