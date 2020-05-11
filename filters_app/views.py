
from rest_framework import viewsets


#from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
#from django_filters.rest_framework import FilterSet, filters
#import rest_framework_filters as filters

from .serializers import EntrySerializer
from .models import Entry


class EntryListView(viewsets.ModelViewSet):
    ''' Entry API list view '''
    
    #queryset = Entry.objects.filter(blog__contains={"name":"2"})
    #queryset = Entry.objects.filter(blog__startswith={'name': 'blog_2'})
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('headline',) #'blog__name'