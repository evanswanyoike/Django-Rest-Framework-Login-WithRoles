from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
import requests
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .models import AdminProfile
from .serializers import AdminLoginSerializer, AdminProfileSerializer, TeacherLoginSerializer, TeacherProfileSerializer, \
    StudentLoginSerializer, StudentProfileSerializer


class AdminLoginView(APIView):
    def post(self, request):
        serializer = AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None and user.role == 'admin':
                login(request, user)
                admin_profile = AdminProfile.objects.get(user=user)
                profile_serializer = AdminProfileSerializer(admin_profile)
                return Response({'message': 'Admin logged in successfully.', 'profile': profile_serializer.data})
            else:
                return Response({'message': 'Invalid credentials or user role.'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Similarly, create TeacherLoginView and StudentLoginView

@api_view(('GET',))
# @renderer_classes(JSONRenderer)
def get_external_data(request):
    # Make the GET request to the external API
    url = 'https://jsonplaceholder.typicode.com/posts'  # Replace with the URL of the external API
    headers = {'Content-Type': 'application/json'}  # Replace with the required headers
    response = requests.get(url, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        # Successful response from the external API
        data = response.json()
        return Response(data)
        # return JsonResponse(data, safe=False)
    else:
        # Error response from the external API
        return Response({'message': 'API call failed'}, status=response.status_code)
