from django.db import models

# Create your models here.
# Constructor to initialize the attributes (members)
class Product(models.Model):
    name=models.CharField(max_length=100)  # Member variable (attribute)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
  
    # Member function (method) 
    def __str__(self):
        return self.name
    
 
class Customer:
    # Constructor (initializer) to initialize object state
    def __init__(self, name, email, contactnumber):
        # The self keyword refers to the current instance of the object
        self.name = name    # Setting the name of the Customer
        self.email = email
        self.contactnumber = contactnumber
    
    # toString method (called when printing the object or converting it to a string)
    def __str__(self):
        return f"{self.name}"

"""
    #Destructor to perform cleanup when the object is deleted
    def __del__(self):
        print(f"Customer object {self} is being destroyed.")

    # Getter method for 'name'
    def get_name(self):
        return self.name

    # Setter method for 'name'
    def set_name(self, new_name):
        self.name = new_name
    
    # Delete the Customer object (destructor is automatically called)
    del object_name

"""