from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='عنوان مطلب',widget=forms.TextInput(attrs={'class':'form-control'}))
    body = forms.CharField(label='توضیحات',widget=forms.Textarea(attrs={'class':'form-control'}))