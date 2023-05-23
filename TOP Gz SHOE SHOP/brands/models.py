from django.db import models


class Brands(models.Model):
    brand_name = models.CharField(max_length=256)
    brand_description = models.TextField()
    no_of_shoes_available = models.PositiveIntegerField()
    brand_in_stock = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand_name


class Color(models.Model):
    color_name = models.TextField(max_length=50)

    def __str__(self):
        return self.color_name


class Jordan(models.Model):
    shoe_image = models.ImageField(upload_to='jordans/', height_field='image_height', width_field='image_width')
    image_height = models.PositiveIntegerField(blank=True, null=True)
    image_width = models.PositiveIntegerField(blank=True, null=True)
    shoe_name = models.CharField(max_length=256)
    shoe_gender = models.TextField()
    shoe_color_available = models.ManyToManyField(Color)
    shoe_price = models.DecimalField(decimal_places=2, max_digits=9)
    shoe_in_stock = models.BooleanField(default=False)
    shoe_price_was = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=9)
    shoe_time_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shoe_name
