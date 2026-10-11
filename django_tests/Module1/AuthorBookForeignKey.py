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
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books"
    )
    publisher = models.ForeignKey(
        Publisher, on_delete=models.PROTECT, null=True, blank=True
    )
    class Meta:
        ordering = ["title"]

#https://www.staffcoder.com/questions/10056?step=41cb91ff-b06e-427d-a044-741d6587e76c