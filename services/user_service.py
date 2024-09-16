from core.models import User

def get_user_details(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None