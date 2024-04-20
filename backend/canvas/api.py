from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import CanvasForm
from .models import Canvas
from account.models import User
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
        canvas.last_user = request.user
        canvas.canvas_data = request.data["canvas_data"]
        print(request.data["canvas_data"])
        canvas.save()
        
        serializer = CanvasSerializer(canvas)
        
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'add something here...'})


@api_view(['GET'])
def search_canvas_by_user(request):
    search_term = request.query_params.get('searchTerm')
    users = User.objects.filter(name__iexact=search_term)
    canvases = Canvas.objects.filter(created_by__in=users)
    
    serializer = CanvasSerializer(canvases, many=True)
    
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_canvas_by_id(request, canvas_id):
    canvas = Canvas.objects.filter(id=canvas_id)
    serializer = CanvasSerializer(canvas, many=True)

    return JsonResponse(serializer.data[0], safe=False)

@api_view(['PUT'])
def canvas_update(request, canvas_id):
    canvas = Canvas.objects.get(id=canvas_id)
    canvas_data = request.data.get('canvas_data')
    if canvas_data:
        canvas.canvas_data = canvas_data
        canvas.save()
        serializer = CanvasSerializer(canvas)
        
        return JsonResponse(serializer.data, safe=False)
    else:

        return JsonResponse(form.errors, status=400)
       
@api_view(['DELETE'])
def delete_canvas(request, canvas_id):
    try:
        canvas = Canvas.objects.get(id=canvas_id)
        canvas.delete()

        return JsonResponse({'message': 'Canvas deleted successfully'})
    except Canvas.DoesNotExist:
        
        return JsonResponse({'error': 'Canvas not found'}, status=404)