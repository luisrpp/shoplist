# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.mail import mail_admins
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from shoplist.contact.forms import ContactForm

def contact(request):
    """Shows the contact form in order to send an e-mail to administrators if the method is get
       Sends an e-mail to the admistrators if the method is post  
    """
    form = None;
    blnmsgsent = False;
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            emailfrom = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            #TODO create a template for the message
            #TODO sent the message using some kind of asynchronous processing
            mail_admins('Contato Site - ShopList', message);
            messages.add_message(request, messages.SUCCESS, 'Mensagem enviada!')
            return HttpResponseRedirect(reverse('contact:contact'))
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html',locals())

