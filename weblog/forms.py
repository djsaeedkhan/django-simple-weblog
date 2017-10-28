from django import forms
from weblog.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
    title = forms.CharField(label='عنوان مطلب',widget=forms.TextInput(attrs={'class':'form-control'}))
    body = forms.CharField(label='توضیحات',widget=forms.Textarea(attrs={'class':'form-control'}))