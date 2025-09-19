from django.contrib import admin
from .models import Blog, BlogComment, Categories


class BlogAdmin (admin.ModelAdmin):

    list_display = ('id', 'blog_title', 'posted_date', 'is_public')
    list_display_links = ('blog_title', 'id')
    list_per_page = 10
    search_fields = ('blog_title',)
    list_editable = ('is_public',)


class catogoryAdmin(admin.ModelAdmin):
    list_display = ('id', "category_name")


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment)
admin.site.register(Categories, catogoryAdmin)
