from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Canvas
from .serializers import CanvasSerializer


@api_view(['GET'])
def canvas_list(request):
    canvases = Canvas.objects.all()
    
    serializer = CanvasSerializer(canvases, many=True)
    
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def canvas_create(request):
    data = request.data
    
    print(data)
    
    return JsonResponse({'hello': 'hepp'})