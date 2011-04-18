from settings import * 

# Include all the settings specific to 'staging' machines
# such as DATABASES, TIME_ZONE, DEFAULT_FILE_STORAGE
DATABASES = {
    'default': {
        'NAME': 'wedding_staging',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost'
    }
}

# Uncomment the following to use Rackspace as the CDN for staging 
# INSTALLED_APPS = INSTALLED_APPS + (
#     'cumulus', # to run ./manage.py syncstatic
# )
# 
# # Credentials to store and retrieve assets and uploads from Rackspace CDN
# CUMULUS_USERNAME         = '[Your username]'
# CUMULUS_API_KEY          = '[Your API key]'
# CUMULUS_CONTAINER        = '[Your container]'
# CUMULUS_FILTER_LIST      = ['.DS_Store']
# CUMULUS_STATIC_CONTAINER = '[Your container]'
# CUMULUS_USE_SERVICENET   = False
# # Timeout for Rackspace read operations (defaults to 5, Rackspace suggests 15)
# CUMULUS_TIMEOUT          = 30
# 
# # Uploads are stored by default on the CDN
# DEFAULT_FILE_STORAGE     = 'cumulus.storage.CloudFilesStorage'
# # Absolute path to the directory that holds stored files.
# MEDIA_ROOT = ''
# # URL that handles the media served from MEDIA_ROOT (must end in a slash)
# MEDIA_URL = '/uploads/' 
# 
# # Static files are retrieved from the CDN, where they should be loaded
# # after every deploy by running ./manage.py syncstatic -v 2 --traceback
# STATIC_URL               = "[Full path to the CDN]"
# # Absolute path to the directory where syncstatic will collect static files 
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
# # Additional locations the staticfiles app will traverse
# STATICFILES_DIRS = []

