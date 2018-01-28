from django import forms


class UserModelForm(forms.Form):
        UserEmail=forms.EmailField(required=True)
        UserPassword=forms.CharField(max_length=30,required=True)

