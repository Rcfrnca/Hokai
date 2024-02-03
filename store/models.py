from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=250, null=True)
    email = models.EmailField(max_length=250, blank=True)
    address = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.date_created}'

class Camera(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250, null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.name

class Lens(models.Model):
    lens_name = models.CharField(max_length=100, null=True)
    product_name = models.ManyToManyField(Product)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.lens_name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered'),
    )
    product_name = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    lens = models.ForeignKey(Lens, null=True, on_delete=models.SET_NULL)  # Corrected case of Lens
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=250, null=True)
    phone = models.IntegerField(null=True)  # Removed max_length for IntegerField
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return f'{self.customer} {self.product_name}'