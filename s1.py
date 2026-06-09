import streamlit as st
from deep_translator import GoogleTranslator
import streamlit.components.v1 as components
import base64

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Language Translation Tool",
    layout="centered"
)

# ============================================
# BACKGROUND IMAGE
# ============================================

def set_bg(image_file):

    with open(image_file, "rb") as f:
        data = f.read()

    encoded = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
            background:
            linear-gradient(
                rgba(255,255,255,0.5),
                rgba(255,255,255,0.5)
            ),
            url("data:image/jpg;base64,{encoded}");

            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* ====================================
           TEXT AREA
        ==================================== */

        textarea {{
            background-color: #111827 !important;
            color: white !important;
            border-radius: 12px !important;
            font-size: 18px !important;
            padding: 10px !important;
        }}

        /* ====================================
           SELECT BOX
        ==================================== */

        div[data-baseweb="select"] > div {{
            background-color: #111827 !important;
            color: white !important;
            border-radius: 12px !important;
            font-size: 16px !important;
        }}

        /* ====================================
           TRANSLATE BUTTON
        ==================================== */

        div.stButton > button {{
            background-color: #111827 !important;
            color: white !important;
            border-radius: 12px !important;
            height: 50px;
            font-size: 20px !important;
            font-weight: bold;
            width: 100%;
            border: none;
        }}

        div.stButton > button:hover {{
            background-color: #1f2937 !important;
            color: white !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

# ============================================
# SET BACKGROUND IMAGE
# ============================================

set_bg("code.jpeg")

# ============================================
# TITLE
# ============================================

st.markdown(
    """
    <h1 style='
    margin-top:80px;
    text-align:center;
    font-size:55px;
    font-weight:900;
    color:black;
    text-shadow:2px 2px 10px rgba(0,0,0,0.2);
    '>
      Language Translation Tool
    </h1>
    """,
    unsafe_allow_html=True
)


languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}


st.markdown(
    """
    <h4 style='
    color:black;
    margin-top:30px;
    margin-bottom:-5px;
    font-weight:bold;
    '>
    Enter Text
    </h4>
    """,
    unsafe_allow_html=True
)

text = st.text_area(
    "",
    height=160
)


st.markdown(
    """
    <h4 style='
    color:black;
    margin-top:15px;
    margin-bottom:-5px;
    font-weight:bold;
    '>
    Select Source Language
    </h4>
    """,
    unsafe_allow_html=True
)

source_lang = st.selectbox(
    "",
    list(languages.keys()),
    key="source"
)



st.markdown(
    """
    <h4 style='
    color:black;
    margin-top:15px;
    margin-bottom:-5px;
    font-weight:bold;
    '>
    Select Target Language
    </h4>
    """,
    unsafe_allow_html=True
)

target_lang = st.selectbox(
    "",
    list(languages.keys()),
    key="target"
)


if st.button("Translate"):

    if text.strip() == "":

        st.markdown(
            """
            <h4 style='color:red;'>
            Please enter some text
            </h4>
            """,
            unsafe_allow_html=True
        )

    else:

        
        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        
        st.markdown(
            """
            <h4 style='
            color:black;
            margin-top:20px;
            font-weight:bold;
            '>
            Translated Text
            </h4>
            """,
            unsafe_allow_html=True
        )

        

        st.success(translated)

        

        speak_text = translated.replace(
            "'",
            "\\'"
        )

        html_code = f"""
        <div>
        <button onclick="
        var msg = new SpeechSynthesisUtterance(`{speak_text}`);
        msg.lang = '{languages[target_lang]}';
        msg.rate = 1;
        msg.pitch = 1;
        msg.volume = 1;
        window.speechSynthesis.speak(msg);
        "
        style="
        background-color:#111827;
        color:white;
        border:none;
        padding:12px 20px;
        border-radius:10px;
        cursor:pointer;
        font-size:18px;
        margin-top:10px;
        ">
        🔊
        </button>
        </div>
        """

        components.html(
            html_code,
            height=80
        )

        

        st.code(translated)
