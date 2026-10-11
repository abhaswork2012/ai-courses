from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"
    
# https://www.staffcoder.com/questions/10055?step=5a49da7d-07b1-4acd-ac84-c7fec5bd8b33