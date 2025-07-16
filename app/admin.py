from django.contrib import admin
#username=bookreview,password=book@333
# Register your models here.
from app.models import Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','isbn')