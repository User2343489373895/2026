import streamlit as st
import time
import os
import base64
import random
import streamlit.components.v1 as components

# 1. Configurazione - DEVE ESSERE LA PRIMA
st.set_page_config(page_title="ESCLUSIVE_PRIVÉ 🥂", page_icon="🔞", layout="centered")

# --- CACHE AUDIO PER VELOCITÀ ---
@st.cache_data
def get_audio_b64(file_path):
    if file_path and os.path.exists(file_path):
        try:
            with open(file_path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        except: return None
    return None

# --- CSS GLOBALE (Centratura e Stile) ---
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
    
    /* Centratura Box Successo */
    div[data-testid="stNotificationContent"] {
        text-align: center !important; justify-content: center !important; width: 100% !important; font-family: 'Orbitron', sans-serif !important;
    }

    .matrix-rain { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 1; opacity: 0.3; }
    .bit { position: absolute; top: -30px; font-family: monospace; font-size: 20px; animation: fall linear infinite; }
    @keyframes fall { to { transform: translateY(110vh); } }
    
    div.stButton > button {
        background-color: transparent !important; color: #ff00ff !important; border: 2px solid #ff00ff !important;
        font-family: 'Orbitron', sans-serif !important; width: 100%; box-shadow: 0 0 10px #ff00ff; height: 50px;
    }
    iframe { position: fixed; top: 0; left: 0; width: 100vw !important; height: 100vh !important; border: none; pointer-events: none; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNZIONI GRAFICHE E AUDIO ---
def play_audio(file_name, loop=False):
    b64 = get_audio_b64(file_name)
    if b64:
        loop_attr = "loop" if loop else ""
        components.html(f"""<audio autoplay="true" {loop_attr}><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>""", height=0)

def show_party_visuals():
    # Pioggia di bit
    chars = ["$", "0", "1", "🥂", "✨", "💎", "2", "0", "2", "6"]
    rain_html = '<div class="matrix-rain">'
    for i in range(50):
        left = i * 2
        rain_html += f'<div class="bit" style="left:{left}%; color:#ff00ff; animation-duration:{random.uniform(2,5)}s;">{random.choice(chars)}</div>'
    st.markdown(rain_html + '</div>', unsafe_allow_html=True)
    
    # Fuochi d'artificio
    components.html("""<canvas id="fCanvas"></canvas><script>const c=document.getElementById('fCanvas');const x=c.getContext('2d');c.width=window.innerWidth;c.height=window.innerHeight;class F{constructor(){this.x=Math.random()*c.width;this.y=c.height;this.sx=Math.random()*4-2;this.sy=Math.random()*-4-8;this.color=`hsl(${Math.random()*360},100%,50%)`;this.ex=false}up(){this.x+=this.sx;this.y+=this.sy;this.sy+=0.15;if(this.sy>=-1)this.ex=true}dr(){x.fillStyle=this.color;x.beginPath();x.arc(this.x,this.y,3,0,Math.PI*2);x.fill()}}let fs=[];function an(){x.clearRect(0,0,c.width,c.height);if(Math.random()<0.05)fs.push(new F());fs.forEach((f,i)=>{f.up();f.dr();if(f.ex)fs.splice(i,1)});requestAnimationFrame(an)}an();</script>""", height=1000)

# --- LOGICA PRINCIPALE (Stato Isolato) ---
def main():
    if 'state' not in st.session_state:
        st.session_state.state = 'login'

    # Unico contenitore per evitare sovrapposizioni
    main_placeholder = st.empty()

    # FASE 1: LOGIN
    if st.session_state.state == 'login':
        with main_placeholder.container():
            st.markdown("<h1 class='neon-text'>THE BACKDOOR</h1>", unsafe_allow_html=True)
            st.markdown("<p style='color:#ff00ff; text-align:center; font-family:Orbitron;'>SECURE VIP ENTRANCE // 2026</p>", unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns([1, 2, 1])
            with c2:
                st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1fe56053-597e-45b3-a3b1-f26197574147/deb1dq7-6605a031-5944-49cc-8beb-dba5e8284c4a.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiIvZi8xZmU1NjA1My01OTdlLTQ1YjMtYTNiMS1mMjYxOTc1NzQxNDcvZGViMWRxNy02NjA1YTAzMS01OTQ0LTQ5Y2MtOGJlYi1kYmE1ZTgyODRjNGEuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.QauebzGlSfy161JK86WvKTuhXb3OfmoXKdV7rOy-I8Y", use_container_width=True)
            
            play_audio("scena1.mp3", loop=True)
            
            pwd = st.text_input("ACCESS KEY:", type="password", key="pwd_login")
            if st.button("AUTHORIZE ENTRANCE"):
                if pwd.lower().strip() == "locandieri":
                    st.session_state.state = 'hacking'
                    main_placeholder.empty()
                    st.rerun()
                else:
                    st.error("BOUNCER: 'You're not on the list.'")

    # FASE 2: HACKING
    elif st.session_state.state == 'hacking':
        with main_placeholder.container():
            play_audio("scena2.mp3", loop=False)
            st.markdown("<h2 class='pink-neon'>OVERRIDING VIP SERVER...</h2>", unsafe_allow_html=True)
            
            log_area = st.empty()
            full_log = ""
            steps = [
                ("> Initializing 'Seductive_Handshake'...", 1.2), 
                ("> Bypassing IDS/IPS...", 1.2), 
                ("> Deep Packet Inspection (DPI)...", 1.5), 
                ("> Privilege Escalation: ROOT granted.", 1.2), 
                ("> Executing HappyNewYear.exe...", 1.0)
            ]
            for text, delay in steps:
                full_log += f"<div class='terminal-text'>{text}</div>"
                log_area.markdown(full_log, unsafe_allow_html=True)
                time.sleep(delay)
            
            st.session_state.state = 'party'
            main_placeholder.empty()
            st.rerun()

    # FASE 3: PARTY
    elif st.session_state.state == 'party':
        with main_placeholder.container():
            # Rimosso audio fuochi per stabilità. Solo musica.mp3
            play_audio("musica.mp3", loop=False)
            show_party_visuals()

            st.markdown("<div style='text-align: center; position: relative; z-index: 10;'><h1 style='color: white; font-family: Orbitron; font-size: 50px; text-shadow: 0 0 20px #ff00ff;'>2026 UNLOCKED</h1></div>", unsafe_allow_html=True)
            
            if os.path.exists("ascii.png"):
                st.image("ascii.png", use_container_width=True)
            
            st.success("🥂 BUON ANNO, LOCANDIERI! 🥂")
            
            if os.path.exists("foto.png"):
                st.image("foto.png", use_container_width=True)
            
            if st.button("TERMINATE CONNECTION"):
                st.session_state.state = 'login'
                main_placeholder.empty()
                st.rerun()

if __name__ == "__main__":
    main()
