import streamlit as st
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

# Streamlit 페이지 설정
st.set_page_config(layout="wide")
st.title("🗺️ 청소년상담복지센터 현황 지도 시각화 (Streamlit)")

# 1. 데이터 로드 및 좌표 데이터 준비
file_path = "여성가족부_청소년상담복지센터 현황_20241029 2.csv"

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    st.error(f"⚠️ 오류: {file_path} 파일을 찾을 수 없습니다. 파일을 앱과 같은 폴더에 넣어주세요.")
    st.stop()

# 사용자님이 제공해주신 위도/경도 데이터 (상위 14개 센터에 매칭)
# 형식: (위도, 경도)
coordinates = [
    (37.59064, 126.99338),  # 1
    (37.53890, 126.96501),  # 2
    (37.55423, 127.02710),  # 3
    (37.54027, 127.06517),  # 4
    (37.57394, 127.02462),  # 5
    (37.57323, 127.08597),  # 6
    (37.64178, 127.02216),  # 7
    (37.67143, 127.05483),  # 8
    (34.93669, 126.56360),  # 9 (다른 지역 좌표로 추정되나, 순서대로 사용)
    (37.58472, 126.91373),  # 10
    (37.55317, 126.90270),  # 11
    (37.47826, 126.99907),  # 12
    (37.48360, 127.08878),  # 13
    (37.48815, 127.11271)   # 14
]

# 상위 14개 데이터에 위도/경도 컬럼 추가
num_coords = len(coordinates)
if len(df) >= num_coords:
    coord_df = pd.DataFrame(coordinates, columns=['위도', '경도'])
    df.loc[:num_coords-1, ['위도', '경도']] = coord_df[['위도', '경도']].values
    df_map = df.dropna(subset=['위도', '경도']).copy() # 시각화에 사용할 데이터프레임
    
    st.info(f"데이터 파일에서 **상위 {len(df_map)}개**의 센터에 제공해주신 좌표를 매칭하여 시각화했습니다.")
    
elif len(df) < num_coords:
    st.warning(f"⚠️ 데이터 파일의 개수({len(df)}개)가 제공된 좌표({num_coords}개)보다 적습니다. 파일 개수에 맞게 시각화합니다.")
    coord_df = pd.DataFrame(coordinates[:len(df)], columns=['위도', '경도'])
    df['위도'] = coord_df['위도']
    df['경도'] = coord_df['경도']
    df_map = df.dropna(subset=['위도', '경도']).copy()
else:
    st.info("시각화할 유효한 데이터가 없습니다.")
    st.stop()


# 2. Folium 지도 생성
# 지도의 중심은 시각화되는 센터들의 평균 좌표로 설정
center_lat = df_map['위도'].mean()
center_lon = df_map['경도'].mean()
m = folium.Map(location=[center_lat, center_lon], zoom_start=10)

# 3. 지도에 마커 추가
for idx, row in df_map.iterrows():
    # 툴팁에 표시할 상세 정보 HTML 생성
    tooltip_html = f"""
    <h4>**{row['센터명']}**</h4>
    <ul>
        <li>**지역:** {row['시도명']} {row['시군구명']}</li>
        <li>**주소:** {row['주소']}</li>
        <li>**전화번호:** {row['전화번호_1']}</li>
    </ul>
    """
    
    # 마커 추가
    folium.Marker(
        [row['위도'], row['경도']],
        tooltip=folium.Tooltip(tooltip_html, permanent=False),
        popup=row['센터명'],
        icon=folium.Icon(color='blue', icon='star')
    ).add_to(m)

# 4. Streamlit에 Folium 지도 표시
st.subheader("청소년상담복지센터 위치 지도")
folium_static(m, width=1200, height=700) # 지도를 Streamlit에 표시

# 시각화에 사용된 데이터 확인 (선택 사항)
if st.checkbox('시각화에 사용된 데이터 보기'):
    st.subheader("사용된 데이터 (상위 14개 센터)")
    st.dataframe(df_map[['센터명', '시도명', '시군구명', '주소', '위도', '경도']])
