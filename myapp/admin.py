from django.contrib import admin
from . models import ContactBook
# Register your models here.
@admin.register(ContactBook)
class ContactBookAdmin(admin.ModelAdmin):
	list_display=['name','email','number','address']
