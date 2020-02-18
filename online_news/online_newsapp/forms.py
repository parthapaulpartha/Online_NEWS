from django import forms
from django.contrib.auth.models import User

from .models import note

# ----------- Note pad Form --------
class NoteForm(forms.ModelForm):
    class Meta:
        model = note
        fields = [
            'note_text',
        ]