from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# OneToOne = user can only have one customer & Customer can only have one user
# on_delete = deletes the item if the users item is deleted


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
        
# this returns an empty image when pic is deleted instead of error


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '' 
        return url   


# digital=if its digital we dont ship it.physical we ship
# # when addx the imagefield you must instal a library called pillow
# pip3 install pillow to install

# foreignkey=customer can have more than 1 order
# if complete=False=we can add more item, True=closes order
# order=relaship b/n the cus & order.cus can have more than 1 order
# b/c id is interger we return in a string str


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.transaction_id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,
                                 null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


           