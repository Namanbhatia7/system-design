"""
Decorator Pattern - Practice Exercise

Scenario: A simple notification system.
- Base: send a plain message.
- Decorators (wrap in any order):
  - Prefix with "[URGENT] "
  - Suffix with " — Please reply."
  - Wrap message in double quotes

Your Task:
1. Define the Component interface `Notifier` with `send() -> str` (returns the final message).
2. Implement `PlainNotifier(message: str)` as ConcreteComponent.
3. Implement abstract `NotifierDecorator` that wraps a `Notifier` and delegates.
4. Implement concrete decorators: `UrgentDecorator`, `ReplyDecorator`, `QuoteDecorator`.
5. In `__main__`, build: Plain -> Urgent -> Quote -> Reply and print the result.

Tip: Each decorator's `send()` should call `self._wrapped.send()` and transform the string.
"""

from abc import ABC, abstractmethod


# ==========================================
# TODO 1: Component interface
# ==========================================
class Notifier(ABC):
    @abstractmethod
    def send(self) -> str:
        """Return the notification text."""
        pass


# ==========================================
# TODO 2: ConcreteComponent
# ==========================================
class PlainNotifier(Notifier):
    """Holds a base message; send() returns it unchanged."""
    
    def __init__(self, message: str) -> None:
        self.message = message
    
    def send(self) -> str:
        return self.message

# ==========================================
# TODO 3: Base Decorator
# ==========================================
class NotifierDecorator(Notifier):
    """Wraps another Notifier; subclasses override send()."""
    def __init__(self, notifier: Notifier) -> None:
        self._notifier = notifier


# ==========================================
# TODO 4: Concrete decorators
# ==========================================
class UrgentDecorator(NotifierDecorator):
    """Prepend '[URGENT] ' to the wrapped send() result."""
    def __init__(self, notifier: Notifier) -> None:
        super().__init__(notifier)
    
    def send(self) -> str:
        return f"[Urgent] {self._notifier.send()}"


class ReplyDecorator(NotifierDecorator):
    """Append ' — Please reply.' to the wrapped send() result."""
    def __init__(self, notifier: Notifier) -> None:
        super().__init__(notifier)
    
    def send(self) -> str:
        return f"{self._notifier.send()} — Please reply."


class QuoteDecorator(NotifierDecorator):
    """Wrap result in double quotes, e.g. " ... " """
    def __init__(self, notifier: Notifier) -> None:
        super().__init__(notifier)
    
    def send(self) -> str:
        return f"\"{self._notifier.send()}\""


# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    # Expected flow (after you implement):
    notify = UrgentDecorator(PlainNotifier("Meeting at 3pm"))
    print(notify.send())
    notify = ReplyDecorator(notify)
    print(notify.send())
    notify = QuoteDecorator(notify)
    print(notify.send())
    # n = ReplyDecorator(QuoteDecorator(UrgentDecorator(PlainNotifier("Meeting at 3pm"))))
    # print(n.send())
    # Something like: " [URGENT] Meeting at 3pm " — Please reply.
    # (Exact formatting is up to your QuoteDecorator design.)
