from django.db import models
from user.models import UserModel
# Create your models here.


class CategoryModel(models.Model):
    category = models.CharField(max_length=20)
    def __str__(self):
        return  self.category


class ProductModel(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    image = models.TextField()
    discription = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    def __str__(self):
        return  self.name


class OrderStatusModel(models.Model):
    order_status = models.CharField(max_length=20)
    def __str__(self):
        return  self.order_status


class ProductOrderModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    count = models.IntegerField()


class UserOrder(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product_order = models.ForeignKey(ProductOrderModel, on_delete=models.CASCADE)
    address = models.TextField()
    order_date = models.DateField()
    total_price = models.IntegerField()
    discount = models.IntegerField()
    result_price = models.IntegerField()
    available = models.BooleanField()
    status = models.ForeignKey(OrderStatusModel, on_delete=models.CASCADE)
