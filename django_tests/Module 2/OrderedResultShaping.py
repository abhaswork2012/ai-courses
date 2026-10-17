from django.db import models
class ItemQuerySet(models.QuerySet):
    def alphabetical(self):
        # Write your code here
        raise NotImplementedError
    def newest_first(self):
        # Write your code here
        raise NotImplementedError
    def top(self, n):
        # Write your code here
        raise NotImplementedError
    def report(self, n=5):
        # Write your code here
        raise NotImplementedError
    def names(self):
        # Write your code here
        raise NotImplementedError
class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField()
    objects = ItemQuerySet.as_manager()
    def __str__(self):
        return self.name