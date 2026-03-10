"""
Dependency Inversion Principle (DIP) - Practice Exercise

Scenario: You are building a system that tracks User activities.
Currently, the `ActivityTracker` high-level class directly instantiates and 
depends on a `MySQLDatabase` low-level class to save activity logs.

Your Task:
Refactor the code using Dependency Inversion.
1. Create a generic database interface (e.g., `DatabaseInterface`).
2. Make `MySQLDatabase` implement that interface.
3. Modify `ActivityTracker` so it depends on the interface and accepts it 
   via dependency injection in the constructor.
4. (Optional) Create a `MongoDatabase` to prove it works with multiple DBs.
"""

from abc import ABC, abstractmethod

# ==========================================
# Bad Practice (Violating DIP)
# ==========================================
class MySQLDatabase_Bad:
    def insert(self, data: str):
        print(f"Inserting '{data}' into MySQL database.")

class ActivityTracker_Bad:
    def __init__(self):
        # Violation: Hardcoded dependency on a concrete, low-level class.
        self.db = MySQLDatabase_Bad()

    def track(self, activity: str):
        self.db.insert(f"User performed: {activity}")


# ==========================================
# Good Practice (TODO)
# ==========================================

# TODO 1: Create an interface/abstraction (`DatabaseInterface`) with an `insert` method
class DatabaseInterface(ABC):
    @abstractmethod
    def insert(self, data: str):
        ...


# TODO 2: Ensure MySQLDatabase implements the abstraction
class MySQLDatabase:
    def insert(self, data: str):
        print(f"Inserting data into MySQL database: {data}")


# TODO 3: Refactor ActivityTracker to depend on `DatabaseInterface` (via constructor injection)
class ActivityTracker:
    def __init__(self, db: DatabaseInterface):
        self.db = db

    def track(self, activity: str):
        self.db.insert(f"User performed: {activity}")


# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    # Test your refactored code here:
    
    db = MySQLDatabase()
    tracker = ActivityTracker(db)
    tracker.track("Logged in")
    
