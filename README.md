# BotTradeErni

A robust, two-component cryptocurrency trading automation system designed for monitoring signals and executing trades via WebSocket and API integration.

## Architecture

The project consists of two independent services:

1. **Crypto Seeker** (`crypto_seeker.py`): Connects to a WebSocket server to monitor, process, and persist incoming trading signals.
2. **Operation Bot** (`operation_bot.py`): Acts as an execution engine, providing a REST API to receive signals and perform trading operations on the configured exchange.

## Prerequisites

- Python 3.8+
- Pip (Python package manager)

## Installation

1. Clone the repository.
2. Install the required dependencies:

bash
pip install -r requirements.txt


## Configuration

Create a `.env` file in the root directory of the project with the following environment variables:

env
WS_SIGNAL=ws://your-websocket-server
EXCHANGE_ID=binance
API_KEY=your-api-key
API_SECRET=your-api-secret
PORT=5000


## Usage

### Starting the Crypto Seeker

The Crypto Seeker connects to the specified WebSocket endpoint and logs incoming signals.

bash
python crypto_seeker.py


### Starting the Operation Bot

The Operation Bot initializes a Flask web server to handle trade execution requests.

bash
python operation_bot.py


### Operation Bot Endpoints

- `POST /webhook`: Receives and processes trading signals.
- `GET /api/botStatus`: Returns the current health and status of the bot.

## Project Structure


.
├── crypto_seeker.py     # Signal monitoring script
├── operation_bot.py     # Trade execution script
├── requirements.txt     # Python dependencies
└── .env                # Configuration file (create manually)


## Logging

Logs are saved in the following format:

YYYY-MM-DD HH:MM:SS - LEVEL - Message


## Security

- **Never** share your API keys or secrets.
- Keep the `.env` file out of version control (e.g., add to `.gitignore`).
- Ensure the environment is secure when running the bot.

## Contributing

Contributions are welcome. Please submit Pull Requests for any improvements.

## License

MIT