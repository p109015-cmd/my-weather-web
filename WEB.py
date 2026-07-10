import streamlit as st
import requests
import datetime

# 1. 網頁頁面基本設定
st.set_page_config(page_title="AI 天氣問答機器人", page_icon="🤖", layout="centered")

# --- 【核心開發者：賴以航 原生穩定版區塊】 ---
with st.container(border=True):
    st.subheader("👨‍💻 核心開發者：賴以航 (Yi-Hang Lai)")
    st.caption("🤖 雲端全端自動化專案 v2.1 | 系統狀態：已成功適應 Python 3.14 雲端環境")

st.title("🤖 AI 天氣問答機器人")
st.write("輸入你想查詢的台灣縣市，我會立刻幫你查詢氣溫、天氣狀態、濕度及降雨機率！")
st.write("---")

# 2. 建立輸入框與按鈕
city_input = st.text_input("💬 請輸入台灣縣市名稱（例如：台北、台中、高雄、花蓮）：", value="雲林")
search_button = st.button("🔍 開始查詢")

# 3. 當使用者按下按鈕時執行
if search_button:
    if city_input:
        with st.spinner("正在連線氣象數據庫中..."):
            try:
                # 將中文縣市轉換為 wttr.in 認識的名稱
                city_mapping = {
                    "台北": "Taipei", "新北": "New_Taipei", "桃園": "Taoyuan",
                    "台中": "Taichung", "台南": "Tainan", "高雄": "Kaohsiung",
                    "基隆": "Keelung", "新竹": "Hsinchu", "苗栗": "Miaoli",
                    "彰化": "Changhua", "南投": "Nantou", "雲林": "Yunlin",
                    "嘉義": "Chiayi", "屏東": "Pingtung", "宜蘭": "Yilan",
                    "花蓮": "Hualien", "台東": "Taitung", "澎湖": "Penghu",
                    "金門": "Kinmen", "馬祖": "Matsu"
                }
                
                # 預設如果查不到就用台灣整體
                english_city = city_mapping.get(city_input.strip().replace("台", "臺"), "Taiwan")
                
                # 爬取該城市的天氣資料
                url = f"https://wttr.in/{english_city}?format=j1"  
                response = requests.get(url, timeout=10)
                weather_data = response.json()
                
                # 擷取目前天氣核心數據
                current_condition = weather_data['current_condition'][0]
                temp = current_condition['temp_C']         
                status = current_condition['weatherDesc'][0]['value'] 
                humidity = current_condition['humidity'] # 濕度
                
                # 擷取今日預報中的「降雨機率」
                try:
                    rain_chance = weather_data['weather'][0]['hourly'][0]['chanceofrain']
                except:
                    rain_chance = "--"

                now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # 4. 機器人回答的介面
                st.chat_message("assistant").write(f"🤖 報告 **賴以航** 總工程師！已成功串接 **{city_input}** 的完整即時天氣：")
                
                # 四欄位完美排版
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric(label="🌡️ 目前氣溫", value=f"{temp} °C")
                with col2:
                    st.metric(label="🌤️ 天氣狀態", value=status)
                with col3:
                    st.metric(label="💧 空氣濕度", value=f"{humidity} %")
                with col4:
                    st.metric(label="🌧️ 降雨機率", value=f"{rain_chance} %")
                    
                st.caption(f"📅 機器人回應時間：{now_time}")

            except Exception as e:
                st.error(f"❌ 哎呀，查詢失敗了！原因：{e}")
    else:
        st.warning("⚠️ 請記得先輸入縣市名稱喔！")

st.write("\n---")
# --- 【頁尾版權宣告：賴以航】 ---
st.caption("⚡ Powered by Streamlit & Python Chat Bot")
st.caption("© 2026 賴以航 (Yi-Hang Lai). All rights reserved. 本網頁產權所有，非經授權請勿複製。")
