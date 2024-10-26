from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the Global Consensus Value (GCV) of Pi coin
GCV_PI_COIN = 314159  # in USD

# Dictionary of fiat currencies and their exchange rates against USD
fiat_currencies = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.75,
    'JPY': 110.0,
    'CHF': 0.92,
    'CAD': 1.25,
    'AUD': 1.35,
    'NZD': 1.40,
    'CNY': 6.45,
    'RUB': 75.0,
    'INR': 74.0,
    'BRL': 5.25,
    'ZAR': 14.5,
    'MXN': 20.0,
    'KRW': 1150.0,
    'TRY': 8.5,
    'SGD': 1.35
}

@app.route('/convert', methods=['POST'])
def convert_pi_to_fiat():
    data = request.json
    pi_amount = data.get('pi_amount', 0)
    currency = data.get('currency', 'USD')

    if currency not in fiat_currencies:
        return jsonify({'error': f"Currency '{currency}' is not supported."}), 400
    
    value_in_usd = pi_amount * GCV_PI_COIN
    conversion_rate = fiat_currencies[currency]
    value_in_fiat = value_in_usd * conversion_rate

    return jsonify({'converted_value': value_in_fiat})

if __name__ == '__main__':
    app.run(debug=True)
