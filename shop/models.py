from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    name = models.CharField(max_length=20)
    shop_l = models.ManyToManyField(Category, through='Order', related_name='shop_p')

    def __str__(self):
        return f'{self.category.name} {self.name}'


class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.item.name} {self.quantity.name}'




