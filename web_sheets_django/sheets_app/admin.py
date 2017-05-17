from django.contrib import admin

# Register your models here.

from .models import *

class BookAdmin(admin.ModelAdmin):
    #fields = ('book_id', 'book_name', 'user_creator', 'is_demo')
    list_display = ('pk', 'book_id', 'book_name', 'user_creator', 'is_demo')
    pass

admin.site.register(Book, BookAdmin)

