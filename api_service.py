import requests
class CurrencyAPI:

    BASE_URL = "https://open.er-api.com/v6/latest/USD"

    @staticmethod
    def get_exchange_rate(target_currency="GEL"):

        try:
            response = requests.get(CurrencyAPI.BASE_URL)
            response.raise_for_status()
            
            data = response.json()
            rates = data.get("rates", {})
            
            rate = rates.get(target_currency)
            if rate is None:
                print(f"Error: Currency '{target_currency}' not found.")
                return None
                
            return rate

        except requests.exceptions.ConnectionError:
            print("API Error: Network connection failed. Please check your internet.")
            return None