from django import forms
from hellodjango.bootstrap.widgets import (
    TextInput
)

class CharField(forms.CharField):
    widget = TextInput
