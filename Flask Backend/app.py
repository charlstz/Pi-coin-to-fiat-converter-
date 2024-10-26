# Define the Global Consensus Value (GCV) of Pi coin
GCV_PI_COIN = 314159  # in USD

# Dictionary of fiat currencies and their exchange rates against USD
fiat_currencies = {
    'USD': 1.0,        # US Dollar
    'EUR': 0.85,      # Euro
    'GBP': 0.75,      # British Pound Sterling
    'JPY': 110.0,     # Japanese Yen
    'CHF': 0.92,      # Swiss Franc
    'CAD': 1.25,      # Canadian Dollar
    'AUD': 1.35,      # Australian Dollar
    'NZD': 1.40,      # New Zealand Dollar
    'CNY': 6.45,      # Chinese Yuan
    'RUB': 75.0,      # Russian Ruble
    'INR': 74.0,      # Indian Rupee
    'BRL': 5.25,      # Brazilian Real
    'ZAR': 14.5,      # South African Rand
    'MXN': 20.0,      # Mexican Peso
    'KRW': 1150.0,    # South Korean Won
    'TRY': 8.5,       # Turkish Lira
    'SGD': 1.35       # Singapore Dollar
}

def convert_pi_to_fiat(pi_amount, currency):
    """
    Convert Pi coin amount to the specified fiat currency.
    
    :param pi_amount: Amount of Pi coins to convert
    :param currency: Target fiat currency
    :return: Equivalent amount in the target fiat currency
    """
    if currency not in fiat_currencies:
        raise ValueError(f"Currency '{currency}' is not supported.")
    
    # Calculate the value of Pi coins in USD
    value_in_usd = pi_amount * GCV_PI_COIN
    
    # Convert USD to the target fiat currency
    conversion_rate = fiat_currencies[currency]
    value_in_fiat = value_in_usd * conversion_rate
    
    return value_in_fiat

# Example usage
if __name__ == "__main__":
    pi_amount = 10  # Amount of Pi coins to convert
    target_currency = 'EUR'  # Target currency for conversion
    
    try:
        converted_value = convert_pi_to_fiat(pi_amount, target_currency)
        print(f"{pi_amount} Pi coins are equivalent to {converted_value:.2f} {target_currency}.")
    except ValueError as e:
        print(e)
