import streamlit as st
import requests
import datetime

# 1. 網頁頁面基本設定
st.set_page_config(page_title="我的即時天氣儀表板", page_icon="🌤️", layout="centered")

st.title("🌤️ 台灣即時天氣儀表板")
st.subheader("這是結合 Python 爬蟲與網頁前端的自動化成果！")
st.write("---")

# 2. 爬蟲核心：抓取網路最新天氣資料
try:
    url = "https://wttr.in/Taiwan?format=j1"  
    response = requests.get(url, timeout=10)
    weather_data = response.json()
    current_condition = weather_data['current_condition'][0]
    
    temp = current_condition['temp_C']         
    status = current_condition['weatherDesc'][0]['value'] 
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 3. 呈現網頁卡片元件
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="💡 目前最新氣溫", value=f"{temp} °C")
    with col2:
        st.metric(label="🌤️ 當前天氣狀態", value=status)
        
    st.info(f"📅 資料最後同步時間：{now_time}")

except Exception as e:
    st.error(f"❌ 抓取氣象失敗，原因：{e}")

st.write("\n---")
st.caption("⚡ Powered by Python & Streamlit")
