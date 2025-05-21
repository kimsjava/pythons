import os
import sys
from django.core.management import execute_from_command_line
from django.conf import settings

def run_server():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_app.settings')
    port = getattr(settings, 'PORT', 8000)  # settings에서 PORT 값을 가져오거나 기본값 8000 사용
    argv = sys.argv
    if len(argv) <= 1:
        argv.append('runserver')
        argv.append(f'0.0.0.0:{port}')
    execute_from_command_line(argv)

if __name__ == '__main__':
    run_server() 