from django.contrib import admin
from .models import User
from .models import Drone
from .models import Alert


admin.site.register(User)
admin.site.register(Drone)
admin.site.register(Alert)