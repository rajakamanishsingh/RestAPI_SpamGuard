from typing import Union
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User, Contact,RandomNumber
from django.http import JsonResponse
from .serializers import UserSerializer, ContactSerializer,RandomNumberSerializer

@api_view(['POST','GET','PUT','DELETE'])
def mark_spam(request, phone_number: str) -> Response:
    """
    Marks a phone number as spam by updating the 'is_spam' field of the corresponding User, Contact, or RandomNumber object in the database.

    Args:
        request: The HTTP request object.
        phone_number: The phone number to be marked as spam.

    Returns:
        A success response with a message indicating that the phone number has been marked as spam successfully.
    """
    try:
        User.objects.filter(phone_number=phone_number).update(is_spam=True)
        return Response({"message": "Phone number marked as spam successfully."}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        try:
            Contact.objects.filter(phone_number=phone_number).update(is_spam=True)
            return Response({"message": "Phone number marked as spam successfully."}, status=status.HTTP_200_OK)
        except Contact.DoesNotExist: 
            randomnum = RandomNumber(phone_number=phone_number)
            randomnum.is_spam = True
            randomnum.save()
            return Response({"message": "Phone number marked as spam successfully."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        try:
            contact = get_object_or_404(Contact, phone_number=id)
            contact.is_spam = True
            contact.save()
            return Response({"message": "Phone number marked as spam successfully."}, status=status.HTTP_200_OK)
        except Contact.DoesNotExist: 
            randomnum = RandomNumber(phone_number=id)
            randomnum.is_spam = True
            randomnum.save()
            return Response({"message": "Phone number marked as spam successfully."}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def search_by_name(request, name_query):
    # Perform the search based on name_query
    search_results = []
    name_results = User.objects.filter(name__icontains=name_query)
    name_results_1 =Contact.objects.filter(name__icontains=name_query)

    for contact in name_results:
    
        contact_data = {
            "name": contact.name,
            "phone_number": contact.phone_number,
            "email":contact.email,
            "is_spam": contact.is_spam
        }

        
        search_results.append({**contact_data})
    
    for contact in name_results_1:
    
        contact_data = {
            "name": contact.name,
            "phone_number": contact.phone_number,
            "email":contact.email,
            "is_spam": contact.is_spam
        }

       
        search_results.append({**contact_data})

    if not search_results:
        return Response({"message": "Phone number Not found"}, status=status.HTTP_200_OK)
    else:
        return Response(search_results, status=status.HTTP_200_OK)
@api_view(['GET'])
def search_by_number(request, phone_number):

    search_results = []
    name_results = User.objects.filter(phone_number=phone_number)

    name_results_1 =Contact.objects.filter(phone_number=phone_number)
    for contact in name_results:
    
        contact_data = {
            "name": contact.name,
            "phone_number": contact.phone_number,
            "email":contact.email,
            "is_spam": contact.is_spam
        }

        search_results.append({**contact_data})
    
    for contact in name_results_1:
    
        contact_data = {
            "name": contact.name,
            "phone_number": contact.phone_number,
            "email":contact.email,
            "is_spam": contact.is_spam
        }

    
        search_results.append({**contact_data})

    if not search_results:
        name_results =RandomNumber.objects.filter(phone_number=phone_number)
        for contact in name_results:
    
            contact_data = {
            "phone_number": contact.phone_number,
            "is_spam": contact.is_spam
            }

            search_results.append({**contact_data})
        if not search_results:
            return Response({"message": "Phone number Not found"}, status=status.HTTP_200_OK)
        else:
            return Response(search_results, status=status.HTTP_200_OK)
    else:
        return Response(search_results, status=status.HTTP_200_OK)