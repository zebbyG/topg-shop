from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ['comment']
