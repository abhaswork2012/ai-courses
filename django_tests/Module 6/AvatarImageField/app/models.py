from django.db import models
class Profile(models.Model):
    """A member profile.
    ``display_name`` is given. The avatar is not: the page has nothing to
    show and nothing to fall back from.
    """
    display_name = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to="avatars/", blank=True)
    # Write your code here
    def __str__(self):
        return self.display_name