from django.contrib import admin

from .models import Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Image, ImageAdmin)