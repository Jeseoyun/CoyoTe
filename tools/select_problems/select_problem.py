import requests
import time
import json
import os
from pprint import pprint
from typing import List, Optional, Dict, Any

# 티어 이름을 solved.ac의 내부 레벨 번호로 변환하기 위한 맵
TIER_TO_LEVEL_MAP = {
    'b5': 1, 'b4': 2, 'b3': 3, 'b2': 4, 'b1': 5,
    's5': 6, 's4': 7, 's3': 8, 's2': 9, 's1': 10,
    'g5': 11, 'g4': 12, 'g3': 13, 'g2': 14, 'g1': 15,
    'p5': 16, 'p4': 17, 'p3': 18, 'p2': 19, 'p1': 20,
    'd5': 21, 'd4': 22, 'd3': 23, 'd2': 24, 'd1': 25,
    'r5': 26, 'r4': 27, 'r3': 28, 'r2': 29, 'r1': 30,
}

LEVEL_TO_TIER_MAP = {
    1: 'b5', 2: 'b4', 3: 'b3', 4: 'b2', 5: 'b1',
    6: 's5', 7: 's4', 8: 's3', 9: 's2', 10: 's1',
    11: 'g5', 12: 'g4', 13: 'g3', 14: 'g2', 15: 'g1',
    16: 'p5', 17: 'p4', 18: 'p3', 19: 'p2', 20: 'p1',
    21: 'd5', 22: 'd4', 23: 'd3', 24: 'd2', 25: 'd1',
    26: 'r5', 27: 'r4', 28: 'r3', 29: 'r2', 30: 'r1',
}

def load_algorithm_tags() -> Dict[str, Any]:
    """
    JSON 파일에서 알고리즘 태그를 로드하는 함수
    
    Returns:
        Dict[str, Any]: 알고리즘 태그 데이터
    """
    json_path = os.path.join(os.path.dirname(__file__), 'algorithm_tags.json')
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✅ 알고리즘 태그 파일을 성공적으로 로드했습니다. (총 {data['metadata']['total_categories']}개 카테고리)")
        return data
    except FileNotFoundError:
        print("❌ algorithm_tags.json 파일을 찾을 수 없습니다.")
        print("🔧 기본 알고리즘 태그를 사용합니다.")
        return get_fallback_tags()
    except json.JSONDecodeError as e:
        print(f"❌ JSON 파일 파싱 오류: {e}")
        print("🔧 기본 알고리즘 태그를 사용합니다.")
        return get_fallback_tags()
    except Exception as e:
        print(f"❌ 파일 로드 오류: {e}")
        print("🔧 기본 알고리즘 태그를 사용합니다.")
        return get_fallback_tags()

def get_fallback_tags() -> Dict[str, Any]:
    """
    기본 알고리즘 태그를 반환하는 함수 (JSON 파일이 없을 때 사용)
    
    Returns:
        Dict[str, Any]: 기본 알고리즘 태그 데이터
    """
    return {
        "categories": {
            "기본 알고리즘": {
                "description": "알고리즘의 기초가 되는 기본적인 기법들",
                "tags": [
                    {"name": "구현", "tag": "implementation"},
                    {"name": "그리디", "tag": "greedy"},
                    {"name": "정렬", "tag": "sorting"},
                    {"name": "브루트포스", "tag": "bruteforcing"},
                    {"name": "시뮬레이션", "tag": "simulation"}
                ]
            },
            "탐색": {
                "description": "데이터를 체계적으로 탐색하는 알고리즘",
                "tags": [
                    {"name": "이진 탐색", "tag": "binary_search"},
                    {"name": "BFS", "tag": "bfs"},
                    {"name": "DFS", "tag": "dfs"}
                ]
            },
            "동적 프로그래밍": {
                "description": "메모이제이션과 최적화를 활용한 문제 해결 기법",
                "tags": [
                    {"name": "동적 프로그래밍", "tag": "dp"},
                    {"name": "DP", "tag": "dp"}
                ]
            }
        },
        "metadata": {
            "version": "1.0.0",
            "total_categories": 3,
            "total_tags": 10
        }
    }

