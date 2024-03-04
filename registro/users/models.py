from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    
    def __str__(self):
        return self.get_full_name() or self.username
