from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class EmailBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user_specific = user_model.objects.get(email=username)
        except user_model.DoesNotExist:
            return None
        else:
            if user_specific.check_password(password):
                return user_specific
        return None
