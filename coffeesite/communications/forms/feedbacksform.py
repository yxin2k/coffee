from django import forms
from communications.models import Submissions, ContentType

class SubmissionForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter your name")
    email = forms.EmailField(max_length=254, help_text="Please enter your email")
    description = forms.CharField(widget=forms.Textarea, help_text="Description")
    contentType = forms.ModelChoiceField(queryset=ContentType.objects.all())

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Submissions
        fields = ('name', 'email', 'description', 'contentType')

