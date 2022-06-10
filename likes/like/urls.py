from django.urls import path

from like.views import LikeQuote


urlpatterns = [
    path('likeQuote/', LikeQuote.as_view())
]
