"""
Factory Pattern - In-Depth Examples

Example 1: Simple Factory (create shapes by type string)
Example 2: Factory Method (document creators: PDF, Word)
Example 3: Abstract Factory (UI theme: Light vs Dark button + checkbox)
"""

from abc import ABC, abstractmethod


# =============================================================================
# EXAMPLE 1: Simple Factory
# =============================================================================

class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        pass


class Circle(Shape):
    def draw(self) -> str:
        return "Drawing a Circle"


class Rectangle(Shape):
    def draw(self) -> str:
        return "Drawing a Rectangle"


class Triangle(Shape):
    def draw(self) -> str:
        return "Drawing a Triangle"


def create_shape(shape_type: str) -> Shape:
    """
    Simple Factory: one function (or static method) that creates the right
    concrete object based on a parameter. Adding a new shape requires
    modifying this function.
    """
    shape_type = shape_type.lower()
    if shape_type == "circle":
        return Circle()
    if shape_type == "rectangle":
        return Rectangle()
    if shape_type == "triangle":
        return Triangle()
    raise ValueError(f"Unknown shape type: {shape_type}")


# =============================================================================
# EXAMPLE 2: Factory Method
# =============================================================================

class Document(ABC):
    @abstractmethod
    def open(self) -> str:
        pass

    @abstractmethod
    def save(self) -> str:
        pass


class PDFDocument(Document):
    def open(self) -> str:
        return "Opening PDF document"

    def save(self) -> str:
        return "Saving as PDF"


class WordDocument(Document):
    def open(self) -> str:
        return "Opening Word document"

    def save(self) -> str:
        return "Saving as .docx"


class DocumentCreator(ABC):
    """
    Creator: declares the factory method. Subclasses override it to
    return their concrete Document.
    """

    @abstractmethod
    def create_document(self) -> Document:
        pass

    def new_document(self) -> str:
        """Template method: uses the factory method."""
        doc = self.create_document()
        return doc.open()


class PDFCreator(DocumentCreator):
    def create_document(self) -> Document:
        return PDFDocument()


class WordCreator(DocumentCreator):
    def create_document(self) -> Document:
        return WordDocument()


# =============================================================================
# EXAMPLE 3: Abstract Factory (UI theme family)
# =============================================================================

class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class LightButton(Button):
    def render(self) -> str:
        return "[Light theme] Button"


class LightCheckbox(Checkbox):
    def render(self) -> str:
        return "[Light theme] Checkbox"


class DarkButton(Button):
    def render(self) -> str:
        return "[Dark theme] Button"


class DarkCheckbox(Checkbox):
    def render(self) -> str:
        return "[Dark theme] Checkbox"


class GUIFactory(ABC):
    """Abstract Factory: interface for creating a family of UI components."""

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class LightFactory(GUIFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> Checkbox:
        return LightCheckbox()


class DarkFactory(GUIFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> Checkbox:
        return DarkCheckbox()


def build_ui(factory: GUIFactory) -> None:
    """Client uses only the abstract factory; it gets a consistent theme."""
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())


# =============================================================================
# Client / Demo
# =============================================================================

def run_simple_factory() -> None:
    print("=== Example 1: Simple Factory ===\n")
    s1 = create_shape("circle")
    s2 = create_shape("rectangle")
    print(s1.draw())
    print(s2.draw())
    print()


def run_factory_method() -> None:
    print("=== Example 2: Factory Method ===\n")
    pdf_creator = PDFCreator()
    word_creator = WordCreator()
    print(pdf_creator.new_document())
    print(word_creator.new_document())
    doc = pdf_creator.create_document()
    print(doc.save())
    print()


def run_abstract_factory() -> None:
    print("=== Example 3: Abstract Factory ===\n")
    print("Light theme:")
    build_ui(LightFactory())
    print("Dark theme:")
    build_ui(DarkFactory())
    print()


if __name__ == "__main__":
    run_simple_factory()
    run_factory_method()
    run_abstract_factory()
