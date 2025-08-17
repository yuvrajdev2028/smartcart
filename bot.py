from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from groqAPI import groq_assistance

API_KEY="YOUR_API_KEY"
BOT_USERNAME="YOUR_USERNAME"

async def start_command(update,context):
    await update.message.reply_text(f'Hello, {update.message.chat.first_name}! What would you like to buy today?')

async def help_command(update,context):
    await update.message.reply_text('------ THIS IS THE HELP GUIDELINE ------')

async def book_command(update,context):
    await update.message.reply_text('Book your product')


async def handle_message(update,context):
    text=update.message.text
    prompt=text

    if BOT_USERNAME in text:
        prompt=text.replace(BOT_USERNAME,'').strip()

    print(f'User {update.message.chat.id} in {update.message.chat.type}: "{prompt}"')

    response = groq_assistance(prompt)

    await update.message.reply_text(response)
    
async def error(update,context):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting Bot...')
    app=Application.builder().token(API_KEY).build()

    print('Adding Handlers...')
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('book',book_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=1)
