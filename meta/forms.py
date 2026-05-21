from django import forms

FOOD_CHOICES = [
    ('pizza', 'Pizza'),
    ('burger', 'Burger'),
    ('pasta', 'Pasta'),
]

class CustomerForm(forms.Form):
    name = forms.CharField(label="Customer Name", max_length=100)
    email = forms.EmailField(label="Email Address")
    age = forms.IntegerField()
    reservation_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    favorite_food = forms.ChoiceField(choices=FOOD_CHOICES, widget=forms.RadioSelect)
    