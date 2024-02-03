from django.contrib import admin
from .models import Customer
from .models import Camera
from .models import Product
from .models import Lens
from .models import Order




admin.site.register(Customer)
admin.site.register(Camera)
admin.site.register(Product)
admin.site.register(Lens)
admin.site.register(Order)