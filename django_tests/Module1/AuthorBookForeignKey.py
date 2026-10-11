from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        ordering = ["name"]
    def __str__(self):
        return self.name
class Publisher(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        ordering = ["name"]
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    # Write your code here