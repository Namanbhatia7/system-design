"""
Interface Segregation Principle (ISP) - Practice Exercise

Scenario: You have a system that manages User Accounts. 
Different types of users (Admin, Regular, Guest) have different privileges.
Currently, the `IUserAccount` interface forces all users to implement `delete_user`,
even if they don't have the permission!

Your Task:
Refactor the interfaces so that users only implement the methods they actually need.
1. Break down `IUserAccount` into smaller interfaces (e.g., `IReader`, `IWriter`, `IAdmin`).
2. Make `RegularUser` and `AdminUser` implement only the interfaces they need.
"""

from abc import ABC, abstractmethod

# ==========================================
# Bad Practice (Violating ISP)
# ==========================================
class IUserAccount_Bad(ABC):
    @abstractmethod
    def view_content(self):
        pass

    @abstractmethod
    def edit_content(self):
        pass

    @abstractmethod
    def delete_user(self, user_id: str):
        pass

class RegularUser_Bad(IUserAccount_Bad):
    def view_content(self):
        print("Viewing content...")

    def edit_content(self):
        print("Editing content...")

    def delete_user(self, user_id: str):
        # Violation! Regular users shouldn't have to implement this at all.
        raise PermissionError("Regular users cannot delete accounts!")


# ==========================================
# Good Practice (TODO)
# ==========================================

# TODO 1: Create smaller interfaces (e.g., IViewer, IEditor, IAdministrator)
class IViewer(ABC):
    @abstractmethod
    def view_content(self):
        ...

class IEditor(ABC):
    @abstractmethod
    def edit_content(self):
        ...

class IAdministrator(ABC):
    def delete_user(self, user_id: str):
        ...

# TODO 2: Implement RegularUser combining only the interfaces it needs
class RegularUser(IViewer):
    def view_content(self):
        print("Viewing content...")

# TODO 3: Implement AdminUser combining the interfaces it needs
class AdminUser(IViewer, IEditor, IAdministrator):
    def view_content(self):
        print("Viewing content...")

    def edit_content(self):
        print("Editing content...")

    def delete_user(self, user_id: str):
        print(f"Deleting user {user_id}")


# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    # Test your refactored code here:
    
    user = RegularUser()
    admin = AdminUser()
    
    user.view_content()
    admin.delete_user("123")