def get_user_settings() -> tuple[list[str], str, str, int, bool, int, int]:
    """
    사용자로부터 설정을 입력받는 함수
    
    Returns:
        tuple: (사용자 핸들 목록, 최소 난이도, 최대 난이도, 문제 개수, 시도한 문제 포함 여부, 최대 시도자 수)
    """
    print("\n" + "="*60)
    print("⚙️ 사용자 설정")
    print("="*60)
    
    # 사용자 핸들 입력
    print("👥 백준 사용자 핸들을 입력하세요 (여러 명은 쉼표로 구분)")
    print("   예시: qja1998, woghks1213y, jeeeseo98")
    while True:
        try:
            user_input = input("사용자 핸들: ").strip()
            if user_input:
                user_handles = [handle.strip() for handle in user_input.split(',')]
                print(f"✅ {len(user_handles)}명의 사용자 설정됨: {', '.join(user_handles)}")
                break
            else:
                print("❌ 사용자 핸들을 입력해주세요.")
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
    
    # 난이도 범위 입력
    print("\n📊 난이도 범위를 입력하세요")
    print("   사용 가능한 티어: b5, b4, b3, b2, b1, s5, s4, s3, s2, s1, g5, g4, g3, g2, g1, p5, p4, p3, p2, p1, d5, d4, d3, d2, d1, r5, r4, r3, r2, r1")
    
    while True:
        try:
            min_tier = input("최소 난이도 (예: g5): ").strip().lower()
            if min_tier in TIER_TO_LEVEL_MAP:
                break
            else:
                print("❌ 유효한 티어를 입력해주세요.")
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
    
    while True:
        try:
            max_tier = input("최대 난이도 (예: g3): ").strip().lower()
            if max_tier in TIER_TO_LEVEL_MAP:
                break
            else:
                print("❌ 유효한 티어를 입력해주세요.")
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
    
    # 문제 개수 입력
    print("\n🔢 가져올 문제의 개수를 입력하세요")
    while True:
        try:
            count_input = input("문제 개수 (기본값: 5): ").strip()
            if count_input:
                count = int(count_input)
                if count > 0:
                    break
                else:
                    print("❌ 1 이상의 숫자를 입력해주세요.")
            else:
                count = 5
                break
        except ValueError:
            print("❌ 유효한 숫자를 입력해주세요.")
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
    
    # 시도한 문제 포함 여부
    print("\n🎯 시도한 문제도 포함하시겠습니까?")
    print("   - No: 풀지 않은 문제만 (기본값)")
    print("   - Yes: 시도한 문제도 포함")
    while True:
        try:
            include_input = input("시도한 문제 포함 (y/N): ").strip().lower()
            if include_input in ['y', 'yes', '예']:
                include_attempted = True
                print("✅ 시도한 문제도 포함하여 검색합니다.")
                break
            elif include_input in ['n', 'no', '아니오', '']:
                include_attempted = False
                print("✅ 풀지 않은 문제만 검색합니다.")
                break
            else:
                print("❌ y 또는 n을 입력해주세요.")
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
    
    # 최소 해결자 수 제한
    print("\n👥 최소 해결자 수를 제한하시겠습니까?")
    print("   - 0: 제한 없음 (기본값)")
    print("   - 숫자: 해당 숫자 이상의 해결자가 있는 문제")
    while True:
        try:
            min_attempts_input = input("최소 해결자 수 (기본값: 0): ").strip()
            if min_attempts_input:
                min_attempts = int(min_attempts_input)
                if min_attempts >= 0:
                    break
                else:
                    print("❌ 0 이상의 숫자를 입력해주세요.")
            else:
                min_attempts = 0
                break
        except ValueError:
            print("❌ 유효한 숫자를 입력해주세요.")
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
    
    if min_attempts > 0:
        print(f"✅ 최소 {min_attempts}명의 해결자가 있는 문제를 검색합니다.")
    else:
        print("✅ 최소 해결자 수 제한 없이 검색합니다.")
    
    # 최대 해결자 수 제한
    print("\n👥 최대 해결자 수를 제한하시겠습니까?")
    print("   - 0: 제한 없음 (기본값)")
    print("   - 숫자: 해당 숫자 이하의 해결자만 있는 문제")
    while True:
        try:
            max_attempts_input = input("최대 해결자 수 (기본값: 0): ").strip()
            if max_attempts_input:
                max_attempts = int(max_attempts_input)
                if max_attempts >= 0:
                    break
                else:
                    print("❌ 0 이상의 숫자를 입력해주세요.")
            else:
                max_attempts = 0
                break
        except ValueError:
            print("❌ 유효한 숫자를 입력해주세요.")
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
    
    if max_attempts > 0:
        print(f"✅ 최대 {max_attempts}명의 해결자만 있는 문제를 검색합니다.")
    else:
        print("✅ 최대 해결자 수 제한 없이 검색합니다.")
    
    return user_handles, min_tier, max_tier, count, include_attempted, min_attempts, max_attempts

