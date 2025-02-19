import os
import json
import logging
from datetime import datetime
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import ccxt

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class OperationBot:
    def __init__(self):
        load_dotenv()
        self.exchange = self.setup_exchange()
        self.trades_history = []
        self.active = True
        self.current_strategy = "Estratégia de Média Móvel"
        
    def setup_exchange(self):
        """
        Configura a conexão com a exchange
        """
        exchange_id = os.getenv('EXCHANGE_ID', 'binance')
        exchange_class = getattr(ccxt, exchange_id)
        exchange = exchange_class({
            'apiKey': os.getenv('API_KEY'),
            'secret': os.getenv('API_SECRET'),
            'enableRateLimit': True,
        })
        return exchange

    def get_balance(self):
        """
        Obtém o saldo da conta
        """
        try:
            balance = self.exchange.fetch_balance()
            return {
                'BTC': balance.get('BTC', {}).get('free', 0),
                'USD': balance.get('USD', {}).get('free', 0)
            }
        except Exception as e:
            logger.error(f"Erro ao obter saldo: {e}")
            return {'BTC': 0, 'USD': 0}

    def execute_trade(self, signal):
        """
        Executa uma operação de trading
        """
        try:
            # Implementar lógica de execução de trade
            trade_info = {
                'timestamp': datetime.now().isoformat(),
                'type': signal.get('action'),
                'pair': signal.get('pair'),
                'price': signal.get('price'),
                'amount': signal.get('amount')
            }
            
            # Registra a operação
            self.trades_history.append(trade_info)
            logger.info(f"Trade executado: {trade_info}")
            
            return trade_info
            
        except Exception as e:
            logger.error(f"Erro ao executar trade: {e}")
            return None

    def calculate_profit_loss(self):
        """
        Calcula o lucro/prejuízo total
        """
        total = 0
        for trade in self.trades_history:
            if trade['type'] == 'BUY':
                total -= float(trade['price']) * float(trade['amount'])
            else:
                total += float(trade['price']) * float(trade['amount'])
        
        return {
            'value': total,
            'type': 'profit' if total > 0 else 'loss'
        }

    def get_status(self):
        """
        Retorna o status atual do bot
        """
        balance = self.get_balance()
        profit_loss = self.calculate_profit_loss()
        
        return {
            'isActive': self.active,
            'lastTrade': self.trades_history[-1] if self.trades_history else None,
            'balance': balance,
            'totalTrades': len(self.trades_history),
            'profitLoss': profit_loss,
            'recentError': None,  # Implementar sistema de registro de erros
            'currentStrategy': self.current_strategy,
            'nextAction': "Esperando sinal de compra",
            'logs': [str(trade) for trade in self.trades_history[-10:]]  # Últimos 10 trades
        }

# Criação da API Flask
app = Flask(__name__)
bot = OperationBot()

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Endpoint para receber sinais de trading
    """
    try:
        signal = request.json
        if not signal:
            return jsonify({'error': 'Sinal inválido'}), 400
            
        # Executa o trade baseado no sinal
        trade_result = bot.execute_trade(signal)
        
        if trade_result:
            return jsonify({'success': True, 'trade': trade_result})
        else:
            return jsonify({'error': 'Falha ao executar trade'}), 500
            
    except Exception as e:
        logger.error(f"Erro no webhook: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/botStatus', methods=['GET'])
def bot_status():
    """
    Endpoint para verificar o status do bot
    """
    return jsonify(bot.get_status())

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 