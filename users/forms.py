from django import forms
from users.models import User
from django_countries.widgets import CountrySelectWidget

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'first_name', 'last_name', 'birth_date', 'gender', 'bio', 'location', 'phone_number', 'website', 'is_private']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={'rows': 3}),
            'location': CountrySelectWidget(layout='{widget}'),
        }

class UserReadonlyForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birth_date', 'gender', 'bio', 'location', 'phone_number', 'website']
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.TextInput(),
            'bio': forms.Textarea(attrs={'rows': 3, 'readonly': 'readonly', 'class': 'form-control-plaintext'}),
            'location': CountrySelectWidget(layout='{widget}', attrs={"disabled": "true"}),
            'phone_number': forms.TextInput(),
            'website': forms.TextInput(),
        }