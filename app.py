import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 점심 메뉴 추천", page_icon="🍽️")

st.title("🍽️ 오늘 뭐 먹지? 점심 메뉴 추천기")
st.write("버튼을 누르면 오늘의 점심 메뉴를 랜덤으로 골라드립니다!")

# 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가하거나 수정해 보세요)
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "초밥",
    "짜장면",
    "짬뽕",
    "쌀국수",
    "햄버거",
    "파스타",
    "국밥",
    "비빔밥",
    "마라탕",
    "샌드위치",
    "카레라이스",
]

# 추천 버튼 생성
if st.button("🎲 오늘의 메뉴 추천받기", type="primary"):
  # random.choice()를 사용해 리스트에서 무작위로 하나 선택
  selected_menu = random.choice(lunch_menus)

  st.success(f"오늘의 추천 점심 메뉴는 **'{selected_menu}'** 입니다! 🎉")
  st.balloons()  # 축하 풍선 효과
