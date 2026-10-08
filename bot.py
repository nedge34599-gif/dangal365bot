from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8753672771:AAGPACRxae380DnmKwbzJxOgnPiQWsUN5xA"

MINI_APP_URL = "https://t.me/Dangal365loginbot/offers"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(
            "🎮 Open Dangal365 Games",
            url=MINI_APP_URL
        )]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎮 Welcome to Dangal365!\n\n"
        "Explore exciting games and enjoy the experience.",
        reply_markup=reply_markup
    )


async def games(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(
            "🎮 Open Games",
            url=MINI_APP_URL
        )]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎮 Explore Dangal365 Games",
        reply_markup=reply_markup
    )


async def casino(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(
            "🎰 Open Casino",
            url=MINI_APP_URL
        )]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎰 Explore Dangal365 Casino",
        reply_markup=reply_markup
    )


async def sports(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(
            "🏏 Open Sports",
            url=MINI_APP_URL
        )]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🏏 Explore Dangal365 Sports",
        reply_markup=reply_markup
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Available commands:\n\n"
        "/start - Start the Dangal365 bot\n"
        "/games - Explore Dangal365 games\n"
        "/casino - Explore casino games\n"
        "/sports - Explore sports games\n"
        "/help - Get help and bot information"
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("games", games))
app.add_handler(CommandHandler("casino", casino))
app.add_handler(CommandHandler("sports", sports))
app.add_handler(CommandHandler("help", help_command))

print("Dangal365 bot is running...")

app.run_polling()