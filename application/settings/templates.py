from base import *
from modules import INSTALLED_MODULES

TEMPLATE_DIRS = ()

for module in INSTALLED_MODULES:
    TEMPLATE_DIRS += (os.path.join(MODULE_PATH, module, 'templates'),)