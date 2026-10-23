# AgriSmart — Smart Farming Prototype

தமிழ் மொழியில் உருவாக்கப்பட்ட Hackathon demo.

## இதில் உள்ள அம்சங்கள்
- முகப்பு Dashboard
- வானிலை திரை (live API இன்னும் இணைக்கப்படவில்லை)
- பயிர் ஆலோசனை
- இலைப் புகைப்பட upload UI (AI model இன்னும் இணைக்கப்படவில்லை)
- Smart irrigation demo advice
- சந்தை விலை திரை (live market data இன்னும் இணைக்கப்படவில்லை)
- விவசாயச் செலவு calculator
- விவசாயக் குறிப்புகள் (current session only)

## இயக்குவது
1. Python 3.10+ நிறுவவும்.
2. Terminal / Command Prompt-ல் இந்த project folder-ஐ திறக்கவும்.
3. `pip install -r requirements.txt`
4. `streamlit run app.py`
5. Browser-ல் திறக்கும் முகவரியை Android phone-ல் அதே Wi-Fi-யில் திறக்கலாம், அல்லது deployment செய்யலாம்.

## முக்கிய குறிப்பு
இது mobile-friendly web prototype; நேரடியாக APK அல்ல. Android APK ஆக மாற்ற, native Android app அல்லது WebView wrapper தேவை. AI disease detection, live weather, live market prices, sensor integration ஆகியவை தனியாக இணைக்கப்பட வேண்டும்.
