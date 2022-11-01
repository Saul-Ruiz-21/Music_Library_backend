# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s(w2ikxn%$hy_oa8z#gy5@*z$il9m1245x+g0l-2sjwn175hoa'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_library_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Password'
    }
}
