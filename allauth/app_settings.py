from django.conf import settings


SOCIALACCOUNT_ENABLED = "allauth.socialaccount" in settings.INSTALLED_APPS

OAUTH2_PROVIDER_ENABLED = "allauth.oauth2_provider" in settings.INSTALLED_APPS

LOGIN_REDIRECT_URL = getattr(settings, "LOGIN_REDIRECT_URL", "/")

USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")

OAUTH2_PROVIDER_APPLICATION = getattr(settings, "OAUTH_TOOLKIT_APPLICATION", None)
