# BotTradeErni

Um sistema robusto de automação de trading de criptomoedas, dividido em duas partes para monitorar sinais e executar operações via WebSocket e integração com exchanges.

## Arquitetura

O projeto é composto por dois serviços independentes:

1.  **Crypto Seeker** (`crypto_seeker.py`): Conecta-se a um servidor WebSocket para monitorar, processar e persistir os sinais de trading recebidos.
2.  **Operation Bot** (`operation_bot.py`): Atua como o motor de execução, fornecendo uma API REST para receber sinais e realizar operações na exchange configurada.

## Pré-requisitos

- Python 3.8+
- Pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório.
2. Instale as dependências necessárias:

bash
pip install -r requirements.txt


## Configuração

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:

env
WS_SIGNAL=ws://seu-websocket-server
EXCHANGE_ID=binance
API_KEY=sua-api-key
API_SECRET=seu-api-secret
PORT=5000


## Uso

### Iniciando o Crypto Seeker

O Crypto Seeker conecta-se ao endpoint WebSocket especificado e registra os sinais recebidos.

bash
python crypto_seeker.py


### Iniciando o Operation Bot

O Operation Bot inicializa um servidor web Flask para lidar com as solicitações de execução de trades.

bash
python operation_bot.py


### Endpoints do Operation Bot

- `POST /webhook`: Recebe e processa os sinais de trading.
- `GET /api/botStatus`: Retorna o status atual e a integridade do bot.

## Estrutura do Projeto


.
├── crypto_seeker.py     # Script de monitoramento de sinais
├── operation_bot.py     # Script de execução de trades
├── requirements.txt     # Dependências do Python
└── .env                # Arquivo de configuração (criar manualmente)


## Logs

Os logs são salvos no seguinte formato:

YYYY-MM-DD HH:MM:SS - LEVEL - Mensagem


## Segurança

- **Nunca** compartilhe suas chaves API ou segredos.
- Mantenha o arquivo `.env` fora do controle de versão (ex: adicione ao `.gitignore`).
- Garanta que o ambiente seja seguro ao executar o bot.

## Contribuição

Contribuições são bem-vindas. Por favor, envie Pull Requests para melhorias.

## Licença

MIT