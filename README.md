# Python Django 4帖入門 연습 프로젝트

이 프로젝트는 **『Python Django 4帖入門』** 책의 내용을 실습하고 연습하기 위해 만들어졌습니다.  
책의 목차에 따라 각 장별로 실습 예제를 구현하고 있습니다.

---

## 프로젝트 설정 및 실행 방법

1. **프로젝트 클론**
    ```bash
    git clone [repository_url]
    cd django_app
    ```

2. **환경 설정**
    ```bash
    # 가상환경 생성 및 활성화 (선택사항)
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    # venv\Scripts\activate  # Windows

    # 의존성 설치
    pip install -r requirements.txt
    ```

3. **로컬 설정**
    ```bash
    # 로컬 설정 파일 생성
    cp django_app/settings/local.py.example django_app/settings/local.py
    
    # local.py 파일에서 필요한 설정 수정
    # - DEBUG
    # - SECRET_KEY
    # - DATABASE
    # - 기타 로컬 환경 설정
    ```

4. **서버 실행**
    ```bash
    # 기본 포트(8000)로 실행
    python run_server.py
    
    # 또는 직접 포트 지정
    python manage.py runserver 8080
    ```

## 프로젝트 구조

```
django_app/
├── django_app/
│   └── settings/
│       ├── __init__.py    # 설정 로드 로직
│       ├── base.py        # 기본 설정 (Git에 포함)
│       ├── local.py       # 로컬 환경 설정 (Git에서 제외)
│       └── local.py.example  # 로컬 설정 예제
├── requirements.txt    # 프로젝트 의존성
├── run_server.py      # 서버 실행 스크립트
└── manage.py
```

---

## 목차

1. **환경설정**
    - Python 및 Django 설치
    - 가상환경 설정
    - 프로젝트 및 앱 생성
        - 서버실행(console)
            > django_app git:(dev) python3 manage.py
    - 기본 설정 파일 수정

2. **View, Template**

    - **View 작성**
        - 함수형 View와 클래스형 View를 작성하여 요청을 처리합니다.
        - 예시: `hello/views.py`에서 `index`, `next` 함수 정의

    - **Template 작성 및 활용**
        - 템플릿 파일은 `hello/templates/hello/index.html`에 위치합니다.
        - 템플릿에서 변수(`{{ title }}`, `{{ msg }}` 등)와 템플릿 태그(`{% url goto %}` 등)를 활용합니다.

    - **URL 매핑**
        - `hello/urls.py`에서 URL 패턴을 View와 연결합니다.
        - 예시: `path('', views.index, name='index')`, `path('next', views.next, name='next')`

    - **템플릿 상속 및 정적 파일 사용**
        - 템플릿 상속 구조를 활용하여 공통 레이아웃을 관리할 수 있습니다.
        - 정적 파일(css 등)은 `hello/static/hello/css/style.css`에 위치하며, 템플릿에서 `{% static %}` 태그로 불러옵니다.

3. **(추가 예정)**

4. **(추가 예정)**

5. **(추가 예정)**

---

## 참고

- 본 프로젝트는 개인 학습 및 연습용입니다.
- 책의 예제와 설명을 따라가며 실습을 진행합니다.

---

---

## Tip

**💡 vscode Tip:** vscode 탐색기 보기
 `app_name/templates/app_name/` 구조로 만드세요.
    ```
        VS Code에서 디렉터리 구조를 **트리(계층 구조)**로 보이게 하려면,
        기본적으로 탐색기(Explorer) 뷰가 트리 구조로 표시됩니다.

        만약 옆으로(플랫하게) 보인다면, 아래 설정을 확인하세요.

        탐색기에서 "압축된 폴더" 해제

        VS Code 좌측 상단의 탐색기(Explorer)에서
        ... (더보기) 메뉴 클릭 → 압축된 폴더 사용(Compact Folders) 체크 해제
        설정에서 직접 변경

        ⌘ + , (설정 열기)
        검색창에 compact folders 입력
        Explorer: Compact Folders 옵션을 끄기(Off)
        이렇게 하면 index.html이
        트리 구조로
        template
        └── hello
            └── index.html
    ```

**💡 Git Tip:** remote 전체 디렉터리 보기

    ```
        ＞　hello git:(dev) ✗ git ls-tree --name-only origin/dev
    ```

**💡 PlantUML Tip:** *.puml파일의 내용을 아래의 PlantUml viewer site에서 확인 가능

    ```
        ＞　https://plantumlviewer.web.app/
    ```

**💡 PlantUML 설치 및 사용 방법 TIP:**

1. **Graphviz 설치 확인**
    ```bash
    # Graphviz 버전 확인
    dot -V
    
    # 설치가 안 되어 있다면 설치 (macOS)
    brew install graphviz
    ```

2. **PlantUML JAR 파일 다운로드**
    ```bash
    # 최신 버전 다운로드 (1.2024.3 버전 기준)
    # 프로젝트 루트 디렉토리에서 실행
    curl -o plantuml.jar -L https://github.com/plantuml/plantuml/releases/download/v1.2024.3/plantuml-1.2024.3.jar

    # 또는 직접 다운로드 후 프로젝트 루트 디렉토리에 복사
    # https://github.com/plantuml/plantuml/releases/latest
    ```

3. **다이어그램 생성 방법**
    ```bash
    # PlantUML 파일로부터 이미지 생성
    java -jar plantuml.jar your-diagram.puml
    
    # 예시: test.puml 파일로부터 test.png 생성
    java -jar plantuml.jar test.puml
    ```

4. **다이어그램 작성 예시**
    ```plantuml
    @startuml
    title 세션 관리 플로우
    actor User
    participant "Browser" as B
    participant "Django View" as V
    
    User -> B: 요청
    B -> V: 처리
    V -> B: 응답
    B -> User: 결과
    @enduml
    ```

---
