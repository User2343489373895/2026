import streamlit as st
import time
import os
import base64
import random
import streamlit.components.v1 as components

# 1. Configurazione Pagina
st.set_page_config(page_title="THE_BACKDOOR_2026", page_icon="💃", layout="centered")

# --- CSS: NEON STRIP CLUB LOOK ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Fira+Code&display=swap');

    .stApp { background-color: #050505; }
    header, footer, #MainMenu {visibility: hidden;}

    /* Testo Neon */
    .neon-text {
        font-family: 'Orbitron', sans-serif;
        color: #ff00ff;
        text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff;
        text-align: center;
    }
    
    .terminal-text {
        font-family: 'Fira Code', monospace;
        color: #00ffff;
        font-size: 14px;
    }

    /* Pioggia di Dollari e Bit */
    .matrix-rain {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none; z-index: 1; opacity: 0.5;
    }
    .bit {
        position: absolute; top: -30px;
        font-family: monospace; font-size: 22px;
        animation: fall linear infinite;
    }
    @keyframes fall { to { transform: translateY(110vh); } }

    /* Bottone Custom */
    div.stButton > button {
        background-color: #ff00ff;
        color: white;
        border: 2px solid #00ffff;
        font-family: 'Orbitron', sans-serif;
        box-shadow: 0 0 15px #ff00ff;
        width: 100%;
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
    cols = 80
    chars = ["$", "0", "1", "🥂", "🍑", "✨", "💎"]
    html_bits = '<div class="matrix-rain">'
    for i in range(cols):
        left = i * 2.5
        duration = random.uniform(2, 5)
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
        st.markdown("<h1 class='neon-text'>THE BACKDOOR</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:white; text-align:center;'>CYBER-STRIP & VIP LOUNGE</p>", unsafe_allow_html=True)
        
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJqZ2Z5Z3Z5Z3Z5Z3Z5Z3Z5Z3Z5Z3Z5Z3Z5Z3Z5Z3Z5JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKMGpxxcaTlg90c/giphy.gif", use_container_width=True) # Un GIF di luci neon o buttafuori

        st.markdown("<br>", unsafe_allow_html=True)
        pwd = st.text_input("INSERT PRIVATE KEY (VIP PASS):", type="password")
        
        if st.button("PAY THE BOUNCER"):
            if pwd.lower() == "2026": # Password semplice o a scelta
                st.session_state.access_granted = True
                st.rerun()
            else:
                st.error("BOUNCER: 'You're not on the list, kid.'")
    else:
        # --- DENTRO IL CLUB (HACKING IL PRIVE) ---
        play_audio("modem.mp3")
        
        st.markdown("<h2 class='neon-text'>ESTABLISHING SECURE CONNECTION...</h2>", unsafe_allow_html=True)
        
        log_placeholder = st.empty()
        full_log = ""
        
        # Log a tema "cyber-strip"
        steps = [
            ("> Connecting to 'NEON_DREAMS_AP'...", 1.5),
            ("> Bypassing 'Velvet_Curtain' Firewall...", 2.0),
            ("> Deep Packet Inspection (DPI) in progress... 😉", 2.5),
            ("> Exploiting 'Hot_Plug' vulnerability...", 2.0),
            ("> Escalating privileges to 'GOD_MODE'...", 3.0),
            ("> Downloading private_content.zip...", 2.5),
            ("> Decrypting 2026 New Year Assets...", 2.0),
            ("> SYSTEM READY FOR THE BIG SHOW.", 1.5),
        ]

        for text, delay in steps:
            full_log += f"<div class='terminal-text'>{text}</div>"
            log_placeholder.markdown(full_log, unsafe_allow_html=True)
            time.sleep(delay)

        # --- GRAN FINALE ---
        st.empty()
        start_vip_rain()
        play_audio("musica.mp3") # La vostra musica rock/dance

        st.markdown("""
            <h1 style='text-align: center; color: white; font-family: Orbitron; background: linear-gradient(90deg, #ff00ff, #00ffff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 50px;'>
                HAPPY NEW YEAR 2026!
            </h1>
            <p style='text-align: center; color: #ff00ff; font-weight: bold;'>Welcome to the VIP Room, Locandieri.</p>
            """, unsafe_allow_html=True)

        # Visualizza le vostre immagini
        if os.path.exists("ascii.png"):
            st.image("ascii.png", caption="[ENCRYPTED_VISUAL]", use_container_width=True)
        
        st.success("SUCCESS: Sei entrato nel 2026 dalla porta sul retro! 🍻")

        if os.path.exists("foto.png"):
            st.image("foto.png", caption="THE CREW", use_container_width=True)
        
        st.markdown("<p class='terminal-font' style='color:#ff00ff; text-align:center;'>session_status: UNLIMITED_ACCESS</p>", unsafe_allow_html=True)
        
        if st.button("LOGOUT FROM CLUB"):
            st.session_state.access_granted = False
            st.rerun()

if __name__ == "__main__":
    main()
