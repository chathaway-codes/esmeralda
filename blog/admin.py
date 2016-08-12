from .models import BlogPost
from django.contrib import admin

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(BlogPost, BlogPostAdmin)
