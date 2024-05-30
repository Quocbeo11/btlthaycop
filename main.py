from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
from datetime import datetime, timedelta

app = FastAPI()

@app.get("/weather")
async def get_weather_data():
    def fetch_weather_data(city, api_key):
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        return response.json()

    def extract_weather_info(data):
        weather_info = {}
        for item in data['list']:
            date = item['dt_txt'].split()[0]
            if date not in weather_info:
                temperature = item['main']['temp']
                humidity = item['main']['humidity']
                weather_info[date] = {'Date': date, 'Temperature': temperature, 'Humidity': humidity}
        return list(weather_info.values())

    def get_past_date(days):
        today = datetime.now()
        past_date = today - timedelta(days=days)
        return past_date.strftime("%Y-%m-%d")

    city = "Thai Nguyen"
    api_key = "093bc10f5336f52a5c3c761e7b731280"
    past_date = get_past_date(7)

    weather_data = fetch_weather_data(city, api_key)
    weather_info = extract_weather_info(weather_data)

    return JSONResponse(content=weather_info)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=1880)
