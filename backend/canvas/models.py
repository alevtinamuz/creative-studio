import uuid

from django.db import models
from django.utils.timesince import timesince

from account.models import User


class Canvas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to='canvas_avatars', blank=True, null=True)
    
    canvas_data = models.CharField(max_length=10**6, blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='canvases', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)  
    last_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    
    class Meta:
        ordering = ('-created_at',)
        
    def updated_at_formatted(self):
        return timesince(self.updated_at)  
    
    def created_at_formatted(self):
        return timesince(self.created_at)
    
    def last_user_formatted(self):
        return f"Canvas state for {self.last_user}"
    