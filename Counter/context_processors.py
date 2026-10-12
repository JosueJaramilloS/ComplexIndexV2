from User.models import Expert

def user_roles(request):
    if request.user.is_authenticated:
        is_admin = request.user.is_staff or request.user.is_superuser
        is_expert = hasattr(request.user, 'expert_profile') or Expert.objects.filter(user=request.user).exists()
        is_regular = not is_admin and not is_expert
        return {
            'is_admin': is_admin,
            'is_expert': is_expert,
            'is_regular': is_regular,
        }
    return {
        'is_admin': False,
        'is_expert': False,
        'is_regular': False,
    }
