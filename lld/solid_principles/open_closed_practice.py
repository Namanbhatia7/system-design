"""
Open/Closed Principle (OCP) - Practice Exercise

Scenario: You have a discount calculator for an e-commerce store.
Currently, the calculator determines discounts based on customer types 
(Regular, Premium) using `if/elif`.

Your Task:
Refactor the code to follow the Open/Closed Principle using abstraction.
If a new customer type (e.g., "VIP" or "Student") is added later, 
the `DiscountCalculator` should NOT need modification.
"""

from abc import ABC, abstractmethod

# ==========================================
# Bad Practice (Violating OCP)
# ==========================================
class DiscountCalculator_Bad:
    def calculate_discount(self, customer_type: str, price: float) -> float:
        if customer_type == "regular":
            return price * 0.05  # 5% discount
        elif customer_type == "premium":
            return price * 0.15  # 15% discount
        # Adding a new type requires modifying this function!
        return 0.0


# ==========================================
# Good Practice (TODO)
# ==========================================

# TODO 1: Create an abstract base class `CustomerDiscount` with an abstract method `get_discount(price)`
class CustomerDiscount(ABC):
    @abstractmethod
    def get_discount(self, price: float) -> float:
        ...




# TODO 2: Create concrete classes like `RegularDiscount` and `PremiumDiscount` 
class RegularDiscount(CustomerDiscount):
    def __init__(self):
        self.price: float | None = 100.0
    
    def get_discount(self, price: float) -> float:
        return price * 0.05

class PremiumDiscount(CustomerDiscount):
    def __init__(self):
        self.price: float | None = 100.0

    def get_discount(self, price: float) -> float:
        return price * 0.15


# TODO 3: Refactor DiscountCalculator so it takes a `CustomerDiscount` object
class DiscountCalculator:
    def calculate_discount_price(self, discount_strategy: CustomerDiscount, price: float) -> float:
        discount = discount_strategy.get_discount(price)
        return price - discount


# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    # Test your refactored code here:
    
    regular = RegularDiscount()
    premium = PremiumDiscount()
    calculator = DiscountCalculator()
    
    print(f"Regular price (100) after discount: {calculator.calculate_discount_price(regular, 100)}")
    print(f"Premium price (100) after discount: {calculator.calculate_discount_price(premium, 100)}")
    
