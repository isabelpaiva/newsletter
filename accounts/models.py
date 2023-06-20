from django.db import models
from django.contrib.auth.models import AbstractUser

# Criar uma classe que herde abstractUser
#  add  no settings.py AUTH_USER_MODEL, tendo como valor o caminho ate a model de usuario
# rodar migraçao

class Account(AbstractUser):
    ...