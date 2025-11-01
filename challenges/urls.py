from django.urls import URLPattern, path

from . import views

urlpatterns :list[URLPattern] = [
    path('' , views.index , name="challenges") ,
    path('<int:month>/' , views.monthly_challenge_by_number),
    path('<str:month>/' , views.monthly_challenge , name='month_challenge'),
]
