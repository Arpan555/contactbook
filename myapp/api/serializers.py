from myapp.models import ContactBook
from rest_framework import serializers

class ContactBookSerializer(serializers.ModelSerializer):
 class Meta:
  model = ContactBook
  fields = ['id', 'name', 'email', 'number','address']