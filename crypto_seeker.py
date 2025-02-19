import os
import json
import websocket
import logging
from dotenv import load_dotenv
from datetime import datetime

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CryptoSeeker:
    def __init__(self):
        load_dotenv()
        self.ws_url = os.getenv('WS_SIGNAL', 'ws://localhost:8080')
        self.ws = None
        self.is_connected = False

    def on_message(self, ws, message):
        try:
            packet = json.loads(message)
            if packet.get('type') == 'signals_created':
                logger.info(f"Sinal recebido: {packet}")
                # Processa o sinal recebido
                self.process_signal(packet.get('content'))
                # Envia confirmação
                ws.send(json.dumps({
                    'type': 'signals_created',
                    'content': 'OK'
                }))
        except Exception as e:
            logger.error(f"Erro ao processar mensagem: {e}")

    def on_error(self, ws, error):
        logger.error(f"Erro na conexão WebSocket: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        logger.info("Conexão WebSocket fechada")
        self.is_connected = False

    def on_open(self, ws):
        logger.info("Conexão WebSocket estabelecida")
        self.is_connected = True

    def process_signal(self, signal_content):
        """
        Processa o sinal recebido e toma ações apropriadas
        """
        try:
            # Aqui você pode implementar a lógica específica para processar os sinais
            # Por exemplo, análise técnica, decisões de trading, etc.
            logger.info(f"Processando sinal: {signal_content}")
            
            # Exemplo de estrutura de sinal processado
            processed_signal = {
                'timestamp': datetime.now().isoformat(),
                'signal': signal_content,
                'action': self.determine_action(signal_content)
            }
            
            # Salva ou envia o sinal processado
            self.save_signal(processed_signal)
            
        except Exception as e:
            logger.error(f"Erro ao processar sinal: {e}")

    def determine_action(self, signal_content):
        """
        Determina a ação a ser tomada com base no sinal
        """
        # Implemente sua lógica de decisão aqui
        return "HOLD"  # Exemplo: BUY, SELL, HOLD

    def save_signal(self, processed_signal):
        """
        Salva o sinal processado (pode ser em arquivo, banco de dados, etc.)
        """
        # Exemplo: salvando em um arquivo JSON
        with open('signals_history.json', 'a') as f:
            json.dump(processed_signal, f)
            f.write('\n')

    def start(self):
        """
        Inicia o CryptoSeeker
        """
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            self.ws_url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open
        )
        self.ws.run_forever()

    def stop(self):
        """
        Para o CryptoSeeker
        """
        if self.ws:
            self.ws.close()

if __name__ == "__main__":
    seeker = CryptoSeeker()
    try:
        seeker.start()
    except KeyboardInterrupt:
        logger.info("Encerrando CryptoSeeker...")
        seeker.stop() 