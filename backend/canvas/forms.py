from django.forms import ModelForm

from .models import Canvas


class CanvasForm(ModelForm):
    class Meta:
        model = Canvas
        fields = ['name']