from django import forms
from django.forms.models import inlineformset_factory


from address.models import Delivery, Address


class Deliveryform(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'
        cl = 'form-control'

        widgets = {
            'date_delivery': forms.TextInput(attrs={'class': cl, 'type': 'date'}),
            'name': forms.TextInput(attrs={'class': cl, }),
            'type': forms.TextInput(attrs={'class': cl, }),
        }

DeliveryAddressFormSet = inlineformset_factory(Delivery, Address, fields=['address'],  # labels for the fields
                                                  # set to false because cant' delete an non-exsitant instance
                                                  can_delete=False,
                                                  # how many inline-forms are sent to the template by default
                                                  extra=1)