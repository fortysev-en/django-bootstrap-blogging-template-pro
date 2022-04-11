from cgitb import text
import string
from django.utils.text import slugify
import random, string

# generate random characters
def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
    return res

# generate slug
def generate_slug(text):
    from blogs.models import Blog
    new_slug = slugify(text)
    # check if the slug is already available
    if Blog.objects.filter(slug = new_slug).exists():
        # if available, generate 5 ramdom characters and add it with the slug
        new_slug = generate_slug(text + '-' + generate_random_string(5))
        return new_slug
    else:
        return new_slug


def get_ip(request):

    #get IP address of a user and save it in a model
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        print ("returning FORWARDED_FOR")
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        print ("returning REAL_IP")
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        print ("returning REMOTE_ADDR")
        ip = request.META.get('REMOTE_ADDR')
    return ip
