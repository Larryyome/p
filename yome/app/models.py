from django.db import models

# Create your models here.

#creating a table people
class People(models.Model):
    username = models.CharField(max_length=222)
    name = models.CharField(max_length=222)
    email= models.EmailField()
    time = models.DateTimeField(auto_now_add=True)

#returning the username for people
    def __str__(self):
        return self.username
    
#creating a table address
class Address(models.Model):
    State = models.CharField(max_length=222)
    city  = models.CharField(max_length=222)
    user = models.OneToOneField(People, on_delete=models.CASCADE)

#returning the state for address
    def __str__(self):
        return self.State
    
#creating a table bio    
class Bio(models.Model):
    bio= models.CharField(max_length=333)
    user2 = models.OneToOneField(People, on_delete=models.CASCADE)

#returning the bio for Bio    
    def __str__(self):
        return self.bio
    
#creating a table doctor    
class Doctor(models.Model):
    doctor_name= models.CharField(max_length=333)
    user3 = models.OneToOneField(People, on_delete=models.CASCADE)

#returning the doctor name   
    def __str__(self):
        return self.doctor_name
    

#creating a table product    
class Product(models.Model):
    product_name=models.CharField(max_length=50)
    price=models.FloatField( default=1)
    quatity= models.IntegerField( default=2)
    
#returning the product name   
    def __str__(self):
        return self.product_name
