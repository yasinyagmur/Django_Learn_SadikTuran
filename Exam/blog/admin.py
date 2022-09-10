from django.contrib import admin
from .models import Blog,Category
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display= ("title","is_activate","is_home","slug")
    list_editable=("is_activate","is_home")
    search_fields= ("title","description")
    # readonly_fields=("description",)
    readonly_fields=("slug",)

class CategoryAdmin(admin.ModelAdmin):
    list_display=("name","slug")


admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CategoryAdmin)