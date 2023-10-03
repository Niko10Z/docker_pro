from wsgiref.util import FileWrapper

from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet

from docstore.models import DocCategory, DocChat, DocRequest, DocFile
from docstore.serializers import DocCategoriesSerializer, DocChatsSerializer, DocRequestsSerializer, DocFilesSerializer


class DocCategoriesViewSet(ModelViewSet):
    queryset = DocCategory.objects.all()
    serializer_class = DocCategoriesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name', 'is_public']
    search_fields = ['name']
    ordering_fields = ['name', 'created_at', 'updated_at']


class DocChatsViewSet(ModelViewSet):
    queryset = DocChat.objects.all()
    serializer_class = DocChatsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name', 'slug']
    search_fields = ['slug']
    ordering_fields = ['slug', 'created_at', 'updated_at']


class DocRequestsViewSet(ModelViewSet):
    queryset = DocRequest.objects.select_related('related_chat').all()
    serializer_class = DocRequestsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'category', 'category__name', 'related_chat', 'related_chat__name', 'related_chat__slug']
    search_fields = ['request_str']
    ordering_fields = ['id', 'created_at', 'updated_at']


class DocFilesViewSet(ModelViewSet):
    queryset = DocFile.objects.all()
    serializer_class = DocFilesSerializer


class FileDownloadListAPIView(ListAPIView):
    def get(self, request, id, format=None):
        queryset = DocFile.objects.get(id=id)
        file_handle = queryset.file.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/msword')
        response['Content-Disposition'] = 'attachment; filename="%s"' % queryset.file.name
        return response
