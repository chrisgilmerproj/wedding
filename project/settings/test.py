from settings import * 

# Include all the settings specific to 'development' machines
# such as DATABASES, TIME_ZONE
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(PROJECT_ROOT, 'wedding_test.db'),
    }
}

# Store e-mail message in memory for testing
EMAIL_BACKEND = 'django.core.mail.backends.locmom.EmailBackend'

# Install applications for integration testing
INSTALLED_APPS += (
    'lettuce.django',    # for Behavior Driven Development
    'adminlettuce' ,     # to generate documentation from features
    'radish',            # tests for admin
)

# List applications with lettuce features
LETTUCE_APPS = ( 
)
