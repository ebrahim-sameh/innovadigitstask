from django.shortcuts import render, get_object_or_404,redirect
from .models import Contact
from .forms import ContactForm, PhoneNumberForm
# from .forms import ContactForm, PhoneNumberFormSet
from django.forms import formset_factory

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})


def add_contact(request):
    PhoneNumberFormSet = formset_factory(PhoneNumberForm, extra=1)

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        phone_numbers_formset = PhoneNumberFormSet(request.POST, prefix='phone_numbers')

        if contact_form.is_valid() and phone_numbers_formset.is_valid():
            contact = contact_form.save(commit=False)
            contact.save()

            for form in phone_numbers_formset:
                if form.cleaned_data.get('number'):
                    phone_number = form.save(commit=False)
                    phone_number.contact = contact
                    phone_number.save()

            contact_pk = contact.pk

            return redirect('contacts:contact_detail', pk=contact_pk)

    else:
        contact_form = ContactForm()
        phone_numbers_formset = PhoneNumberFormSet(prefix='phone_numbers')

    return render(request, 'contacts/add_contact.html', {
        'contact_form': contact_form,
        'phone_numbers_formset': phone_numbers_formset,
    })