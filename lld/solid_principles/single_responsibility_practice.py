"""
Single Responsibility Principle (SRP) - Practice Exercise

Scenario: You have a class that manages a shopping cart. 
Currently, it handles adding items, calculating the total, and printing an invoice.
This violates SRP because printing the invoice is a presentation/formatting responsibility,
while managing the cart is a business logic responsibility.

Your Task:
Refactor the code to follow the Single Responsibility Principle.
1. Keep the `ShoppingCart` class focused only on managing items and calculating the total.
2. Create a new class `InvoicePrinter` responsible solely for printing the invoice.
"""

# ==========================================
# Bad Practice (Violating SRP)
# ==========================================
class ShoppingCart_Bad:
    def __init__(self):
        self.items = []

    def add_item(self, item_name: str, price: float):
        self.items.append({"name": item_name, "price": price})

    def calculate_total(self) -> float:
        return sum(item["price"] for item in self.items)

    def print_invoice(self):
        # Violation: The cart shouldn't be responsible for formatting/printing.
        print("\n--- INVOICE ---")
        for item in self.items:
            print(f"- {item['name']}: ${item['price']:.2f}")
        print("-" * 15)
        print(f"TOTAL: ${self.calculate_total():.2f}")
        print("---------------\n")


# ==========================================
# Good Practice (TODO)
# ==========================================

# TODO 1: Refactor ShoppingCart so it ONLY manages items and total.
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name: str, price: float):
        self.items.append({"name": item_name, "price": price})

    def calculate_total(self) -> float:
        return sum(item["price"] for item in self.items)


# TODO 2: Create a separate InvoicePrinter class for formatting and printing.
class InvoicePrinter:
    @staticmethod
    def print_invoice(cart: ShoppingCart):
        print("-----INVOICE-----")
        for item in cart.items:
            print(f"{item['name']}: {item['price']:.2f}")
        
        print(f"Total: {cart.calculate_total():.2f}")
        print("---------------")


# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    # Test your refactored code here:
    
    cart = ShoppingCart()
    cart.add_item("Laptop", 1200.00)
    cart.add_item("Mouse", 25.50)
    
    InvoicePrinter.print_invoice(cart)

