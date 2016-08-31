# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import send_mail
from django.conf import settings # esta maneira acessamos o settings.py com todas as constantes. esta é melhor pratica para pegar ele.
# se fizermos import settings ele iria importar só as constantes do arquivo sem as configurações do django

from simplemooc.core.mail import send_mail_template



class ContactCourse(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='messagem/Dúvida', widget=forms.Textarea) # desta forma montamos um Textarea


    def send_mail(self, course):
        subject = '[{}] Contato'.format(course)

        context = {
            'name':self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message']
        }


        template_name = 'courses/contact_email.html'
        send_mail_template(
                subject, template_name, context,
                [settings.CONTACT_EMAIL]
            )
