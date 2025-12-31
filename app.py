import streamlit as st
import time
import os
import base64
import random
import streamlit.components.v1 as components

# 1. Configurazione Iniziale (Deve essere la prima istruzione)
st.set_page_config(page_title="2026 UNLOCKED 💎", page_icon="🔞", layout="centered")

# --- FUNZIONI AUDIO ---
@st.cache_data
def get_audio_b64(file_path):
    if file_path and os.path.exists(file_path):
        try:
            with open(file_path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        except: return None
    return None

def play_audio(file_name, loop=False):
    b64 = get_audio_b64(file_name)
    if b64:
        loop_attr = "loop" if loop else ""
        components.html(f"""<audio autoplay="true" {loop_attr}><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>""", height=0)

# --- CSS GLOBALE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Fira+Code&display=swap');
    
    /* Reset pagina */
    .stApp { background-color: #050505 !important; }
    header, footer, #MainMenu {visibility: hidden;}
    
    /* Contenitore principale per evitare scroll inutili */
    .main-content {
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }

    /* Stile Scritte Hacker */
    .pink-neon { 
        color: #ff00ff; 
        text-shadow: 0 0 15px #ff00ff; 
        font-family: 'Orbitron', sans-serif; 
        font-size: clamp(24px, 8vw, 55px); 
        font-weight: 900; 
        margin-bottom: 5px;
    }
    .cyan-sub {
        color: #00ffff;
        text-shadow: 0 0 8px #00ffff;
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(14px, 4vw, 20px);
        font-weight: bold;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 20px;
    }

    /* 2026 UNLOCKED - Responsive e d'impatto */
    .unlocked-title {
        color: white; 
        font-family: 'Orbitron', sans-serif; 
        font-size: clamp(40px, 12vw, 90px); 
        text-shadow: 0 0 20px #ff00ff, 0 0 40px #ff00ff;
        font-weight: 900;
        margin: 25px 0;
        line-height: 1;
    }

    /* BOX BUON ANNO - Ora non si spezza mai */
    .custom-success-box {
        background-color: rgba(0, 255, 65, 0.1);
        border: 2px solid #00ff41;
        color: #00ff41;
        border-radius: 12px;
        padding: 20px;
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(16px, 5vw, 32px);
        font-weight: bold;
        text-shadow: 0 0 10px #00ff41;
        width: 100%;
        max-width: 800px;
        text-align: center;
        white-space: nowrap; /* Impedisce l'andata a capo */
        overflow: hidden;    /* Evita sbordamenti su schermi minuscoli */
        margin: 20px auto;
    }

    .terminal-text {
        font-family: 'Fira Code', monospace; 
        color: #00ff41; 
        font-size: 14px;
        background: rgba(0, 255, 65, 0.05); 
        padding: 12px; 
        border-left: 3px solid #00ff41; 
        margin-bottom: 8px;
        text-align: left;
        width: 100%;
    }
    
    /* Matrix Rain */
    @keyframes fall { to { transform: translateY(110vh); } }

    /* Fuochi d'artificio */
    @keyframes fireworks {
        0% { opacity: 1; transform: translateY(0) scale(0.5); }
        100% { opacity: 0; transform: translateY(-150vh) scale(1.5); }
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGICA DI NAVIGAZIONE ---
if 'state' not in st.session_state:
    st.session_state.state = 'login'

# Placeholder unico per pulire lo schermo tra una fase e l'altra
placeholder = st.empty()

# --- SCENA 1: LOGIN ---
if st.session_state.state == 'login':
    with placeholder.container():
        st.markdown("<div class='main-content'><div class='pink-neon'>THE BACKDOOR</div><div class='cyan-sub'>SECURE VIP ENTRANCE</div></div>", unsafe_allow_html=True)
        st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1fe56053-597e-45b3-a3b1-f26197574147/deb1dq7-6605a031-5944-49cc-8beb-dba5e8284c4a.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiIvZi8xZmU1NjA1My01OTdlLTQ1YjMtYTNiMS1mMjYxOTc1NzQxNDcvZGViMWRxNy02NjA1YTAzMS01OTQ0LTQ5Y2MtOGJlYi1kYmE1ZTgyODRjNGEuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.QauebzGlSfy161JK86WvKTuhXb3OfmoXKdV7rOy-I8Y", use_container_width=True)
        play_audio("scena1.mp3", loop=True)
        
        pwd = st.text_input("ACCESS KEY:", type="password", key="pass")
        if st.button("AUTHORIZE ENTRANCE"):
            if pwd.lower().strip() == "locandieri":
                st.session_state.state = 'hacking'
                st.rerun()
            else:
                st.error("ACCESS DENIED")

# --- SCENA 2: HACKING ---
elif st.session_state.state == 'hacking':
    with placeholder.container():
        play_audio("scena2.mp3")
        st.markdown("<div class='pink-neon'>OVERRIDING SYSTEM...</div>", unsafe_allow_html=True)
        log_area = st.empty()
        full_log = ""
        steps = [
                ("> Initializing 'Seductive_Handshake' protocol...", 1.2), 
                ("> Bypassing IDS/IPS (Intrusion Desire System)...", 1.5), 
                ("> Deep Packet Inspection of 'Private_Area'...", 1.8), 
                ("> Escalating privileges: Root granted.", 1.5), 
                ("> Extracting 'Secret_Payload.bin'...", 2.0), 
                ("> SUCCESS: Access granted.", 1.2), 
                ("> WELCOME!", 1.5)
        ]
        for msg, t in steps:
            full_log += f"<div class='terminal-text'>{msg}</div>"
            log_area.markdown(full_log, unsafe_allow_html=True)
            time.sleep(t)
        
        st.session_state.state = 'party'
