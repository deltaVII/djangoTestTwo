from django.contrib import admin
from .models import Posts

#возможность управления БД одменом
admin.site.register(Posts)
