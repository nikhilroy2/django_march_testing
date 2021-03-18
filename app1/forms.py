from django import forms
from .models import CRUD_Create
class create_forms(forms.ModelForm):
    class Meta:
        model = CRUD_Create
        fields = "__all__"