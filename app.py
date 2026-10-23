import streamlit as st
from datetime import date
import random

st.set_page_config(page_title="AgriSmart | ஸ்மார்ட் விவசாயம்", page_icon="🌾", layout="wide")

# Demo app: example values are for prototype display, not live agricultural advice/data.
st.markdown("""
<style>
.stApp {background: linear-gradient(180deg,#f3faef 0%,#ffffff 45%);}
section[data-testid="stSidebar"] {background:#e6f4df;}
.hero {padding:1.25rem;border-radius:18px;background:linear-gradient(120deg,#14532d,#3f8f46);color:white;}
.small-note {color:#526052;font-size:0.9rem;}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🌾 AgriSmart")
st.sidebar.caption("உங்கள் ஸ்மார்ட் விவசாய உதவியாளர்")
page = st.sidebar.radio("மெனு", [
    "முகப்பு", "வானிலை", "பயிர் ஆலோசனை", "AI நோய் கண்டறிதல்",
    "நீர்ப்பாசனம்", "சந்தை விலை", "செலவு கணக்கு", "விவசாய குறிப்புகள்"
])

st.sidebar.divider()
st.sidebar.info("இது Hackathon-க்கான Prototype. நேரடி வானிலை/சந்தைத் தரவு அல்லது உறுதிப்படுத்தப்பட்ட AI நோய் கண்டறிதல் இணைக்கப்படவில்லை.")

crops = {
    "நெல்": {"season":"பருவம் மற்றும் உள்ளூர் நீர் வசதியைப் பொறுத்தது", "water":"மண் ஈரப்பதம் மற்றும் வளர்ச்சி நிலையை அடிக்கடி கண்காணிக்கவும்", "tip":"உள்ளூர் வேளாண்மை அலுவலரின் பரிந்துரைப்படி உரம் இடவும்."},
    "மஞ்சள்": {"season":"உள்ளூர் மழை மற்றும் மண் நிலைக்கு ஏற்ப", "water":"நீர் தேங்காமல் மிதமான ஈரப்பதம் பராமரிக்கவும்", "tip":"நல்ல வடிகால் வசதி மற்றும் நோய் கண்காணிப்பு முக்கியம்."},
    "வாழை": {"season":"நீர் வசதி மற்றும் வகையைப் பொறுத்தது", "water":"மண்ணின் ஈரப்பதம் மற்றும் வெப்பநிலைக்கு ஏற்ப பாசனம் செய்யவும்", "tip":"காற்று பாதுகாப்பு, ஊட்டச்சத்து மற்றும் இலை அறிகுறிகளை கண்காணிக்கவும்."},
    "தக்காளி": {"season":"வெப்பநிலை மற்றும் உள்ளூர் பருவத்திற்கு ஏற்ப", "water":"சீரான ஈரப்பதம் தேவை; இலைகளை விட வேர் பகுதியில் நீர் கொடுக்கவும்", "tip":"இலைகள் மஞ்சளாகுதல், புள்ளிகள், பூச்சி அறிகுறிகளை கவனிக்கவும்."},
    "பருத்தி": {"season":"பகுதி மற்றும் விதை வகைக்கு ஏற்ப", "water":"மண் ஈரப்பதம் மற்றும் பயிர் நிலையைப் பார்த்து பாசனம் செய்யவும்", "tip":"பூச்சி கண்காணிப்பை முறையாகச் செய்யவும்."},
    "தேங்காய்": {"season":"தோட்டத்தின் வயது மற்றும் மழைக்கு ஏற்ப", "water":"மழை, மண் மற்றும் மர வயதைக் கருத்தில் கொண்டு நீர்ப்பாசனம் திட்டமிடவும்", "tip":"மண் பரிசோதனை அடிப்படையில் ஊட்டச்சத்து திட்டம் அமைக்கவும்."},
}

if page == "முகப்பு":
    st.markdown('<div class="hero"><h1>🌱 AgriSmart</h1><h3>விவசாயத்திற்கு ஒரே இடத்தில் ஸ்மார்ட் உதவி</h3><p>வானிலை • பயிர் ஆலோசனை • நோய் அறிகுறிகள் • பாசனம் • சந்தை • செலவு</p></div>', unsafe_allow_html=True)
    st.write("")
    a,b,c = st.columns(3)
    a.metric("சேவைகள்", "7", "Prototype modules")
    b.metric("பயிர்கள்", "6", "Demo crop library")
    c.metric("மொழி", "தமிழ்", "Mobile-friendly")
    st.subheader("விரைவு அணுகல்")
    cols = st.columns(3)
    shortcuts = [("🌦️ வானிலை","வானிலை"),("🌿 பயிர் ஆலோசனை","பயிர் ஆலோசனை"),("📷 நோய் கண்டறிதல்","AI நோய் கண்டறிதல்"),("💧 நீர்ப்பாசனம்","நீர்ப்பாசனம்"),("💹 சந்தை விலை","சந்தை விலை"),("🧾 செலவு கணக்கு","செலவு கணக்கு")]
    for i,(label,target) in enumerate(shortcuts):
        with cols[i%3]:
            st.info(label)
            st.caption("இடதுபுற மெனுவில் தேர்வு செய்யவும்")
    st.warning("கவனம்: இங்குள்ள வானிலை மற்றும் சந்தை விலை பகுதிகள் டெமோ வடிவம். உண்மையான முடிவுகளுக்கு நம்பகமான நேரடி தரவு இணைக்க வேண்டும்.")

elif page == "வானிலை":
    st.title("🌦️ வானிலைத் தகவல்")
    location = st.text_input("உங்கள் ஊர் / மாவட்டம்", "Tiruppur, Tamil Nadu")
    st.caption(f"தேர்ந்தெடுத்த இடம்: {location}")
    x,y,z = st.columns(3)
    x.metric("வெப்பநிலை", "—", "Live API இணைக்கப்படவில்லை")
    y.metric("மழை வாய்ப்பு", "—", "Live API இணைக்கப்படவில்லை")
    z.metric("காற்று வேகம்", "—", "Live API இணைக்கப்படவில்லை")
    st.info("அடுத்த கட்டத்தில் OpenWeather போன்ற வானிலை API இணைத்து நேரடி தரவைப் பெறலாம். மழை முன்னறிவிப்பை உறுதி செய்து பாசன முடிவெடுக்கவும்.")

elif page == "பயிர் ஆலோசனை":
    st.title("🌿 பயிர் ஆலோசனை")
    crop = st.selectbox("பயிரைத் தேர்ந்தெடுக்கவும்", list(crops.keys()))
    stage = st.selectbox("பயிரின் நிலை", ["நடவு / விதைப்பு", "வளர்ச்சி", "பூக்கும் நிலை", "அறுவடைக்கு முன்"])
    area = st.number_input("நில அளவு (ஏக்கர்)", min_value=0.1, value=1.0, step=0.1)
    if st.button("ஆலோசனை பார்க்க", type="primary"):
        info = crops[crop]
        st.success(f"{crop} — {stage}")
        st.write(f"**பருவம்:** {info['season']}")
        st.write(f"**நீர் மேலாண்மை:** {info['water']}")
        st.write(f"**முக்கிய குறிப்பு:** {info['tip']}")
        st.caption(f"நில அளவு: {area:.1f} ஏக்கர். உரம்/மருந்து அளவை இந்த Prototype கணக்கிடாது.")
    st.warning("பரிந்துரைகள் பொதுவானவை. மண் பரிசோதனை, உள்ளூர் பருவம் மற்றும் வேளாண்மை அலுவலரின் ஆலோசனை அடிப்படையில் முடிவு செய்யவும்.")

elif page == "AI நோய் கண்டறிதல்":
    st.title("📷 AI பயிர் நோய் அறிகுறி உதவி")
    st.write("பயிர் இலையின் தெளிவான புகைப்படத்தைப் பதிவேற்றவும்.")
    crop = st.selectbox("பயிர்", list(crops.keys()))
    photo = st.file_uploader("இலைப் புகைப்படம்", type=["png","jpg","jpeg"])
    if photo:
        st.image(photo, caption="பதிவேற்றிய படம்", use_container_width=True)
        st.info("Prototype நிலை: படம் பதிவேற்றம் செயல்படுகிறது; பயிற்சி பெற்ற நோய் வகைப்படுத்தும் AI மாடல் இன்னும் இணைக்கப்படவில்லை.")
        st.write("அடுத்த கட்டத்தில் PlantVillage போன்ற சரியான dataset-இல் பயிற்சி பெற்ற மாடலை இணைக்கலாம்.")
    st.warning("இந்த திரை இப்போது நோயை உறுதிப்படுத்தாது. படத்தின் அடிப்படையில் மட்டும் பூச்சிக்கொல்லி/மருந்து பயன்படுத்த வேண்டாம். உள்ளூர் வேளாண் நிபுணரை அணுகவும்.")

elif page == "நீர்ப்பாசனம்":
    st.title("💧 Smart Irrigation ஆலோசனை")
    crop = st.selectbox("பயிர்", list(crops.keys()))
    moisture = st.slider("மண் ஈரப்பதம் (சென்சார் அல்லது மாதிரி மதிப்பு)", 0, 100, 45, help="இது டெமோ slider; உண்மையான சென்சார் இணைக்கப்படவில்லை.")
    rain = st.selectbox("அடுத்த 24 மணி நேர மழை முன்னறிவிப்பு", ["தெரியவில்லை", "மழை இல்லை", "சிறிய மழை", "கனமழை வாய்ப்பு"])
    if st.button("நீர்ப்பாசன ஆலோசனை", type="primary"):
        if rain == "கனமழை வாய்ப்பு":
            advice = "மழை முன்னறிவிப்பை உள்ளூர் தகவலுடன் உறுதி செய்யவும்; உடனடி பாசனத்தைத் தள்ளிப்போடுவது பொருத்தமாக இருக்கலாம்."
        elif moisture < 30 and rain == "மழை இல்லை":
            advice = "மண்/பயிர் நிலையை நேரில் சரிபார்த்து பாசனம் தேவைப்படுகிறதா என மதிப்பிடவும்."
        elif moisture > 70:
            advice = "மண் ஈரப்பதம் அதிகமாக இருக்கலாம்; நீர் தேங்குகிறதா என்று பாருங்கள்."
        else:
            advice = "மண் மற்றும் பயிரின் வளர்ச்சி நிலையை மீண்டும் சரிபார்த்து பாசனத்தைத் திட்டமிடவும்."
        st.success(advice)
        st.caption(f"தேர்ந்தெடுத்த பயிர்: {crop} | மாதிரி ஈரப்பதம்: {moisture}%")
    st.caption("உண்மையான Smart Irrigation-க்கு soil-moisture sensor / IoT board இணைக்க வேண்டும்.")

elif page == "சந்தை விலை":
    st.title("💹 சந்தை விலை (Demo)")
    st.caption("கீழே உள்ள எண்கள் மாதிரி மதிப்புகள் மட்டுமே; இவை தற்போதைய சந்தை விலைகள் அல்ல.")
    market = [
        {"பயிர்":"நெல்","மாதிரி விலை (₹/குவிண்டால்)": "—"},
        {"பயிர்":"மஞ்சள்","மாதிரி விலை (₹/குவிண்டால்)": "—"},
        {"பயிர்":"தக்காளி","மாதிரி விலை (₹/குவிண்டால்)": "—"},
        {"பயிர்":"பருத்தி","மாதிரி விலை (₹/குவிண்டால்)": "—"},
    ]
    st.dataframe(market, use_container_width=True, hide_index=True)
    st.info("உண்மையான விலைகளை இணைக்க Agmarknet அல்லது e-NAM போன்ற அதிகாரப்பூர்வ தரவு மூலங்களின் அணுகல் முறையைச் சரிபார்க்க வேண்டும்.")
    st.text_input("சந்தை / மாவட்டம்", "Tiruppur")

elif page == "செலவு கணக்கு":
    st.title("🧾 விவசாயச் செலவு கணக்கு")
    crop = st.selectbox("பயிர்", list(crops.keys()))
    land = st.number_input("நில அளவு (ஏக்கர்)", min_value=0.1, value=1.0, step=0.1)
    seeds = st.number_input("விதை செலவு (₹)", min_value=0.0, value=1500.0, step=100.0)
    fertilizer = st.number_input("உரம் செலவு (₹)", min_value=0.0, value=2500.0, step=100.0)
    labour = st.number_input("தொழிலாளர் செலவு (₹)", min_value=0.0, value=4000.0, step=100.0)
    water = st.number_input("பாசனம் / மின்சாரம் (₹)", min_value=0.0, value=1000.0, step=100.0)
    other = st.number_input("மற்ற செலவுகள் (₹)", min_value=0.0, value=500.0, step=100.0)
    total = seeds + fertilizer + labour + water + other
    st.metric("மொத்த செலவு", f"₹{total:,.2f}")
    st.metric("ஏக்கருக்கு செலவு", f"₹{total/land:,.2f}")
    st.caption(f"பயிர்: {crop} | கணக்கு உங்கள் உள்ளீடுகளை மட்டுமே அடிப்படையாகக் கொண்டது.")

elif page == "விவசாய குறிப்புகள்":
    st.title("📒 விவசாய குறிப்புகள்")
    if "notes" not in st.session_state:
        st.session_state.notes = []
    with st.form("note_form"):
        note_date = st.date_input("தேதி", value=date.today())
        crop = st.selectbox("பயிர்", list(crops.keys()))
        note = st.text_area("குறிப்பு", placeholder="உதா: இன்று வயலில் கவனித்தது...")
        submitted = st.form_submit_button("குறிப்பைச் சேமிக்கவும்")
        if submitted and note.strip():
            st.session_state.notes.append({"தேதி": str(note_date), "பயிர்": crop, "குறிப்பு": note.strip()})
            st.success("இந்த அமர்வில் குறிப்பு சேமிக்கப்பட்டது.")
    if st.session_state.notes:
        st.dataframe(list(reversed(st.session_state.notes)), use_container_width=True, hide_index=True)
    else:
        st.caption("இன்னும் குறிப்புகள் இல்லை. இந்த Prototype-இல் குறிப்புகள் தற்போதைய அமர்வு வரை மட்டுமே இருக்கும்.")

st.divider()
st.caption("AgriSmart Prototype • கல்வி / Hackathon Demo • உண்மையான விவசாய முடிவுகளுக்கு உள்ளூர் நிபுணர் மற்றும் அதிகாரப்பூர்வ தரவைப் பயன்படுத்தவும்.")
