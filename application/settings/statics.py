from base import *
from modules import *
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# Additional locations of static files
STATICFILES_DIRS = ()


for module in INSTALLED_MODULES:
    if DEBUG:
        STATICFILES_DIRS += (os.path.join(MODULE_PATH, module, 'static'),)


PIPELINE_JS = {
    'vendor': {
        'source_filenames': (
          'vendor/jquery/*.js',
          'vendor/lodash/*.js',
        ),
        'output_filename': 'compiled/vendor.min.js',
    }
}

for module in INSTALLED_MODULES:
    PIPELINE_JS.update({
        module: {
            'source_filenames': (
                module + '/javascript/controller/*.js',
                module + '/javascript/directive/*.js',
                module + '/javascript/*.js',
            ),
            'output_filename': 'compiled/' + module + '.min.js',
        }
    })

PIPELINE_CSS = {
    'styles': {
        'source_filenames': (
          'compiled/styles.css',
        ),
        'output_filename': 'compiled/styles.min.css',
    },
}
