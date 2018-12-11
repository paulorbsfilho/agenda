from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect
from contacts.forms import *
from contacts.models import Contact


def contacts_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contacts_list.html', {'contacts': contacts})


def groups_list(request):
    groups = Group.objects.all()
    return render(request, 'contacts/groups_list.html', {'groups': groups})


def contacts_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})


def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'contacts/group_detail.html', {'group': group})


def contact_new(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('contacts_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_new.html', {'form': form})


def group_new(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            return redirect('groups_list')
    else:
        form = GroupForm()
    return render(request, 'contacts/group_new.html', {'form': form})


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


def group_edit(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            return redirect('groups_list')
    else:
        form = GroupForm(instance=group)
    return render(request, 'contacts/group_edit.html', {'form': form})


def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('contacts_list')


def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()
    return redirect('groups_list')
