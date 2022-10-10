from django.contrib import admin
from .models import ContactModel, ContactLink, About, ImageAbout, Social

admin.site.register(Social)
admin.site.register(ContactLink)

class ImageAboutInline(admin.StackedInline):
    model = ImageAbout
    extra: 1

@admin.register(ContactModel)
class AdminContactModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'create_at']
    list_display_links = ('name',)

@admin.register(About)
class AdminAbout(admin.ModelAdmin):
    inlines = [ImageAboutInline]

# Register your models here.
