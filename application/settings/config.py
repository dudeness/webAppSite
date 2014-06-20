from base import *

"""
This file composes the settings and extends config environment.

Examples:
from config_dev import *
from config_stage import *
from config_prod import *
"""

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


from internationalisation import *
from database import *
from middlewares import *
from apps import *
from modules import *
from statics import *
from templates import *

from config_dev import *
