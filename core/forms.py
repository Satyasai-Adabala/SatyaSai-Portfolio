from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name", "autocomplete": "name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@email.com", "autocomplete": "email"}),
            "subject": forms.TextInput(attrs={"placeholder": "What's this about?"}),
            "message": forms.Textarea(attrs={"placeholder": "Tell me about the role, project, or just say hi.", "rows": 5}),
        }
