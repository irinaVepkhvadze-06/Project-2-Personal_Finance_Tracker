from models import Transaction, FinanceManager
from storage import FinanceStorage

class FinanceMenu:
    def __init__(self):
        self.manager = FinanceManager()
        self.manager.transactions = FinanceStorage.load_transactions()

    def display_menu(self):  # მართავს მენიუს, აჩვენებს ვარიანტებს, ამუშავებს მომხმარებლის არჩევანს.

        while True:  
            print("Select an option")
            print("1: Add Transaction")
            print("2: View Transaction")
            print("3: Check USD to GEL Rate")
            print("4: Exit")

            action = input("Please Enter a number(1-3): ")

            if action == "1":
                while True:
                    print("Select Type: ")
                    print("1. Income")
                    print("2. Expense")
                    option = input("Please enter a number (1-2): ").strip()

                    if option == "1":
                        transaction_type = "Income" 
                        break
                    elif option == "2":
                        transaction_type = "Expense"
                        break
                    print("Invalid type! Please type 'Income' or 'Expense'.")

                while True:   #თანხის ვალიდაცია try-except ბლოკით
                    amount = input("Amount: ")
                    try: 
                        value_amount = float(amount)
                        if value_amount <= 0:
                            print("Validation Error: Amount must be greater than 0!")
                            continue
                        break
                    except ValueError:
                        print("Validation Error: Amount must be a valid number!")
                        continue

                category = input("Category (e.g. Salary, Food, Transport): ")
                data = input("Data (DD.MM.YYYY): ")
                comment = input("Comment: ")
                # # ვქმნით ტრანზაქციის ობიექტს
                new_transaction = Transaction(transaction_type, value_amount, category, data, comment)

                if self.manager.add_transaction(new_transaction):
                    FinanceStorage.save_transactions(self.manager.transactions)
                    print("Transaction saved successfully!")
                else:
                    print("Transaction was not saved")
                

            elif action =="2":   #ტრანზაქციების სია და ფინანსური შეჯამებები
                if not self.manager.transactions:
                    print("Transaction list is empty")
                else:
                    counter = 1
                    for item in self.manager.transactions:
                        print(f"{counter}.", end="")
                        item.display()
                        counter += 1

                    total_income = self.manager.get_total_income()
                    total_expense = self.manager.get_total_expense()
                    balance = self.manager.get_balance()

                    print("Financial Summary: ")
                    print(f"Total Income: {total_income}")
                    print(f"Total Expense: {total_expense}")
                    print(f"Current Balance: {balance}")
                    print("-------------------------\n")

            elif action == "3":   # გარე API-ს გამოძახება ვალუტის კურსის სანახავად
                from api_service import CurrencyAPI
                rate = CurrencyAPI.get_exchange_rate("GEL")
                if rate:
                    print("Current Exchange Rate: ")
                    print(f"1 USD = {rate} GEL")
                    print("-----------------------------\n")

            elif action == "4":
                print("Thank you! Goodbye!")
                break
            else:
                print("Invalid option! Please choose 1, 2, 3 or 4")
