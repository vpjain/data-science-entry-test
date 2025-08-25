class Car:
    """
    Represents a car with make, model, and year attributes.

    Methods:
        __init__(self, make, model, year)
            Initializes the car with the provided make, model, and year.

        describe_car(self)
            Prints the car's details in the format: "Year Make Model".
    """
    def __init__(self, make, model, year):
        """
        Initializes a Car instance.

        Parameters:
            make (str): The manufacturer of the car (e.g., 'Toyota').
            model (str): The model of the car (e.g., 'Corolla').
            year (int): The manufacturing year of the car (e.g., 2020).
        """
        self.make = make      # Manufacturer of the car
        self.model = model    # Model name
        self.year = year      # Year of manufacture

    def describe_car(self):
        """
        Prints the information of the car in "Year Make Model" format.
        """
        print(f"{self.year} {self.make} {self.model}")


# ===========================
# Example usage for Task 2
# ===========================

# Create an instance of Car with the specified attributes
my_car = Car("Toyota", "Corolla", 2020)
# Call the describe_car method to print car details
my_car.describe_car()  # Output: 2020 Toyota Corolla
