from django.urls import path, include


urlpatterns = [
    path('', include('resume.apps.urls')),
]
