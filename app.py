from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
TOKEN = '7096122446:AAGZ92TkAjurHTZKxkujRSpomriGY0dn6Dk'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if 'message' in data:
        message = data['message']
        chat_id = message['chat']['id']
        username = message['from'].get('username', 'Unknown')
        
        if message.get('text') == '/start':
            send_message(chat_id, f'Welcome! Your username is {username}')
        else:
            send_message(chat_id, f'Your username is {username}')
    return jsonify({'status': 'ok'})

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

curl -F "url=https://21f2-39-47-27-89.ngrok-free.app/webhook" https://api.telegram.org/bot7096122446:AAGZ92TkAjurHTZKxkujRSpomriGY0dn6Dk/setWebhook
