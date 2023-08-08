from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    title = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    comment = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ('title', 'comment')
