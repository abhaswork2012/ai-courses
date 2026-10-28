from django import forms
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
def validate_file_size(file):
    max_size = 1 * 1024 * 1024  # 5 MB
    if file.size > max_size:
        raise ValidationError("The image must be 1 MB or smaller.")
class PhotoForm(forms.Form):
    """The upload form.
    ``title`` is declared. The image field and its two rules are not.
    """
    title = forms.CharField()
    image = forms.ImageField(validators=[FileExtensionValidator(['png','jpg','jpeg'],message='Only PNG and JPEG images are accepted.'),validate_file_size])