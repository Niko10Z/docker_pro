from django.urls import path
from rest_framework.routers import SimpleRouter

from docstore.views import DocCategoriesViewSet, DocChatsViewSet, DocRequestsViewSet, DocFilesViewSet, \
    FileDownloadListAPIView

doc_store_router = SimpleRouter()
doc_store_router.register(r'doc-categories', DocCategoriesViewSet)
doc_store_router.register(r'doc-chats', DocChatsViewSet)
doc_store_router.register(r'doc-requests', DocRequestsViewSet)
doc_store_router.register(r'doc-files', DocFilesViewSet)

urlpatterns = doc_store_router.urls
urlpatterns.append(path('download/<int:id>/', FileDownloadListAPIView.as_view()))
