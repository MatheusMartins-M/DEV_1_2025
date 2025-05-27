from django.shortcuts import render
from django.views import View
from DEV_1_2025.forms import ContactForm

class ContactView(View):
    @staticmethod
    def get(request):
        form = ContactForm()
        context = {
            'form': form
        }

        return render(request, 'contact/page_contact.html', context)

    @staticmethod
    def post(request):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get("subject")
            sender = form.cleaned_data.get("sender")
            message = form.cleaned_data.get("message")
            cc_myself = form.cleaned_data.get("cc_myself")

            print("Subject: ", subject)
            print("Sender: ", sender)
            print("Message: ", message)
            print("CC Myself: ", cc_myself)

            recipients = ["2022012834@aluno.restinga.ifrs.edu.br"]
            if cc_myself:
                recipients.append(sender)

            #TODO: Configurar o settings.py com as as credenciais para envio do email
            #chamada para enviar email
            #send_mail(subject, message, sender, recipients)

            context = {
                'recipients': recipients,
                'form': form,
            }
            return render(request, 'contact/thanks.html', context)

        context = {
            'form': form
        }
        return render(request, 'contact/page_contact.html', context)