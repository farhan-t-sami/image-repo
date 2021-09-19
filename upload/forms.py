from django import forms
from .models import Images

# Utilizes the attributes of Images model
class ModelFormWithFileField(forms.ModelForm):
    class Meta:
        model = Images
        fields = '__all__'