import streamlit as st
import time
import os
import base64
import random
import streamlit.components.v1 as components

# 1. Configurazione Pagina (Deve essere la prima istruzione)
st.set_page_config(page_title="ESCLUSIVE_PRIVÉ 🥂", page_icon="🔞", layout="centered")

# --- FUNZIONE CACHE AUDIO (Risolve il problema del caricamento lento) ---
@st.cache_data
def get_audio_b64(file_path):
    if file_path and os.path.exists(file_path):
        try:
            with open(file_path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        except Exception as e:
            return None
    return None

# --- CSS GLOBALE (Mantenuto esattamente il tuo) ---
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
    
    div[data-testid="stNotificationContent"] {
        text-align: center !important;
        justify-content: center !important;
        width: 100% !important;
        font-family: 'Orbitron', sans-serif !important;
    }

    .matrix-rain { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 1; opacity: 0.3; }
    .bit { position: absolute; top: -30px; font-family: monospace; font-size: 20px; animation: fall linear infinite; }
    @keyframes fall { to { transform: translateY(110vh); } }
    
    div.stButton > button {
        background-color: transparent !important; color: #ff00ff !important; border: 2px solid #ff00ff !important;
        font-family: 'Orbitron', sans-serif !important; width: 100%; box-shadow: 0 0 10px #ff00ff; height: 50px;
        position: relative; z-index: 100;
    }
    iframe { position: fixed; top: 0; left: 0; width: 100vw !important; height: 100vh !important; border: none; pointer-events: none; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNZIONE AUDIO OTTIMIZZATA ---
def play_audio_scene(main_file, bg_file=None, main_loop=False, bg_loop=True, bg_volume=0.2):
    # Carichiamo solo i file necessari per la scena corrente
    main_b64 = get_audio_b64(main_file)
    bg_b64 = get_audio_b64(bg_file) if bg_file else None
    
    loop_attr = "loop" if main_loop else ""
    bg_loop_attr = "loop" if bg_loop else ""
    
    audio_html = f"""<div id="audio_container">"""
    if main_b64:
        audio_html += f"""<audio autoplay="true" {loop_attr}><source src="data:audio/mp3;base64,{main_b64}" type="audio/mp3"></audio>"""
    if bg_b64:
        audio_html += f"""<audio id="bg_track" autoplay="true" {bg_loop_attr}><source src="data:audio/mp3;base64,{bg_b64}" type="audio/mp3"></audio>
        <script>document.getElementById('bg_track').volume = {bg_volume};</script>"""
    audio_html += "</div>"
    components.html(audio_html, height=0)

# --- EFFETTI VISIVI ---
def show_real_fireworks():
    components.html("""<canvas id="fwCanvas"></canvas><script>const canvas=document.getElementById('fwCanvas');const ctx=canvas.getContext('2d');canvas.width=window.innerWidth;canvas.height=window.innerHeight;class F{constructor(){this.x=Math.random()*canvas.width;this.y=canvas.height;this.sx=Math.random()*4-2;this.sy=Math.random()*-4-8;this.c=`hsl(${Math.random()*360},100%,50%)`;this.ex=false}up(){this.x+=this.sx;this.y+=this.sy;this.sy+=0.15;if(this.sy>=-1)this.ex=true}dr(){ctx.fillStyle=this.c;ctx.beginPath();ctx.arc(this.x,this.y,3,0,Math.PI*2);ctx.fill()}}let fs=[];function an(){ctx.clearRect(0,0,canvas.width,canvas.height);if(Math.random()<0.05)fs.push(new F());fs.forEach((f,i)=>{f.up();f.dr();if(f.ex)fs.splice(i,1)});requestAnimationFrame(an)}an();</script>""")

def start_cyber_rain():
    chars = ["$", "0", "1", "🥂", "✨", "💎", "🍑" , "2", "0", "2", "6"]
    html_bits = '<div class="matrix-rain">'
    for i in range(60): # Ridotto leggermente per performance
        left = i * 1.6
        html_bits += f'<div class="bit" style="left:{left}%; color:#ff00ff; animation-duration:{random.uniform(2,5)}s;">{random.choice(chars)}</div>'
    st.markdown(html_bits + '</div>', unsafe_allow_html=True)

# --- LOGICA PRINCIPALE ---
def main():
    if 'state' not in st.session_state:
        st.session_state.state = 'login'

    placeholder = st.empty()

    # FASE 1: LOGIN
    if st.session_state.state == 'login':
        with placeholder.container():
            st.markdown("<h1 class='neon-text'>THE BACKDOOR</h1>", unsafe_allow_html=True)
            st.markdown("<p style='color:#ff00ff; text-align:center; font-family:Orbitron;'>SECURE VIP ENTRANCE // 2026</p>", unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns([1, 2, 1])
            with c2:
                # Tua immagine GIF originale
                st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1fe56053-597e-45b3-a3b1-f26197574147/deb1dq7-6605a031-5944-49cc-8beb-dba5e8284c4a.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiIvZi8xZmU1NjA1My01OTdlLTQ1YjMtYTNiMS1mMjYxOTc1NzQxNDcvZGViMWRxNy02NjA1YTAzMS01OTQ0LTQ5Y2MtOGJlYi1kYmE1ZTgyODRjNGEuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.QauebzGlSfy161JK86WvKTuhXb3OfmoXKdV7rOy-I8Y", use_container_width=True)
            
            play_audio_scene("scena1.mp3", main_loop=True) 
            
            pwd = st.text_input("ACCESS KEY:", type="password", key="login_pwd")
            if st.button("AUTHORIZE ENTRANCE"):
                if pwd.lower().strip() == "locandieri":
                    st.session_state.state = 'hacking'
                    st.rerun()
                else:
                    st.error("BOUNCER: 'You're not on the list.'")

    # FASE 2: HACKING
    elif st.session_state.state == 'hacking':
        with placeholder.container():
            # In questa fase carichiamo solo scena2.mp3
            play_audio_scene("scena2.mp3", main_loop=False)
            st.markdown("<h2 class='pink-neon'>OVERRIDING VIP SERVER...</h2>", unsafe_allow_html=True)
            log_area = st.empty()
            full_log = ""
            steps = [
                ("> Initializing 'Seductive_Handshake'...", 1.5), 
                ("> Bypassing IDS/IPS...", 1.5), 
                ("> Deep Packet Inspection (DPI)...", 2.0), 
                ("> Privilege Escalation: ROOT granted.", 1.5), 
                ("> Executing HappyNewYear.exe...", 1.2)
            ]
            for text, delay in steps:
                full_log += f"<div class='terminal-text'>{text}</div>"
                log_area.markdown(full_log, unsafe_allow_html=True)
                time.sleep(delay)
            st.session_state.state = 'party'
            st.rerun()

    # FASE 3: PARTY
    elif st.session_state.state == 'party':
        with placeholder.container():
            # Qui carichiamo musica.mp3 e fuochi.mp3
            play_audio_scene("musica.mp3", bg_file="fuochi.mp3", main_loop=False, bg_loop=True, bg_volume=0.25)
            show_real_fireworks()
            start_cyber_rain()

            st.markdown("<div style='text-align: center; position: relative; z-index: 10;'><h1 style='color: white; font-family: Orbitron; font-size: 50px; text-shadow: 0 0 20px #ff00ff;'>2026 UNLOCKED</h1></div>", unsafe_allow_html=True)
            
            if os.path.exists("ascii.png"):
                st.image("ascii.png", use_container_width=True)
            
            st.success("🥂 BUON ANNO, LOCANDIERI! 🥂")
            
            if os.path.exists("foto.png"):
                st.image("foto.png", use_container_width=True)
            
            if st.button("TERMINATE CONNECTION"):
                st.session_state.state = 'login'
                st.rerun()

if __name__ == "__main__":
    main()
