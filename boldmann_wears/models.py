from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import User


CATEGORY = (
    ("Boots", "Boots"),
    ("Monkstrap", "Monkstrap"),
    ("Brogues", "Brogues"),
    ("Leather slides", "Leather slides"),
    ("Oxfords", "Oxfords"),
    ("Loafers", "Loafers"),
    ("Leather mules", "Leather mules"),
)

LABEL = (
    ("New Arrival", "New Arrival"),
    ("Out of Stock", "Out of Stock"),
)
class Bolducts(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	image = models.ImageField(upload_to='static/product_listed_image' , blank=True, null=True)
	date_added = models.DateTimeField(auto_now_add=True)
	discount_price = models.FloatField(blank=True, null=True)
	category = models.CharField(choices=CATEGORY, max_length=50)
	label = models.CharField(choices=LABEL, max_length=50)
	description = models.TextField()
	show_boots = models.BooleanField()
	
	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse("boldmann_wears:product", kwargs={ 
			"pk" : self.pk
		})
		
	def get_add_to_cart_url(self):
		return reverse("boldmann_wears:add_to_cart", kwargs={
			"pk" : self.pk
		})
		
	def get_remove_from_cart_url(self):
		return reverse("boldmann_wears:remove_from_cart", kwargs={
			"pk" : self.pk
		})


# class Item(models.Model):
    # item_name = models.CharField(max_length=100)
    # price = models.FloatField()
    # discount_price = models.FloatField(blank=True, null=True)
    # category = models.CharField(choices=CATEGORY, max_length=2)
    # label = models.CharField(choices=LABEL, max_length=2)
    # description = models.TextField()

    # def __str__(self):
        # return self.item_name

    # def get_absolute_url(self):
        # return reverse("core:product", kwargs={
            # "pk" : self.pk
        
        # })

    # def get_add_to_cart_url(self):
        # return reverse("core:add-to-cart", kwargs={
            # "pk" : self.pk
        # })

    # def get_remove_from_cart_url(self):
        # return reverse("core:remove-from-cart", kwargs={
            # "pk" : self.pk
        # })

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Bolducts, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_discount_item_price()
        return self.get_total_item_price()
    
    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

# Create your models here.

