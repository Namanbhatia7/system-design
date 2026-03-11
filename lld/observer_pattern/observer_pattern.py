"""
Observer Pattern - In-Depth Examples

Example 1: News Publisher (PUSH model — subject passes data to update())
Example 2: Stock Ticker (PUSH model with structured data)
Example 3: Config Store (PULL model — observers get subject reference and fetch what they need)
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


# =============================================================================
# EXAMPLE 1: News Publisher (PUSH model/ Classic Observer)
# =============================================================================

class NewsObserver(ABC):
    """Observer interface: any subscriber must implement update()."""

    @abstractmethod
    def update(self, headline: str, body: str) -> None:
        pass


class NewsPublisher:
    """
    Subject (Observable). Maintains a list of observers and notifies them
    when new news is published. Does not depend on concrete observer types.
    """
    def __init__(self) -> None:
        self._observers: List[NewsObserver] = []
        self._latest_headline = ""
        self._latest_body = ""

    def attach(self, observer: NewsObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: NewsObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def _notify(self) -> None:
        # PUSH: we send the data as arguments; observers don't need a reference to us
        for observer in self._observers:
            observer.update(self._latest_headline, self._latest_body)

    def publish(self, headline: str, body: str) -> None:
        self._latest_headline = headline
        self._latest_body = body
        self._notify()


class EmailSubscriber(NewsObserver):
    def __init__(self, email: str) -> None:
        self.email = email

    def update(self, headline: str, body: str) -> None:
        print(f"[Email to {self.email}] Breaking: {headline}")
        print(f"  Preview: {body[:50]}...")


class SMSSubscriber(NewsObserver):
    def __init__(self, phone: str) -> None:
        self.phone = phone

    def update(self, headline: str, body: str) -> None:
        print(f"[SMS to {self.phone}] Alert: {headline}")


# =============================================================================
# EXAMPLE 2: Stock Ticker (Push model with structured data)
# =============================================================================

@dataclass
class StockUpdate:
    """Data object pushed to observers (push model)."""
    symbol: str
    price: float
    change_percent: float


class StockObserver(ABC):
    @abstractmethod
    def on_stock_update(self, update: StockUpdate) -> None:
        pass


class StockTicker:
    """Subject: notifies observers with structured data (push)."""
    def __init__(self) -> None:
        self._observers: List[StockObserver] = []

    def subscribe(self, observer: StockObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: StockObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def set_price(self, symbol: str, price: float, previous_price: float) -> None:
        change_pct = ((price - previous_price) / previous_price) * 100 if previous_price else 0.0
        update = StockUpdate(symbol=symbol, price=price, change_percent=change_pct)
        for obs in self._observers:
            obs.on_stock_update(update)


class PortfolioDisplay(StockObserver):
    """Displays updates for symbols the user cares about."""
    def __init__(self, watched_symbols: List[str]) -> None:
        self.watched_symbols = set(watched_symbols)

    def on_stock_update(self, update: StockUpdate) -> None:
        if update.symbol in self.watched_symbols:
            sign = "+" if update.change_percent >= 0 else ""
            print(f"[Portfolio] {update.symbol}: ${update.price:.2f} ({sign}{update.change_percent:.2f}%)")


class AlertService(StockObserver):
    """Alerts when a stock moves beyond a threshold."""
    def __init__(self, threshold_percent: float) -> None:
        self.threshold_percent = threshold_percent

    def on_stock_update(self, update: StockUpdate) -> None:
        if abs(update.change_percent) >= self.threshold_percent:
            print(f"[Alert] {update.symbol} moved {update.change_percent:+.2f}% (threshold: {self.threshold_percent}%)")


# =============================================================================
# EXAMPLE 3: Config Store (PULL model)
# =============================================================================
# In PULL, the subject only says "I changed." Observers receive a reference to
# the subject and call getters to fetch only the data they need.

class ConfigObserver(ABC):
    """Observer receives the subject and pulls whatever data it needs."""

    @abstractmethod
    def update(self, subject: "ConfigStore") -> None:
        pass


class ConfigStore:
    """
    Subject. When config changes, we notify observers by passing self.
    Observers then call get_theme(), get_language(), etc. to pull what they need.
    """
    def __init__(self) -> None:
        self._observers: List[ConfigObserver] = []
        self._theme = "light"
        self._language = "en"
        self._font_size = 14

    def attach(self, observer: ConfigObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: ConfigObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def _notify(self) -> None:
        # PULL: we only pass ourselves; each observer pulls what it needs
        for observer in self._observers:
            observer.update(self)

    def set_config(self, theme: str = None, language: str = None, font_size: int = None) -> None:
        if theme is not None:
            self._theme = theme
        if language is not None:
            self._language = language
        if font_size is not None:
            self._font_size = font_size
        self._notify()

    # Getters for observers to PULL data
    def get_theme(self) -> str:
        return self._theme

    def get_language(self) -> str:
        return self._language

    def get_font_size(self) -> int:
        return self._font_size


class ThemeDisplay(ConfigObserver):
    """Only cares about theme; pulls only get_theme()."""
    def update(self, subject: ConfigStore) -> None:
        theme = subject.get_theme()
        print(f"[Pull/Theme] Config changed. Current theme: {theme}")


class LocalizationDisplay(ConfigObserver):
    """Only cares about language; pulls only get_language()."""
    def update(self, subject: ConfigStore) -> None:
        lang = subject.get_language()
        print(f"[Pull/Localization] Config changed. Current language: {lang}")


class FullConfigDisplay(ConfigObserver):
    """Pulls all config values."""
    def update(self, subject: ConfigStore) -> None:
        print(f"[Pull/Full] theme={subject.get_theme()}, language={subject.get_language()}, font_size={subject.get_font_size()}")


# =============================================================================
# Client / Demo
# =============================================================================

def run_news_example() -> None:
    print("=== Example 1: News Publisher ===\n")
    publisher = NewsPublisher()
    email_sub = EmailSubscriber("alice@example.com")
    sms_sub = SMSSubscriber("+1-555-0100")
    publisher.attach(email_sub)
    publisher.attach(sms_sub)
    publisher.publish("Market hits new high", "The stock market reached a new all-time high today amid strong earnings.")
    publisher.detach(sms_sub)
    publisher.publish("Follow-up: Fed meeting", "The Federal Reserve announced no change in rates.")
    print()


def run_stock_example() -> None:
    print("=== Example 2: Stock Ticker (Push) ===\n")
    ticker = StockTicker()
    portfolio = PortfolioDisplay(["AAPL", "GOOGL"])
    alerts = AlertService(threshold_percent=5.0)
    ticker.subscribe(portfolio)
    ticker.subscribe(alerts)
    ticker.set_price("AAPL", 150.0, 140.0)   # ~7.14% -> portfolio + alert
    ticker.set_price("GOOGL", 142.0, 141.0) # ~0.7% -> portfolio only
    ticker.set_price("MSFT", 400.0, 380.0)  # ~5.26% -> alert only
    ticker.unsubscribe(alerts)
    ticker.set_price("AAPL", 155.0, 150.0)
    print()


def run_pull_example() -> None:
    print("=== Example 3: Config Store (Pull) ===\n")
    store = ConfigStore()
    theme_display = ThemeDisplay()
    lang_display = LocalizationDisplay()
    full_display = FullConfigDisplay()
    store.attach(theme_display)
    store.attach(lang_display)
    store.attach(full_display)

    store.set_config(theme="dark")
    store.set_config(language="es")
    store.set_config(font_size=16)
    store.detach(full_display)
    store.set_config(theme="light")
    print()


if __name__ == "__main__":
    run_news_example()
    run_stock_example()
    run_pull_example()
