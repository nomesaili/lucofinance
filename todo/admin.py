from django.contrib import admin
from .models import Todo
from .models import Contact

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo, TodoAdmin)
admin.site.register(Contact, ContactAdmin)
