from django.contrib import admin
from django.contrib.admin import ModelAdmin

from docstore.models import DocCategory, DocFile, DocChat, DocRequest


@admin.register(DocCategory)
class DocCategoryAdmin(ModelAdmin):
    pass


# admin.site.register(DocCategory)
admin.site.register(DocFile)
admin.site.register(DocChat)
admin.site.register(DocRequest)
