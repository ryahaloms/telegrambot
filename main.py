from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from Commands import start_command, help_command, custom_command
from Weather import Weather

TOKEN: str ='xyz'
BOT_USERNAME : str = 'live_data_1970_bot'
IsraWeather = Weather()

#Responses
def handle_response(text: str) -> str:
    request = text.lower()

    if 'hello' in request:
        return 'hi there!'
    if 'how are you' in request:
        return 'I am fine!'
    answer = IsraWeather.get_Weather(text)
    if (answer != ""):
        return answer

    return 'I do not understand what do you mean'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text:str = update.message.text

    print("Incoming Message:" + text)

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text:str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   app = Application.builder().token(TOKEN).build()

   # Commands
   app.add_handler(CommandHandler('start',  start_command))
   app.add_handler(CommandHandler('help',   help_command))
   app.add_handler(CommandHandler('custom', custom_command))


   # Messages
   app.add_handler(MessageHandler(filters.TEXT, handle_message))

   #Errors
   app.add_error_handler(error)

   print("Start Polling")
   app.run_polling(poll_interval=3)


