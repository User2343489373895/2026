import streamlit as st
import time
import os
import base64
import random
import streamlit.components.v1 as components

# 1. Configurazione Pagina
st.set_page_config(page_title="THE_BACKDOOR_2026", page_icon="🔞", layout="centered")

# --- CSS NEON LOOK ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Fira+Code&display=swap');
    .stApp { background-color: #050505; }
    header, footer, #MainMenu {visibility: hidden;}
    
    .neon-title {
        font-family: 'Orbitron', sans-serif;
        color: #ff00ff;
        text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 40px #ff00ff;
        text-align: center;
        font-size: 50px;
        margin-bottom: 0px;
    }
    .terminal-text {
        font-family: 'Fira Code', monospace;
        color: #00ffff;
        font-size: 14px;
        background: rgba(0, 255, 255, 0.05);
        padding: 5px;
        border-left: 3px solid #00ffff;
        margin-bottom: 5px;
    }
    /* Pioggia di Dollari e Bit */
    .matrix-rain {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none; z-index: 1; opacity: 0.3;
    }
    .bit {
        position: absolute; top: -30px;
        font-family: monospace; font-size: 22px;
        animation: fall linear infinite;
    }
    @keyframes fall { to { transform: translateY(110vh); } }
    
    /* Bottone Custom */
    div.stButton > button {
        background-color: #ff00ff !important;
        color: white !important;
        border: 2px solid #00ffff !important;
        font-family: 'Orbitron', sans-serif !important;
        box-shadow: 0 0 20px #ff00ff !important;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        box-shadow: 0 0 40px #00ffff !important;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

def play_audio(file_name):
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            md = f"""<audio autoplay="true" style="display:none;"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>"""
            components.html(md, height=0, width=0)

def start_vip_rain():
    chars = ["$", "0", "1", "🥂", "🍑", "💎", "💸"]
    html_bits = '<div class="matrix-rain">'
    for i in range(70):
        left = i * 2.5
        duration = random.uniform(2, 6)
        color = "#ff00ff" if i % 2 == 0 else "#00ffff"
        char = random.choice(chars)
        html_bits += f'<div class="bit" style="left:{left}%; color:{color}; animation-duration:{duration}s;">{char}</div>'
    html_bits += '</div>'
    st.markdown(html_bits, unsafe_allow_html=True)

def main():
    if 'access_granted' not in st.session_state:
        st.session_state.access_granted = False

    if not st.session_state.access_granted:
        # --- ENTRATA CLUB ---
        st.markdown("<h1 class='neon-title'>THE BACKDOOR</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:white; text-align:center; font-family:Orbitron;'>CYBER-STRIP & VIP LOUNGE 2026</p>", unsafe_allow_html=True)
        
        # GIF Buttafuori (Link aggiornato e più stabile da Tenor/Giphy)
        # Se il link si rompe, mostra un'immagine statica di stile cyberpunk
        bouncer_url = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3ZidW5pZ3MwaHh6OHZidW5pZ3MwaHh6OHZidW5pZ3MwaHh6OHZidW5pZ3MmZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/3o7TKVUn7iM8FMEU24/giphy.gif"
        st.image(bouncer_url, caption="BOUNCER: 'Key or GTFO.'", use_container_width=True)

        st.markdown("<br>", unsafe_allow_html=True)
        pwd = st.text_input("ENTER VIP PASS (PASSWORD):", type="password")
        
        if st.button("AUTHORIZE ENTRANCE"):
            if pwd.lower().strip() in ["locandieri", "2026"]:
                st.session_state.access_granted = True
                st.rerun()
            else:
                st.error("ACCESS DENIED: The bouncer stares at you coldly.")
    else:
        # --- DENTRO IL CLUB ---
        play_audio("modem.mp3")
        
        st.markdown("<h2 class='neon-title' style='font-size:30px;'>ESTABLISHING VIP LINK...</h2>", unsafe_allow_html=True)
        
        log_placeholder = st.empty()
        full_log = ""
        
        steps = [
            ("> Tunneling through 'Pink_Light' Proxy...", 1.2),
            ("> Bypassing 'Velvet_Door' Firewall...", 1.5),
            ("> Sniffing 'Champagne_Packets'...", 1.8),
            ("> Injecting 'Midnight_Surprise.js'...", 2.0),
            ("> Accessing 'Main_Stage' root shell...", 2.5),
            ("> Privilege Escalation: [STRIPPER_ADMIN] granted.", 1.5),
            ("> 3... 2... 1... HAPPY NEW YEAR!", 1.0),
        ]

        for text, delay in steps:
            full_log += f"<div class='terminal-text'>{text}</div>"
            log_placeholder.markdown(full_log, unsafe_allow_html=True)
            time.sleep(delay)

        # --- GRAN FINALE ---
        st.empty()
        start_vip_rain()
        play_audio("musica.mp3")

        st.markdown("""
            <h1 style='text-align: center; color: white; font-family: Orbitron; background: linear-gradient(90deg, #ff00ff, #00ffff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 55px; font-weight: 900;'>
                2026 UNLOCKED!
            </h1>
            <p style='text-align: center; color: #ff00ff; font-family: Orbitron; font-size: 20px;'>
                Welcome to the Privé, Locandieri. 🥂🔥
            </p>
            """, unsafe_allow_html=True)

        # GIF Finale Celebrazione
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHRydHk0NHRydHk0NHRydHk0NHRydHk0NHRydHk0NHRydHk0NHJ5JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l41lTfuxV3XyQG2pa/giphy.gif", use_container_width=True)

        if os.path.exists("ascii.png"):
            st.image("ascii.png", use_container_width=True)
        
        st.success("SUCCESS: La backdoor è aperta per tutto il 2026!")

        if os.path.exists("foto.png"):
            st.image("foto.png", caption="THE CREW", use_container_width=True)
        
        if st.button("TERMINATE SESSION"):
            st.session_state.access_granted = False
            st.rerun()

if __name__ == "__main__":
    main()
