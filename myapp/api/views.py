from myapp.models import ContactBook
from myapp.api.serializers import ContactBookSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .pagination import MyPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters  import  SearchFilter
class ContactBookViewSet(viewsets.ModelViewSet):
 queryset = ContactBook.objects.all()
 serializer_class = ContactBookSerializer
 authentication_classes = [SessionAuthentication]
 permission_classes = [IsAuthenticatedOrReadOnly]
 pagination_class = MyPageNumberPagination
 filter_backends = [DjangoFilterBackend]
 filterset_fields = ['name','email']
 # filter_backends=[SearchFilter]
 # search_fields=['name','email']