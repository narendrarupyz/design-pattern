
"""Builder Design Pattern
📘 Definition
The Builder Pattern is a creational design pattern that separates the construction of a complex object from its representation.
This pattern provides a step-by-step approach to build an object, allowing the same construction process to create different representations.

It’s useful when:

The object construction process is complicated

You want to hide the construction logic from the client

You need to reuse the same building process for multiple variations

✅ Pros

> Separation of Concerns: The object creation logic is abstracted away from the business logic.

> Flexibility: Easily construct different variations of objects using the same process.

> Improved Readability: Encapsulates the building logic and makes the code cleaner and easier to maintain.

> Immutable Objects: Supports step-by-step construction before returning a fully initialized object.

> Reusable Code: The same builder logic can be reused to create different objects.

⚠️ Cons

> Increased Complexity: More classes/interfaces are introduced than a simple object creation.

> Overkill for Simple Objects: Not worth using when the object is simple or has fewer configuration parameters.

> Maintenance Overhead: More code to maintain as you have to define builders and directors if used.

💼 Use Cases
Domain	Use Case
🏨 Hotel Booking System	Construct different room types (Standard, Deluxe, Suite) with custom pricing, availability.

Use Builder when object creation is complex, has many options, or needs customization.

Avoid it for simple models or when a simple constructor is enough.

Can be used with or without interfaces — supports open/closed principle and separation of concerns.

"""
# Abstract Hotel Room
class HotelRoom:

    # Enforce child classes to set rate and occupancy during instantiation
    def __init__(self):
        self.set_rate()
        self.set_max_occupancy()

    # Must be overridden by subclasses to define specific rate
    def set_rate(self):
        raise NotImplementedError

    # Must be overridden by subclasses to define specific occupancy
    def set_max_occupancy(self):
        raise NotImplementedError

    # String representation of the room with rate and max occupancy
    def __repr__(self):
        return 'Rate: ₹{0.rate}/night | Max Occupancy: {0.max_occupancy} person(s)'.format(self)


# Concrete Room: Standard
class StandardRoom(HotelRoom):
    def set_rate(self):
        self.rate = 2000

    def set_max_occupancy(self):
        self.max_occupancy = 2

    def __str__(self):
        return "Standard Room"


# Concrete Room: Deluxe
class DeluxeRoom(HotelRoom):
    def set_rate(self):
        self.rate = 3500

    def set_max_occupancy(self):
        self.max_occupancy = 3

    def __str__(self):
        return "Deluxe Room"


# Concrete Room: Suite
class SuiteRoom(HotelRoom):
    def set_rate(self):
        self.rate = 6000

    def set_max_occupancy(self):
        self.max_occupancy = 4

    def __str__(self):
        return "Suite Room"


# Base class for custom room types (not inheriting from HotelRoom)
class CustomRoom:
    def __repr__(self):
        return 'Rate: ₹{0.rate}/night | Max Occupancy: {0.max_occupancy} person(s)'.format(self)


# Custom implementation for Penthouse, without automatic initialization
class Penthouse(CustomRoom):
    def set_rate(self):
        self.rate = 10000

    def set_max_occupancy(self):
        self.max_occupancy = 6


# Generic builder function to construct any room that follows the CustomRoom style
def construct_room(cls):
    """
    Builder-like method to initialize and return a room object
    It ensures that the rate and occupancy are properly set.
    Used especially for classes like Penthouse that don't auto-init.
    """
    room = cls()  # Instantiate the room
    room.set_rate()  # Set the pricing
    room.set_max_occupancy()  # Set occupancy
    return room


# Main execution block (used when this script is run directly)
if __name__ == "__main__":

    # Create and print Standard Room instance
    std = StandardRoom()
    print("Standard:", std)
    print(std)

    # Create and print Deluxe Room instance
    deluxe = DeluxeRoom()
    print("Deluxe:", deluxe)
    print(deluxe)

    # Create and print Suite Room instance
    suite = SuiteRoom()
    print("Suite:", suite)
    print(suite)

    # Manual creation and setup of a Penthouse instance (custom logic required)
    penthouse = Penthouse()
    penthouse.set_rate()
    penthouse.set_max_occupancy()
    print(penthouse)

    # Dynamic creation of a Penthouse using builder function (cleaner approach)
    penthouse = construct_room(Penthouse)
    print("Penthouse (Custom):", penthouse)
