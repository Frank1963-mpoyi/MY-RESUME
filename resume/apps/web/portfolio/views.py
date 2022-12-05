from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.views.generic import View, TemplateView

from xhtml2pdf import pisa

from resume.common.email import ContactNotificationEmail
from resume.apps.web.portfolio.models import GetInTouch
from resume.apps.web.portfolio.forms import GetInTouchForm

User = get_user_model()


class HomeView(View):
    template_name = 'apps/portfolio/index.html'

    def get(self, request, **kwargs):
        
        form = GetInTouchForm
        
        context = {'form': form}
        
        return render(request, self.template_name, context)
    
    # def post(self, request, **kwargs):

    #     form = GetInTouchForm(request.POST or None)

    #     name = request.POST.get('name', '')
        
    #     if form.is_valid():
            
    #         messages_email = render_to_string('email.html', {'name': name})
            
    #         data = GetInTouch(**form.cleaned_data)
            
    #         data.save() 
            
    #         messages.success(request, "Thanks for contacting us! We will be in touch with you shortly.")
            
    #         if data:
    #             email = ContactNotificationEmail(data, messages_email)
    #             email.run() 
                
    #         return redirect(self.request.META['HTTP_REFERER'])
    #     else:
    #         messages.success(request, "Oops! your contact details failed please try again !")  
            
    #     context = {'form': form}

    #     return render(request, self.template_name, context)



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