from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/convert_currency', methods=['GET'])
def convert_currency():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = float(request.args.get('amount'))

    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url).json()
    
    if to_currency in response['rates']:
        converted_amount = amount * response['rates'][to_currency]
        return jsonify({'converted_amount': converted_amount})
    else:
        return jsonify({'error': 'Invalid currency'})

if __name__ == '__main__':
    app.run(debug=True)
