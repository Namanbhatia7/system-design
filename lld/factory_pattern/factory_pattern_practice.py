"""
Factory Pattern — Three Practice Exercises

Each section targets one variant:
  Part 1 — Simple Factory
  Part 2 — Factory Method
  Part 3 — Abstract Factory

Run this file after implementing the TODOs in each part.
"""

from abc import ABC, abstractmethod


# =============================================================================
# PART 1: SIMPLE FACTORY
# =============================================================================
# Scenario: Create loggers by name without the client importing concrete classes.
# One function (or class method) decides which class to instantiate.

class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> str:
        """Return a string showing how the message was logged."""
        pass


class ConsoleLogger(Logger):
    """TODO: log() returns something like '[console] <message>'"""
    
    def log(self, message: str) -> str:
        """Return a string showing how the message was logged."""
        return f"[console] {message}"


class FileLogger(Logger):
    """TODO: log() returns something like '[file] <message>'"""
    def log(self, message: str) -> str:
        """Return a string showing how the message was logged."""
        return f"[file] {message}"


class RemoteLogger(Logger):
    """TODO: log() returns something like '[remote] <message>'"""
    def log(self, message: str) -> str:
        """Return a string showing how the message was logged."""
        return f"[remote] {message}"


def create_logger(kind: str) -> Logger:
    """
    Simple Factory: map kind to concrete Logger.
    Accept e.g. "console", "file", "remote" (case-insensitive).
    Raise ValueError for unknown kind.
    """
    if kind == "console":
        return ConsoleLogger()
    elif kind == "file":
        return FileLogger()
    elif kind == "remote":
        return RemoteLogger()
    else:
        raise ValueError(f"Unknown logger type: {kind}")


# =============================================================================
# PART 2: FACTORY METHOD
# =============================================================================
# Scenario: A game spawns different enemies. The base "spawner" defines how
# spawning works; subclasses override which enemy is created.

class Enemy(ABC):
    @abstractmethod
    def attack(self) -> str:
        pass


class Goblin(Enemy):
    def attack(self) -> str:
        return "Goblin attacks"


class Orc(Enemy):
    def attack(self) -> str:
        return "Orc attacks"


class Dragon(Enemy):
    def attack(self) -> str:
        return "Dragon attacks"


class EnemySpawner(ABC):
    """
    Creator: subclasses override create_enemy() -> Enemy.
    spawn_wave() is a template that uses the factory method.
    """

    @abstractmethod
    def create_enemy(self) -> Enemy:
        pass

    def spawn_wave(self) -> str:
        """TODO: create one enemy via create_enemy() and return attack() result."""
        enemy = self.create_enemy()
        return enemy.attack()


class GoblinSpawner(EnemySpawner):
    def create_enemy(self) -> Enemy:
        return Goblin()


class OrcSpawner(EnemySpawner):
    def create_enemy(self) -> Enemy:
        return Orc()


class DragonSpawner(EnemySpawner):
    def create_enemy(self) -> Enemy:
        return Dragon()


# =============================================================================
# PART 3: ABSTRACT FACTORY
# =============================================================================
# Scenario: Two UI themes. Each theme produces a matching Toolbar + Dialog
# (same family — client never mixes Light toolbar with Dark dialog).

class Toolbar(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Dialog(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class LightToolbar(Toolbar):
    def render(self) -> str:
        return "[Light theme] Toolbar"


class LightDialog(Dialog):
    def render(self) -> str:
        return "[Light theme] Dialog"


class DarkToolbar(Toolbar):
    def render(self) -> str:
        return "[Dark theme] Toolbar"


class DarkDialog(Dialog):
    def render(self) -> str:
        return "[Dark theme] Dialog"


class ThemeFactory(ABC):
    """Abstract Factory: one family of related UI widgets."""

    @abstractmethod
    def create_toolbar(self) -> Toolbar:
        pass

    @abstractmethod
    def create_dialog(self) -> Dialog:
        pass


class LightThemeFactory(ThemeFactory):
    def create_toolbar(self) -> Toolbar:
        return LightToolbar()

    def create_dialog(self) -> Dialog:
        return LightDialog()


class DarkThemeFactory(ThemeFactory):
    def create_toolbar(self) -> Toolbar:
        return DarkToolbar()

    def create_dialog(self) -> Dialog:
        return DarkDialog()


def render_app_screen(factory: ThemeFactory) -> None:
    """
    Client code: only depends on ThemeFactory.
    TODO: create toolbar + dialog from factory and print both render() outputs.
    """
    toolbar = factory.create_toolbar()
    dialog = factory.create_dialog()
    print(toolbar.render())
    print(dialog.render())


# =============================================================================
# Demos (uncomment / call after you implement)
# =============================================================================

def demo_simple_factory() -> None:
    print("--- Part 1: Simple Factory ---")
    c = create_logger("console")
    f = create_logger("file")
    print(c.log("hello"))
    print(f.log("hello"))
    print("(implement create_logger and concrete loggers)\n")


def demo_factory_method() -> None:
    print("--- Part 2: Factory Method ---")
    g = GoblinSpawner()
    o = OrcSpawner()
    print(g.spawn_wave())
    print(o.spawn_wave())
    print("(implement Enemy, Spawners, spawn_wave)\n")


def demo_abstract_factory() -> None:
    print("--- Part 3: Abstract Factory ---")
    render_app_screen(LightThemeFactory())
    render_app_screen(DarkThemeFactory())
    print("(implement ThemeFactory, widgets, render_app_screen)\n")


if __name__ == "__main__":
    demo_simple_factory()
    demo_factory_method()
    demo_abstract_factory()
