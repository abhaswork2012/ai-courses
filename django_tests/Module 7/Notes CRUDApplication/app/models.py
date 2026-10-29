from django.conf import settings
from django.db import models
from django.urls import reverse
class Note(models.Model):
    """One note, belonging to whoever wrote it.
    The fields and the owner are given. What the model cannot yet answer is
    where one of its instances lives on the site.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    created_on = models.DateField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              related_name="notes")
    def get_absolute_url(self):
        return reverse("note-detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title