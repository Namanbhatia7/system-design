"""
Liskov Substitution Principle (LSP) - Practice Exercise

Scenario: You are building an app to process payments using Credit Cards.
Initially, the `CreditCard` base class had a method to process payments.
Later, a `PrepaidCard` subclass was added. But wait... prepaid cards might not
have enough balance and throw exceptions when normal cards would succeed. 
This breaks LSP!

Your Task:
Refactor the hierarchy so that subclasses don't unexpectedly fail or throw errors 
for operations that the parent class promised would work.
1. Create a better abstraction (`PaymentCard` or `Card` interface).
2. Separate the logic so that `CreditCard` and `PrepaidCard` adhere to LSP.
"""

# ==========================================
# Bad Practice (Violating LSP)
# ==========================================
from abc import abstractmethod


class CreditCard_Bad:
    def process_payment(self, amount: float):
        print(f"Processing credit payment of ${amount}")

class PrepaidCard_Bad(CreditCard_Bad):
    def __init__(self, balance: float):
        self.balance = balance

    def process_payment(self, amount: float):
        # Violation: A function expecting a CreditCard doesn't expect a balance check exception!
        if self.balance < amount:
            raise ValueError("Insufficient balance on prepaid card!")
        self.balance -= amount
        print(f"Processed prepaid payment of ${amount}. Remaining: ${self.balance}")


# ==========================================
# Good Practice (TODO)
# ==========================================

# TODO 1: Create a generic abstract base class/interface (e.g., PaymentCard)
class PaymentCard:
    @abstractmethod
    def can_pay(self, amount: float) -> bool:
        ...
    
    def pay(self, amount: float) -> None:
        ...


# TODO 2: Ensure CreditCard correctly implements the base interface
class CreditCard:
    def can_pay(self, amount: float) -> bool:
        return True
    
    def pay(self, amount: float) -> None:
        print(f"Processing payment of {amount}")



# TODO 3: Ensure PrepaidCard correctly implements the base interface 
# (Handle the insufficient balance gracefully or change the design so it doesn't break substituting)
class PrepaidCard:
    def __init__(self, balance: float):
        self.balance = balance
    
    def can_pay(self, amount: float) -> bool:
        if self.balance < amount:
            return False
        else:
            return True
    
    def pay(self, amount: float) -> None:
        print(f"Processing payment of {amount}")

def checkout(card: PaymentCard, amount: float):
    if card.can_pay(amount):
        card.pay(amount)

# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    # Test your refactored code here:
    
    # def checkout(card: PaymentCard, amount: float):
    #     card.process_payment(amount)
    
    my_credit = CreditCard()
    my_prepaid = PrepaidCard(50.0)
    
    # checkout(my_credit, 100)
    # checkout(my_prepaid, 20)  # Should succeed
    # checkout(my_prepaid, 100) # How will you handle this without breaking LSP?

    checkout(my_credit, 100)
    checkout(my_prepaid, 20)  # Should succeed
    checkout(my_prepaid, 100)

