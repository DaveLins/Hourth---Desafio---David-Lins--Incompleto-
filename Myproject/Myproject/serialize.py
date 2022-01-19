from Myproject.models import empmodel

from rest_framework import serializers

class empserializers(serializers.ModelSerializer):

    class Meta:

        model = empmodel

        fields = "__all__"