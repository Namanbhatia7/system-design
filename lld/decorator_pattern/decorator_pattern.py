"""
Decorator Pattern - In-Depth Examples

Example 1: Coffee shop (classic Component + Decorators wrapping cost & description)
Example 2: Text processor (stack decorators: bold, italic, underline)
"""

from abc import ABC, abstractmethod


# =============================================================================
# EXAMPLE 1: Coffee (classic Decorator)
# =============================================================================

class Beverage(ABC):
    """Component interface."""

    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass


class Espresso(Beverage):
    """ConcreteComponent."""

    def cost(self) -> float:
        return 2.50

    def description(self) -> str:
        return "Espresso"


class HouseBlend(Beverage):
    """ConcreteComponent."""

    def cost(self) -> float:
        return 1.99

    def description(self) -> str:
        return "House Blend Coffee"


class BeverageDecorator(Beverage):
    """
    Decorator base: wraps a Beverage and delegates; subclasses add behavior.
    """

    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage


class Milk(BeverageDecorator):
    """ConcreteDecorator."""

    def cost(self) -> float:
        return self._beverage.cost() + 0.50

    def description(self) -> str:
        return self._beverage.description() + ", Milk"


class Mocha(BeverageDecorator):
    """ConcreteDecorator."""

    def cost(self) -> float:
        return self._beverage.cost() + 0.60

    def description(self) -> str:
        return self._beverage.description() + ", Mocha"


class Whip(BeverageDecorator):
    """ConcreteDecorator."""

    def cost(self) -> float:
        return self._beverage.cost() + 0.70

    def description(self) -> str:
        return self._beverage.description() + ", Whip"


# =============================================================================
# EXAMPLE 2: Text formatting (stack decorators)
# =============================================================================

class TextComponent(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class PlainText(TextComponent):
    def __init__(self, text: str) -> None:
        self._text = text

    def render(self) -> str:
        return self._text


class TextDecorator(TextComponent):
    def __init__(self, wrapped: TextComponent) -> None:
        self._wrapped = wrapped


class BoldDecorator(TextDecorator):
    def render(self) -> str:
        return f"<b>{self._wrapped.render()}</b>"


class ItalicDecorator(TextDecorator):
    def render(self) -> str:
        return f"<i>{self._wrapped.render()}</i>"


class UnderlineDecorator(TextDecorator):
    def render(self) -> str:
        return f"<u>{self._wrapped.render()}</u>"


# =============================================================================
# Client / Demo
# =============================================================================

def run_coffee_example() -> None:
    print("=== Example 1: Coffee Decorators ===\n")
    drink1 = Espresso()
    print(f"{drink1.description()} — ${drink1.cost():.2f}")

    drink2 = Mocha(Milk(Espresso()))
    print(f"{drink2.description()} — ${drink2.cost():.2f}")

    drink3 = Whip(Mocha(Milk(HouseBlend())))
    print(f"{drink3.description()} — ${drink3.cost():.2f}")
    print()


def run_text_example() -> None:
    print("=== Example 2: Text Decorators (order matters) ===\n")
    base = PlainText("Hello")
    # Outer Bold wraps Italic wraps base
    styled = BoldDecorator(ItalicDecorator(base))
    print(styled.render())

    styled2 = UnderlineDecorator(BoldDecorator(PlainText("World")))
    print(styled2.render())
    print()


if __name__ == "__main__":
    run_coffee_example()
    run_text_example()
