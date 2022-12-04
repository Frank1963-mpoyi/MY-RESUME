from django.urls import path

from .views import HomeView #PdfCvCreate, Invoive
# from .views_old import HomeView, views_pdf, views_csv, views_text, pdf_report_create


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('pdf_cv_create', PdfCvCreate.as_view(), name='pdf_cv_create'),
    # path('pdf_invoice_create', Invoive, name='pdf_invoice_create'),
    # path('view_pdf/', views_pdf, name='views_pdf'),
    # path('views_csv/', views_csv, name='views_csv'),
    # path('views_text/', views_text, name='views_text'),
    # path('pdf_report_create/', pdf_report_create, name='pdf_report_create'),
]