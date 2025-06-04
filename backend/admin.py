from django.contrib import admin

from backend.models import Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name','public_ip')

    exclude = ('public_ip',)  # Hides it from the form