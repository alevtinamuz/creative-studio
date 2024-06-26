from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .forms import SignupForm
from .models import User
from .serializers import UserSerializer
from rest_framework import status
# from rest_framework.authtoken.models import Token


@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'
    
    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })
    
    if form.is_valid():
        form.save()
        
    else:
        message: 'error'
    
    return JsonResponse({'status': message})

@api_view(['GET'])
def search_by_name(request):
    search_term = request.query_params.get('searchTerm')
    users = User.objects.filter(name__icontains=search_term)
    serializer = UserSerializer(users, many=True)
    
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def search_by_email(request):
    search_term = request.query_params.get('searchTerm')
    users = User.objects.filter(email__icontains=search_term)
    serializer = UserSerializer(users, many=True)
    
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def search_by_id(request, user_id):
    user = User.objects.filter(id=user_id)
    serializer = UserSerializer(user, many=True)

    return JsonResponse(serializer.data[0], safe=False)


@api_view(['GET'])
def user_list(request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        
        return JsonResponse(serializer.data, safe=False)


@api_view(['PUT'])
def add_canv(request, user_id):
    user = User.objects.get(id=user_id)
    canv_id = request.data.get('canv_id')
    if (user.canv is None):
        user.canv = canv_id
        user.save()
        serializer = UserSerializer(user)
        
        return JsonResponse(serializer.data, safe=False)
    else:
        if (not canv_id in user.canv):
            user.canv += ',' + canv_id
            user.save()
        serializer = UserSerializer(user)
        
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_canv(request, user_id):
    user = User.objects.filter(id=user_id)
    serializer = UserSerializer(user, many=True)

    return JsonResponse(serializer.data[0], safe=False)