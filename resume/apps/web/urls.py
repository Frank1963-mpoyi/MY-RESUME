from django.urls import path, include


urlpatterns = [
    path('', include('resume.apps.web.portfolio.urls')),
    path('accounts/', include('resume.apps.web.accounts.urls')),
]
