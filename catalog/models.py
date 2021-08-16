from enum import unique
from django.db import models
from django.contrib import admin
from django.db.models import constraints
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

from django.utils.safestring import mark_safe


class Brand(models.Model):
    # Appear as Loloi
    name = models.CharField(max_length=30, unique=True)
    website = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.name

class Size(models.Model):
    SHAPE_CHOICES = (
    ('D', 'Rectangle'),
    ('R', 'Runner'),
    ('C', 'Round'),
    )
    # Constants in Model class
    RECTANGLE = 'D'
    shape = models.CharField(max_length=20,
                choices=SHAPE_CHOICES,
                default=RECTANGLE)
    length = models.DecimalField(decimal_places=2, max_digits=8)
    width = models.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['length', 'width', 'shape'], name="unique_size_t")]

    def __str__(self):
        return (f"{str(self.width)} ft x {str(self.length)} ft {self.shape}")

class Color(models.Model):
    # Appear as Beige/Cream
    primary_color = models.CharField(max_length=20)
    texture_color = models.CharField(max_length=20, blank=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['primary_color', 'texture_color'], name="unique_color_t")]

    def __str__(self):
        return (f"{self.primary_color}_{self.texture_color}")


class Collection(models.Model):
    # Appear as Alvita
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=CASCADE, null=True)
    pile_count = models.IntegerField(blank=True, null=True)
    pile_length = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)

    available_sizes = models.ManyToManyField(Size)

    def __str__(self):
        return self.name

class Design(models.Model):
    # Appear as 6208B
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True)

    available_colors = models.ManyToManyField(Color, through='DesignInColor')

    def __str__(self):
        return self.name
from django.conf import settings

def GetImagePath(dic):
    print(settings.MEDIA_ROOT)
    print(dic.design.collection.name)
    print(dic.design.name)
    print(dic.color)
    return()

import pathlib

def design_image_path(instance, filename):
    return 'catalog/DesignColor/{0}/{1}_{2}{3}'.format(instance.design.collection.name, instance.design.name, instance.color, pathlib.Path(filename).suffix)

import os
import re
from django.conf import settings

def get_default_image(design, color):
    mediaDir = str(settings.MEDIA_ROOT) + 'catalog/DesignColor'
    # print(mediaDir)
    # breakpoint()
    collectionDir = mediaDir + '/{0}'.format(design.collection.name)
    regexExp = '({0})+.({1})'.format(color.primary_color, color.texture_color)
    print(regexExp)
    regex = re.compile(regexExp)
    for root, dirs, files in os.walk(mediaDir):
        for file in files:
            # print(file)
            if re.search(design.name[:-1], file, re.IGNORECASE):
                if re.search(regexExp, file, re.IGNORECASE):
                    # if re.search(color.texture_color, file, re.IGNORECASE):
                    print("FOUND")
                    return os.path.join(root, file)
    # return 'catalog/DesignColor/{0}/{1}_{2}.{3}'.format(design.collection.name, design.name, color, "jpg")
    return None
    # breakpoint()

class DesignInColor(models.Model):
    design = models.ForeignKey(Design, on_delete=models.CASCADE, null = True)
    color = models.ForeignKey(Color, on_delete=CASCADE, null = True)
    image_file = models.ImageField(upload_to=design_image_path, blank=True, null=True)

    def __str__(self):
        return (f"({str(self.design.collection)}) "
                f"{self.design} in "
                f"{self.color}")

    def image_tag(self):
        if self.image_file:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image_file.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    class Meta:
        constraints = [models.UniqueConstraint(fields=['design', 'color'], name="unique_design_color_t")]

    # def save(self, *args, **kwargs):
    #     if(not self.image_file):
    #         self.image_file.name = get_default_image(self.design, self.color)
    #         # breakpoint()
    #     super(DesignInColor, self).save(*args, **kwargs)
    #     # breakpoint()

class Carpet(models.Model):
    designColor = models.ForeignKey(DesignInColor, on_delete=models.CASCADE, null = True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null = True)
    image_file = models.ImageField(upload_to='catalog/DesignColorSize', null=True)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return (f"({str(self.designColor)} - {self.size}) ")

    def in_stock(self):
        return self.inventory > 0

    def image_tag(self):
        if self.image_file:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.image_file.url)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'

    class Meta:
        constraints = [models.UniqueConstraint(fields=['designColor','size'], name="unique_ein_t")]
