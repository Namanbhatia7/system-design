"""
Single Responsibility Principle (SRP) - In-Depth Example

Scenario: Managing employee data and saving it to a file.
"""

# ==========================================
# Bad Practice (Violating SRP)
# ==========================================
class Employee_Bad:
    """
    This class handles two responsibilities:
    1. Managing employee properties/data.
    2. File I/O operations (saving to a database or file).
    """
    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position

    def get_details(self) -> str:
        return f"{self.name} works as a {self.position}"

    def save_to_file(self, filename: str):
        # Violation: The Employee class shouldn't know how to save itself.
        # If the saving mechanism changes (e.g. to a database), this class has to change.
        with open(filename, "a") as f:
            f.write(self.get_details() + "\n")
        print(f"Saved {self.name} to {filename}")


# ==========================================
# Good Practice (Following SRP)
# ==========================================
class Employee:
    """
    Responsibility: Managing employee properties/data only.
    """
    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position

    def get_details(self) -> str:
        return f"{self.name} works as a {self.position}"


class EmployeeRepository:
    """
    Responsibility: Handling data persistence (saving/loading).
    """
    @staticmethod
    def save_to_file(employee: Employee, filename: str):
        with open(filename, "a") as f:
            f.write(employee.get_details() + "\n")
        print(f"[SRP] Saved {employee.name} to {filename} using EmployeeRepository")


# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    print("=== Single Responsibility Principle Demonstration ===\n")

    # Creating an employee
    emp1 = Employee("Alice", "Software Engineer")
    print("Employee Details:", emp1.get_details())

    # Saving the employee using a separate class dedicated to file I/O
    EmployeeRepository.save_to_file(emp1, "employees.txt")
