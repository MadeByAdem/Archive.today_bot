import telebot
import re
import os

botkey = os.getenv('BOTKEY')
bot = telebot.TeleBot(botkey)


def get_archive_url(url):
    # Extract the URL from the message text using regular expressions
    match = re.search(r"(?P<url>https?://[^\s]+)", url)
    # If a URL is found, append the archive.today base URL to it
    if match:
        archive_url = 'https://archive.today/newest/'  # Archive.today base URL
        input_modified = f'{archive_url}{match.group("url")}'  # Append URL to base URL
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
            # Extract the URL from the message text
            output = get_archive_url(message.text)
            if output:
                # Send the archived version of the URL to the user
                bot.reply_to(message, output)
            else:
                # Reply with a message indicating that no valid URL was found
                bot.reply_to(message, "No valid URL found in the message.")
        except Exception as e:
            # Print the error and reply with an error message
            print(f"Error fetching the URL: {e}")
            bot.reply_to(message, "An error occurred while fetching the URL.")

# Start the bot's polling mechanism to receive messages from users
bot.polling()

