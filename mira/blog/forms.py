from django import forms

class NameForm(forms.Form):
    name = forms.TextInput(max_length=50)

    return name