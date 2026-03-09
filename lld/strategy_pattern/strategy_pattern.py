"""
Strategy Pattern - In-Depth Example

Scenario: An e-commerce system that needs to process payments using different 
payment methods (Credit Card, PayPal, Crypto).

The Strategy Pattern allows us to add new payment methods without changing
the core shopping cart logic.
"""

from abc import ABC, abstractmethod

# ==========================================
# 1. The Strategy Interface
# ==========================================
class PaymentStrategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.
    """
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


# ==========================================
# 2. Concrete Strategies
# ==========================================
class CreditCardPayment(PaymentStrategy):
    def __init__(self, name: str, card_number: str, cvv: str, expiry_date: str):
        self.name = name
        self.card_number = card_number
        self.cvv = cvv
        self.expiry_date = expiry_date

    def pay(self, amount: float) -> None:
        # In a real app, you would integrate with Stripe or another payment gateway here
        print(f"Processing Credit Card payment...")
        print(f"Paid ${amount:.2f} using Credit Card (ending in {self.card_number[-4:]}).")


class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float) -> None:
        # In a real app, you would integrate with the PayPal API here
        print(f"Processing PayPal payment...")
        print(f"Paid ${amount:.2f} using PayPal (account: {self.email}).")


class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float) -> None:
        # In a real app, you would verify a blockchain transaction here
        print(f"Processing Cryptocurrency payment...")
        print(f"Paid ${amount:.2f} using Cryptocurrency (wallet: {self.wallet_address}).")


# ==========================================
# 3. The Context
# ==========================================
class ShoppingCart:
    """
    The Context defines the interface of interest to clients.
    It maintains a reference to a Strategy object and delegates the actual
    work to it.
    """
    def __init__(self, strategy: PaymentStrategy = None):
        self._items = []
        # The context can be initialized with a default strategy or left empty
        self._payment_strategy = strategy

    def add_item(self, item_name: str, price: float):
        self._items.append({"name": item_name, "price": price})
        print(f"Added '{item_name}' to cart. Price: ${price:.2f}")

    def calculate_total(self) -> float:
        return sum(item["price"] for item in self._items)

    def set_payment_strategy(self, strategy: PaymentStrategy):
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """
        print(f"\n[System] Changing payment strategy to {strategy.__class__.__name__}")
        self._payment_strategy = strategy

    def checkout(self):
        """
        The Context delegates the work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """
        if not self._payment_strategy:
            print("Checkout failed: No payment strategy selected.")
            return

        total_amount = self.calculate_total()
        if total_amount == 0:
            print("Cart is empty. Nothing to pay.")
            return

        print(f"\nChecking out... Total Amount Due: ${total_amount:.2f}")
        # Delegate the payment processing to the strategy
        self._payment_strategy.pay(total_amount)


# ==========================================
# 4. Client Code
# ==========================================
if __name__ == "__main__":
    print("=== Strategy Pattern Demonstration ===")
    
    # Create the context
    cart = ShoppingCart()
    cart.add_item("Design Patterns Book", 45.00)
    cart.add_item("Mechanical Keyboard", 120.50)

    # Client chooses PayPal strategy
    paypal = PayPalPayment("user@example.com")
    cart.set_payment_strategy(paypal)
    cart.checkout()

    # Later, client changes mind and switches to Crypto strategy at runtime
    crypto = CryptoPayment("0x1A2B3C4D5E6F")
    cart.set_payment_strategy(crypto)
    cart.checkout()
