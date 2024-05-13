from django import forms


class TodoCreateForm(forms.ModelForm):
    title = forms.CharField()
    body = forms.CharField()
    created = forms.DateTimeField()
