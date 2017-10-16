from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


def validate_unique_user(value):

    if User.objects.filter(username=value).exists():
        raise ValidationError('Já existe um usuário com esse username.')
