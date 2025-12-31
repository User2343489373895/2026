import streamlit as st
import time
import os
import base64
import random
import streamlit.components.v1 as components

# 1. Configurazione (Deve essere la prima cosa)
st.set_page_config(page_title="NEON_OVERRIDE_2026", page_icon="📟", layout="centered")

# --- CSS GLOBALE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Fira+Code&display=swap');
    .stApp { background-color: #050505 !important; }
    header, footer, #MainMenu {visibility: hidden;}
    .neon-text { font-family: 'Orbitron', sans-serif; color: #00ffff; text-shadow: 0 0 10px #00ffff; text-align: center; }
    .pink-neon { color: #ff00ff; text-shadow: 0 0 10px #ff00ff; font-family: 'Orbitron', sans-serif; text-align: center; font-size: 24px; }
    .terminal-text {
        font-family: 'Fira Code', monospace; color: #00ff41; font-size: 14px;
        background: rgba(0, 255, 65, 0.1); padding: 15px; border-left: 3px solid #00ff41; margin-bottom: 5px;
    }
    .matrix-rain { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 1; opacity: 0.4; }
    .bit { position: absolute; top: -30px; font-family: monospace; font-size: 20px; animation: fall linear infinite; }
    @keyframes fall { to { transform: translateY(110vh); } }
    div.stButton > button {
        background-color: transparent !important; color: #ff00ff !important; border: 2px solid #ff00ff !important;
        font-family: 'Orbitron', sans-serif !important; width: 100%; box-shadow: 0 0 10px #ff00ff; height: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

def play_audio(file_name):
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            md = f"""<audio autoplay="true" style="display:none;"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>"""
            components.html(md, height=0, width=0)

def start_cyber_rain():
    chars = ["$", "0", "1", "💎", "👾", "🥂", "🍑", "✨"]
    html_bits = '<div class="matrix-rain">'
    for i in range(80):
        left = i * 1.25
        duration = random.uniform(2, 5)
        color = "#ff00ff" if i % 2 == 0 else "#00ffff"
        char = random.choice(chars)
        html_bits += f'<div class="bit" style="left:{left}%; color:{color}; animation-duration:{duration}s;">{char}</div>'
    html_bits += '</div>'
    st.markdown(html_bits, unsafe_allow_html=True)

# --- LOGICA PRINCIPALE ---
if 'state' not in st.session_state:
    st.session_state.state = 'login'

# Creiamo un contenitore unico che copre tutta l'app
placeholder = st.empty()

# FASE 1: LOGIN
if st.session_state.state == 'login':
    with placeholder.container():
        st.markdown("<h1 class='neon-text'>THE BACKDOOR</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#ff00ff; text-align:center; font-family:Orbitron;'>SECURE VIP ENTRANCE // 2026</p>", unsafe_allow_html=True)
        
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3ZidW5pZ3MwaHh6OHZidW5pZ3MwaHh6OHZidW5pZ3MwaHh6OHZidW5pZ3MmZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/3o7TKVUn7iM8FMEU24/giphy.gif")

        pwd = st.text_input("ACCESS KEY:", type="password")
        if st.button("BYPASS FIREWALL"):
            if pwd.lower().strip() == "locandieri":
                st.session_state.state = 'hacking'
                placeholder.empty() # CANCELLA TUTTO IL LOGIN
                st.rerun()
            else:
                st.error("ACCESS DENIED: Firewall is holding strong.")

# FASE 2: HACKING
elif st.session_state.state == 'hacking':
    with placeholder.container():
        play_audio("modem.mp3")
        st.markdown("<h2 class='pink-neon'>OVERRIDING VIP SERVER...</h2>", unsafe_allow_html=True)
        
        log_area = st.empty()
        full_log = ""
        
        steps = [
            ("> Initializing 'Seductive_Handshake' protocol...", 1.2),
            ("> Bypassing IDS/IPS (Intrusion Desire System)...", 1.5),
            ("> Deep Packet Inspection of 'Private_Area'...", 1.8),
            ("> Escalating privileges to 'GOD_MODE'...", 1.5),
            ("> Extracting 'Secret_Payload_2026.bin'...", 2.0),
            ("> SUCCESS: System compromised.", 1.0),
        ]

        for text, delay in steps:
            full_log += f"<div class='terminal-text'>{text}</div>"
            log_area.markdown(full_log, unsafe_allow_html=True)
            time.sleep(delay)
        
        st.session_state.state = 'party'
        placeholder.empty() # CANCELLA TUTTI I LOG
        st.rerun()

# FASE 3: PARTY FINALE
elif st.session_state.state == 'party':
    with placeholder.container():
        start_cyber_rain()
        play_audio("musica.mp3") # <--- Ding Ding Dong qui

        st.markdown("""
            <div style='text-align: center;'>
                <h1 style='color: white; font-family: Orbitron; font-size: 50px; text-shadow: 0 0 20px #ff00ff;'>2026 UNLOCKED</h1>
                <p style='color: #00ffff; font-family: Orbitron; font-size: 20px;'>The backdoor is open. Enjoy the show.</p>
            </div>
            """, unsafe_allow_html=True)

        if os.path.exists("ascii.png"):
            st.image("ascii.png", use_container_width=True)
        
        st.success("BUON ANNO, LOCANDIERI! 🥂🔥")

        if os.path.exists("foto.png"):
            st.image("foto.png", caption="THE CREW", use_container_width=True)
        
        if st.button("TERMINATE CONNECTION"):
            st.session_state.state = 'login'
            placeholder.empty()
            st.rerun()
