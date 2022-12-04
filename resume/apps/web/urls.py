from django.urls import path, include


urlpatterns = [
    path('accounts/', include('resume.apps.web.accounts.urls')),
    path('portfolio/', include('resume.apps.web.portfolio.urls')),
]
