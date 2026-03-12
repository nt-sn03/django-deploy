from telegram import ForceReply, Update, Bot
from telegram.ext import Updater, CommandHandler, ContextTypes, MessageHandler, Filters, Dispatcher
from django.conf import settings

bot = Bot(settings.TOKEN)
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)


def start(update: Update, context: ContextTypes) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: ContextTypes) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text("Help!")


def echo(update: Update, context: ContextTypes) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def add_handlers():
    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

add_handlers()

def handle_udpate(data: dict):
    update = Update.de_json(data, bot)
    dispatcher.process_update(update)
