from django.db import models
from models import Transaction
question = Transaction.objects.get(category=765)
print(question)