def select_algorithms() -> List[str]:
    """
    사용자가 알고리즘을 선택할 수 있도록 하는 함수
    
    Returns:
        List[str]: 선택된 알고리즘 태그들의 리스트
    """
    # 알고리즘 태그 데이터 로드
    algorithm_data = load_algorithm_tags()
    categories = algorithm_data['categories']
    
    # print("\n" + "="*60)
    # print("📚 사용 가능한 알고리즘 목록:")
    # print("="*60)
    
    # # 모든 알고리즘을 플랫 리스트로 변환
    # all_algorithms = {}
    # category_names = list(categories.keys())
    
    # for category_name, category_info in categories.items():
    #     print(f"\n🔹 {category_name}:")
    #     print(f"   📝 {category_info['description']}")
    #     for i, tag_info in enumerate(category_info['tags'], 1):
    #         all_algorithms[f"{category_name}_{i}"] = {
    #             'name': tag_info['name'],
    #             'tag': tag_info['tag'],
    #             'category': category_name
    #         }
    #         print(f"   {i:2d}. {tag_info['name']}")
    
    print("\n" + "="*60)
    print("💡 알고리즘을 선택하세요 (여러 개 선택 가능)")
    print("   예시: 1,3,5 또는 1 3 5 또는 '구현,dp,bfs'")
    print("   'all'을 입력하면 모든 알고리즘을 선택합니다")
    print("   'category:기본 알고리즘'을 입력하면 특정 카테고리의 모든 알고리즘을 선택합니다")
    print("="*60)
    
    while True:
        try:
            user_input = input("선택할 알고리즘: ").strip()
            
            if user_input.lower() == 'all':
                selected_tags = []
                for category_info in categories.values():
                    selected_tags.extend([tag_info['tag'] for tag_info in category_info['tags']])
                print(f"✅ 모든 알고리즘 ({len(selected_tags)}개) 선택됨")
                return selected_tags
            
            # 카테고리 전체 선택
            if user_input.startswith('category:'):
                category_name = user_input[9:].strip()
                if category_name in categories:
                    selected_tags = [tag_info['tag'] for tag_info in categories[category_name]['tags']]
                    print(f"✅ '{category_name}' 카테고리의 모든 알고리즘 ({len(selected_tags)}개) 선택됨")
                    return selected_tags
                else:
                    print(f"❌ 알 수 없는 카테고리: {category_name}")
                    print(f"사용 가능한 카테고리: {', '.join(categories.keys())}")
                    continue
            
            # 쉼표나 공백으로 구분된 입력 처리
            if ',' in user_input:
                selections = [s.strip() for s in user_input.split(',')]
            else:
                selections = user_input.split()
            
            selected_tags = []
            for selection in selections:
                if selection.isdigit():
                    # 숫자로 선택한 경우 (전체 알고리즘 중에서)
                    idx = int(selection) - 1
                    all_algos_list = list(all_algorithms.values())
                    if 0 <= idx < len(all_algos_list):
                        selected_tags.append(all_algos_list[idx]['tag'])
                    else:
                        print(f"❌ 잘못된 번호: {selection}")
                        continue
                else:
                    # 이름으로 선택한 경우
                    found = False
                    for category_info in categories.values():
                        for tag_info in category_info['tags']:
                            if tag_info['name'] == selection:
                                selected_tags.append(tag_info['tag'])
                                found = True
                                break
                        if found:
                            break
                    
                    if not found:
                        print(f"❌ 알 수 없는 알고리즘: {selection}")
                        continue
            
            if selected_tags:
                # 선택된 알고리즘의 한글 이름을 표시
                selected_names = []
                for tag in selected_tags:
                    for category_info in categories.values():
                        for tag_info in category_info['tags']:
                            if tag_info['tag'] == tag:
                                selected_names.append(tag_info['name'])
                                break
                        else:
                            continue
                        break
                
                print(f"✅ 선택된 알고리즘: {', '.join(selected_names)}")
                return selected_tags
            else:
                print("❌ 유효한 알고리즘을 선택해주세요.")
                
        except KeyboardInterrupt:
            print("\n\n❌ 사용자가 취소했습니다.")
            return []
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
            print("다시 시도해주세요.")

