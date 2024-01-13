from django.contrib.auth.models import User
from django import forms

class MyUserCreationForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        firs_name = cleaned_data.get("firs_name")
        last_name = cleaned_data.get("last_name")
        if not firs_name and not last_name:
            raise forms.ValidationError('Заполните Имя и Фамилию!')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']