import pytest 
from models import Transaction

def test_transaction_creation(): # ვამოწმებთ ტრანზაქციის ობიექტის შექმნას
        
        t = Transaction("Income", 1500, "Salary", "2026-11-14", "Test")
        assert t.amount == 1500
        assert t.category == "Salary"


def test_transaction_to_dict(): # ვამოწმებთ ტრანზაქციის ლექსიკონად გადაქცევას (სერიალიზაციას)
        
        t = Transaction("Expense", 50.0, "Food", "2026-11-14", "Lunch")
        d = t.to_dict()
        
        assert d["amount"] ==  50.0
        assert d["category"] =="Food"
        assert d["transaction_type"] == "Expense"