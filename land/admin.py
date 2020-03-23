from django.contrib import admin
from land.models import (Book, Category)


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, CategoryAdmin)
admin.site.register(Category, CategoryAdmin)
