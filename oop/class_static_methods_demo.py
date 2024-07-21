class Calculator:
    calculation_type = "Arithmetic Operations"  # Class attribute

    @staticmethod
    def add(a, b):
        """Static method to add two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to multiply two numbers.
        It also prints the type of calculation based on a class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

