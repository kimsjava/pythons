# Django Application

이 애플리케이션은 친구 정보를 관리하는 간단한 Django CRUD 기능을 제공합니다.

## 프로젝트 구조

```
django_app/                 # 프로젝트 루트 디렉터리
│
├── django_app/             # 프로젝트 설정 패키지
│   ├── __init__.py         # Python 패키지임을 나타내는 파일
│   ├── settings.py         # 프로젝트 설정 파일
│   ├── urls.py             # 프로젝트 URL 설정 (hello 앱으로 라우팅)
│   ├── asgi.py             # ASGI 호환 웹 서버 진입점
│   └── wsgi.py             # WSGI 호환 웹 서버 진입점
│
├── hello/                  # hello 애플리케이션 패키지
│   ├── __init__.py         # Python 패키지임을 나타내는 파일
│   ├── admin.py            # 관리자 인터페이스 설정
│   ├── apps.py             # 앱 설정
│   ├── forms.py            # 폼 클래스 정의 (HelloForm, FriendForm)
│   ├── migrations/         # 데이터베이스 마이그레이션 파일 디렉터리
│   │   ├── __init__.py
│   │   └── 0001_initial.py # 초기 마이그레이션 파일
│   ├── models.py           # Friend 모델 정의
│   ├── tests.py            # 테스트 코드
│   ├── urls.py             # 앱 URL 설정 (index, create, edit, delete 등)
│   ├── views.py            # 뷰 함수 및 클래스 정의
│   └── templates/          # 템플릿 디렉터리
│       └── hello/          # 앱 이름으로 된 하위 디렉터리
│           ├── index.html      # 메인 목록 화면
│           ├── create.html     # 데이터 생성 폼
│           ├── edit.html       # 데이터 수정 폼
│           ├── delete.html     # 데이터 삭제 확인
│           ├── friend_list.html    # 클래스 기반 뷰용 목록 화면
│           └── friend_detail.html  # 클래스 기반 뷰용 상세 화면
│
├── static/                 # 정적 파일 디렉터리
│   └── hello/              # 앱 이름으로 된 하위 디렉터리
│       └── css/            # CSS 파일 디렉터리
│           └── style.css   # 스타일시트 파일
│
├── .vscode/                # VS Code 설정 디렉터리
│   └── settings.json       # VS Code 설정 파일
│
├── venv/                   # 가상 환경
│
├── manage.py               # Django 프로젝트 관리 스크립트
│
├── db.sqlite3              # SQLite 데이터베이스 파일
│
├── README.md               # 프로젝트 설명 문서
└── README-DIR.md           # 프로젝트 구조 설명 문서
```

## 설치 및 실행 방법

1. 저장소 클론:

   ```
   git clone <repository-url>
   cd django_app
   ```

2. 가상 환경 생성 및 활성화:

   ```
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   # 또는
   venv\Scripts\activate  # Windows
   ```

3. 의존성 설치:

   ```
   pip install -r requirements.txt
   # 또는
   pip install django
   ```

4. 데이터베이스 마이그레이션:

   ```
   python manage.py migrate
   ```

5. 개발 서버 실행:
   ```
   python manage.py runserver
   ```

## 애플리케이션 접근

- 메인 페이지: http://127.0.0.1:8000/ 또는 http://127.0.0.1:8000/hello/
- 관리자 인터페이스: http://127.0.0.1:8000/admin/

## 기능

- 친구 정보 관리 (생성, 조회, 수정, 삭제)
- 함수 기반 뷰와 클래스 기반 뷰 예시
- ModelForm을 사용한 폼 처리
- SQLite 데이터베이스 통합
