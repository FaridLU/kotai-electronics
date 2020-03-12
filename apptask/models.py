from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
import time
import os
from datetime import datetime
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.contrib.sites.shortcuts import get_current_site
# from django.contrib.sites.models import get_current_site

User = get_user_model()

# Create your models here.

class Task(models.Model):
    weight_scale = models.TextField(max_length=250)
    license_scale = models.TextField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


