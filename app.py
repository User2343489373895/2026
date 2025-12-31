import streamlit as st
import time
import os
import base64
import random
import streamlit.components.v1 as components

# 1. Configurazione Pagina
st.set_page_config(page_title="GÜNTHER_BACKDOOR_2026", page_icon="🫦", layout="centered")

# --- CSS: NEON, GLOSS E BASS SHAKE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Fira+Code&display=swap');
    
    .stApp { background-color: #0d000d; overflow-x: hidden; }
    header, footer, #MainMenu {visibility: hidden;}

    /* Effetto vibrazione per il finale */
    @keyframes shake {
        0% { transform: translate(1px, 1px) rotate(0deg); }
        10% { transform: translate(-1px, -2px) rotate(-1deg); }
        20% { transform: translate(-3px, 0px) rotate(1deg); }
        30% { transform: translate(3px, 2px) rotate(0deg); }
        40% { transform: translate(1px, -1px) rotate(1deg); }
        50% { transform: translate(-1px, 2px) rotate(-1deg); }
    }

    .neon-title {
        font-family: 'Orbitron', sans-serif;
        color: #ff00ff;
        text-shadow: 0 0 10px #ff00ff, 0 0 30px #ff00ff;
        text-align: center;
        font-size: 45px;
    }

    .terminal-text {
        font-family: 'Fira Code', monospace;
        color: #ff00ff;
        font-size: 14px;
        background: rgba(255, 0, 255, 0.1);
        padding: 8px;
        border-left: 3px solid #00ffff;
        margin-bottom: 5px;
    }

    .matrix-rain {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none; z-index: 1; opacity: 0.4;
    }
    .bit {
        position: absolute; top: -30px;
        font-family: monospace; font-size: 24px;
        animation: fall linear infinite;
    }
    @keyframes fall { to { transform: translateY(110vh); } }
    
    div.stButton > button {
        background: linear-gradient(45deg, #ff00ff, #00ffff) !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        box-shadow: 0 0 20px #ff00ff !important;
    }
    </style>
    """, unsafe_allow_html=True)

def play_audio(file_name):
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            md = f"""<audio autoplay="true" style="display:none;"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>"""
            components.html(md, height=0, width=0)

def start_gunther_rain():
    # Pioggia di elementi a tema Günther e Cyber
    chars = ["🫦", "🕶️", "✨", "0", "1", "$", "🔥", "🥂"]
    html_bits = '<div class="matrix-rain">'
    for i in range(80):
        left = i * 2.5
        duration = random.uniform(1.5, 4)
        color = "#ff00ff" if i % 2 == 0 else "#00ffff"
        char = random.choice(chars)
        html_bits += f'<div class="bit" style="left:{left}%; color:{color}; animation-duration:{duration}s;">{char}</div>'
    html_bits += '</div>'
    st.markdown(html_bits, unsafe_allow_html=True)

def main():
    if 'access' not in st.session_state:
        st.session_state.access = False

    if not st.session_state.access:
        st.markdown("<h1 class='neon-title'>THE BACKDOOR 2026</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:white; text-align:center;'>Access the Private Deep_Dong Server</p>", unsafe_allow_html=True)
        
        # GIF di Günther o stile Cyber-Sexy (Sostituito con uno stabile)
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3ZidW5pZ3MwaHh6OHZidW5pZ3MwaHh6OHZidW5pZ3MwaHh6OHZidW5pZ3MmZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/3o7TKVUn7iM8FMEU24/giphy.gif")

        pwd = st.text_input("ENTER SECRET PASSCODE:", type="password")
        if st.button("TOUCH MY TRALALA"):
            if pwd.lower().strip() in ["gunther", "dingdong", "2026"]:
                st.session_state.access = True
                st.rerun()
            else:
                st.error("BOUNCER: 'You don't have enough mustache for this club.'")
    else:
        # --- SEQUENZA DI HACKING ---
        play_audio("modem.mp3")
        st.markdown("<h2 class='neon-title' style='font-size:25px;'>INJECTING GÜNTHER_PAYLOAD.EXE...</h2>", unsafe_allow_html=True)
        
        log_placeholder = st.empty()
        full_log = ""
        
        steps = [
            ("> Scanning 'Tralala' sectors...", 1.2),
            ("> Bypassing Virgin_Firewall_v2.0...", 1.5),
            ("> Deep Dong Inspection in progress...", 1.8),
            ("> Escalating mustache privileges...", 1.5),
            ("> Cracking 'Ding_Ding_Dong.key'...", 2.0),
            ("> Root access granted. Oh, you touched it!", 1.5),
        ]

        for text, delay in steps:
            full_log += f"<div class='terminal-text'>{text}</div>"
            log_placeholder.markdown(full_log, unsafe_allow_html=True)
            time.sleep(delay)

        # --- FINALE ---
        st.empty()
        # Applica l'animazione di vibrazione allo schermo intero
        st.markdown("<script>document.body.style.animation = 'shake 0.5s infinite';</script>", unsafe_allow_html=True)
        
        start_gunther_rain()
        play_audio("musica.mp3") # DEVE ESSERE DING DING DONG

        st.markdown("""
            <div style='text-align: center;'>
                <h1 style='color: #ff00ff; font-family: Orbitron; font-size: 60px; margin-bottom: 0;'>2026</h1>
                <h2 style='color: #00ffff; font-family: Orbitron; font-size: 30px;'>YOU UNLOCKED THE DONG</h2>
            </div>
            """, unsafe_allow_html=True)

        # GIF DI GÜNTHER (Iconica)
        st.image("https://media1.tenor.com/m/Xz_V6D_8_6sAAAAd/gunther-ding-ding-dong.gif", use_container_width=True)

        if os.path.exists("ascii.png"):
            st.image("ascii.png", use_container_width=True)
        
        st.success("BUON ANNO LOCANDIERI! 🥂🫦")

        if os.path.exists("foto.png"):
            st.image("foto.png", use_container_width=True)
        
        if st.button("LOGOUT (DON'T TOUCH IT ANYMORE)"):
            st.session_state.access = False
            st.rerun()

if __name__ == "__main__":
    main()
