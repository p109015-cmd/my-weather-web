# --- 【超級氣象中文字典：英文全部改成小寫】 ---
                weather_dict = {
                    "sunny": "晴天 ☀️", 
                    "clear": "晴朗 🌤️",
                    "partly cloudy": "多雲時晴 ⛅", 
                    "cloudy": "陰天 ☁️", 
                    "overcast": "多雲轉陰 🌥️", 
                    "mist": "有霧 🌫️", 
                    "fog": "大霧 🌫️", 
                    "freezing fog": "凍霧 🌫️",
                    "patchy rain nearby": "局部短暫雨 🌧️", 
                    "patchy rain possible": "可能下局部雨 🌧️",
                    "light rain": "小雨 🌧️", 
                    "light rain shower": "短暫小雨 🌧️",
                    "moderate rain": "中雨 🌧️", 
                    "moderate rain at times": "時有中雨 🌧️",
                    "heavy rain": "大雨 ⛈️", 
                    "heavy rain at times": "時有大雨 ⛈️",
                    "torrential rain shower": "暴雨 ⛈️",
                    "patchy snow possible": "可能下局部雪 ❄️", 
                    "light snow": "小雪 ❄️",
                    "heavy snow": "大雪 ❄️", 
                    "ice pellets": "冰雹 🌨️",
                    "thundery outbreaks possible": "可能雷陣雨 ⛈️",
                    "patchy light rain with thunder": "雷陣雨帶小雨 ⛈️",
                    "moderate or heavy rain with thunder": "大雷陣雨 ⛈️",
                    "patchy light drizzle": "局部毛毛雨 🌧️", 
                    "light drizzle": "毛毛雨 🌧️"
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
                
                # 【防錯核心】：把抓下來的英文強制變小寫 (.lower())，再去查字典！
                status_cht = weather_dict.get(status_eng.lower(), f"{status_eng} 🌍")
