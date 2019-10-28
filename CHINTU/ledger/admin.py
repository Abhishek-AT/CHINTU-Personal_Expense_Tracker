from django.contrib import admin
from .models import Group,Transaction,GroupTransaction

# Register your models here.


admin.site.register(Group)
admin.site.register(Transaction)
admin.site.register(GroupTransaction)
