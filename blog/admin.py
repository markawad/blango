from django.contrib import admin
from blog.models.tag import Tag
from blog.models.post import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    exclude = ['created_at']


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
