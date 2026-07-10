import streamlit as st
import requests
import datetime
import pandas as pd

# 1. 網頁頁面基本設定
st.set_page_config(page_title="AI 天氣問答機器人 Pro", page_icon="🤖", layout="centered")

# --- 【核心開發者：賴以航 原生穩定版區塊】 ---
with st.container(border=True):
    st.subheader("👨‍💻 核心開發者：賴以航 (Yi-Hang Lai)")
    st.caption("🤖 雲端全端自動化專案 v3.1 | 系統狀態：超級天氣中文字典已全面補齊，排版優化完成")

st.title("🤖 AI 智慧天氣助理 Pro")
st.write("輸入台灣縣市，為您提供即時天氣、AI 穿搭防雨建議，以及未來三日氣溫趨勢圖！")
st.write("---")

# 2. 建立輸入框與按鈕
city_input = st.text_input("💬 請輸入台灣縣市名稱（例如：台北、台中、高雄、花蓮）：", value="雲林")
search_button = st.button("🔍 啟動智慧分析")

# 3. 當使用者按下按鈕時執行
if search_button:
    if city_input:
        with st.spinner("AI 正在分析氣象大數據..."):
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
                
                # --- 【超級氣象中文字典：全面補齊】 ---
                weather_dict = {
                    "Sunny": "晴天 ☀️", "Clear": "晴朗 🌤️",
                    "Partly Cloudy": "多雲時晴 ⛅", "Partly cloudy": "多雲時晴 ⛅",
                    "Cloudy": "陰天 ☁️", "Overcast": "多雲轉陰 🌥️", 
                    "Mist": "有霧 🌫️", "Fog": "大霧 🌫️", "Freezing fog": "凍霧 🌫️",
                    "Patchy rain nearby": "局部短暫雨 🌧️", "Patchy rain possible": "可能下局部雨 🌧️",
                    "Light rain": "小雨 🌧️", "Light rain shower": "短暫小雨 🌧️",
                    "Moderate rain": "中雨 🌧️", "Moderate rain at times": "時有中雨 🌧️",
                    "Heavy rain": "大雨 ⛈️", "Heavy rain at times": "時有大雨 ⛈️",
                    "Torrential rain shower": "暴雨 ⛈️",
                    "Patchy snow possible": "可能下局部雪 ❄️", "Light snow": "小雪 ❄️",
                    "Heavy snow": "大雪 ❄️", "Ice pellets": "冰雹 🌨️",
                    "Thundery outbreaks possible": "可能雷陣雨 ⛈️",
                    "Patchy light rain with thunder": "雷陣雨帶小雨 ⛈️",
                    "Moderate or heavy rain with thunder": "大雷陣雨 ⛈️",
                    "Patchy light drizzle": "局部毛毛雨 🌧️", "Light drizzle": "毛毛雨 🌧️"
                }
                
                english_city = city_mapping.get(city_input.strip().replace("台", "臺"), "Taiwan")
                
                # 爬取該城市的天氣資料
                url = f"https://wttr.in/{english_city}?format=j1"  
                response = requests.get(url, timeout=10)
                weather_data = response.json()
                
                # A. 擷取目前天氣核心數據
                current_condition = weather_data['current_condition'][0]
                temp = int(current_condition['temp_C'])         
                status_eng = current_condition['weatherDesc'][0]['value'] 
                humidity = current_condition['humidity'] 
                
                # 自動翻譯天氣狀態，若找不到則顯示原英文並加上 🌍 標籤
                status_cht = weather_dict.get(status_eng, f"{status_eng} 🌍")
                
                try:
                    rain_chance = int(weather_data['weather'][0]['hourly'][0]['chanceofrain'])
                except:
                    rain_chance = 0

                now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # B. 智慧穿搭與帶傘小建議
                tips = []
                if rain_chance >= 40:
                    tips.append("🌧️ **帶傘提醒：** 降雨機率較高，出門記得帶把傘，免得淋成落湯雞喔！")
                else:
                    tips.append("🌤️ **防雨提醒：** 目前降雨機率低，可以放心出門！")
                    
                if temp >= 30:
                    tips.append("🥵 **穿搭建議：** 天氣炎熱！建議穿著透氣短袖，並注意防曬、多補充水分。")
                elif temp <= 18:
                    tips.append("🥶 **穿搭建議：** 天氣偏涼！記得加件外套防風保暖，別感冒囉。")
                else:
                    tips.append("🧥 **穿搭建議：** 氣溫舒適，穿件薄長袖或舒適短袖搭配薄外套即可.")

                # 4. 機器人回答的介面
                st.chat_message("assistant").write(f"🤖 報告 **賴以航** 總工程師！AI 已完成 **{city_input}** 的大數據分析：")
                
                # 調整欄位配置：將「天氣狀態」單獨放大一行顯示，徹底解決長文字被切斷（...）的問題！
                st.markdown(f"### 📊 當前天氣狀況")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric(label="🌡️ 目前氣溫", value=f"{temp} °C")
                with col2:
                    st.metric(label="💧 空氣濕度", value=f"{humidity} %")
                with col3:
                    st.metric(label="🌧️ 降雨機率", value=f"{rain_chance} %")
                
                # 獨立一條大橫條來優雅顯示中文化天氣狀態
                st.success(f"✨ **當前天氣型態：** {status_cht}")
                
                # 顯示 AI 貼心建議
                st.info("\n".join(tips))
                
                # C. 處理未來三天預報趨勢圖表
                st.subheader("📈 未來三日氣溫預報趨勢")
                forecast_list = []
                for day in weather_data['weather']:
                    date_str = day['date']
                    max_t = int(day['maxtempC'])
                    min_t = int(day['mintempC'])
                    forecast_list.append({"日期": date_str, "最高氣溫 (°C)": max_t, "最低氣溫 (°C)": min_t})
                
                df = pd.DataFrame(forecast_list)
                df.set_index("日期", inplace=True)
                st.line_chart(df)
                
                st.caption(f"📅 系統分析時間：{now_time}")

            except Exception as e:
                st.error(f"❌ 數據解析失敗！原因：{e}")
    else:
        st.warning("⚠️ 請記得先輸入縣市名稱喔！")

st.write("\n---")
st.caption("⚡ Powered by Streamlit & Python Chat Bot")
st.caption("© 2026 賴以航 (Yi-Hang Lai). All rights reserved. 本網頁產權所有，非經授權請勿複製。")
