import json
from models import Transaction

class FinanceStorage:
    @staticmethod
    def save_transactions(transactions): #ყველა ტრანზაქციის ობიექტს ვაქცევთ dict-ად და ვინახავთ json-ის ფაილში
        data = [t.to_dict() for t in transactions]
        with open ("transactions.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            
    @staticmethod
    def load_transactions():
        try:
            with open("transactions.json", "r", encoding="utf-8") as file:
                data = json.load(file) #JSON ტექსტი იქცევა ჩვეულებრივ dict-ად 
                transactions = [] # ლექსიკონიდან ვიღებთ მონაცემებს და ვქმნით Transaction ობიექტს
                for item in data:
                    t = Transaction(
                        transaction_type=item["transaction_type"],
                        amount=item["amount"],
                        category=item["category"],
                        data=item["data"],
                        comment=item["comment"]
                    )
                    transactions.append(t)
                return transactions
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return[]