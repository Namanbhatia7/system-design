"""
Strategy Pattern - Practice Exercise

Scenario: You are building a Text Formatter application. 
Users can input text and choose different formats to output it:
1. Uppercase format
2. Lowercase format
3. Title case format

Your Task:
1. Implement the Strategy Interface (`TextFormatterStrategy`).
2. Implement three Concrete Strategies (`UppercaseStrategy`, `LowercaseStrategy`, `TitlecaseStrategy`).
3. Implement the Context class (`TextEditor`) which uses the strategy to publish text.
4. Write client code to test your implementation.
"""

from abc import ABC, abstractmethod

# ==========================================
# TODO 1: Create the Strategy Interface
# ==========================================
class TextFormatterStrategy(ABC):
    """
    Define an abstract method `format_text(text: str) -> str` that all 
    concrete strategies must implement.
    """
    @abstractmethod
    def format_text(self, text: str) -> str:
        pass



# ==========================================
# TODO 2: Create Concrete Strategies
# ==========================================
class UppercaseStrategy(TextFormatterStrategy): # Hint: Inherit from TextFormatterStrategy
    """
    Implement the format_text method to return the text in all UPPERCASE.
    """
    def format_text(self, text: str) -> str:
        return text.upper()

class LowercaseStrategy(TextFormatterStrategy):
    """
    Implement the format_text method to return the text in all lowercase.
    """
    def format_text(self, text: str) -> str:
        return text.lower()

class TitlecaseStrategy(TextFormatterStrategy):
    """
    Implement the format_text method to return the text in Title Case.
    """
    def format_text(self, text: str) -> str:
        return text.title()


# ==========================================
# TODO 3: Create the Context
# ==========================================
class TextEditor:
    """
    The Context class. It should:
    - Have a reference to a TextFormatterStrategy (pass via init and/or setter).
    - Have a method `set_strategy(strategy: TextFormatterStrategy)` to change the strategy at runtime.
    - Have a method `publish(text: str)` that uses the current strategy to format 
      and print the text.
    """
    def __init__(self, strategy: TextFormatterStrategy = None):
        self.strategy = strategy
    
    def set_strategy(self, strategy: TextFormatterStrategy):
        self.strategy = strategy
    
    def publish(self, text: str):
        print(self.strategy.format_text(text))


# ==========================================
# TODO 4: Client Code
# ==========================================
if __name__ == "__main__":
    sample_text = "heLLo wORLd! tHiS iS a tEsT."
    print("Original text:", sample_text)
    print("-" * 30)
    
    # Step 1: Instantiate the context (TextEditor)
    text_editor = TextEditor()
    
    # Step 2: Set the strategy to Uppercase and publish the text
    text_editor.set_strategy(UppercaseStrategy())
    text_editor.publish(sample_text)
    
    # Step 3: Change the strategy to Lowercase and publish the text
    text_editor.set_strategy(LowercaseStrategy())
    text_editor.publish(sample_text)
    
    # Step 4: Change the strategy to Titlecase and publish the text
    text_editor.set_strategy(TitlecaseStrategy())
    text_editor.publish(sample_text)
    
    print("\n[!] Implement the TODOs above to see the Strategy Pattern in action!")
