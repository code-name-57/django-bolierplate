from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

class Brand(models.Model):
    # Appear as Loloi
    name = models.CharField(max_length=30)
    website = models.CharField(max_length=50)

class Collections(models.Model):
    # Appear as Alvita
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    brand = models.ForeignKey(Brand, on_delete=CASCADE, null=True)
    pile_count = models.IntegerField()
    pile_length = models.DecimalField(decimal_places=2, max_digits=5)

class Design(models.Model):
    # Appear as 6208B
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    collection = models.ForeignKey(Collections, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class Color(models.Model):
    # Appear as Beige/Cream
    primary_color = models.CharField(max_length=10)
    texture_color = models.CharField(max_length=10)

class Size(models.Model):
    SHAPE_CHOICES = (
    (1, 'Rectangle'),
    (2, 'Oval'),
    (3, 'Round'),
    )
    # Constants in Model class
    RECTANGLE = 1
    OVAL = 2
    ROUND = 3
    shape = models.CharField(max_length=20,
                choices=SHAPE_CHOICES,
                default=RECTANGLE)
    length = models.DecimalField(decimal_places=2, max_digits=5)
    width = models.DecimalField(decimal_places=2, max_digits=5)
class Carpet(models.Model):
    design = models.ForeignKey(Design, on_delete=models.CASCADE, null = True)
    color = models.ForeignKey(Color, on_delete=CASCADE, null = True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null = True)
    image_file = models.FileField(upload_to='carpets/', null=True)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return (f"{self.name}: {str(self.image)} - "
                f"{self.color} color of "
                f"{self.pattern} pattern "
                f"in the {self.design}")

    def in_stock(self):
        return self.inventory > 0
