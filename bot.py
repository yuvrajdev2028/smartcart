from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from amazonSearch import search_amazon
from groqAPI import groq_assistance, search_query_gen, prompt_categorisation
import os

API_KEY=os.environ['BOT_API_KEY']
BOT_USERNAME=os.environ['BOT_USERNAME']

products=''

async def start_command(update,context):
    await update.message.reply_text(f'Hello, {update.message.chat.first_name}! What would you like to buy today?')

async def help_command(update,context):
    await update.message.reply_text('------ THIS IS THE HELP GUIDELINE ------')

async def book_command(update,context):
    await update.message.reply_text('Book your product')


async def handle_message(update,context):
    text=update.message.text
    prompt=text
    global products

    if BOT_USERNAME in text:
        prompt=text.replace(BOT_USERNAME,'').strip()

    print(f'User {update.message.chat.id} in {update.message.chat.type}: "{prompt}"')

    category=prompt_categorisation(prompt)
    if products=='' or category.lower()=='search query':
        search_query=search_query_gen(prompt)
        response=search_amazon(search_query)
        products=response
    elif category.lower()=='consumer query':
        response=groq_assistance(products,prompt)
    else:
        response='Kindly rephrase your request'

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