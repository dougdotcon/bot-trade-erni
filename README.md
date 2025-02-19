# Bot de Trading Crypto

Este projeto consiste em dois componentes principais:

1. **Crypto Seeker** (`crypto_seeker.py`): Responsável por monitorar e processar sinais de trading.
2. **Operation Bot** (`operation_bot.py`): Executa as operações de trading com base nos sinais recebidos.

## Requisitos

- Python 3.8+
- Pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
WS_SIGNAL=ws://seu-websocket-server
EXCHANGE_ID=binance
API_KEY=sua-api-key
API_SECRET=seu-api-secret
PORT=5000
```

## Uso

### Iniciando o Crypto Seeker

```bash
python crypto_seeker.py
```

O Crypto Seeker irá:
- Conectar ao WebSocket especificado
- Monitorar sinais de trading
- Processar e salvar os sinais recebidos

### Iniciando o Operation Bot

```bash
python operation_bot.py
```

O Operation Bot irá:
- Iniciar um servidor Flask na porta especificada
- Expor endpoints para receber sinais e verificar status
- Executar operações de trading baseadas nos sinais recebidos

### Endpoints do Operation Bot

- `POST /webhook`: Recebe sinais de trading
- `GET /api/botStatus`: Retorna o status atual do bot

## Estrutura do Projeto

```
├── crypto_seeker.py     # Script do monitor de sinais
├── operation_bot.py     # Script do bot de operações
├── requirements.txt     # Dependências do projeto
└── .env                # Configurações (criar manualmente)
```

## Logs

Os logs são salvos no formato:
```
YYYY-MM-DD HH:MM:SS - LEVEL - Mensagem
```

## Segurança

- Nunca compartilhe suas chaves API
- Mantenha o arquivo .env seguro
- Use apenas em redes seguras

## Contribuição

Sinta-se à vontade para contribuir com melhorias através de Pull Requests.

## Licença

MIT 