import streamlit as st
import time
import os
import base64
import random
import streamlit.components.v1 as components

# 1. Configurazione Iniziale (Deve essere la prima istruzione)
st.set_page_config(page_title="Exclusive VIP Lounge 💎", page_icon="🔞", layout="centered")

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
        st.rerun()

# --- SCENA 3: PARTY ---
elif st.session_state.state == 'party':
    # 1. Fuochi d'Artificio JS (Canvas fisso sullo sfondo)
    components.html("""
    <canvas id="canvas" style="position:fixed; top:0; left:0; width:100vw; height:100vh; pointer-events:none; z-index:999;"></canvas>
    <script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    let w = canvas.width = window.innerWidth;
    let h = canvas.height = window.innerHeight;
    let fireworks = [];
    let particles = [];

    class Firework {
        constructor() {
            this.x = Math.random() * w;
            this.y = h; // Parte dal basso
            this.targetY = Math.random() * (h / 2.5);
            this.speed = Math.random() * 3 + 4;
            this.color = `hsl(${Math.random() * 360}, 100%, 60%)`;
            this.exploded = false;
        }
        update() {
            this.y -= this.speed;
            if (this.y <= this.targetY) {
                this.exploded = true;
                for (let i = 0; i < 40; i++) particles.push(new Particle(this.x, this.y, this.color));
            }
        }
        draw() {
            ctx.fillStyle = this.color;
            ctx.beginPath(); ctx.arc(this.x, this.y, 3, 0, Math.PI * 2); ctx.fill();
        }
    }

    class Particle {
        constructor(x, y, color) {
            this.x = x; this.y = y; this.color = color;
            this.vel = { x: Math.random() * 6 - 3, y: Math.random() * 6 - 3 };
            this.alpha = 1;
        }
        update() {
            this.x += this.vel.x; this.y += this.vel.y;
            this.vel.y += 0.05; // Gravità
            this.alpha -= 0.015;
        }
        draw() {
            ctx.globalAlpha = this.alpha;
            ctx.fillStyle = this.color;
            ctx.beginPath(); ctx.arc(this.x, this.y, 2, 0, Math.PI * 2); ctx.fill();
        }
    }

    function loop() {
        ctx.clearRect(0, 0, w, h);
        if (Math.random() < 0.06) fireworks.push(new Firework());
        fireworks = fireworks.filter(f => {
            f.update(); f.draw();
            return !f.exploded;
        });
        particles = particles.filter(p => {
            p.update(); p.draw();
            return p.alpha > 0;
        });
        requestAnimationFrame(loop);
    }
    loop();
    window.onresize = () => { w = canvas.width = window.innerWidth; h = canvas.height = window.innerHeight; };
    </script>
    """, height=0)

    # 2. Contenuto della Pagina
    with placeholder.container():
        play_audio("musica.mp3", loop=True)
        
        # Matrix Rain Emoji (Solo qui)
        chars = ["0", "1", "🥂", "🍸","🚬", "✨", "💎", "💰", "🍑", "🔞" , "2", "0", "2", "6"]
        rain_html = '<div style="position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:0; opacity:0.3;">'
        for i in range(25):
            left = i * 4
            rain_html += f'<div style="position:absolute; left:{left}%; top:-50px; color:#ff00ff; font-size:24px; animation: fall {random.uniform(2,5)}s linear infinite;">{random.choice(chars)}</div>'
        st.markdown(rain_html + '</div>', unsafe_allow_html=True)

        if os.path.exists("ascii.png"):
            st.image("ascii.png", use_container_width=True)
        
        st.markdown("<div class='unlocked-title'>2026 UNLOCKED</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='custom-success-box'>🥂 BUON ANNO, LOCANDIERI! 🥂</div>", unsafe_allow_html=True)
        
        if os.path.exists("foto.png"):
            st.image("foto.png", use_container_width=True)
            
        if st.button("TERMINATE CONNECTION"):
            st.session_state.state = 'login'
            st.rerun()
