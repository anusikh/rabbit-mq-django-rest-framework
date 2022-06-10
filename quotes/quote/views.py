from rest_framework import generics
from rest_framework.response import Response

from quote.models import QuoteTable

# Create your views here.


class AddQuote(generics.GenericAPIView):

    def post(self, request):
        res = {}
        content = request.data["content"]
        QuoteTable.objects.create(
            content=content
        )
        res = {"status": "PASS"}
        return Response(res)
