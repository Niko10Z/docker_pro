from rest_framework.serializers import ModelSerializer

from docstore.models import DocCategory, DocFile, DocChat, DocRequest


class DocCategoriesSerializer(ModelSerializer):
    class Meta:
        model = DocCategory
        fields = '__all__'


class DocFilesSerializer(ModelSerializer):
    class Meta:
        model = DocFile
        fields = '__all__'


class DocChatsSerializer(ModelSerializer):
    class Meta:
        model = DocChat
        fields = '__all__'


class DocRequestsSerializer(ModelSerializer):
    class Meta:
        model = DocRequest
        fields = '__all__'
