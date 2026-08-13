import os
import sys
import django

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sos_state_co_us')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'sos_state_co_us.settings'


django.setup()