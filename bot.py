import logging
import os
import json
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# --- CONFIG ---
BOT_TOKEN = os.getenv("BOT_TOKEN")  # from Koyeb environment
ADMIN_ID = int(os.getenv("ADMIN_ID", "7547946252"))  # your Telegram user ID

WELCOME_FILE = "welcome.json"
USERS_FILE = "users.json"

# --- LOGGING ---
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# --- STORAGE HELPERS ---
def load_json(file, default):
    if not os.path.exists(file):
        return default
    with open(file, "r") as f:
        return json.load(f)

def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f)

WELCOME = load_json(WELCOME_FILE, {"welcome": "👋 Welcome to the bot!"})
USERS = load_json(USERS_FILE, [])

# --- COMMANDS ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in USERS:
        USERS.append(user_id)
        save_json(USERS_FILE, USERS)
    await update.message.reply_text(WELCOME["welcome"])

async def setwelcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    if not context.args:
        await update.message.reply_text("⚠️ Usage: /setwelcome <message>")
        return
    msg = " ".join(context.args)
    WELCOME["welcome"] = msg
    save_json(WELCOME_FILE, WELCOME)
    await update.message.reply_text(f"✅ Welcome message updated:\n\n{msg}")

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    if not context.args:
        await update.message.reply_text("⚠️ Usage: /broadcast <message>")
        return
    msg = " ".join(context.args)
    count = 0
    for uid in USERS:
        try:
            await context.bot.send_message(chat_id=uid, text=msg)
            count += 1
        except Exception:
            pass
    await update.message.reply_text(f"📢 Broadcast sent to {count} users.")

# --- MAIN ---
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("setwelcome", setwelcome))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.run_polling()

if __name__ == "__main__":
    main()
