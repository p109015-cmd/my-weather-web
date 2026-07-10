import streamlit as st
import requests
import datetime
import pandas as pd

# 1. 網頁頁面基本設定
st.set_page_config(page_title="AI 天氣問答機器人 終極完全體", page_icon="⛈️", layout="centered")

# --- 【核心定位技術：自動偵測 IP 所在縣市】 ---
def get_current_city_by_ip():
    try:
        # 連線到地理位置 API 偵測當前 IP
        response = requests.get("http://ip-api.com/json/?lang=zh-CN", timeout=5)
        data = response.json()
        if data.get("status") == "success":
            region = data.get("regionName", "")
            city = data.get("city", "")
            full_loc = region + city
            
            # 台灣縣市智慧過濾字典
            taiwan_cities = ["台北", "新北", "桃園", "台中", "台南", "高雄", "基隆", "新竹", "苗栗", "彰化", "南投", "雲林", "嘉義", "屏東", "宜蘭", "花蓮", "台東", "澎湖", "金門", "馬祖"]
            for c in taiwan_cities:
                if c in full_loc:
                    return c
    except:
        pass
    return "雲林" # 若偵測失敗，預設以賴總工程師大本營雲林為出發點

# 首次載入時自動初始化定位
if "default_city" not in st.session_state:
    st.session_state.default_city = get_current_city_by_ip()

# --- 【核心開發者：賴以航 原生穩定版區塊】 ---
with st.container(border=True):
    st.subheader("👨‍💻 核心開發者：賴以航 (Yi-Hang Lai)")
    st.caption("🤖 雲端全端自動化專案 v4.0 終極版 | 系統狀態：雙核心IP自動定位與動態魔幻背景已實裝")

st.title("⛈️ AI 智慧天氣助理 終極完全體")
st.write("本系統支援 **智慧 IP 自動定位**。您可直接查詢，或手動修正您想查詢的縣市。")
st.write("---")

# 2. 建立輸入框與功能按鈕（排版優化）
col_input, col_gps = st.columns([3, 1])
with col_input:
    city_input = st.text_input("💬 輸入台灣縣市名稱：", value=st.session_state.default_city)
with col_gps:
    st.write("<br>", unsafe_allow_html=True) # 稍微對齊
    gps_button = st.button("📡 重新定位IP")

if gps_button:
    st.session_state.default_city = get_current_city_by_ip()
    st.rerun()

search_button = st.button("🔍 啟動魔幻氣象分析", use_container_width=True)

# 3. 當使用者按下按鈕時執行
if search_button:
    if city_input:
        with st.spinner("AI 正在解析氣象大數據並計算動態視覺效果..."):
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
                
                # 超級氣象中文字典
                weather_dict = {
                    "sunny": "晴天 ☀️", "clear": "晴朗 🌤️", "partly cloudy": "多雲時晴 ⛅", 
                    "cloudy": "陰天 ☁️", "overcast": "多雲轉陰 🌥️", "mist": "有霧 🌫️", "fog": "大霧 🌫️", 
                    "patchy rain nearby": "局部短暫雨 🌧️", "patchy rain possible": "可能下局部雨 🌧️",
                    "light rain": "小雨 🌧️", "light rain shower": "短暫小雨 🌧️", "moderate rain": "中雨 🌧️", 
                    "heavy rain": "大雨 ⛈️", "heavy rain at times": "時有大雨 ⛈️", "torrential rain shower": "暴雨 ⛈️",
                    "thundery outbreaks possible": "可能雷陣雨 ⛈️", "patchy light rain with thunder": "雷陣雨帶小雨 ⛈️",
                    "moderate or heavy rain with thunder": "大雷陣雨 ⛈️", "light drizzle": "毛毛雨 🌧️"
                }
                
                english_city = city_mapping.get(city_input.strip().replace("台", "臺"), "Taiwan")
                url = f"https://wttr.in/{english_city}?format=j1"  
                response = requests.get(url, timeout=10)
                weather_data = response.json()
                
                current_condition = weather_data['current_condition'][0]
                temp = int(current_condition['temp_C'])         
                status_eng = current_condition['weatherDesc'][0]['value'] 
                humidity = current_condition['humidity'] 
                
                status_cht = weather_dict.get(status_eng.lower(), f"{status_eng} 🌍")
                
                try:
                    rain_chance = int(weather_data['weather'][0]['hourly'][0]['chanceofrain'])
                except:
                    rain_chance = 0

                now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # --- 【核心動態特效技術：根據天氣動態注入 CSS 魔法背景】 ---
                status_lower = status_eng.lower()
                bg_style = ""
                
                if "sunny" in status_lower or "clear" in status_lower:
                    # 晴天：陽光活力黃橘渐層背景，深色字
                    bg_style = """
                    <style>
                    .stApp {
                        background: linear-gradient(135deg, #FFFDE4 0%, #FFD861 100%) !important;
                    }
                    h1, h2, h3, p, span, label { color: #5d4037 !important; }
                    </style>
                    """
                elif "rain" in status_lower or "thunder" in status_lower or "drizzle" in status_lower:
                    # 下雨/雷雨：警告深紅灰色漸層背景，白色字，充滿震懾感
                    bg_style = """
                    <style>
                    .stApp {
                        background: linear-gradient(135deg, #4A1525 0%, #2C3E50 100%) !important;
                    }
                    h1, h2, h3, p, span, label { color: #FFFFFF !important; }
                    </style>
                    """
                else:
                    # 多雲/陰天/其餘天氣：質感的舒適莫蘭迪藍灰漸層
                    bg_style = """
                    <style>
                    .stApp {
                        background: linear-gradient(135deg, #E0EAFC 0%, #CFDEF3 100%) !important;
                    }
                    </style>
                    """
                # 注入 HTML 魔法
                st.markdown(bg_style, unsafe_allow_html=True)

                # B. AI 智慧穿搭小建議
                tips = []
                if rain_chance >= 40:
                    tips.append("🌧️ **帶傘提醒：** 降雨機率高，出門請務必攜帶雨具，注意行車安全！")
                else:
                    tips.append("🌤️ **防雨提醒：** 目前降雨機率低，是個適合出門的好天氣。")
                    
                if temp >= 30:
                    tips.append("🥵 **穿搭建議：** 烈日炎炎！建議穿著輕薄透氣衣物，並做好防曬防中暑。")
                elif temp <= 18:
                    tips.append("🥶 **穿搭建議：** 涼意襲來！請增添外套，做好保暖措施。")
                else:
                    tips.append("🧥 **穿搭建議：** 天氣舒適，單穿長袖或短袖配件薄外套即可。")

                # 4. 機器人回答的介面
                st.chat_message("assistant").write(f"🤖 報告 **賴以航** 總工程師！雙核心系統已啟動，**{city_input}** 氣象視覺渲染完畢：")
                
                st.markdown(f"### 📊 當前天氣狀況")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric(label="🌡️ 目前氣溫", value=f"{temp} °C")
                with col2:
                    st.metric(label="💧 空氣濕度", value=f"{humidity} %")
                with col3:
                    st.metric(label="🌧️ 降雨機率", value=f"{rain_chance} %")
                
                st.success(f"✨ **當前天氣型態：** {status_cht}")
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
                st.error(f"❌ 數據渲染失敗！原因：{e}")
    else:
        st.warning("⚠️ 請記得先輸入縣市名稱喔！")

st.write("\n---")
st.caption("⚡ Powered by Streamlit & Python Chat Bot")
st.caption("© 2026 賴以航 (Yi-Hang Lai). All rights reserved. 本網頁產權所有，非經授權請勿複製。")
