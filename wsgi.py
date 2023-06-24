import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hammer_doors.settings')


sys.path.remove('/usr/lib/python3/dist-packages')
sys.path.append('/home/c/cw35033/public_html/hammer_doors')
sys.path.append('/home/c/cw35033/public_html/venv/lib/python3.6/site-packages')


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
