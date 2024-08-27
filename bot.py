from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler
from config import TELEGRAM_BOT_TOKEN
import asyncio

FLASK_APP_URL = 'https://c64e-147-182-157-217.ngrok-free.app'

# Create the Application
application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

async def start(update: Update, context):
    referral_id = context.args[0] if context.args else None
    keyboard = [[InlineKeyboardButton("Play", web_app=WebAppInfo(url=f'{FLASK_APP_URL}?username={update.effective_user.username}&id={update.effective_user.id}&ref_id={referral_id}'))]]
    # keyboard = [[InlineKeyboardButton("Play", web_app=WebAppInfo(url=f'{FLASK_APP_URL}?username={update.effective_user.username}&id={update.effective_user.id}&ref_id="1"'))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f'Hey: {update.effective_user.username} Wellcome to mining app:', reply_markup=reply_markup)

# Register handlers
application.add_handler(CommandHandler('start', start))
print("bot has been")
if __name__ == '__main__':

    asyncio.run(application.run_polling())