def get_random_problems(
    user_handles: list[str],
    min_tier: str,
    max_tier: str,
    tags: list[str],
    count: int = 10,
    language: str = 'ko',
    include_attempted: bool = False,
    min_attempts: int = 0,
    max_attempts: int = 0
):
    """
    solved.ac API를 사용해 조건에 맞는 무작위 문제를 가져옵니다.

    Args:
        user_handles (list[str]): solved.ac 사용자 핸들 목록.
        min_tier (str): 검색할 최저 티어 (예: 'g5', 's1').
        max_tier (str): 검색할 최고 티어 (예: 'g3', 'p2').
        tags (list[str]): 검색에 포함할 태그 목록 (예: ['implementation', 'binary_search']).
        count (int, optional): 가져올 문제의 개수. 기본값은 10입니다.
        language (str, optional): 문제 제목 등의 언어 ('ko' 또는 'en'). 기본값은 'ko'입니다.
        include_attempted (bool, optional): 시도한 문제도 포함할지 여부. 기본값은 False입니다.
        max_attempts (int, optional): 최대 시도자 수 제한. 0이면 제한 없음. 기본값은 0입니다.

    Returns:
        list: 문제 정보가 담긴 딕셔너리의 리스트. 오류 발생 시 빈 리스트를 반환합니다.
    """
    # 1. 입력받은 티어 이름을 숫자 레벨로 변환
    try:
        min_level = TIER_TO_LEVEL_MAP[min_tier.lower()]
        max_level = TIER_TO_LEVEL_MAP[max_tier.lower()]
    except KeyError as e:
        print(f"잘못된 티어 이름: {e}")
        return []

    if min_level > max_level:
        min_level, max_level = max_level, min_level

    # 2. API 요청을 위한 쿼리 문자열 생성
    query_parts = []
    
    # **사용자 필터링**
    if include_attempted:
        # 시도한 문제도 포함하는 경우: 풀지 않은 문제만 제외
        for handle in user_handles:
            query_parts.append(f"-solved_by:{handle}")
        print("🔍 필터링: 풀지 않은 문제만 제외 (시도한 문제 포함)")
    else:
        # 기본: 풀지 않은 문제만
        for handle in user_handles:
            query_parts.append(f"-solved_by:{handle}")
        print("🔍 필터링: 풀지 않은 문제만")
        
    query_parts.append(f"tier:{min_level}..{max_level}")
    
    # 한국어 문제만 필터링
    query_parts.append("lang:ko")
    print("🔍 언어 필터링: 한국어 문제만")
    
    # 해결한 사용자 수 제한 (최소/최대)
    if min_attempts > 0 and max_attempts > 0:
        # 최소와 최대가 모두 설정된 경우
        query_parts.append(f"solved:{min_attempts}..{max_attempts}")
        print(f"🔍 해결한 사용자 수 제한: {min_attempts}명 ~ {max_attempts}명")
    elif min_attempts > 0:
        # 최소만 설정된 경우
        query_parts.append(f"solved:{min_attempts}..")
        print(f"🔍 해결한 사용자 수 제한: 최소 {min_attempts}명")
    elif max_attempts > 0:
        # 최대만 설정된 경우
        query_parts.append(f"solved:..{max_attempts}")
        print(f"🔍 해결한 사용자 수 제한: 최대 {max_attempts}명")
    
    # 태그를 OR 조건으로 쿼리 (여러 태그 중 하나라도 포함된 문제)
    if tags:
        if len(tags) == 1:
            # 태그가 하나인 경우
            query_parts.append(f"tag:{tags[0]}")
        else:
            # 태그가 여러 개인 경우 OR 조건으로 쿼리
            tag_query = " | ".join([f"tag:{tag}" for tag in tags])
            query_parts.append(f"({tag_query})")
            print(f"🔍 태그 필터링: OR 조건 ({len(tags)}개 태그)")

    query_string = " ".join(query_parts)
    print(f"API 쿼리: {query_string}")

    # 3. API 요청 및 데이터 수집
    found_problems = []
    page = 1
    API_URL = "https://solved.ac/api/v3/search/problem"
    headers = {"Accept": "application/json", "x-solvedac-language": language}

    while len(found_problems) < count:
        params = {"query": query_string, "page": page, "sort": "random"}
        try:
            response = requests.get(API_URL, headers=headers, params=params)
            response.raise_for_status()
            
            data = response.json()
            items = data.get("items", [])
            
            if not items:
                print("\n조건에 맞는 문제 없음")
                break
            
            found_problems.extend(items)
            page += 1
            time.sleep(0.5)

        except requests.exceptions.RequestException as e:
            print(f"\nAPI 요청 오류: {e}")
            return []
        
    return found_problems[:count]

