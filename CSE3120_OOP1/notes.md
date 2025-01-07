## Definitions
**Object-Oriented Analysis (OOA)** is the process of looking at a proble, system, or task and identifying the objects and interactions between those objects. It answers the question, *what needs to be done?*

**Object-Oriented Design (OOD)** is the process of converting the identified objects and interactions from OOA into the object behaviours. It answers the question *how things need to be done.*

**Object-Oriented Programming (OOP)* is the process of implementing the outcome of OOD into a functioning program.

A **Class** is a model of an object. Classes contain *attributes* and *behaviours* which are inherited by objects **Intantiated** from the class. Another defintiion of a class is a blueprint or template.
* An **Attribute** is a property or a characteristic an object possesses. Each object can have different values for the attribute, but all objects instantiated from the class inherits the same attributes. (the object vairables) 
* A **Behaviour** is an action that can be performed on an object. Behaviours are formally named *Methods* and are written the same as a fucntion. Therefore, methods can also accept parameters, arguments and return values.
    * One major advantage of the methods is that they automatically have access to all attributes of the object. Therefore, object attributes neither need to be passed as a parameter or globalled into the method.
    * Methods always have atleast one parameter, ```self```, which indicates that the function is refercing the current object.
        * __Constructors__ are methods that provide the object with the default set of attributes. In python it is ```self.\_\_init\_\_(self)```. Constructors create the object from the class template with values within the attributes. The constructor can have arguments passed into the object attributes upon construction. Other attributes can be set as defaults within the class.
            *In general, all attributes of the object should be present in the Contstructor, even if their default value is None.

```python
class Ex:
    def \_\_init\_\_(self):
        self.MAX = 1
        self.MIN = -1
    def \_\_init\_\_(self, MAX, MIN):
        self.MAX = MAX
        self.MIN = MIN
```
an **object** is a unique set of data and functions instantiated from a class. An object accesses attributes and methods using *dot notation,* which identifies the object, then the attribute or method.

```python
<object name>.<attribute name> Value
<object name>.<method name>(arguments)
```

## Unified Modeling Language

A standarized modelling language that unifies otational systems and approahces for data management and software design. This language is programming language agnostic and does not require a programming background to utilize. UML focuses on managing *data* and grouping that data together. It is composed of three main diagram types: Structe, Behaviour, and interactions.

NOTE: While software developers require knowledge of all three types, this program will only focs on a structure UML tables.

A class diagram is a common strucutres diagram. It contains the name of the class, the attributes, and methods of the class.

| Bank Account | |
| --- | --- |
| *Attributes* | *dataType* |
| accountNo | int |
| balance | float |
| *Methods(param)* | *return* |
| transfer(float) | float |
| withdraw(float) | float |
| deposit(float) | None |
| getBalance() | float |

each class within a program can be designed using a UML table. During the design process, developers can determine which classes will have which attributes and behaviours and map out how the objects will interact with each other (flow charts)
 . A given program should have multiple classes for multiple types of objects.
* NOTES: If a program only has one class, it indicates that the developer is still primarily programming functionally. This one object that possesses all attributes and methods of the pgoram is often called a *God Object* or a *system object*

## Why OOP?

1. **Encapsulation:** The process of protecting or hiding data through the implementation of an *interface.* The interface is often a collection of methods such as setter (modifier) and getter (accessor) methods that other objects can itneract with.
    * A television encapsulates all the hardware and software into a small box with which the user interacts through a few buttons their remote
    * It is important to emphasize the need for setter and getter methods and how each of the attributes within a class should only be accessed through setter and getter methods.
```python
class Main:
    def __init__(self):

        self.UNPROTECTED = 0
        self.__PROTECTED = 1

MAIN = Main()
print(MAIN.UNPROTECTED) # Print 0
print(MAIN.__PROTECTED) # Error: Cannot find Variable
```

2. **Abstraction:** The process of setting the level of detail and complexity to what is appropriate for the given task.
    * A driver only needs to interact with the steering, accelerator, brakes, and signals of the car to drive. but a mechanic has a much more complex understanding of the car in order to repair and maintain it. Therefore, the mechanic's abstraction of the car is more complex than the driver's.
    * To calculate a student's average, one requires the student ID, courses taken, and grades received. While a person has many more traits (heigh, hair colour, ethnicity, postal code, etc.) they are not needed for the purpose of the calculation and are therefore omitted.

3. **Aggregation:** The process of grouping objects together. objects exist independently of each other. All compositions are aggregates, but object compositions have relationships that connect objects together.
    * The students in a classroom are an aggregation of student objects.

4. **Composition:** The process of creating a complex object by collecting several smaller objects together.
    * A car is composed of an engine, transmission, starter, headlights, windshield, etc. each of the car's objects are required for the car to function properly.