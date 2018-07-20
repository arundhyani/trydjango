from django.contrib import admin

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display  = ["__str__","update","timestamp"]
    list_display_links = ["update"]
    list_filter = ("update","timestamp")
    search_fields = ['title']
    class Meta :
        model = Post
admin.site.register(Post,PostModelAdmin)
