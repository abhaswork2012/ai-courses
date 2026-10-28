from django import forms
class PhotoForm(forms.Form):
    """The upload form.
    ``title`` is declared. The image field and its two rules are not.
    """
    title = forms.CharField()
    # Write your code here