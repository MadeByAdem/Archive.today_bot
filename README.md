# Archive.today Telegram Bot

This project is a simple Telegram bot that receives URLs from users and responds with the latest archived version of the page using Archive.today. If the URL has not been archived before, the bot will provide a link to archive it.

## Features

- Start command with a welcome message.
- URL detection and archiving.
- Error handling for invalid URLs and other exceptions.

## Files

- `archive_bot.py`: The main script for the bot.
- `.env.example`: An example environment file to store your Telegram bot key.
- `archive_bot.service`: A systemd service file to run the bot as a service.

## Setup

### Prerequisites

- Python 3.x
- `pip` package manager
- A Telegram bot token. You can get one by creating a bot through the [BotFather](https://core.telegram.org/bots#botfather).

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/archive_bot.git
    cd archive_bot
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your environment variables:**

    Copy the `.env.example` file to `.env` and replace `YOURTELEGRAMBOTKEY` with your actual bot key.
    ```bash
    cp .env.example .env
    ```

5. **Run the bot:**
    ```bash
    python archive_bot.py
    ```

### Setting up as a Systemd Service

1. **Modify the service file:**

    Update the `archive_bot.service` file with your actual paths:
    ```ini
    [Unit]
    Description=Archive.today Bot
    After=network.target

    [Service]
    ExecStart=/your/path/to/archive_bot/venv/bin/python /your/path/to/archive_bot/archive_bot.py
    WorkingDirectory=/your/path/to/archive_bot
    User=root
    Restart=always

    [Install]
    WantedBy=multi-user.target
    ```

2. **Copy the service file to systemd:**
    ```bash
    sudo cp archive_bot.service /etc/systemd/system/
    ```

3. **Reload systemd and start the service:**
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl start archive_bot.service
    ```

4. **Enable the service to start on boot:**
    ```bash
    sudo systemctl enable archive_bot.service
    ```

## Usage

1. Start a chat with your bot on Telegram.
2. Use the `/start` command to receive the welcome message.
3. Send any URL to the bot, and it will reply with the latest archived version of that URL.

## Example

```text
User: /start
Bot: Welcome to Archive.today Bot. Send a URL, and you'll receive the latest archived version of that page.

User: https://example.com
Bot: https://archive.today/newest/https://example.com
```	

## Environment Variables

- `BOTKEY`: Your Telegram bot key. This should be kept secret and never shared.

## Contributing
Feel free to submit issues or pull requests if you have suggestions for improvements or new features. Please follow the existing coding style.

## License
This project is licensed under the Custom License. See the [LICENSE](LICENSE) file for more details.
