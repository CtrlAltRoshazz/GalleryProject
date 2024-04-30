from django.contrib import admin
from . models import CategoryModel , ImageModel

# Register your models here.

admin.site.register(CategoryModel)


@admin.register(ImageModel)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'cat', 'image', 'uploaded_by','uploaded_at']
    