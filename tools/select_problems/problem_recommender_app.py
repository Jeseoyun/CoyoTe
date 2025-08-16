import streamlit as st
import json
from typing import List, Dict, Any
from select_problem import get_random_problems as select_problem_get_random_problems, TIER_TO_LEVEL_MAP, LEVEL_TO_TIER_MAP

# ============================================================================
# 페이지 설정
# ============================================================================
st.set_page_config(
    page_title="CoyoTe 문제 추천 시스템",
    page_icon="🚀",
    layout="wide"
)

# ============================================================================
# 상수 정의 (select_problem.py에서 import)
# ============================================================================

# 안전한 난이도 표시를 위한 함수
def get_safe_tier_display(level: int) -> str:
    """안전하게 난이도를 표시용으로 변환합니다."""
    try:
        if level in LEVEL_TO_TIER_MAP:
            return LEVEL_TO_TIER_MAP[level].upper()
        else:
            # solved.ac의 난이도 체계에 맞게 매핑
            if level == 0:
                return "❓ UNRATED"
            elif 1 <= level <= 5:
                return f"🥉 B{6-level}"
            elif 6 <= level <= 10:
                return f"🥈 S{11-level}"
            elif 11 <= level <= 15:
                return f"🥇 G{16-level}"
            elif 16 <= level <= 20:
                return f"💎 P{21-level}"
            elif 21 <= level <= 25:
                return f"💠 D{26-level}"
            elif 26 <= level <= 30:
                return f"🔴 R{31-level}"
            else:
                return f"❓ Level {level}"
    except (TypeError, ValueError):
        return f"❓ Level {level}"

DIFFICULTY_GROUPS = {
    'unrated': ['unrated'],
    'bronze': ['b5', 'b4', 'b3', 'b2', 'b1'],
    'silver': ['s5', 's4', 's3', 's2', 's1'],
    'gold': ['g5', 'g4', 'g3', 'g2', 'g1'],
    'platinum': ['p5', 'p4', 'p3', 'p2', 'p1'],
    'diamond': ['d5', 'd4', 'd3', 'd2', 'd1'],
    'ruby': ['r5', 'r4', 'r3', 'r2', 'r1']
}

# 기본 선택 태그
DEFAULT_TAGS = ['graph', 'dfs', 'bfs', 'implementation', 'tree', 'simulation']

# 기본 사용자 목록
DEFAULT_USERS = ["qja1998", "woghks1213y", "jeeeseo98", "nimootmic"]

