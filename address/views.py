from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import  CreateView
# from address.forms import DeliveryForm

from django.forms import inlineformset_factory

from .models import Delivery, Address
from .forms import Deliveryform, DeliveryAddressFormSet
from django.http import HttpResponseRedirect

#
# def note_view(request):
#     # Create formset based on our parent model and child model. We are going to allow up to 3 items in form.
#     DeliveyFormSet = inlineformset_factory(Delivery, Address, fields='__all__', extra=3)
#
#     # generate form and formset
#     form = Deliveryform(request.POST or None, request.FILES or None)
#     formset = DeliveyFormSet(request.POST or None, request.FILES or None)
#
#     if form.is_valid() and formset.is_valid():
#         note = form.save()
#         for form in formset.forms:
#             item = form.save(commit=False)
#             item.rec_note_id = note
#             item.save()
#
#     return render(request, 'formset.html', {'form': form, 'formset': formset})

class DeliveryCreateView(CreateView):
    template_name = 'formset.html'
    model = Delivery
    # fields = "__all__"
    form_class = Deliveryform
    object = None

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        delivery_address_form = DeliveryAddressFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  delivery_address_form=delivery_address_form,
                                  )
        )

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        delivery_address_form = DeliveryAddressFormSet(self.request.POST, self.request.FILES,instance=form.instance)
        if form.is_valid() and delivery_address_form.is_valid():
            return self.form_valid(form, delivery_address_form)
        else:
            return self.form_invalid(form, delivery_address_form)

    def form_valid(self, form, delivery_address_form):
        """
        Called if all forms are valid. Creates Assignment instance along with the
        associated AssignmentQuestion instances then redirects to success url
        Args:
            form: Assignment Form
            delivery_address_form: Assignment Question Form

        Returns: an HttpResponse to success url

        """
        self.object = form.save(commit=False)
        # pre-processing for Assignment instance here...
        self.object.save()

        # saving AssignmentQuestion Instances
        delivery_address = delivery_address_form.save(commit=False)
        for aq in delivery_address:
            #  change the AssignmentQuestion instance values here
            #  aq.some_field = some_value
            aq.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, delivery_address_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.

        Args:
            form: Assignment Form
            delivery_address_form: Assignment Question Form
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  delivery_address_form=delivery_address_form
                                  )
        )

    #
    #
    # def get_context_data(self, **kwargs):
    #     context = super(DeliveryCreateView, self).get_context_data(**kwargs)
    #     if self.request.POST:
    #         context['deliveryaddress_form'] = DeliveryAddressFormSet(self.request.POST, self.request.FILES)
    #         context['form'] = Deliveryform(self.request.POST, self.request.FILES)
    #
    #     else:
    #         context['deliveryaddress_form'] = DeliveryAddressFormSet()
    #     return context
    #
    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     deliveryaddress_form = context['deliveryaddress_form']
    #     if form.is_valid() and deliveryaddress_form.is_valid() :
    #         self.object = form.save()
    #         deliveryaddress_form.instance = self.object
    #         deliveryaddress_form.save()
    #         return HttpResponseRedirect('thanks/')
    #     else:
    #         return self.render_to_response(self.get_context_data(form=form))

