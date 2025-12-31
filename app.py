import streamlit as st
import time
import os
import base64
import random
import streamlit.components.v1 as components
from datetime import datetime

# 1. Configurazione Pagina
st.set_page_config(page_title="SYS_UPGRADE_2026", page_icon="💾", layout="centered")

# --- CSS AVANZATO: GLITCH E TERMINALE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;500&display=swap');

    .stApp { background-color: #0d0d0d; }
    header, footer, #MainMenu {visibility: hidden;}

    .terminal-font {
        font-family: 'Fira Code', monospace;
        color: #00FF41;
    }

    /* Effetto Glitch per il titolo */
    .glitch {
        font-size: 3rem;
        font-weight: bold;
        text-transform: uppercase;
        position: relative;
        text-shadow: 0.05em 0 0 #00fffc, -0.03em -0.04em 0 #fc00ff,
                     0.025em 0.04em 0 #fffc00;
        animation: glitch 725ms infinite;
    }

    @keyframes glitch {
        0% { text-shadow: 0.05em 0 0 #00fffc, -0.03em -0.04em 0 #fc00ff, 0.025em 0.04em 0 #fffc00; }
        15% { text-shadow: 0.05em 0 0 #00fffc, -0.03em -0.04em 0 #fc00ff, 0.025em 0.04em 0 #fffc00; }
        16% { text-shadow: -0.05em -0.025em 0 #00fffc, 0.025em 0.035em 0 #fc00ff, -0.05em -0.05em 0 #fffc00; }
        49% { text-shadow: -0.05em -0.025em 0 #00fffc, 0.025em 0.035em 0 #fc00ff, -0.05em -0.05em 0 #fffc00; }
        50% { text-shadow: 0.05em 0.035em 0 #00fffc, 0.03em 0 0 #fc00ff, 0 -0.04em 0 #fffc00; }
        99% { text-shadow: 0.05em 0.035em 0 #00fffc, 0.03em 0 0 #fc00ff, 0 -0.04em 0 #fffc00; }
        100% { text-shadow: -0.05em 0 0 #00fffc, -0.025em -0.025em 0 #fc00ff, -0.025em -0.05em 0 #fffc00; }
    }

    /* Overlay per scanline (effetto vecchio monitor) */
    .overlay {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.1) 50%), 
                    linear-gradient(90deg, rgba(255, 0, 0, 0.03), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.03));
        background-size: 100% 2px, 3px 100%;
        pointer-events: none; z-index: 1000;
    }
    </style>
    <div class="overlay"></div>
    """, unsafe_allow_html=True)

def play_audio(file_name):
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio autoplay="true" style="display:none;">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
            components.html(md, height=0, width=0)

def main():
    if 'stage' not in st.session_state:
        st.session_state.stage = 'lock'

    # --- STAGE 1: LOCK SCREEN ---
    if st.session_state.stage == 'lock':
        st.markdown('<div class="glitch" style="text-align:center;">CRITICAL_ERROR</div>', unsafe_allow_html=True)
        st.markdown("<br><p class='terminal-font' style='text-align:center;'>UNEXPECTED TEMPORAL DRIFT DETECTED: 2025 -> 2026</p>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            if st.button("INITIATE EMERGENCY PATCH"):
                st.session_state.stage = 'patching'
                st.rerun()

    # --- STAGE 2: PATCHING (INTERATTIVO) ---
    elif st.session_state.stage == 'patching':
        st.markdown("<h2 class='terminal-font'>ROOT@CACTUS_CORE: patching kernel...</h2>", unsafe_allow_html=True)
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        log_area = st.empty()
        
        logs = [
            "Stopping epoch_clock.service...",
            "Overriding UTC_limit_2025...",
            "Rebuilding timestamp_headers...",
            "Injecting 'HappyNewYear.so' library...",
            "Clearing 2025 cache files...",
            "Synchronizing with atomic_clock_v6..."
        ]
        
        for i, log in enumerate(logs):
            status_text.markdown(f"<p class='terminal-font'>[RUNNING]: {log}</p>", unsafe_allow_html=True)
            progress_bar.progress((i + 1) * 16)
            time.sleep(random.uniform(0.8, 2.0))
        
        st.session_state.stage = 'countdown'
        st.rerun()

    # --- STAGE 3: COUNTDOWN E CELEBRAZIONE ---
    elif st.session_state.stage == 'countdown':
        # Qui facciamo finta che manchino pochi secondi alla mezzanotte o al "reboot"
        st.markdown("<div class='glitch' style='text-align:center;'>SYSTEM REBOOT</div>", unsafe_allow_html=True)
        
        # Countdown finto di 5 secondi per suspense
        placeholder = st.empty()
        for i in range(5, 0, -1):
            placeholder.markdown(f"<h1 style='text-align:center; font-size:100px; color:white;'>{i}</h1>", unsafe_allow_html=True)
            time.sleep(1)
        
        placeholder.empty()
        st.session_state.stage = 'success'
        st.rerun()

    # --- STAGE 4: FINALE 2026 ---
    elif st.session_state.stage == 'success':
        play_audio("musica.mp3") # La vostra musica rock
        
        # Titolo Finale
        st.markdown("""
            <h1 style='text-align: center; color: #00FF41; font-family: monospace; border: 2px solid #00FF41; padding: 20px;'>
                MISSION ACCOMPLISHED: WELCOME TO 2026
            </h1>
            """, unsafe_allow_html=True)
        
        st.balloons()
        
        # Immagine ASCII o Foto
        if os.path.exists("ascii.png"):
            st.image("ascii.png", use_container_width=True)
        
        st.success("Buon Anno, Locandieri! Il sistema è stabile. Per ora.")
        
        if os.path.exists("foto.png"):
            st.image("foto.png", use_container_width=True)

        st.markdown("<p class='terminal-font' style='opacity:0.5;'>uptime: 0 days, 0 hours, 1 minute. No errors found.</p>", unsafe_allow_html=True)
        
        if st.button("RELOG TO SYSTEM"):
            st.session_state.stage = 'lock'
            st.rerun()

if __name__ == "__main__":
    main()