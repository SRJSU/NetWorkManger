from django import forms


class UserModelForm(forms.Form):
        UserEmail=forms.EmailField(required=True)
        UserPassword=forms.CharField(max_length=30,required=True)

class UserInfoForm(forms.Form):
        UserEmail = forms.EmailField(required=True)
        UserPassword = forms.CharField(max_length=30, required=True)
        PhoneNum=forms.CharField(max_length=30,required=True)
        Introduction=forms.TextInput()