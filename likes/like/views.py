from rest_framework import generics
from rest_framework.response import Response

from like.producer import publish


class LikeQuote(generics.GenericAPIView):

    def post(self, request):
        res = {}
        quoteId = request.data["id"]
        publish('add_like', quoteId)
        return Response(res)
