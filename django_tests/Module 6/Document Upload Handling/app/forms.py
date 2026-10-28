from django import forms
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
def validate_file_size(file):
    max_size = 2 * 1024 * 1024  # 5 MB
    if file.size > max_size:
        raise ValidationError("The document must be 2 MB or smaller.")
class ApplicationForm(forms.Form):
    """An application with its supporting document.
    ``applicant`` is declared. The document field, and the two rules it has
    to enforce, are not.
    """
    applicant = forms.CharField()
    # Write your code here
    document = forms.FileField(validators=[
            FileExtensionValidator(allowed_extensions=["pdf"],message="Only PDF files are accepted."),
            validate_file_size,
        ],)