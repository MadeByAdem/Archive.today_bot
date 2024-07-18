import telebot
import re
import os

botkey = os.getenv('BOTKEY')
bot = telebot.TeleBot(botkey)


def get_archive_url(url):
    # Extract the URL from the message text using regular expressions
    match = re.search(r"(?P<url>https?://[^\s]+)", url)
    if match:
        archive_url = 'https://archive.today/newest/'
        input_modified = f'{archive_url}{match.group("url")}'
        return input_modified
    else:
        return None


@bot.message_handler(commands=['start'])
def handle_start(message):
    # Code to execute when /start command is sent
    bot.reply_to(message, "Welcome to Archive.today Bot. Send a URL, and you'll receive the latest archived version of that page.\n\n"
                          "If the URL has not been saved before, you will be able to save it from the URL provided.\n\n"
                          "Good luck!")


@bot.message_handler(func=lambda message: True)
def handle_input(message):
    if message.text and message.text.strip():
        try:
            output = get_archive_url(message.text)
            if output:
                bot.reply_to(message, output)
            else:
                bot.reply_to(message, "No valid URL found in the message.")
        except Exception as e:
            print(f"Error fetching the URL: {e}")
            bot.reply_to(message, "An error occurred while fetching the URL.")

bot.polling()
