from django.db import models
from django.contrib import admin
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

from django.utils.safestring import mark_safe


class Brand(models.Model):
    # Appear as Loloi
    name = models.CharField(max_length=30)
    website = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Size(models.Model):
    SHAPE_CHOICES = (
    ('Rectangle', 'Rectangle'),
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

    def __str__(self):
        return (f"{str(self.width)} ft x {str(self.length)} ft {self.shape}")

class Color(models.Model):
    # Appear as Beige/Cream
    primary_color = models.CharField(max_length=10)
    texture_color = models.CharField(max_length=10)

    def __str__(self):
        return (f"{self.primary_color} / {self.texture_color}")


class Collection(models.Model):
    # Appear as Alvita
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    brand = models.ForeignKey(Brand, on_delete=CASCADE, null=True)
    pile_count = models.IntegerField()
    pile_length = models.DecimalField(decimal_places=2, max_digits=5)

    available_sizes = models.ManyToManyField(Size)

    def __str__(self):
        return self.name

class Design(models.Model):
    # Appear as 6208B
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True)

    available_colors = models.ManyToManyField(Color)

    def __str__(self):
        return self.name



class Carpet(models.Model):
    design = models.ForeignKey(Design, on_delete=models.CASCADE, null = True)
    color = models.ForeignKey(Color, on_delete=CASCADE, null = True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null = True)
    image_file = models.FileField(upload_to='carpets/', null=True)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return (f"({str(self.design.collection)}) "
                f"{self.design} "
                f"{self.color} -"
                f"({self.size})")

    def in_stock(self):
        return self.inventory > 0

    def image_tag(self):
        if self.image_file:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image_file.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'


