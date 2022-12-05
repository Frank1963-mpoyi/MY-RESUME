from django.urls import path

from .views import HomeView , PdfCvCreate


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('pdf_cv_create', PdfCvCreate.as_view(), name='pdf_cv_create'),
]