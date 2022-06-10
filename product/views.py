from django.shortcuts import render
from .models import *

# Create your views here.


def main(request, category):
    if request.method == "GET":
        categories = CategoryModel.objects.all()
        now_category = CategoryModel.objects.get(category=category)
        product =
        return render(request, 'main.html')