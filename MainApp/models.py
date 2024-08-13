from django.db import models

# Create your models here.

class Color(models.Model):
   name = models.CharField(max_length=32)

   def __repr__(self) -> str:
      return f"Color({self.name})"

class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   count = models.PositiveIntegerField()
   descr = models.TextField(max_length=200, default='здесь должно быть описание')
   colors = models.ManyToManyField(to=Color)

   def __repr__(self) -> str:
      return f"Item({self.name})"

