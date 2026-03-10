"""
Interface Segregation Principle (ISP) - In-Depth Example

Scenario: An old and new multi-function printer.
"""

from abc import ABC, abstractmethod

# ==========================================
# Bad Practice (Violating ISP)
# ==========================================
class Machine_Bad(ABC):
    """
    A "fat" interface forcing clients to implement methods they don't need.
    """
    @abstractmethod
    def print_document(self, document: str):
        pass

    @abstractmethod
    def scan_document(self, document: str):
        pass

    @abstractmethod
    def fax_document(self, document: str):
        pass

class OldFashionedPrinter_Bad(Machine_Bad):
    def print_document(self, document: str):
        print(f"Printing: {document}")

    def scan_document(self, document: str):
        # Violation: The old printer can't scan, but it MUST implement it!
        raise NotImplementedError("This printer cannot scan!")

    def fax_document(self, document: str):
        raise NotImplementedError("This printer cannot fax!")


# ==========================================
# Good Practice (Following ISP)
# ==========================================
class Printer(ABC):
    @abstractmethod
    def print_document(self, document: str):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self, document: str):
        pass

class FaxMachine(ABC):
    @abstractmethod
    def fax_document(self, document: str):
        pass

class OldFashionedPrinter(Printer):
    """
    Now, the old printer only implements the interface it actually uses.
    """
    def print_document(self, document: str):
        print(f"[ISP] Printing: {document} using OldFashionedPrinter")

class MultiFunctionPrinter(Printer, Scanner, FaxMachine):
    """
    A multi-function printer implements all the interfaces it needs!
    """
    def print_document(self, document: str):
        print(f"[ISP] Printing: {document} using MFP")

    def scan_document(self, document: str):
        print(f"[ISP] Scanning: {document} using MFP")

    def fax_document(self, document: str):
        print(f"[ISP] Faxing: {document} using MFP")


# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    print("=== Interface Segregation Principle Demonstration ===\n")

    old_printer = OldFashionedPrinter()
    old_printer.print_document("My Report.pdf")
    # Note: old_printer.scan_document() doesn't even exist, so it can't crash unexpectedly!

    mfp = MultiFunctionPrinter()
    mfp.scan_document("Receipt.jpg")
    mfp.fax_document("Contract.pdf")
    mfp.print_document("Contract.pdf")
