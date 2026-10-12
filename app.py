
import streamlit as st

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="HomeAid | Your Personal Care Guide",
    page_icon="🌷",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "user_name" not in st.session_state:
    st.session_state.user_name = "Sneha"

if "symptom" not in st.session_state:
    st.session_state.symptom = "Fever"

if "details" not in st.session_state:
    st.session_state.details = ""

# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&display=swap');

.stApp {
    background: linear-gradient(145deg, #fff9ee 0%, #fff0ed 52%, #fff5d9 100%);
    font-family: 'Nunito', sans-serif;
    color: #51443f;
}

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu, footer {
    visibility: hidden;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    background: rgba(255,255,255,0.83);
    border: 1px solid #f7dfd4;
    border-radius: 30px;
    padding: 45px 25px;
    text-align: center;
    box-shadow: 0 12px 35px rgba(183, 128, 103, 0.10);
    margin: 15px 0 24px;
}

.eyebrow {
    color: #bd7b6a;
    font-size: 13px;
    letter-spacing: 3px;
    font-weight: 800;
    text-transform: uppercase;
}

.hero h1 {
    color: #80594f;
    font-size: clamp(35px, 6vw, 54px);
    line-height: 1.2;
    margin: 15px 0;
}

.hero p {
    color: #806e66;
    font-size: 17px;
    line-height: 1.8;
}

.emoji {
    font-size: 65px;
    margin-bottom: 15px;
}

.soft-card {
    background: rgba(255,255,255,0.8);
    border: 1px solid #f5ded4;
    border-radius: 22px;
    padding: 23px;
    margin: 15px 0;
}

.section-title {
    color: #80594f;
    font-size: 27px;
    font-weight: 800;
    text-align: center;
}

.small-note {
    color: #947c72;
    font-size: 13px;
    text-align: center;
}

.stButton > button {
    background: #e99d8b;
    color: white;
    border: none;
    border-radius: 16px;
    padding: 0.75rem 1.1rem;
    font-weight: 800;
    min-height: 48px;
    transition: 0.2s ease;
}

.stButton > button:hover {
    background: #d98777;
    color: white;
    border: none;
    transform: translateY(-2px);
}

.stTextArea textarea, .stTextInput input {
    border-radius: 12px;
}

[data-testid="stRadio"] label {
    color: #634f47;
}

hr {
    border-color: #f0d9cf;
}

</style>
""", unsafe_allow_html=True)


# ---------------- WELCOME SCREEN ----------------
if st.session_state.page == "welcome":

    st.markdown("""
    <div class="hero">
        <div class="emoji">🌷 ☀️ 🌷</div>
        <div class="eyebrow">A little care goes a long way</div>
        <h1>Welcome, Sneha! 💗</h1>
        <p>
            We're so happy you're here.<br>
            Welcome to <b>HomeAid</b> — your friendly
            guide to everyday health and first aid.
        </p>
        <p>
            Take a deep breath. You're in a space
            made to help you feel informed, calm,
            and cared for. 🌼
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="soft-card" style="text-align:center;">
        <h3 style="color:#80594f;">Your well-being matters. 🌸</h3>
        <p>
            From everyday discomforts to simple first-aid
            guidance, let's take things one step at a time.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("🌼  Start Your Journey", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

    st.markdown(
        '<p class="small-note">Made with care, just for you ♡</p>',
        unsafe_allow_html=True
    )


# ---------------- SYMPTOM SELECTION SCREEN ----------------
elif st.session_state.page == "home":

    st.markdown("""
    <div class="hero">
        <div class="emoji">🩷 🌻 🩷</div>
        <div class="eyebrow">We're here for you</div>
        <h1>How can we help?</h1>
        <p>Tell us what's bothering you today.<br>
        We'll help you understand the next safe step.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🌸 Choose what you're experiencing")

    st.session_state.symptom = st.radio(
        "Select an option",
        [
            "Fever",
            "Headache",
            "Stomach pain",
            "Fall or minor injury",
            "Cough or cold",
            "Skin irritation or itching",
            "Other"
        ],
        horizontal=False
    )

    st.markdown("### 💬 Tell us a little more (optional)")

    st.session_state.details = st.text_area(
        "Describe your symptoms",
        placeholder="For example: When did it start? How severe is it?",
        height=110
    )

    st.info(
        "🚨 If you have trouble breathing, severe chest pain, "
        "uncontrolled bleeding, confusion, or another life-threatening "
        "symptom, seek emergency medical help immediately."
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("← Back", use_container_width=True):
            st.session_state.page = "welcome"
            st.rerun()

    with col2:
        if st.button("Get My Care Guide →", use_container_width=True):
            st.session_state.page = "care"
            st.rerun()


# ---------------- CARE GUIDE SCREEN ----------------
elif st.session_state.page == "care":

    st.markdown("""
    <div class="hero">
        <div class="emoji">🌼 🩹 🌼</div>
        <div class="eyebrow">Your personal care guide</div>
        <h1>Let's take care. 💗</h1>
        <p>Here are some general safety steps to consider.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f'<div class="section-title">Your concern: {st.session_state.symptom}</div>',
        unsafe_allow_html=True
    )

    st.write("")

    guidance = {
        "Fever": [
            "Rest and drink fluids regularly.",
            "Check your temperature with a thermometer.",
            "Seek medical advice for persistent or worsening fever."
        ],
        "Headache": [
            "Rest in a quiet, comfortable place and drink water.",
            "Take a break from screens if they worsen your discomfort.",
            "Seek urgent care for a sudden, extremely severe headache or one with weakness, confusion, or vision changes."
        ],
        "Stomach pain": [
            "Rest and take small sips of water if you can.",
            "Avoid foods that seem to worsen the discomfort.",
            "Seek urgent care for severe or worsening pain, a rigid abdomen, fainting, or blood in vomit or stool."
        ],
        "Fall or minor injury": [
            "Rest and protect the injured area.",
            "For a recent sprain, apply a cold pack wrapped in cloth for 15–20 minutes at a time.",
            "Seek medical care if you cannot bear weight, have severe pain, deformity, numbness, or major swelling."
        ],
        "Cough or cold": [
            "Rest and drink fluids.",
            "Warm drinks may soothe throat discomfort.",
            "Seek urgent care for breathing difficulty, blue or grey lips, or severe chest pain."
        ],
        "Skin irritation or itching": [
            "Avoid suspected irritants and stop using products that cause burning.",
            "Gently wash the area and keep it dry; avoid scratching.",
            "Seek medical advice for spreading, painful, persistent, or infected-looking rashes. Facial or tongue swelling with breathing difficulty is an emergency."
        ],
        "Other": [
            "Describe your symptoms to a qualified healthcare professional.",
            "Note when the symptoms started and whether they are getting worse.",
            "Seek urgent medical help for severe or rapidly worsening symptoms."
        ]
    }

    st.markdown('<div class="soft-card">', unsafe_allow_html=True)

    for step in guidance[st.session_state.symptom]:
        st.markdown(f"🌷 {step}")
        st.write("")

    st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.details.strip():
        st.markdown("#### Your description")
        st.write(st.session_state.details)

    st.warning(
        "HomeAid provides general educational guidance, not a diagnosis "
        "or a personalised prescription. It cannot confirm that an "
        "illness is minor. Consult a healthcare professional when needed."
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("← Change Selection", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()

    with col2:
        if st.button("Finish & Thank You 💗", use_container_width=True):
            st.session_state.page = "thanks"
            st.rerun()


# ---------------- THANK YOU SCREEN ----------------
elif st.session_state.page == "thanks":

    st.markdown("""
    <div class="hero">
        <div class="emoji">🌻 🦋 🌷</div>
        <div class="eyebrow">A little reminder from HomeAid</div>
        <h1>Thank You! 💗</h1>
        <p>
            Thank you for spending a little time with us.
        </p>
        <p>
            Remember to take care of yourself,<br>
            listen to your body, and ask for help when you need it.
        </p>
        <h3 style="color:#bd7b6a;">
            Stay healthy. Stay happy. Stay safe. ☀️
        </h3>
        <p>You deserve care, kindness, and a little sunshine every day.</p>
        <p>With love, <b> HomeAid</b> 🌸</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🏡 Back to Home", use_container_width=True):
        st.session_state.page = "welcome"
        st.session_state.details = ""
        st.rerun()

    st.markdown(
        '<p class="small-note">HomeAid — Caring starts at home ♡</p>',
        unsafe_allow_html=True
    )
