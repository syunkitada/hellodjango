from django import forms

class TextInput(forms.TextInput):
    def __init__(self, attrs=None):
        base_attrs = { 'class': 'form-control' }
        if attrs:
            attrs.update(base_attrs)
        else:
            attrs = base_attrs
        attrs = {}
        super(TextInput, self).__init__(attrs={'class': 'form-control'})
