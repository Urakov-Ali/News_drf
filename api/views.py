from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import NewsSerialzer
from news.models import New

class CreateNewsList(generics.ListCreateAPIView):
    queryset = New.objects.all()
    serializer_class = NewsSerialzer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title__title', 'author')

    def perform_create(self, serializer):
        serializer.save()

class EditNewsList(generics.RetrieveUpdateDestroyAPIView):
    queryset = New.objects.all()
    serializer_class = NewsSerialzer

#class for retrieving the base objects by date descending
class NewsListReverse(generics.ListAPIView):
    queryset = New.objects.order_by('-date')
    serializer_class = NewsSerialzer
    filter_backends = (OrderingFilter,)
    ordering_fields = ('title__title',)



    