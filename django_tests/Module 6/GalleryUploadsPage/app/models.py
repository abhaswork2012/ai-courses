from django.db import models
class Photo(models.Model):
    """One gallery photo.
    ``title`` is given. The image is not.
    """
    title = models.CharField(max_length=200)
    # Write your code here
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="gallery/%Y/%m/",blank=True)
    def __str__(self):
        return self.title