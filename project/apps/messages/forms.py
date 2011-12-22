from django import forms

from apps.messages.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
