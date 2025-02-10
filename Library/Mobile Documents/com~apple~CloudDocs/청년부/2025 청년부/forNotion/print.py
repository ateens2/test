# from notion_client import Client
# from datetime import datetime, timedelta

# # Notion API 토큰과 데이터베이스 ID 설정
# NOTION_TOKEN = "secret_FbMvTZb2BAxM4M37YbmiMN3fbN2clsSIjzptBxLCBVT"
# DATABASE_ID = "18f8c1b30be8803db9fadd8d05dad424"

# # Notion 클라이언트 초기화
# notion = Client(auth=NOTION_TOKEN)

# def get_sundays_2025():
#     # 2025년 1월 1일부터 시작
#     current_date = datetime(2025, 1, 1)
    
#     # 첫 번째 일요일 찾기
#     while current_date.weekday() != 6:  # 6은 일요일을 의미
#         current_date += timedelta(days=1)
    
#     sundays = []
#     # 2025년의 모든 일요일 수집
#     while current_date.year == 2025:
#         sundays.append(current_date.strftime("%Y-%m-%d"))
#         current_date += timedelta(days=7)
    
#     return sundays

# def find_related_page(database_id, date):
#     # 디버깅을 위한 출력 추가
#     print(f"\n검색 중: DB {database_id}, 날짜 {date}")
    
#     response = notion.databases.query(
#         database_id=database_id,
#         filter={
#             "property": "이름",
#             "title": {
#                 "equals": date
#             }
#         }
#     )
    
#     # 검색 결과 디버깅
#     if response["results"]:
#         print(f"페이지 찾음: {response['results'][0]['id']}")
#         return response["results"][0]["id"]
#     else:
#         print(f"페이지를 찾을 수 없음")
#         return None

# def find_page_in_main_db(date):
#     # 메인 데이터베이스에서 특정 날짜의 페이지 찾기
#     response = notion.databases.query(
#         database_id=DATABASE_ID,
#         filter={
#             "property": "이름",
#             "title": {
#                 "equals": date
#             }
#         }
#     )
    
#     if response["results"]:
#         return response["results"][0]["id"]
#     return None

# def update_page_relations():
#     sundays = get_sundays_2025()
    
#     # 관계형 DB의 ID들
#     RELATED_DB_1_ID = "1718c1b30be8801d934cca85e9030067"
#     RELATED_DB_2_ID = "1718c1b30be880e5936dff8bb8760138"
    
#     for sunday in sundays:
#         try:
#             print(f"\n=== {sunday} 처리 중 ===")
            
#             main_page_id = find_page_in_main_db(sunday)
#             if not main_page_id:
#                 print(f"메인 페이지를 찾을 수 없음: {sunday}")
#                 continue
            
#             # 각 관계형 DB에서 관련 페이지 찾기
#             related_page_1 = find_related_page(RELATED_DB_1_ID, sunday)
#             related_page_2 = find_related_page(RELATED_DB_2_ID, sunday)
            
#             properties = {}
            
#             if related_page_1:
#                 properties["예배 출석 DB"] = {
#                     "relation": [{"id": related_page_1}]
#                 }
#                 print(f"예배 출석 DB 관계 추가됨: {related_page_1}")
            
#             if related_page_2:
#                 properties["가연 출석 DB"] = {
#                     "relation": [{"id": related_page_2}]
#                 }
#                 print(f"가연 출석 DB 관계 추가됨: {related_page_2}")
            
#             # 페이지 업데이트 시도
#             if properties:
#                 print("업데이트할 속성:", properties)
#                 notion.pages.update(
#                     page_id=main_page_id,
#                     properties=properties
#                 )
#                 print(f"페이지 관계 업데이트 완료: {sunday}")
            
#         except Exception as e:
#             print(f"페이지 업데이트 실패 ({sunday}): {str(e)}")

# if __name__ == "__main__":
#     update_page_relations()
print("Hello, World!")