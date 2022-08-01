# Django Login/Logout/Signup Module

This Django login module is a pluggable app for Django 4.0.

## Startup

* Register the app in settings.py
* Route the URLs through the project-wide urls.py using the two lines below.
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/", include("accounts.urls")),
