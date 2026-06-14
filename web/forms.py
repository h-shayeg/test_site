from django import forms
from web.models import contact, Newslatter
from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = contact
        fields = ['name', 'email', 'subject', 'message']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newslatter
        fields = '__all__'