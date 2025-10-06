# Subito pyrogram

Telegram bot and web scraper for monitoring new listings on [subito.it](https://www.subito.it/). It allows you to define search queries and receive notifications via Telegram when new items matching your criteria are posted.

Based on <https://github.com/morrolinux/subito-it-searcher>

## Requirements

- Python 3.10+
- MySQL server
- Telegram bot token and credentials

## Setup

1. **Clone the repository and setup venv**

   ```sh
   git clone https://github.com/Antonio-Ciociola/subito-pyro.git
   cd subito
   virtualenv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure credentials:**

   - Create a `secretsCred.py` file in `src/utils/` with your Telegram API credentials and chat ID.
   - Example:

     ```python
     api_id = YOUR_API_ID
     api_hash = 'YOUR_API_HASH'
     bot_token = 'YOUR_BOT_TOKEN'
     chat_id = YOUR_CHAT_ID
     ```

3. **Configure MySQL:**

   - Edit the connection string in `src/database/db_class.py` to match your MySQL setup.

4. **(Optional) Systemd Service:**

   - Use `subito.service` to run the bot as a service. Update paths as needed.

## Usage

- Start the bot:

  ```sh
  ./run.sh
  ```

## File Structure

- `src/` — Main source code
  - `main.py` — Entry point
  - `bot.py` — Telegram bot setup
  - `scraper.py` — subito.it scraper
  - `database/` — Database models and functions
  - `plugins/` — Bot command handlers
  - `utils/` — Secrets and utility functions
- `requirements.txt` — Python dependencies
- `run.sh` — Script to start the bot
- `subito.service` — Example systemd service file
- `commands.txt` — List of bot commands to send to botfather
