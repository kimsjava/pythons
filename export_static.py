import os
import requests
import django
import shutil
from django.conf import settings
from django.urls import get_resolver, URLPattern, URLResolver

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_app.settings')
django.setup()

BASE_URL = "http://127.0.0.1:8000"
EXPORT_PATH = "hugo_site/public"

def extract_urls(urlpatterns, prefix=""):
    urls = []
    for pattern in urlpatterns:
        if isinstance(pattern, URLPattern):
            # 변수 패턴이 없는 경우만 추출
            if not pattern.pattern.converters:
                path = prefix + str(pattern.pattern)
                # 끝에 $가 붙는 경우 제거
                if path.endswith('$'):
                    path = path[:-1]
                urls.append(path)
        elif isinstance(pattern, URLResolver):
            urls += extract_urls(pattern.url_patterns, prefix + str(pattern.pattern))
    return urls

urlpatterns = get_resolver().url_patterns
all_urls = extract_urls(urlpatterns)

os.makedirs(EXPORT_PATH, exist_ok=True)

# URL → 파일명 매핑 자동 생성
url_to_filename = {}
for url in all_urls:
    url_path = url.lstrip('/').rstrip('/')
    filename = url_path.replace('/', '_') or 'index'
    filename += '.html'
    # 절대경로와 상대경로 모두 치환
    url_to_filename[f'href="/{url_path}/"'] = f'href="{filename}"'
    url_to_filename[f"href='/{url_path}/'"] = f"href='{filename}'"
    url_to_filename[f'href="/{url_path}"'] = f'href="{filename}"'
    url_to_filename[f"href='/{url_path}'"] = f"href='{filename}'"

for url in all_urls:
    # url이 ''이면 루트, 아니면 앞뒤 슬래시 정리
    url_path = url.lstrip('/').rstrip('/')
    filename = url_path.replace('/', '_') or 'index'
    filename += '.html'
    full_url = f"{BASE_URL}/{url_path}" if url_path else BASE_URL
    print(f"Requesting: {full_url} -> {filename}")
    try:
        res = requests.get(full_url)
        if res.status_code == 200:
            with open(os.path.join(EXPORT_PATH, filename), "w", encoding="utf-8") as f:
                html = res.text
                # static 경로 치환
                html = html.replace('href="/static/', 'href="static/')
                # 모든 내부 링크 자동 치환
                for old, new in url_to_filename.items():
                    html = html.replace(old, new)
                f.write(html)
            print(f"Exported: {filename}")
        else:
            print(f"Failed: {full_url} ({res.status_code})")
    except Exception as e:
        print(f"Error: {full_url} ({e})")

# Django static 폴더 경로 (앱별 static 폴더 기준)
STATIC_SRC = "hello/static"
STATIC_DST = os.path.join(EXPORT_PATH, "static")

# static 폴더 전체 복사 (기존 내용 삭제 후 복사)
if os.path.exists(STATIC_DST):
    shutil.rmtree(STATIC_DST)
shutil.copytree(STATIC_SRC, STATIC_DST)
print(f"Static files copied: {STATIC_SRC} -> {STATIC_DST}")