# ============================================================================
# 데이터 로딩 함수
# ============================================================================
def load_algorithm_tags() -> Dict[str, Any]:
    """algorithm_tags.json 파일에서 알고리즘 태그를 로드합니다."""
    try:
        with open('algorithm_tags.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("algorithm_tags.json 파일을 찾을 수 없습니다.")
        return {"categories": {}, "metadata": {}}
    except json.JSONDecodeError:
        st.error("algorithm_tags.json 파일 형식이 올바르지 않습니다.")
        return {"categories": {}, "metadata": {}}

# 알고리즘 태그 로드 및 카테고리 설정
ALGORITHM_TAGS = load_algorithm_tags()

# 태그 카테고리별 그룹화
TAG_CATEGORIES = {}
for category_name, category_data in ALGORITHM_TAGS.get("categories", {}).items():
    emoji_map = {
        "기본 알고리즘": "📚", "탐색": "🔍", "동적 프로그래밍": "📊",
        "그래프 이론": "🌐", "트리": "🌳", "자료구조": "🏗️",
        "문자열": "📝", "수학": "🔢", "기하학": "📐",
        "조합론": "🎲", "최적화": "⚡", "고급 기법": "💡"
    }
    
    emoji = emoji_map.get(category_name, "📋")
    display_name = f"{emoji} {category_name}"
    tags = [item["tag"] for item in category_data.get("tags", [])]
    TAG_CATEGORIES[display_name] = tags

# 모든 태그를 평면화
AVAILABLE_TAGS = [tag for category in TAG_CATEGORIES.values() for tag in category]

# ============================================================================
# API 관련 함수
# ============================================================================
def build_api_query(
    user_handles: list[str],
    tags: list[str],
    korean_only: bool,
    min_acceptance_rate: float,
    max_acceptance_rate: float,
    min_attempted_users: int,
    max_attempted_users: int,
    tier_range: tuple = None,
    language: str = 'ko',
    debug: bool = False
) -> str:
    """API 쿼리 문자열을 구성합니다."""
    query_parts = []
    
    # 사용자 필터
    if user_handles:
        query_parts.append(f"!solved_by:{','.join(user_handles)}")
    
    # 난이도 필터
    if tier_range:
        min_level, max_level = tier_range
        query_parts.append(f"tier:{min_level}..{max_level}")
    
    # 태그 필터
    if tags:
        query_parts.append(f"tag:{'|'.join(tags)}")
    
    # 언어 필터
    if korean_only:
        query_parts.append("lang:ko")
    elif language == 'ko':
        query_parts.append("lang:ko")
    elif language == 'en':
        query_parts.append("lang:en")
    
    # 정답률 필터
    if min_acceptance_rate > 0 or max_acceptance_rate < 100:
        query_parts.append(f"acceptance_rate:{min_acceptance_rate}..{max_acceptance_rate}")
    
    # 시도한 사람 수 필터
    if min_attempted_users >= 0 and max_attempted_users <= 100000:
        if min_attempted_users > 0 or max_attempted_users < 100000:
            query_parts.append(f"attempted_users:{min_attempted_users}..{max_attempted_users}")
            if debug:
                st.write(f"🔍 **시도한 사람 필터**: {min_attempted_users} ~ {max_attempted_users}")
    
    return " ".join(query_parts)

def fetch_problems_from_api(query: str, count: int, debug: bool = False) -> List[Dict[str, Any]]:
    """solved.ac API에서 문제를 가져옵니다."""
    try:
        url = "https://solved.ac/api/v3/search/problem"
        # solved.ac API는 count 파라미터를 지원하지 않으므로 page 크기를 조정
        # 한 페이지당 최대 50개 문제를 가져와서 필요한 만큼만 반환
        page_size = min(count * 2, 50)  # 여유분을 두고 가져옴
        params = {"query": query, "page": 1, "sort": "random"}
        
        if debug:
            st.write(f"🔗 **API URL**: {url}")
            st.write(f"📝 **API 쿼리**: `{query}`")
            st.write(f"📊 **요청 파라미터**: {params}")
            st.write(f"🎯 **요청 개수**: {count}개 (페이지 크기: {page_size})")
        
        response = requests.get(url, params=params, headers={"Accept": "application/json"})
        response.raise_for_status()
        
        data = response.json()
        problems = data.get('items', [])
        
        if debug:
            st.write(f"✅ **응답 결과**: {len(problems)}개 문제 발견")
            if problems:
                # 첫 번째 문제의 난이도 정보 표시
                first_problem = problems[0]
                st.write(f"📊 **첫 번째 문제**: ID {first_problem.get('problemId')}, 난이도 Level {first_problem.get('level')}")
        
        # 요청한 개수만큼 반환
        return problems[:count]
        
    except Exception as e:
        st.error(f"API 호출 중 오류 발생: {e}")
        return []

def get_problems_by_difficulty_ratio(
    user_handles: list[str],
    tags: list[str],
    language: str,
    korean_only: bool,
    min_acceptance_rate: float,
    max_acceptance_rate: float,
    min_attempted_users: int,
    max_attempted_users: int,
    difficulty_ratios: dict,
    min_tier: str = None,
    max_tier: str = None
) -> List[Dict[str, Any]]:
    """난이도별 비율에 따라 문제를 추천합니다. select_problem.py의 get_random_problems를 사용합니다."""
    all_problems = []
    
    # 전체 난이도 범위 계산
    if min_tier and max_tier:
        global_min_level = TIER_TO_LEVEL_MAP[min_tier.lower()]
        global_max_level = TIER_TO_LEVEL_MAP[max_tier.lower()]
        st.write(f"🎯 **전체 난이도 범위**: {min_tier.upper()} ~ {max_tier.upper()} (Level {global_min_level}-{global_max_level})")
        st.write(f"🔍 **전달받은 파라미터**: min_tier='{min_tier}', max_tier='{max_tier}'")
    else:
        global_min_level = 0
        global_max_level = 30
        st.write(f"🎯 **전체 난이도 범위**: 제한 없음 (Level 0-30)")
        st.write(f"🔍 **전달받은 파라미터**: min_tier={min_tier}, max_tier={max_tier}")
    
    st.write("🔍 **난이도별 문제 추천 진행 상황**")
    
    for difficulty, count in difficulty_ratios.items():
        if count > 0:
            st.write(f"📋 **{difficulty.upper()} 난이도**: {count}개 문제 요청")
            
            if difficulty == 'unrated':
                # UNRATED 문제는 최소/최대 난이도 범위 내에서만 처리
                if global_min_level <= 0 <= global_max_level:
                    st.write(f"⚠️ **UNRATED 경고**: 시도한 사람 수 필터가 제대로 작동하지 않을 수 있습니다.")
                    
                    # select_problem.py의 get_random_problems 사용
                    problems = select_problem_get_random_problems(
                        user_handles=user_handles,
                        min_tier='b5',  # UNRATED는 b5로 대체 (Level 1)
                        max_tier='b5',
                        tags=tags,
                        count=count,
                        language=language,
                        include_attempted=False,  # 시도한 문제는 제외
                        min_attempts=min_attempted_users if min_attempted_users > 0 else 0,
                        max_attempts=max_attempted_users if max_attempted_users > 0 else 0
                    )
                    st.write(f"❓ **UNRATED 결과**: {len(problems)}개 문제 발견")
                else:
                    st.write(f"⏭️ **UNRATED 건너뜀**: 난이도 범위 {global_min_level}-{global_max_level}에 포함되지 않음")
                    continue
            else:
                tier_list = DIFFICULTY_GROUPS[difficulty]
                difficulty_min_level = TIER_TO_LEVEL_MAP[tier_list[0]]
                difficulty_max_level = TIER_TO_LEVEL_MAP[tier_list[-1]]
                
                # 난이도 범위와 겹치는지 확인 (올바른 로직)
                # 두 범위가 겹치는지 확인: (a1, a2)와 (b1, b2)가 겹치려면 a1 <= b2 AND b1 <= a2
                ranges_overlap = (global_min_level <= difficulty_max_level) and (difficulty_min_level <= global_max_level)
                
                st.write(f"🔍 **{difficulty.upper()} 범위 계산**:")
                st.write(f"  - 전체 범위: Level {global_min_level}-{global_max_level}")
                st.write(f"  - {difficulty} 범위: Level {difficulty_min_level}-{difficulty_max_level}")
                st.write(f"  - 겹침 여부: {'예' if ranges_overlap else '아니오'}")
                
                if ranges_overlap:
                    # 겹치는 범위가 있는 경우, select_problem.py의 get_random_problems 사용
                    # 실제 겹치는 부분 계산
                    overlap_min = max(global_min_level, difficulty_min_level)
                    overlap_max = min(global_max_level, difficulty_max_level)
                    overlap_min_tier = LEVEL_TO_TIER_MAP[overlap_min]
                    overlap_max_tier = LEVEL_TO_TIER_MAP[overlap_max]
                    
                    problems = select_problem_get_random_problems(
                        user_handles=user_handles,
                        min_tier=overlap_min_tier,
                        max_tier=overlap_max_tier,
                        tags=tags,
                        count=count,
                        language=language,
                        include_attempted=False,  # 시도한 문제는 제외
                        min_attempts=min_attempted_users if min_attempted_users > 0 else 0,
                        max_attempts=max_attempted_users if max_attempted_users > 0 else 0
                    )
                    st.write(f"🎯 **{difficulty.upper()} 결과**: {len(problems)}개 문제 발견 (Level {overlap_min}-{overlap_max}, 원래 범위: {difficulty_min_level}-{difficulty_max_level})")
                else:
                    # 겹치는 범위가 없는 경우
                    st.write(f"⏭️ **{difficulty.upper()} 건너뜀**: 난이도 범위 {global_min_level}-{global_max_level}와 겹치지 않음 (원래 범위: {difficulty_min_level}-{difficulty_max_level})")
                    continue
            
            all_problems.extend(problems)
        else:
            st.write(f"⏭️ **{difficulty.upper()} 난이도**: 건너뜀 (설정값: 0)")
    
    st.success(f"🎉 **총 {len(all_problems)}개 문제 추천 완료!**")
    return all_problems

def get_random_problems(
    user_handles: list[str],
    min_tier: str,
    max_tier: str,
    tags: list[str],
    count: int = 10,
    language: str = 'ko',
    korean_only: bool = False,
    min_acceptance_rate: float = 0,
    max_acceptance_rate: float = 100,
    min_attempted_users: int = 0,
    max_attempted_users: int = 100000,
    difficulty_ratios: dict = None
) -> List[Dict[str, Any]]:
    """사용자들이 풀지 않은 문제 중에서 조건에 맞는 문제를 추천합니다. select_problem.py의 함수를 사용합니다."""
    
    # 난이도별 비율이 설정된 경우
    if difficulty_ratios:
        return get_problems_by_difficulty_ratio(
            user_handles, tags, language, korean_only,
            min_acceptance_rate, max_acceptance_rate,
            min_attempted_users, max_attempted_users,
            difficulty_ratios, min_tier, max_tier
        )
    
    # select_problem.py의 get_random_problems 사용
    return select_problem_get_random_problems(
        user_handles=user_handles,
        min_tier=min_tier,
        max_tier=max_tier,
        tags=tags,
        count=count,
        language=language,
        include_attempted=False,  # 시도한 문제는 제외
        min_attempts=min_attempted_users if min_attempted_users > 0 else 0,
        max_attempts=max_attempted_users if max_attempted_users > 0 else 0
    )

# ============================================================================
# 유틸리티 함수
# ============================================================================
def get_tier_emoji(tier: str) -> str:
    """티어에 해당하는 이모지를 반환합니다."""
    emoji_map = {
        'g': "🥇", 'b': "🥉", 's': "🥈", 
        'p': "💎", 'd': "💠", 'r': "🔴"
    }
    return emoji_map.get(tier[0], "")

def format_tier_display(tier: str) -> str:
    """티어를 표시용으로 포맷합니다."""
    return f"{get_tier_emoji(tier)}{tier.upper()}"

# ============================================================================
# UI 컴포넌트 함수
# ============================================================================
def create_difficulty_ratio_ui() -> dict:
    """난이도별 비율 설정 UI를 생성하고 값을 반환합니다."""
    st.write("**난이도별 문제 수 비율**")
    st.caption("각 난이도에서 몇 개씩 문제를 가져올지 설정하세요")
    
    # UNRATED 경고
    st.warning("⚠️ **UNRATED 문제는 난이도가 정해지지 않은 문제로, 필터링이 제대로 작동하지 않을 수 있습니다.**")
    
    # 첫 번째 행: UNRATED, 브론즈, 실버
    col1, col2, col3 = st.columns(3)
    
    with col1:
        unrated_ratio = st.slider("❓ UNRATED", 0, 10, 0, 1, key="unrated_ratio")
        if unrated_ratio > 0:
            st.info("💡 UNRATED 문제는 시도한 사람 수 필터가 제대로 작동하지 않을 수 있습니다.")
    with col2:
        bronze_ratio = st.slider("🥉 브론즈", 0, 10, 0, 1, key="bronze_ratio")
    with col3:
        silver_ratio = st.slider("🥈 실버", 0, 10, 1, 1, key="silver_ratio")
    
    # 두 번째 행: 골드, 플래티넘, 다이아몬드
    col4, col5, col6 = st.columns(3)
    
    with col4:
        gold_ratio = st.slider("🥇 골드", 0, 10, 2, 1, key="gold_ratio")
    with col5:
        platinum_ratio = st.slider("💎 플래티넘", 0, 10, 0, 1, key="platinum_ratio")
    with col6:
        diamond_ratio = st.slider("💠 다이아몬드", 0, 10, 0, 1, key="diamond_ratio")
    
    # 세 번째 행: 루비
    col7, col8, col9 = st.columns(3)
    
    with col7:
        ruby_ratio = st.slider("🔴 루비", 0, 10, 0, 1, key="ruby_ratio")
    with col8:
        pass  # 빈 공간
    with col9:
        pass  # 빈 공간
    
    # 총 문제 수 계산 및 표시
    total_ratio = unrated_ratio + bronze_ratio + silver_ratio + gold_ratio + platinum_ratio + diamond_ratio + ruby_ratio
    
    if total_ratio > 0:
        st.success(f"📊 총 {total_ratio}개 문제 (❓{unrated_ratio} 🥉{bronze_ratio} 🥈{silver_ratio} 🥇{gold_ratio} 💎{platinum_ratio} 💠{diamond_ratio} 🔴{ruby_ratio})")
    else:
        st.warning("⚠️ 최소 하나의 난이도에서 문제를 선택해주세요")
    
    return {
        'unrated': unrated_ratio,
        'bronze': bronze_ratio,
        'silver': silver_ratio,
        'gold': gold_ratio,
        'platinum': platinum_ratio,
        'diamond': diamond_ratio,
        'ruby': ruby_ratio
    }

def display_user_info(handle: str) -> None:
    """사용자 정보를 표시합니다."""
    try:
        user_url = f"https://solved.ac/api/v3/user/show?handle={handle}"
        response = requests.get(user_url, headers={"Accept": "application/json"})
        
        if response.status_code == 200:
            user_data = response.json()
            
            with st.expander(f"👤 {handle}", expanded=True):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("티어", user_data.get('tier', 'Unknown'))
                    st.metric("랭킹", f"#{user_data.get('rank', 'Unknown')}")
                
                with col2:
                    st.metric("해결한 문제", f"{user_data.get('solvedCount', 0):,}개")
                    st.metric("평균 시도", f"{user_data.get('averageTries', 0):.1f}회")
                
                with col3:
                    st.metric("최고 연속 해결", f"{user_data.get('maxStreak', 0)}일")
                    st.metric("현재 연속 해결", f"{user_data.get('currentStreak', 0)}일")
                
                # 사용자 프로필 링크
                profile_url = f"https://solved.ac/profile/{handle}"
                st.markdown(f"**프로필:** [solved.ac에서 보기]({profile_url})")
        
        else:
            st.error(f"사용자 {handle}의 정보를 가져올 수 없습니다.")
            
    except Exception as e:
        st.error(f"사용자 {handle} 정보 확인 중 오류: {e}")

def display_problem_info(problems: List[Dict[str, Any]], difficulty_ratios: dict = None) -> None:
    """추천된 문제 정보를 표시합니다."""
    st.success(f"✅ 총 {len(problems)}개의 문제를 찾았습니다!")
    
    # 난이도별 비율 정보 표시
    if difficulty_ratios:
        ratio_info = []
        for difficulty, count in difficulty_ratios.items():
            if count > 0:
                emoji = {'unrated': '❓', 'bronze': '🥉', 'silver': '🥈', 'gold': '🥇',
                        'platinum': '💎', 'diamond': '💠', 'ruby': '🔴'}[difficulty]
                ratio_info.append(f"{emoji}{difficulty.title()}: {count}개")
        
        if ratio_info:
            st.info(f"📊 난이도별 구성: {' | '.join(ratio_info)}")
    
    # 문제 정보 표시
    for i, prob in enumerate(problems, 1):
        with st.expander(f"#{i} - {prob['titleKo']} (ID: {prob['problemId']})", expanded=True):
            col1, col2 = st.columns([1, 2])
            
            with col1:
                # 안전한 난이도 표시
                tier_display = get_safe_tier_display(prob['level'])
                st.metric("난이도", tier_display)
                
                st.metric("문제 ID", prob['problemId'])
                
                # 태그 표시
                tag_names = [tag['displayNames'][0]['name'] for tag in prob['tags']]
                st.write("**태그:**")
                for tag in tag_names:
                    st.markdown(f"- {tag}")
            
            with col2:
                # 문제 링크
                problem_url = f"https://www.acmicpc.net/problem/{prob['problemId']}"
                st.markdown(f"**문제 링크:** [BOJ #{prob['problemId']}]({problem_url})")
                
                # 문제 제목
                st.markdown(f"**제목:** {prob['titleKo']}")
                
                # 통계 정보
                if 'acceptedUserCount' in prob:
                    st.metric("맞힌 사람", f"{prob['acceptedUserCount']:,}명")
                
                if 'averageTries' in prob:
                    st.metric("평균 시도", f"{prob['averageTries']:.1f}회")
    
    # 전체 문제 링크
    st.markdown("---")
    st.markdown("### 🔗 전체 문제 링크")
    for prob in problems:
        problem_url = f"https://www.acmicpc.net/problem/{prob['problemId']}"
        st.markdown(f"- [{prob['problemId']} - {prob['titleKo']}]({problem_url})")

# ============================================================================
# 메인 함수
# ============================================================================
def main():
    st.title("🚀 CoyoTe 문제 추천 시스템")
    st.markdown("---")
    
    # 사이드바 - 사용자 관리
    with st.sidebar:
        st.header("👥 사용자 관리")
        
        # 사용자 추가
        new_user = st.text_input("새 사용자 추가", placeholder="사용자 핸들 입력")
        if st.button("➕ 추가", use_container_width=True):
            if new_user and new_user not in st.session_state.user_handles:
                st.session_state.user_handles.append(new_user)
                st.rerun()
        
        # 현재 사용자 목록
        if 'user_handles' not in st.session_state:
            st.session_state.user_handles = DEFAULT_USERS.copy()
        
        st.write("**현재 사용자 목록:**")
        for i, handle in enumerate(st.session_state.user_handles):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"• {handle}")
            with col2:
                if st.button("🗑️", key=f"del_{i}", use_container_width=True):
                    st.session_state.user_handles.pop(i)
                    st.rerun()
        
        # 사용자 목록 관리 버튼들
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 목록 초기화", use_container_width=True):
                st.session_state.user_handles = DEFAULT_USERS.copy()
                st.rerun()
        with col2:
            if st.button("📋 사용자 확인", use_container_width=True):
                st.session_state.check_users = True
        
        if not st.session_state.user_handles:
            st.warning("최소 한 명의 사용자를 추가해주세요.")
            return
        
        st.success(f"총 {len(st.session_state.user_handles)}명의 사용자")
        st.info("💡 문제 필터는 메인 영역에서 설정하세요!")
    
    # 메인 필터 UI
    st.header("🔍 문제 필터 설정")
    
    # 사용자 설정 확인
    if not st.session_state.user_handles:
        st.warning("⚠️ 먼저 사이드바에서 사용자를 추가해주세요!")
        st.info("👈 왼쪽 사이드바에서 '👥 사용자 관리' 섹션을 확인하세요.")
        return
    
    st.success(f"✅ {len(st.session_state.user_handles)}명의 사용자가 설정되었습니다")
    st.markdown("아래에서 문제 조건을 선택하고 추천받으세요.")
    
    # 메인 필터 섹션을 expander로 감싸기
    expander_expanded = not st.session_state.get('recommend_clicked', False)
    with st.expander("🔍 문제 필터 설정", expanded=expander_expanded):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 기본 필터")
            
            # 난이도 설정
            st.write("**난이도 범위 선택**")
            col_min, col_max = st.columns(2)
            
            with col_min:
                min_tier = st.selectbox(
                    "최소 난이도",
                    options=list(TIER_TO_LEVEL_MAP.keys()),
                    index=8,  # g5
                    key="main_min_tier",
                    format_func=format_tier_display
                )
            
            with col_max:
                max_tier = st.selectbox(
                    "최대 난이도",
                    options=list(TIER_TO_LEVEL_MAP.keys()),
                    index=12,  # g3
                    key="main_max_tier",
                    format_func=format_tier_display
                )
                
                # 선택된 난이도 범위 표시
                min_level = TIER_TO_LEVEL_MAP[min_tier.lower()]
                max_level = TIER_TO_LEVEL_MAP[max_tier.lower()]
                st.info(f"**선택된 난이도**: {format_tier_display(min_tier)} ~ {format_tier_display(max_tier)} (Level {min_level}-{max_level})")
                
                # 난이도 범위 경고
                if min_level > max_level:
                    st.error("⚠️ 최소 난이도가 최대 난이도보다 높습니다!")
                    st.info("💡 난이도 범위를 올바르게 설정해주세요.")
            
            # 태그 선택 시스템
            st.write("**📚 태그 선택**")
            st.caption("카테고리별로 전체 선택하거나 개별 태그를 선택할 수 있습니다. 검색으로도 태그를 찾을 수 있습니다.")
            
            # session_state에서 선택된 태그 상태 관리
            if 'selected_tags_state' not in st.session_state:
                st.session_state.selected_tags_state = set(DEFAULT_TAGS)
            
            # 기본 태그들이 항상 선택되어 있는지 확인
            for tag in DEFAULT_TAGS:
                if tag not in st.session_state.selected_tags_state:
                    st.session_state.selected_tags_state.add(tag)
            
            # 전체 태그 검색
            global_search_query = st.text_input(
                "🔍 전체 태그 검색",
                placeholder="태그명, 한국어 이름, 또는 키워드로 검색... (예: 'dp', '그래프', 'tree', '구현')",
                key="global_tag_search"
            )
            
            # 검색 결과 표시 및 선택
            if global_search_query:
                search_results = []
                search_lower = global_search_query.lower()
                
                # 모든 카테고리에서 검색
                for category_name, category_tags in TAG_CATEGORIES.items():
                    original_name = category_name.split(" ", 1)[1] if " " in category_name else category_name
                    category_data = ALGORITHM_TAGS.get("categories", {}).get(original_name, {})
                    
                    for tag in category_tags:
                        for tag_item in category_data.get("tags", []):
                            if tag_item["tag"] == tag:
                                # 한국어 이름과 영문 태그 모두에서 검색
                                if (search_lower in tag_item['name'].lower() or 
                                    search_lower in tag.lower()):
                                    search_results.append({
                                        'category': category_name,
                                        'display_name': f"{tag_item['name']} ({tag})",
                                        'tag': tag,
                                        'description': category_data.get("description", "")
                                    })
                                break
                
                if search_results:
                    st.success(f"🔍 '{global_search_query}' 검색 결과: {len(search_results)}개")
                    
                    # 검색 결과를 카테고리별로 그룹화
                    results_by_category = {}
                    for result in search_results:
                        cat = result['category']
                        if cat not in results_by_category:
                            results_by_category[cat] = []
                        results_by_category[cat].append(result)
                    
                    # 검색 결과 표시 및 선택
                    for category_name, results in results_by_category.items():
                        with st.expander(f"{category_name} - {len(results)}개 결과", expanded=True):
                            st.caption(f"💡 {results[0]['description']}")
                            
                            # 체크박스로 선택
                            for i, result in enumerate(results):
                                is_selected = result['tag'] in st.session_state.selected_tags_state
                                if st.checkbox(
                                    f"✅ {result['display_name']}", 
                                    value=is_selected,
                                    key=f"search_{result['tag']}_{category_name}_{i}"
                                ):
                                    st.session_state.selected_tags_state.add(result['tag'])
                                else:
                                    if result['tag'] in st.session_state.selected_tags_state:
                                        st.session_state.selected_tags_state.remove(result['tag'])
                else:
                    st.warning(f"🔍 '{global_search_query}'에 대한 검색 결과가 없습니다.")
                    st.info("💡 다른 키워드로 검색해보세요 (예: 'dp', '그래프', 'tree', '구현' 등)")
            
            # 카테고리별 태그 선택
            for category_name, category_tags in TAG_CATEGORIES.items():
                # 원본 카테고리명 추출 (이모지 제거)
                original_name = category_name.split(" ", 1)[1] if " " in category_name else category_name
                category_data = ALGORITHM_TAGS.get("categories", {}).get(original_name, {})
                description = category_data.get("description", "")
                
                # 기본 태그가 포함된 카테고리는 자동으로 펼침
                has_default_tags = any(tag in category_tags for tag in DEFAULT_TAGS)
                
                with st.expander(f"{category_name} ({len(category_tags)}개)", expanded=has_default_tags):
                    if description:
                        st.caption(f"💡 {description}")
                    
                    # 전체 선택 체크박스
                    all_selected = all(tag in st.session_state.selected_tags_state for tag in category_tags)
                    if st.checkbox(
                        f"✅ {category_name} 전체 선택",
                        value=all_selected,
                        key=f"cat_{category_name}"
                    ):
                        # 모든 태그를 선택
                        for tag in category_tags:
                            st.session_state.selected_tags_state.add(tag)
                        st.success(f"📚 {category_name}의 모든 태그가 선택되었습니다!")
                    else:
                        # 모든 태그를 선택 해제
                        for tag in category_tags:
                            if tag in st.session_state.selected_tags_state:
                                st.session_state.selected_tags_state.remove(tag)
                        
                        # 개별 태그 선택
                        tag_options = []
                        tag_name_map = {}
                        
                        for tag in category_tags:
                            # JSON에서 해당 태그의 한국어 이름 찾기
                            for tag_item in category_data.get("tags", []):
                                if tag_item["tag"] == tag:
                                    display_name = f"{tag_item['name']} ({tag})"
                                    tag_options.append(display_name)
                                    tag_name_map[display_name] = tag
                                    break
                            else:
                                tag_options.append(tag)
                                tag_name_map[tag] = tag
                        
                        if tag_options:
                            # 현재 선택된 태그들을 display_name으로 변환 (기본 태그 포함)
                            currently_selected = []
                            for tag in st.session_state.selected_tags_state:
                                if tag in category_tags:
                                    for display_name, tag_value in tag_name_map.items():
                                        if tag_value == tag:
                                            currently_selected.append(display_name)
                                            break
                            
                            # 기본 태그가 이 카테고리에 있다면 강제로 선택 상태로 표시
                            for tag in DEFAULT_TAGS:
                                if tag in category_tags:
                                    for display_name, tag_value in tag_name_map.items():
                                        if tag_value == tag and display_name not in currently_selected:
                                            currently_selected.append(display_name)
                                            break
                            
                            category_selected_display = st.multiselect(
                                f"{category_name}에서 개별 선택",
                                options=tag_options,
                                default=currently_selected,
                                key=f"tags_{category_name}"
                            )
                            
                            # 선택된 태그를 실제 태그명으로 변환하고 session_state 업데이트
                            category_selected = [tag_name_map[display_name] for display_name in category_selected_display]
                            
                            # 현재 카테고리의 모든 태그를 session_state에서 제거 (기본 태그 제외)
                            for tag in category_tags:
                                if tag in st.session_state.selected_tags_state and tag not in DEFAULT_TAGS:
                                    st.session_state.selected_tags_state.remove(tag)
                            
                            # 새로 선택된 태그들을 session_state에 추가
                            for tag in category_selected:
                                st.session_state.selected_tags_state.add(tag)
                            
                            # 기본 태그는 항상 유지
                            for tag in DEFAULT_TAGS:
                                if tag in category_tags:
                                    st.session_state.selected_tags_state.add(tag)
            
            # session_state에서 최신 선택된 태그 가져오기
            selected_tags = list(st.session_state.selected_tags_state)
            
            # 선택된 태그 표시 (기본 태그 강조)

            if selected_tags:
                # 기본 태그와 일반 태그 분리
                default_selected = [tag for tag in selected_tags if tag in DEFAULT_TAGS]
                other_selected = [tag for tag in selected_tags if tag not in DEFAULT_TAGS]
                
                if default_selected:
                    st.success(f"✅ 기본 선택 태그: {', '.join(default_selected)}")
                
                if other_selected:
                    st.info(f"📚 추가 선택 태그: {', '.join(other_selected)}")
                
                st.success(f"📊 총 선택된 태그: {len(selected_tags)}개")
            else:
                st.warning("⚠️ 최소 하나의 태그를 선택해주세요")
            
            # 문제 개수
            problem_count = st.number_input(
                "추천받을 문제 개수",
                min_value=1,
                max_value=20,
                value=3,
                step=1,
                key="main_count"
            )
            
            # 난이도별 문제 수 비율 설정
            difficulty_ratios = create_difficulty_ratio_ui()
            
            # 디버깅: 난이도별 비율 값 확인
            st.write("🔍 **설정된 난이도별 비율 값:**")
            for difficulty, count in difficulty_ratios.items():
                st.write(f"  {difficulty}: {count}")
        
        with col2:
            st.subheader("🌐 언어 및 고급 필터")
            
            # 언어 설정
            language = st.selectbox(
                "언어",
                options=['ko', 'en'],
                format_func=lambda x: '한국어' if x == 'ko' else 'English',
                key="main_language"
            )
            
            # 한국어 문제 필터
            korean_only = st.checkbox(
                "한국어 문제만 추천",
                value=True,
                key="main_korean_only"
            )
            
            # 고급 필터 (접을 수 있음)
            with st.expander("📊 고급 필터 (선택사항)", expanded=False):
                # 정답률 필터
                st.write("**정답률 범위**")
                min_acceptance_rate, max_acceptance_rate = st.slider(
                    "정답률 (%)",
                    min_value=0,
                    max_value=100,
                    value=(35, 80),
                    key="main_acceptance_rate"
                )
                
                # 시도한 사람 수 필터
                st.write("**시도한 사람 수 범위**")
                col_min_users, col_max_users = st.columns(2)
                with col_min_users:
                    min_attempted_users = st.number_input(
                        "최소 시도한 사람",
                        min_value=0,
                        value=500,
                        step=100,
                        key="main_min_attempted"
                    )
                with col_max_users:
                    max_attempted_users = st.number_input(
                        "최대 시도한 사람",
                        min_value=0,
                        value=10000,
                        step=1000,
                        key="main_max_attempted"
                    )
        
        # 추천 버튼
        st.markdown("---")
        if st.button("🚀 문제 추천받기", type="primary", use_container_width=True):
            # 난이도별 비율 검증
            total_ratio = sum(difficulty_ratios.values())
            if total_ratio == 0:
                st.error("⚠️ 최소 하나의 난이도에서 문제를 선택해주세요")
                return
            
            # 필터 값들을 세션 상태에 저장 (최신 selected_tags 사용)
            st.session_state.main_filter_values = {
                'min_tier': min_tier,
                'max_tier': max_tier,
                'selected_tags': list(st.session_state.selected_tags_state),  # 최신 상태 사용
                'problem_count': problem_count,
                'language': language,
                'korean_only': korean_only,
                'min_acceptance_rate': min_acceptance_rate,
                'max_acceptance_rate': max_acceptance_rate,
                'min_attempted_users': min_attempted_users,
                'max_attempted_users': max_attempted_users,
                'difficulty_ratios': difficulty_ratios
            }
            
            # 추천 클릭 상태 설정
            st.session_state.recommend_clicked = True
            st.rerun()
    
    # 사용자 정보 확인 섹션
    if 'check_users' in st.session_state and st.session_state.check_users:
        st.markdown("---")
        st.header("👥 사용자 정보 확인")
        
        with st.spinner("사용자 정보를 확인하고 있습니다..."):
            for handle in st.session_state.user_handles:
                display_user_info(handle)
        
        if st.button("🔙 돌아가기"):
            st.session_state.check_users = False
            st.rerun()
    
    # 추천 결과 영역
    if 'recommend_clicked' in st.session_state and st.session_state.recommend_clicked:
        st.markdown("---")
        st.header("📋 추천 문제 목록")
        
        # 입력 검증
        if 'main_filter_values' not in st.session_state:
            st.error("필터 설정을 먼저 완료해주세요.")
            return
            
        filter_values = st.session_state.main_filter_values
        
        if not filter_values['selected_tags']:
            st.error("⚠️ 최소 하나의 태그를 선택해주세요.")
            st.info("💡 카테고리별 전체 선택이나 개별 태그 선택을 통해 원하는 태그를 선택하세요.")
            return
        
        if filter_values['min_tier'] and filter_values['max_tier']:
            min_level = TIER_TO_LEVEL_MAP[filter_values['min_tier'].lower()]
            max_level = TIER_TO_LEVEL_MAP[filter_values['max_tier'].lower()]
            
            if min_level > max_level:
                st.error("최소 난이도가 최대 난이도보다 높습니다.")
                return
        
        # 필터 정보 디버깅 표시
        st.info(f"🔍 **적용된 필터 정보**")
        st.write(f"**난이도 범위**: {filter_values['min_tier']} ~ {filter_values['max_tier']}")
        st.write(f"**언어**: {'한국어' if filter_values['language'] == 'ko' else 'English'}")
        st.write(f"**한국어만**: {'예' if filter_values['korean_only'] else '아니오'}")
        st.write(f"**정답률 범위**: {filter_values['min_acceptance_rate']}% ~ {filter_values['max_acceptance_rate']}%")
        st.write(f"**시도한 사람 수**: {filter_values['min_attempted_users']:,}명 ~ {filter_values['max_attempted_users']:,}명")
        st.write(f"**선택된 태그**: {', '.join(filter_values['selected_tags'])}")
        
        # 난이도별 비율 상세 정보
        st.write("**난이도별 비율 상세:**")
        for difficulty, count in filter_values['difficulty_ratios'].items():
            if count > 0:
                emoji = {'unrated': '❓', 'bronze': '🥉', 'silver': '🥈', 'gold': '🥇',
                        'platinum': '💎', 'diamond': '💠', 'ruby': '🔴'}[difficulty]
                st.write(f"  {emoji} {difficulty.title()}: {count}개")
            else:
                st.write(f"  ⏭️ {difficulty.title()}: {count}개 (건너뜀)")
        
        # 난이도 매핑 정보 표시
        st.write(f"**난이도 매핑**: {filter_values['min_tier']} → Level {TIER_TO_LEVEL_MAP.get(filter_values['min_tier'], 'N/A')}, {filter_values['max_tier']} → Level {TIER_TO_LEVEL_MAP.get(filter_values['max_tier'], 'N/A')}")
        
        # 문제 추천 실행
        problems = get_random_problems(
            user_handles=st.session_state.user_handles,
            min_tier=filter_values['min_tier'],
            max_tier=filter_values['max_tier'],
            tags=filter_values['selected_tags'],
            count=filter_values['problem_count'],
            language=filter_values['language'],
            korean_only=filter_values['korean_only'],
            min_acceptance_rate=filter_values['min_acceptance_rate'],
            max_acceptance_rate=filter_values['max_acceptance_rate'],
            min_attempted_users=filter_values['min_attempted_users'],
            max_attempted_users=filter_values['max_attempted_users'],
            difficulty_ratios=filter_values['difficulty_ratios']
        )
        
        # 결과 표시
        if problems:
            display_problem_info(problems, filter_values['difficulty_ratios'])
        else:
            st.warning("⚠️ 조건에 맞는 문제를 찾을 수 없습니다.")
            st.info("💡 필터 조건을 조정해보세요.")
        
        # 새로운 추천 받기 버튼
        if st.button("🔄 새로운 추천 받기"):
            st.session_state.recommend_clicked = False
            st.rerun()

if __name__ == "__main__":
    main()
