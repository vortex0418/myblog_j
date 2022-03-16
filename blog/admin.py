from django.contrib import admin
from blog.models import Post, Category, Comment

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name', )}
    #prepopulated_fields = { 'slug' : ['name']}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post)
admin.site.register(Comment)
