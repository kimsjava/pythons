# Python Django 4帖入門 연습 프로젝트

이 프로젝트는 **『Python Django 4帖入門』** 책의 내용을 실습하고 연습하기 위해 만들어졌습니다.  
책의 목차에 따라 각 장별로 실습 예제를 구현하고 있습니다.

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


---
