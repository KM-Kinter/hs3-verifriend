# Discord Welcome Bot

A Discord bot that sends welcome messages with random questions to new users.

## Features

- Automatically detects when 3 users join the server and send something on source channel to be verified
- Sends a welcome message with user mentions
- Includes random questions in both Polish and English
- Uses webhooks for message delivery
- Environment-based configuration
- Docker support for easy deployment

## Prerequisites

- Python 3.11 or higher
- Docker (optional)
- Discord Bot Token
- Discord Webhook URL
- Source and Target Channel IDs

## Installation

### Using Docker

1. Clone the repository:
```bash
git clone https://github.com/KM-Kinter/hs3-verifriend
cd hs3-verifriend
```

2. Create a `.env` file with your configuration:
```env
DISCORD_TOKEN=your_bot_token
SOURCE_CHANNEL_ID=your_source_channel_id
TARGET_CHANNEL_ID=your_target_channel_id
WEBHOOK_URL=your_webhook_url
```

3. Build and run the Docker container:
```bash
docker build -t discord-bot .
docker run --env-file .env discord-bot
```

### Without Docker

1. Clone the repository:
```bash
git clone https://github.com/KM-Kinter/hs3-verifriend
cd hs3-verifriend
```

2. Create a `.env` file with your configuration:
```env
DISCORD_TOKEN=your_bot_token
SOURCE_CHANNEL_ID=your_source_channel_id
TARGET_CHANNEL_ID=your_target_channel_id
WEBHOOK_URL=your_webhook_url
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the bot:
```bash
python main.py
```

## How it works

1. The bot monitors the source channel for new messages
2. When 3 different users send messages in the source channel
3. The bot generates a welcome message with:
   - User mentions
   - Standard questions (1-4)
   - A random question (5) from the predefined list
4. The message is sent via webhook to the target channel

## Configuration

### Environment Variables

- `DISCORD_TOKEN`: Your Discord bot token
- `SOURCE_CHANNEL_ID`: Channel ID where users need to send messages
- `TARGET_CHANNEL_ID`: Channel ID where welcome messages will be sent
- `WEBHOOK_URL`: Discord webhook URL for sending messages

### Questions

You can modify the questions in the `QUESTIONS` list in `main.py`. Each question should be a tuple with Polish and English versions.

## Troubleshooting

### Docker Issues

1. Make sure Docker Desktop is running
2. Check if the `.env` file exists and has correct values
3. Try rebuilding the container:
```bash
docker build --no-cache -t discord-bot .
```

### Python Issues

1. Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```
2. Check if the `.env` file exists and has correct values

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 

## Author

Kinter - [Website](https://kinter.netlify.app/) | [GitHub](https://github.com/KM-Kinter)

---

Made with ❤️ by Kinter 
