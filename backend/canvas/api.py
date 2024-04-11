from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import CanvasForm
from .models import Canvas
from .serializers import CanvasSerializer


@api_view(['GET'])
def canvas_list(request):
    canvases = Canvas.objects.all()
    
    serializer = CanvasSerializer(canvases, many=True)
    
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def canvas_list_feed(request, id):
    canvases = Canvas.objects.filter(created_by_id=id)
    
    serializer = CanvasSerializer(canvases, many=True)
    
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def canvas_create(request):
    form = CanvasForm(request.data)
    
    if form.is_valid():
        canvas = form.save(commit=False)
        canvas.created_by = request.user
        canvas.save()
        
        serializer = CanvasSerializer(canvas)
        
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'add something here...'})