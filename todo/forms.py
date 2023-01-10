from django.forms import ModelForm
from .models import Loan
from .models import Contact

class TodoForm(ModelForm):
    class Meta:
        model = Loan
        fields = ['title', 'memo', 'important']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'memo', 'email', 'phone']