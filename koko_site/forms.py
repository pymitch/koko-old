from django import forms

class AddWordForm(forms.Form):
    new_word = forms.CharField(label='New Word', max_length=50)