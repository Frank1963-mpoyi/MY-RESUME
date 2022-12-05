from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.views.generic import View

from xhtml2pdf import pisa

from resume.common.email import ContactNotificationEmail
from resume.apps.web.portfolio.models import GetInTouch

User = get_user_model()


class HomeView(View):
    template_name = 'apps/portfolio/index.html'

    def get(self, request, **kwargs):
        
        context={}
        
        return render(request, self.template_name, context)
    
    def post(self, request, **kwargs):
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        if name  and email and message:
            # name_obj = GetInTouch.objects.filter(name=name).exists()

            # if name_obj:
            #     message = {'msg':f'Oops! {name} already exists please try again'}
            #     return JsonResponse(message) 

            messages_email = render_to_string('email.html', {'name': name})
            
            contact_obj = GetInTouch.objects.create(name=name, email=email, message=message)
            
            if contact_obj:
                email = ContactNotificationEmail(name, email, message, messages_email)
                email.run() 
                
            message = {'msg':'Your form has been submitted successfully' }
            return JsonResponse(message)

        else:
            message = {'msg':'Oops ! There were some errors in your form input.' }
            return JsonResponse(message)  
    

class PdfCvCreate(View):
    
    def get(self, request,**kwargs):

        data = [{"name":"Mpoyi"}]

        template_path = 'apps/portfolio/cv.html'

        context = {'data': data}

        response = HttpResponse(content_type='application/pdf')

        response['Content-Disposition'] = 'filename="mpoyi_cv.pdf"'

        template = get_template(template_path)

        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(html, dest=response)
        
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response