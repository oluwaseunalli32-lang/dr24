import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# It is best practice to load the token from an environment variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a welcome message and an educational fact."""
    user = update.effective_user
    welcome_text = (
        f"Hi {user.first_name}! I am DR-24, your sports education bot. 🏅\n\n"
        "Here is a fact: A standard marathon is 26.2 miles (42.195 km) long. "
        "Use /help to see what else I can do."
    )
    await update.message.reply_text(welcome_text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Displays a list of available commands."""
    help_text = "I can share sports facts, rules, and history. Try /start to see an example."
    await update.message.reply_text(help_text)

def main():
    """Starts the bot."""
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN environment variable not set.")
        return

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    print("DR-24 is starting...")
    application.run_polling()

if __name__ == "__main__":
    main()
