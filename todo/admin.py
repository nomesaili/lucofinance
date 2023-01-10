from django.contrib import admin
from .models import Loan
from .models import Contact

class LoanAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Loan, LoanAdmin)
admin.site.register(Contact, ContactAdmin)
