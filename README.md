# Findbyid

### What is It?
The ```findbyid``` utility is a package that can keep track of all objects that are created from a class that inherits from the ```findbyid.FindByIDFactory```  metaclass.
It creates automatically a specific _ID_ for the instance-in-question and provides ```classmethod```s to retrieve the object later by its _ID_.

### What Should I use if For?

Let's say that we have a web server and a client. 
The server provides the client and interface to an object and needs 
to pass the client a reference to the object of which interface the client is using. 
Without the ```findbyid``` package, 
the only way would be to serialize the object and send it to the client somehow. 
Not only would that be not very practical in terms of the amount of network traffic, 
but also it would make dynamic changes to the object impossible. 
With the ```findbyid``` module though, we can just pass the _reference ID_ to the client.
That way the client can access the object by its _ID_, 
so that the actual data doesn't need to be carried over.

It is also handy when you have to access a certain object 
from two different contexts: you just pass the _ID_ instead of 
the whole object to the other context.


### How do I use It?
The usage of the package is simple:
```python
import findbyid

class ExampleClass(findbyid.FindByIDFactory):
    def __init__(self, example_val):
        super().__init__()

        self.example_val = example_val

    ...

instance = ExampleClass("Foo")
print(instance.ID)
print(instance is ExampleClass.findByID(instance.ID))
```
---
```bash
>>> 98658
>>> True
```
 The _ID_ is random so do not be confused if your _ID_ is different.


### In-depth Look

#### Method signatures and such
* ```def __init__(self: object, *args, **kwargs) -> None```  
    All subclasses need to call the instantiator for the utility to work properly.


* ```def findByID(cls, ID: int) -> object:```  
    Returns an object with the given _ID_. If no object is found, a ```NotFoundException``` is raised.  
    ```@classmethod```.

* ```def getInstances(cls) -> list[object]:```  
    Returns all objects of a class.  
    ```@classmethod```.
* ```ID```  
    The specific tag that is assigned to every instance of a class inheriting from the ```findbyid.FindByIDFactory``` metaclass.
 
 ### Features to be Added
 * A possibility to be able to serialize and save an object to disk and retrieve it using
 the same ways that it is done currenty with RAM.
 
