from django.db import models
from django.contrib.auth.models import User
from brands.models import Product
import random
import string


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=250, null=True)

    def __str__(self):
        return str(self.transaction_id)

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            self.transaction_id = self.generate_transaction_id(self.user_id)
        return super().save(*args, **kwargs)

    @staticmethod
    def generate_transaction_id(user_id):
        user = User.objects.get(id=user_id) if user_id else None
        username = user.username if user else ''  # Get the username if the user exists
        max_length = max(8, min(12, 12 - len(username)))  # Calculate the maximum length for the random part

        random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=max_length))
        transaction_id = random_part + "-" + username
        return transaction_id

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.shoe_name

    @property
    def get_total(self):
        total_price = self.product.shoe_price * self.quantity
        return total_price


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    country = models.CharField(max_length=250, null=True, default="Kenya")
    address = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250, null=True)
    state = models.CharField(max_length=250, null=True)
    zip_code = models.CharField(max_length=250, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

