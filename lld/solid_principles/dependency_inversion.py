"""
Dependency Inversion Principle (DIP) - In-Depth Example

Scenario: A high-level Order Processor sending notifications.
"""

from abc import ABC, abstractmethod

# ==========================================
# Bad Practice (Violating DIP)
# ==========================================
class EmailSender_Bad:
    """
    A low-level module that handles sending emails.
    """
    def send_email(self, message: str):
        print(f"Sending Email: {message}")

class OrderProcessor_Bad:
    """
    A high-level module containing the business logic.
    Violation: It directly depends on the concrete EmailSender.
    If we want to switch to SMS notifications, we have to modify the OrderProcessor.
    """
    def __init__(self):
        # High-level module creates the low-level module! Tightly coupled!
        self.notifier = EmailSender_Bad()

    def process_order(self, order_id: str):
        print(f"Processing order {order_id}...")
        self.notifier.send_email(f"Your order {order_id} is confirmed!")


# ==========================================
# Good Practice (Following DIP)
# ==========================================
class MessageSender(ABC):
    """
    An abstraction (interface) that both high-level and low-level modules will depend on.
    """
    @abstractmethod
    def send(self, message: str):
        pass

class EmailSender(MessageSender):
    """
    Low-level module depends on the abstraction.
    """
    def send(self, message: str):
        print(f"[DIP] Sending Email: {message}")

class SMSSender(MessageSender):
    """
    Another low-level module depends on the abstraction.
    """
    def send(self, message: str):
        print(f"[DIP] Sending SMS: {message}")

class OrderProcessor:
    """
    High-level module depends on the abstraction (`MessageSender`).
    It receives the dependency via its constructor (Dependency Injection).
    """
    def __init__(self, notifier: MessageSender):
        self.notifier = notifier

    def process_order(self, order_id: str):
        print(f"Processing order {order_id}...")
        self.notifier.send(f"Your order {order_id} is confirmed!")


# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    print("=== Dependency Inversion Principle Demonstration ===\n")

    # The client code decides which low-level module to inject!
    email_notifier = EmailSender()
    processor1 = OrderProcessor(email_notifier)
    processor1.process_order("ORD-123")

    # Switching to SMS is trivial and doesn't require modifying the OrderProcessor!
    print("\nSwitching to SMS notifications...")
    sms_notifier = SMSSender()
    processor2 = OrderProcessor(sms_notifier)
    processor2.process_order("ORD-999")
