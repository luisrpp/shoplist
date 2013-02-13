# -*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder':'Digite o seu nome...'}))
    email = forms.EmailField(label="E-mail", required=True, widget=forms.TextInput(attrs={'placeholder':'Digite o seu e-mail...'}))
    message = forms.CharField(label="Mensagem", widget=forms.Textarea(attrs={'placeholder':'Digite a mensagem...', 'style': 'width:300px', 'rows': 10}))


    


    