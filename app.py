from flask import Flask
import os
import threading
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "IPD Bot is running!"

def run_bot():
    # Esegue lo script principale del bot
    subprocess.run(["python", "main.py"]) # Sostituisci "main.py" con il comando d'avvio reale del bot se diverso

if __name__ == "__main__":
    # Avvia il bot in un thread separato
    t = threading.Thread(target=run_bot)
    t.daemon = True
    t.start()
    
    # Avvia il server web sulla porta richiesta da Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)