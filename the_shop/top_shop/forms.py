from .models import Message
from django import forms


class MessageForm(forms.ModelForm):
    first_name = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=500, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Message
        fields = ('first_name', 'last_name', 'email', 'message')