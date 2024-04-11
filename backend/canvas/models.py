import uuid

from django.db import models

from account.models import User


class Canvas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, default='')
    avatar = models.ImageField(upload_to='canvas_avatars', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='canvases', on_delete=models.CASCADE)