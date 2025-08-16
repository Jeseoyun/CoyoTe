# 🧩 CoyoTe 문제 추천 시스템

`solved.ac` API를 활용하여 개인화된 알고리즘 문제를 추천해주는 Streamlit 웹 애플리케이션입니다.

## 🚀 주요 기능

- **개인화된 추천**: 여러 사용자가 모두 풀지 않은 문제만 추천
- **난이도별 필터링**: 원하는 난이도 범위 내에서 문제 선택
- **태그 기반 검색**: 특정 알고리즘이나 주제에 집중
- **무작위 추천**: 매번 다른 문제를 추천받을 수 있음
- **사용자 친화적 UI**: 직관적인 웹 인터페이스

## 📋 사용법

### 1. 설치 및 실행

```bash
# 의존성 설치
pip install -r requirements.txt

# 앱 실행
streamlit run problem_recommender_app.py
```

### 2. 설정 방법

1. **사용자 핸들 입력**: solved.ac에서 사용하는 핸들을 한 줄에 하나씩 입력
2. **난이도 설정**: 원하는 난이도 범위 선택 (B5 ~ R1)
3. **태그 선택**: 원하는 알고리즘/주제 태그 선택 (최대 5개)
4. **문제 개수**: 추천받을 문제 개수 설정 (1~20개)
5. **언어 설정**: 한국어 또는 영어 선택

### 3. 추천 받기

설정을 완료한 후 "🚀 문제 추천받기" 버튼을 클릭하면 맞춤형 문제를 추천받을 수 있습니다.

## 🎯 지원하는 태그

- **기본 알고리즘**: implementation, dp, greedy, binary_search, sorting
- **자료구조**: graph, tree, string, stack, queue, deque, priority_queue
- **고급 알고리즘**: union_find, segment_tree, fenwick_tree, sparse_table
- **수학**: math, geometry, combinatorics, number_theory
- **기타**: simulation, bruteforce, two_pointer, prefix_sum

## 🔧 기술 스택

- **Frontend**: Streamlit
- **Backend**: Python
- **API**: solved.ac API v3
- **HTTP Client**: requests

## 📱 화면 구성

- **사이드바**: 사용자 설정 및 옵션
- **메인 영역**: 추천된 문제 목록 및 상세 정보
- **확장 가능한 카드**: 각 문제의 상세 정보를 깔끔하게 표시

## ⚠️ 주의사항

- solved.ac API의 요청 제한을 고려하여 적절한 딜레이를 적용했습니다
- 사용자 핸들은 정확하게 입력해야 합니다
- 인터넷 연결이 필요합니다

## 🚀 향후 개선 계획

- [ ] 문제 히스토리 저장
- [ ] 추천 알고리즘 개선
- [ ] 사용자 선호도 학습
- [ ] 모바일 최적화
- [ ] 다크 모드 지원

## 📞 문의

문제가 있거나 개선 제안이 있으시면 언제든 연락주세요!

