import uuid

from django.db import models
from django.utils.timesince import timesince

from account.models import User


class Canvas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to='canvas_avatars', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='canvases', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('-created_at',)
        
    def created_at_formatted(self):
        return timesince(self.created_at)
    