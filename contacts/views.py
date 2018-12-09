from django.shortcuts import render, get_object_or_404, redirect
from contacts.forms import *
from contacts.models import Contact


def contacts_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contacts_list.html', {'contacts': contacts})


def contacts_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})


def contact_new(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('contacts_list')
    else:
        form = ContactForm()
        return render(request, 'contacts/contact_edit.html', {'form': form})


def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('contacts_list')
    else:
        form = ContactForm(instance=contact)
        return render(request, 'contacts/contact_edit.html', {'form': form})

