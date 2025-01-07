# CSE3130 - Object Oriented programming 2 - Notes
## Why Object oriented Programming?

1.__Encapsulation__ is the process of protecting or hiding data through the implemenation of an _interface_. The interface is often a collection of methods, such as setter (modifier) and getter (accesor) methods, that other objects can itneract with that object.
    - A televesion encapsulates all the hardware and software into a small box which the user interacts through an interface of only a few buttons on a remote control.
    - It is important to emphasize the need for setter and getter mehtods and how each of the attributes in the class should have a setter or getter method if it is accessible outside of the object.
2. __Abstraction__ is the process of setting the level of detail and complexity to what is appropriate for the given task.
    - A driver only needs to interact with the steering, accelerator, and brakes of a car to drive. But a mechanic has a much more complex understanding of the car in order to repair and maintain it. Therefore, the mechanic's abstraction of the car is more complex than the driver's.

3 and 4 are in last unit's notes

5. __Inheritance__ is the process where one class inherits attributes and methods from another class. While some languages, like Java, prohibit it, classes can inherit from multiple parent classes. However, this process of multiple inheritences is often avoided because of potential conflicts from duplucate attribute or method names.
    - Inheritance describes as Is-A relationship.
        - The _deck_ __is a__ _group of cards_, but the _deck_ is not a _hand_.
        - __Abstract Classes__ (as opposed to concrete classes) are classes that are never instantiated by themselves, but are written soley for the purpose of inheritance. Oftentimes, these classes have __abstract methods__ which cannot be fully called within the Abstract Class, but relies on data of the subclasses.
        - Beginner mistakes include looking for inheritance, where classes inherit several levels deep. Inheritance often reveals itself in the design process.

6. __Polymorphism__ is the ability to treat a class method differently. The subclass often will refactor the statements for the method.

```python
class Animal:

    def getCry():
        return ""

class Dog(Animal):

    def getCry():
        return "Woof"

class Cat(Animal):

    def getCry():
        return "Meow"

```