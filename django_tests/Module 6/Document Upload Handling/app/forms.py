from django import forms
class ApplicationForm(forms.Form):
    """An application with its supporting document.
    ``applicant`` is declared. The document field, and the two rules it has
    to enforce, are not.
    """
    applicant = forms.CharField()
    # Write your code here