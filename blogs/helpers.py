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
        return generate_slug(text + generate_random_string(5))
    return new_slug