from django import forms
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .models import Msg

class MsgCreateForm(forms.Form):
    title = forms.CharField(label='Title', max_length=120)
    content = forms.CharField(label='Content', widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        try:
            Msg.objects.get(title=title)
        except ObjectDoesNotExist:
            return title
        raise forms.ValidationError('The title have existed.')
