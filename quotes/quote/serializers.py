from rest_framework import serializers

from quote.models import QuoteTable


class QuoteTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteTable
        fields = "__all__"
