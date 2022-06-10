from django.contrib import admin
from user.models import *
from product.models import *
# Register your models here.

admin.site.register(UserModel)
admin.site.register(ProductModel)
admin.site.register(ProductOrderModel)
admin.site.register(CategoryModel)
admin.site.register(OrderStatusModel)
admin.site.register(UserOrder)