from django.db import models
class ItemQuerySet(models.QuerySet):
    def alphabetical(self):
        # Write your code here
        return self.order_by('name')
    def newest_first(self):
        # Write your code here
        return self.order_by('-created_at','name')
    def top(self, n):
        # Write your code here
        return self.newest_first()[:n]
    def report(self, n=5):
        # Write your code here
        return self.newest_first().values('name','price')[:n]
    def names(self):
        # Write your code here
        return self.newest_first().values_list('name',flat=True)
        
class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField()
    objects = ItemQuerySet.as_manager()
    def __str__(self):
        return self.name

# https://www.staffcoder.com/paths/django/querysets-and-orm-basics/ordered-result-shaping