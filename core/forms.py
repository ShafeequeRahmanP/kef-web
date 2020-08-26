from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.forms import ModelForm
from django.forms import Textarea
from django import forms
from django.forms import ModelForm
from .models import Message
from django.forms import ModelForm, TextInput, EmailField
PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal'),
    ('PO', 'Pay on delivery'),

)

class ContactForm(ModelForm):
    class Meta:
        model = Message
        fields = ('name','contact_number','email','subject','message')
        # widgets={
        # 'name' : forms.CharField(
        #     attrs = {
        #         'class':'form-control'
        #         }
        #     ,required = True)
        # # contact_number = forms.CharField(required = True)
        # # email = forms.EmailField(required=True)
        # # subject = forms.CharField(required=True)
        # # message = forms.CharField(widget=forms.Textarea, required=True)
        # }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class':'form-control'}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Enter contact number', 'class':'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class':'form-control'}),
            'subject': forms.TextInput(attrs={ 'class':'form-control'}),
            'message': forms.TextInput(attrs={'placeholder': 'type your message...', 'class':'form-control'}),
        }
class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    # shipping_country = CountryField(blank_label='(select country)').formfield(
    #     required=False,
    #     widget=CountrySelectWidget(attrs={
    #         'class': 'custom-select d-block w-100',
    #     }))
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)
