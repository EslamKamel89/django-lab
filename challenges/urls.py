from django.urls import URLPattern, path

from . import views

urlpatterns :list[URLPattern] = [
    path('<month>/' , views.monthly_challenge),
]
