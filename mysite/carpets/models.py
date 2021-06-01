from django.db import models
from django.db.models.base import Model

class Design(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Carpet(models.Model):
    color = models.CharField(max_length=30)
    pattern = models.IntegerField()
    design = models.ForeignKey(Design, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    image_file = models.FileField(upload_to='carpets/', null=True)

    length = models.DecimalField(decimal_places=2, max_digits=5)
    width = models.DecimalField(decimal_places=2, max_digits=5)

    thread_count = models.IntegerField()
    thread_length = models.DecimalField(decimal_places=2, max_digits=5)

    inventory = models.IntegerField(default=0)

    def __str__(self):
        return (f"{self.name}: {str(self.image)} - "
                f"{self.color} color of "
                f"{self.pattern} pattern "
                f"in the {self.design}")

    def in_stock(self):
        return self.inventory > 0


