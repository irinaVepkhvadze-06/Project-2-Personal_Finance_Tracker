# დეკორატორი რომელიც ამოწმებს შეყვანილი თანხის სისწორეს (უნდა იყოს დადებითი რიცხვი)
def validate_amount(function): 
    def wrapper(self, transaction):
        try:
            amount_value = float(transaction.amount)
            if amount_value <= 0:
                print("Validation Error: Amount must be greater than 0!")
                return False

            transaction.amount = amount_value

        except ValueError:
            print("Validation Error: Amount must be a valid number!")
            return False

        return function(self, transaction)
    return wrapper


class Transaction: 
    def __init__(self, transaction_type, amount,category, data, comment):
        self.transaction_type = transaction_type
        self.amount = amount
        self.category = category
        self.data = data
        self.comment = comment

    def to_dict(self):  # აბრუნებს ტრანზაქციის ობიექტს dict-ის სახით, json-ში შესანახად
        return {
        "transaction_type": self.transaction_type,
        "amount": float(self.amount),
        "category": self.category,
        "data": self.data,
        "comment": self.comment

        }

    def display(self):
        print(f"Data: {self.data}, Type: {self.transaction_type}, "
              f"Category: {self.category}, Amount: {float(self.amount)}, "
              f"Comment: {self.comment}")


class FinanceManager:
    def __init__(self): # ვქმნით ცარიელ სია ტრანზაქციების შესანახად
        self.transactions = [] 

    @validate_amount
    def add_transaction(self, transaction): # ამატებს ახალ ტრანზაქციას საერთო სიაში
        self.transactions.append(transaction)
        return True

    def get_total_income(self):      #ითვლის ყველა Income ტიპის ტრანზაქციის ჯამს
        return sum(t.amount for t in self.transactions if t.transaction_type == "Income")

    def get_total_expense(self):     #ითვლის ყველა Expense ტიპის ტრანზაქციის ჯამს
        return sum(t.amount for t in self.transactions if t.transaction_type == "Expense")

    def get_balance(self):  #ითვლის საბოლოო ბალანსს
        return self.get_total_income() - self.get_total_expense()

