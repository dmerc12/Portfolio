from django.http import JsonResponse
from contact.models import Contact
from django.views.decorators.csrf import csrf_exempt

from django.middleware.csrf import get_token

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})

# Contact view
# @csrf_exempt
def contact(request):
    if request.method == 'POST':
        ## Get data from fields
        data = request.POST

        ## Assign fields to variables
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        phone_number = data.get('phone_number')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')

        ## Initialize error dictionary
        errors = {}

        ## Check for empty fields
        if not first_name:
            errors['first_name'] = 'First name is required'
        if not last_name:
            errors['last_name'] = 'Last name is required'
        if not phone_number:
            errors['phone_number'] = 'Phone number is required'
        if not email:
            errors['email'] = 'Email is required'
        if not subject:
            errors['subject'] = 'Subject is required'
        if not message:
            errors['message'] = 'Message is required'

        ## Respond for errors
        if errors:
            response = {'errors': errors}
            return JsonResponse(response, status=422)

        ## Check legth requirerments on fields
        if len(first_name) > 100:
            errors['first_name'] = 'First name cannot exceed 100 characters'
        if len(last_name) > 100:
            errors['last_name'] = 'Last name cannot exceed 100 characters'
        if len(phone_number) > 15:
            errors['phone_number'] = 'Phone number cannot exceed 15 characters'
        if len(email) > 250:
            errors['email'] = 'Email cannot exceed 250 characters'
        if len(subject) > 250:
            errors['subject'] = 'Subject cannot exceed 250 characters'
        if len(message) > 500:
            errors['message'] = 'Message cannot exceed 500 characters'

        ## Respond for errors
        if errors:
            response = {'errors': errors}
            return JsonResponse(response, status=422)

        ## Respond for success
        contact = Contact.objects.create(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email, subject=subject, message=message)
        contact.save()
        response = {'message': 'Submitted successfully, I will be in contact soon!'}
        return JsonResponse(response, status=201)
    else:
        ## Respond for incorrect HTTP method
        response = {'error': 'Invalid HTTP method'}
        return JsonResponse(response, status=403)
