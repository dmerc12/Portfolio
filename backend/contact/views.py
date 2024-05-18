from django.shortcuts import render, redirect, get_object_or_404
from contact.serializers import ContactSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from contact.models import Contact
from rest_framework import status

# Contact view
@api_view(['POST'])
def contact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Form successfully submitted. I will be in contact soon!'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Contact home view
def contact_home(request):
    if request.user.is_authenticated:
        contacts = Contact.objects.all()
        return render(request, 'contact/home.html', {'contacts': contacts})
    else:
        messages.error(request, 'You must be a site admin to access this page!')
        return redirect('login')

# Mark contact responded view
def mark_response(request, contact_id):
    if request.user.is_authenticated:
        contact = get_object_or_404(Contact, pk=contact_id)
        if not contact.responded:
            contact.responded = True
            contact.save()
        else:
            contact.responded = False
            contact.save()
        messages.success(request, 'Response noted!')
        return redirect('contact-home')
    else:
        messages.error(request, 'You must be a site admin to access this page!')
        return redirect('login')

# Delete contact view
def delete_contact(request, contact_id):
    if request.user.is_authenticated:
        contact = get_object_or_404(Contact, pk=contact_id)
        if request.method == 'POST':
            contact.delete()
            messages.success(request, 'Message successfully deleted!')
            return redirect('contact-home')
        return render(request, 'contact/delete.html', {'contact': contact})
    else:
        messages.error(request, 'You must be a site admin to access this page!')
        return redirect('login')
