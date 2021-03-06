from calendar import monthrange
from datetime import date, datetime
 
from django import forms

from mainapp.models import Sale
from shopping_cart.forms import  CCExpWidget, CCExpField


class SignupForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=30, label='first_name')
    last_name = forms.CharField(required=True, max_length=30, label='last_name')
    mobile = forms.CharField(max_length=50, label='Mobile')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name'] 
        user.mobile_number = self.cleaned_data['mobile']       
        
class SalePaymentForm(forms.Form):
    number = forms.IntegerField(required=True, label="Card Number")
    expiration = CCExpField(required=True, label="Expiration")
    amount=forms.CharField(widget=forms.HiddenInput(),required=False,label="")
    cvc = forms.IntegerField(required=True, label="CCV Number",
                    max_value=9999, widget=forms.TextInput(attrs={'size': '4'}))

    def clean(self):
        cleaned = super(SalePaymentForm, self).clean()
 
        if not self.errors:
            number = self.cleaned_data["number"]
            exp_month = self.cleaned_data["expiration"].month
            exp_year = self.cleaned_data["expiration"].year
            cvc = self.cleaned_data["cvc"]
            sale = Sale()
        success, instance = sale.charge(int(float(self.amount)), number, exp_month,
                                                exp_year, cvc)
        if not success:
                raise forms.ValidationError("Error: %s" % instance.message)
        else:
                instance.save()
                pass
        return cleaned
        