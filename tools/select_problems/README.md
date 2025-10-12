# CoyoTe 문제 추천 시스템

CoyoTe 팀을 위한 백준 온라인 저지 문제 추천 시스템입니다. solved.ac API를 활용하여 사용자의 실력과 선호도에 맞는 문제를 추천합니다.

## 🚀 주요 기능

- **맞춤형 문제 추천**: 사용자의 실력과 선호하는 알고리즘 태그를 기반으로 문제 추천
- **난이도 필터링**: Bronze부터 Ruby까지 다양한 난이도 선택 가능
- **알고리즘 태그 기반 검색**: 구현, 그리디, BFS/DFS, DP 등 다양한 알고리즘 분야별 문제 추천
- **Streamlit 웹 인터페이스**: 직관적이고 사용하기 쉬운 웹 UI
- **문제 상세 정보**: 각 문제의 난이도, 태그, 해결자 수 등 상세 정보 제공

## 📋 요구사항

- Python 3.11 이상
- solved.ac API 접근 가능

## 🛠️ 설치 및 실행

### 1. 의존성 설치

```sh
# pip 사용
pip install streamlit requests

# 또는 uv 사용 (권장)
uv add streamlit requests
```

### 2. 웹 애플리케이션 실행 

```sh
# Streamlit 앱 실행
streamlit run problem_recommender_app.py

# 또는 직접 실행
python problem_recommender_app.py
```

### 3. 브라우저에서 접속

애플리케이션이 실행되면 터미널에 표시되는 URL(보통 `http://localhost:8501`)로 접속하세요.

## 📁 프로젝트 구조

```
tools/select_problems/
├── problem_recommender_app.py  # Streamlit 웹 애플리케이션
├── select_problem.py          # 문제 추천 로직
├── algorithm_tags.json        # 알고리즘 태그 데이터
├── requirements.txt           # Python 의존성
├── pyproject.toml            # 프로젝트 설정
└── README.md                 # 프로젝트 문서
```

## 🎯 사용 방법

1. **웹 애플리케이션 실행** 후 브라우저에서 접속
2. **사용자 설정** 입력:
   - 선호하는 알고리즘 태그 선택
   - 원하는 난이도 범위 설정
   - 추천받을 문제 개수 설정
3. **문제 추천** 버튼 클릭하여 맞춤형 문제 목록 확인
4. **문제 상세 정보** 확인 후 백준 온라인 저지에서 문제 해결

## 🔧 설정 옵션

- **알고리즘 태그**: 구현, 그리디, BFS, DFS, DP, 이진 탐색 등
- **난이도**: Bronze 5~1, Silver 5~1, Gold 5~1, Platinum 5~1, Diamond 5~1, Ruby 5~1
- **문제 개수**: 1~20개 (기본값: 5개)
- **해결자 수 필터**: 최소/최대 해결자 수 범위 설정

## 📊 API 정보

이 프로젝트는 [solved.ac API](https://solved.ac/api)를 사용하여 문제 데이터를 가져옵니다.

## 🤝 기여하기

1. 이 저장소를 포크합니다
2. 새로운 기능 브랜치를 생성합니다 (`git checkout -b feature/새기능`)
3. 변경사항을 커밋합니다 (`git commit -am 'feat: 새 기능 추가'`)
4. 브랜치에 푸시합니다 (`git push origin feature/새기능`)
5. Pull Request를 생성합니다

## 📝 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 🐛 문제 신고

버그를 발견하거나 기능 요청이 있으시면 [Issues](https://github.com/your-repo/issues) 페이지에서 신고해 주세요.

---