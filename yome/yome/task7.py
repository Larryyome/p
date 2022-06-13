from app.models import Product

#insert a new record
product1=Product(product_name="hair r", price=900, quatity=1)

#saving the new product to database
product1.save()

#printing out all the object in Product
Product.objects.all()

#printing a particular product 
product1.product_name

#filter the product name hair r
Product.objects.filter(product_name="hair r")



