"""
Liskov Substitution Principle (LSP) - In-Depth Example

Scenario: Birds flying. 
A classic violation occurs when modeling Penguins as subclass of Bird.
"""

# ==========================================
# Bad Practice (Violating LSP)
# ==========================================
class Bird_Bad:
    def fly(self):
        print("I am flying high in the sky!")

class Sparrow_Bad(Bird_Bad):
    pass

class Penguin_Bad(Bird_Bad):
    """
    Violates LSP: Penguins can't fly, so overriding fly to raise an exception
    means you can't substitute a Penguin anywhere a Bird is expected.
    """
    def fly(self):
        raise NotImplementedError("Penguins cannot fly!")

def let_bird_fly(bird: Bird_Bad):
    # This code assumes all birds can fly. Passing a Penguin here breaks the app.
    bird.fly()


# ==========================================
# Good Practice (Following LSP)
# ==========================================
class Bird:
    """
    Instead of assuming all birds fly, we make 'Bird' the abstract base
    for common bird behaviors (e.g. eating, sleeping).
    """
    def eat(self):
        print("I am pecking at food.")

class FlyingBird(Bird):
    """
    Only birds that can fly inherit from FlyingBird.
    """
    def fly(self):
        print("I am flying high in the sky!")

class NonFlyingBird(Bird):
    """
    Birds that cannot fly inherit from NonFlyingBird.
    """
    def walk(self):
        print("I am waddling around.")

class Sparrow(FlyingBird):
    pass

class Penguin(NonFlyingBird):
    # Now, a Penguin IS-A NonFlyingBird and IS-A Bird.
    # It does not inherit a fly() method it has to break!
    pass


# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    print("=== Liskov Substitution Principle Demonstration ===\n")

    sparrow = Sparrow()
    penguin = Penguin()

    print("Sparrow:")
    sparrow.eat()
    sparrow.fly()

    print("\nPenguin:")
    penguin.eat()
    penguin.walk()
    # penguin.fly()  # This would fail at compile/lint time, avoiding runtime crashes!
