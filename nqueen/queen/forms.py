from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    board_size = forms.IntegerField(widget= forms.NumberInput(attrs={'class':'form-control','placeholder': 'Enter Board Size*'}))
    
    class Meta:
        model = Board
        fields = [
                "board_size",
            ]