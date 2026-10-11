from django.db import models

class Product(models.Model):
    # Write your code here
    name = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        # Write your code here
        raise NotImplementedError
