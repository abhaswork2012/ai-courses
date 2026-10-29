from django.db import models
from django.urls import reverse
class Article(models.Model):
    """One article.
    The fields are given. What the model cannot yet answer is where one of
    its instances lives on the site.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    published_on = models.DateField()
    # Write your code here
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"slug": self.slug})