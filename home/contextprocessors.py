from .models import SocialMedia, Contact

def social_and_contact(request):
    try:
        social_media = SocialMedia.objects.last()  
    except SocialMedia.DoesNotExist:
        social_media = None

    try:
        contact_info = Contact.objects.last()  
    except Contact.DoesNotExist:
        contact_info = None

    return {
        'social_media': social_media,
        'contact_info': contact_info
    }