import streamlit as st
import time
import os
import base64
import random
import streamlit.components.v1 as components

# 1. Configurazione (Prima di tutto)
st.set_page_config(page_title="Exclusive VIP Lounge 💎", page_icon="🔞", layout="centered")

# --- CACHE AUDIO ---
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

# --- CSS GLOBALE (Risolve Spazi e Allineamento) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Fira+Code&display=swap');
    
    /* Rimuove lo spazio bianco in alto */
    .block-container { padding-top: 0rem !important; }
    .stApp { background-color: #050505 !important; }
    header, footer, #MainMenu {visibility: hidden;}

    /* Titoli Hacker */
    .pink-neon { 
        color: #ff00ff; text-shadow: 0 0 15px #ff00ff; 
        font-family: 'Orbitron', sans-serif; font-size: clamp(24px, 8vw, 55px); 
        font-weight: 900; text-align: center; margin-top: 20px;
    }
    .cyan-sub {
        color: #00ffff; text-shadow: 0 0 8px #00ffff;
        font-family: 'Orbitron', sans-serif; font-size: clamp(12px, 4vw, 20px);
        font-weight: bold; text-align: center; letter-spacing: 2px; text-transform: uppercase;
    }

    /* 2026 UNLOCKED - Centrato e proporzionato */
    .unlocked-title {
        color: white; font-family: 'Orbitron', sans-serif; 
        font-size: clamp(38px, 12vw, 90px); 
        text-shadow: 0 0 20px #ff00ff, 0 0 40px #ff00ff;
        font-weight: 900; text-align: center;
        width: 100%; margin: 20px 0; line-height: 1.1;
    }

    /* BUON ANNO LOCANDIERI - Box robusto che non si storce */
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
        max-width: 700px;
        margin: 20px auto;
        text-align: center;
        display: flex; justify-content: center; align-items: center;
        box-sizing: border-box;
    }

    .terminal-text {
        font-family: 'Fira Code', monospace; color: #00ff41; font-size: 14px;
        background: rgba(0, 255, 65, 0.05); padding: 12px; border-left: 3px solid #00ff41; 
        margin-bottom: 5px; text-align: left;
    }

    /* Animazione Fall */
    @keyframes fall { to { transform: translateY(110vh); } }
    </style>
    """, unsafe_allow_html=True)

# --- LOGICA DI NAVIGAZIONE ---
if 'state' not in st.session_state:
    st.session_state.state = 'login'

# Placeholder unico: pulisce TUTTO ad ogni cambio stato
placeholder = st.empty()

# --- 1. LOGIN ---
if st.session_state.state == 'login':
    with placeholder.container():
        st.markdown("<div class='pink-neon'>THE BACKDOOR</div><div class='cyan-sub'>SECURE VIP ENTRANCE</div>", unsafe_allow_html=True)
        st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1fe56053-597e-45b3-a3b1-f26197574147/deb1dq7-6605a031-5944-49cc-8beb-dba5e8284c4a.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiIvZi8xZmU1NjA1My01OTdlLTQ1YjMtYTNiMS1mMjYxOTc1NzQxNDcvZGViMWRxNy02NjA1YTAzMS01OTQ0LTQ5Y2MtOGJlYi1kYmE1ZTgyODRjNGEuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.QauebzGlSfy161JK86WvKTuhXb3OfmoXKdV7rOy-I8Y", use_container_width=True)
        play_audio("scena1.mp3", loop=True)
        pwd = st.text_input("ACCESS KEY:", type="password")
        if st.button("AUTHORIZE ENTRANCE"):
            if pwd.lower().strip() == "locandieri":
                st.session_state.state = 'hacking'
                st.rerun()

# --- 2. HACKING ---
elif st.session_state.state == 'hacking':
    with placeholder.container():
        play_audio("scena2.mp3")
        st.markdown("<div class='pink-neon'>OVERRIDING VIP SERVER...</div>", unsafe_allow_html=True)
        log_area = st.empty()
        full_log = ""
        logs = [
                ("> Initializing 'Seductive_Handshake' protocol...", 1.2), 
                ("> Bypassing IDS/IPS (Intrusion Desire System)...", 1.5), 
                ("> Deep Packet Inspection of 'Private_Area'...", 1.8), 
                ("> Escalating privileges: Root granted.", 1.5), 
                ("> Extracting 'Secret_Payload.bin'...", 2.0), 
                ("> SUCCESS: Access granted.", 1.2), 
                ("> WELCOME!", 1.5)
        ]
        for line, delay in logs:
            full_log += f"<div class='terminal-text'>{line}</div>"
            log_area.markdown(full_log, unsafe_allow_html=True)
            time.sleep(delay)
        st.session_state.state = 'party'
        st.rerun()

# --- 3. PARTY (PAGINA FINALE) ---
elif st.session_state.state == 'party':
    # VISUALS (Fuochi + Pioggia) - Caricati solo qui dentro
    components.html("""
    <div id="visuals" style="position:fixed; top:0; left:0; width:100vw; height:100vh; pointer-events:none; z-index:9999;">
        <canvas id="fw"></canvas>
    </div>
    <script>
    const canvas = document.getElementById('fw');
    const ctx = canvas.getContext('2d');
    let w = canvas.width = window.innerWidth;
    let h = canvas.height = window.innerHeight;
    let particles = [];
    let rockets = [];

    class Rocket {
        constructor() {
            this.x = Math.random() * w;
            this.y = h; // Parte esattamente dal basso
            this.sy = Math.random() * -3 - 8; // Velocità verso l'alto
            this.color = `hsl(${Math.random() * 360}, 100%, 60%)`;
        }
        update() {
            this.y += this.sy;
            this.sy += 0.1; // Gravità che rallenta il razzo
            if (this.sy >= 0) { // Al culmine esplode
                for(let i=0; i<40; i++) particles.push(new Particle(this.x, this.y, this.color));
                return false;
            }
            return true;
        }
        draw() {
            ctx.fillStyle = this.color;
            ctx.beginPath(); ctx.arc(this.x, this.y, 3, 0, Math.PI*2); ctx.fill();
        }
    }

    class Particle {
        constructor(x, y, color) {
            this.x = x; this.y = y; this.color = color;
            this.dx = Math.random() * 6 - 3;
            this.dy = Math.random() * 6 - 3;
            this.alpha = 1;
        }
        update() {
            this.x += this.dx; this.y += this.dy;
            this.dy += 0.05; this.alpha -= 0.015;
        }
        draw() {
            ctx.globalAlpha = this.alpha;
            ctx.fillStyle = this.color;
            ctx.beginPath(); ctx.arc(this.x, this.y, 2.5, 0, Math.PI*2); ctx.fill();
        }
    }

    function anim() {
        ctx.clearRect(0, 0, w, h);
        if (Math.random() < 0.06) rockets.push(new Rocket());
        rockets = rockets.filter(r => { r.draw(); return r.update(); });
        particles = particles.filter(p => { p.draw(); p.update(); return p.alpha > 0; });
        requestAnimationFrame(anim);
    }
    anim();
    </script>
    """, height=0)

    with placeholder.container():
        # Pioggia Emoji (Renderizzata SOLO qui)
        chars = ["0", "1", "🥂", "🍸","🚬", "✨", "💎", "💰", "🍑", "🔞" , "2", "0", "2", "6"]
        rain_html = '<div style="position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:0; opacity:0.3;">'
        for i in range(25):
            left = i * 4
            rain_html += f'<div style="position:absolute; left:{left}%; top:-50px; color:#ff00ff; font-size:24px; animation: fall {random.uniform(2,5)}s linear infinite;">{random.choice(chars)}</div>'
        st.markdown(rain_html + "</div>", unsafe_allow_html=True)

        play_audio("musica.mp3", loop=True)
        
        if os.path.exists("ascii.png"):
            st.image("ascii.png", use_container_width=True)
        
        # 2026 UNLOCKED
        st.markdown("<div class='unlocked-title'>2026 UNLOCKED</div>", unsafe_allow_html=True)
        
        # BUON ANNO LOCANDIERI
        st.markdown("<div class='custom-success-box'>🥂 BUON ANNO, LOCANDIERI! 🥂</div>", unsafe_allow_html=True)
        
        if os.path.exists("foto.png"):
            st.image("foto.png", use_container_width=True)
            
        if st.button("TERMINATE CONNECTION"):
            st.session_state.state = 'login'
            st.rerun()

