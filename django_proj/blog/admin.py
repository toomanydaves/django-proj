from django.contrib import admin

from .models import Post, Tag, SEO

class SEOAdminInline(admin.TabularInline):
    model = SEO

class PostAdmin(admin.ModelAdmin):
    inlines = (SEOAdminInline, )

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(SEO)