# --- 함수 사용 예시 ---
if __name__ == "__main__":
    print("🚀 CoyoTe 알고리즘 문제 선택기")
    print("=" * 60)
    
    # 사용자 설정 입력
    user_handles, min_difficulty, max_difficulty, problem_count, include_attempted, min_attempts, max_attempts = get_user_settings()
    
    print(f"\n👥 대상 사용자: {', '.join(user_handles)}")
    print(f"📊 난이도: {min_difficulty.upper()} ~ {max_difficulty.upper()}")
    print(f"🔢 문제 개수: {problem_count}")
    print(f"🎯 시도한 문제 포함: {'예' if include_attempted else '아니오'}")
    print(f"🌏 언어: 한국어 문제만")
    if min_attempts > 0:
        print(f"👥 최소 해결자 수: {min_attempts}명")
    else:
        print(f"👥 최소 해결자 수: 제한 없음")
    if max_attempts > 0:
        print(f"👥 최대 해결자 수: {max_attempts}명")
    else:
        print(f"👥 최대 해결자 수: 제한 없음")
    
    # 알고리즘 선택
    selected_algorithms = select_algorithms()
    
    if not selected_algorithms:
        print("❌ 알고리즘이 선택되지 않았습니다. 프로그램을 종료합니다.")
        exit()
    
    # 선택된 알고리즘의 한글 이름을 표시
    algorithm_data = load_algorithm_tags()
    selected_names = []
    for tag in selected_algorithms:
        for category_info in algorithm_data['categories'].values():
            for tag_info in category_info['tags']:
                if tag_info['tag'] == tag:
                    selected_names.append(tag_info['name'])
                    break
            else:
                continue
            break
    
    print(f"\n🎯 선택된 알고리즘: {', '.join(selected_names)}")
    
    print("\n" + "=" * 60)
    print("🔍 문제 검색 중...")
    print("=" * 60)
    
    problems = get_random_problems(
        user_handles=user_handles,
        min_tier=min_difficulty,
        max_tier=max_difficulty,
        tags=selected_algorithms,
        count=problem_count,
        include_attempted=include_attempted,
        min_attempts=min_attempts,
        max_attempts=max_attempts
    )

    if problems:
        print(f"\n✅ 총 {len(problems)} 문제를 찾았습니다!\n")
        for i, prob in enumerate(problems, 1):
            tag_names = [tag['displayNames'][0]['name'] for tag in prob['tags']]
            
            # 시도자 수 정보 가져오기
            accepted_count = prob.get('acceptedUserCount', 0)  # 해결한 사용자 수
            average_tries = prob.get('averageTries', 0)       # 평균 시도 횟수
            
            # 시도자 수 정보 표시 (해결한 사용자 수와 평균 시도 횟수)
            if accepted_count > 0:
                accepted_info = f"{accepted_count:,}명"
            else:
                accepted_info = "0명"
                
            if average_tries > 0:
                tries_info = f"{average_tries:.1f}회"
            else:
                tries_info = "0회"
            
            print(f"📝 문제 {i}:")
            print(f"   ID: {prob['problemId']}")
            print(f"   레벨: {LEVEL_TO_TIER_MAP[prob['level']]}")
            print(f"   제목: {prob['titleKo']}")
            print(f"   해결한 사용자: {accepted_info}")
            print(f"   평균 시도 횟수: {tries_info}")
            print(f"   태그: {', '.join(tag_names)}")
            print(f"   링크: https://www.acmicpc.net/problem/{prob['problemId']}")
            print()
    else:
        print("\n❌ 조건에 맞는 문제를 찾을 수 없습니다.")
        print("💡 다음을 시도해보세요:")
        print("   - 난이도 범위를 넓혀보기")
        print("   - 알고리즘 태그를 줄여보기")
        print("   - 사용자 수를 줄여보기")