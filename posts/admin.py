from django.contrib import admin
from .models import Post, Group
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("text", "pub_date", "author", "group")
    search_fields = ("text",)
    list_filter = ("pub_date",)


class GroupAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "description")
    search_fields = ("title",)


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
