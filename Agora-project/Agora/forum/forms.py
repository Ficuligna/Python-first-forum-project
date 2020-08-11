from django import forms
from .models import Discussione, Post

class FormDiscussione(forms.ModelForm):
    contenuto = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Inserisci il testo del post"}))

    class Meta:
        model = Discussione
        fields = ["titolo","contenuto"]

class AggiungiRisposta(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["testo"]
