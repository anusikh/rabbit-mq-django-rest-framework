from django.urls import path

from quote.views import AddQuote


urlpatterns = [
    path('add/', AddQuote.as_view())
]
