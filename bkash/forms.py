from django import forms

class RecentProduct(forms.Form):
    mobile = forms.CharField(max_length=15)
    laptop = forms.CharField(max_length=50)
    email = forms.EmailField()
