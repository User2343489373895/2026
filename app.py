import streamlit as st
import time
import os
import base64
import random
import streamlit.components.v1 as components

# 1. Configurazione (Deve essere la prima)
st.set_page_config(page_title="Exclusive VIP Lounge 2026 💎", page_icon="🔞", layout="centered")

# --- CACHE AUDIO ---
@st.cache_data
def get_audio_b64(file_path):
    if file_path and os.path.exists(file_path):
        try:
            with open(file_path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        except: return None
    return None

# --- CSS DEFINITIVO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Fira+Code&display=swap');
    
    /* App Background */
    .stApp { background-color: #050505 !important; overflow: hidden; }
    header, footer, #MainMenu {visibility: hidden;}
    
    /* Contenitore Testi Centrati */
    .center-box {
        text-align: center;
        width: 100%;
        z-index: 10;
        position: relative;
    }

    /* THE BACKDOOR (PINK) */
    .pink-neon { 
        color: #ff00ff; 
        text-shadow: 0 0 15px #ff00ff, 0 0 30px #ff00ff; 
        font-family: 'Orbitron', sans-serif; 
        font-size: clamp(24px, 8vw, 60px); 
        font-weight: 900; 
        margin-bottom: 5px;
    }

    /* 2026 UNLOCKED - GLOW ANIMATION */
    .unlocked-title {
        color: #ffffff; 
        font-family: 'Orbitron', sans-serif; 
        font-size: clamp(40px, 15vw, 120px); 
        font-weight: 900;
        text-transform: uppercase;
        text-align: center;
        line-height: 0.9;
        margin: 20px 0;
        z-index: 10;
        position: relative;
        text-shadow: 0 0 20px #ff00ff, 0 0 40px #ff00ff, 0 0 60px #00ffff;
        animation: pulse 2s infinite alternate;
    }

    @keyframes pulse {
        from { transform: scale(1); text-shadow: 0 0 20px #ff00ff; }
        to { transform: scale(1.05); text-shadow: 0 0 40px #ff00ff, 0 0 70px #00ffff; }
    }

    /* BOX BUON ANNO - NEON GREEN */
    .custom-success-box {
        background: rgba(0, 255, 65, 0.1);
        border: 3px solid #00ff41;
        box-shadow: 0 0 20px rgba(0, 255, 65, 0.5);
        color: #00ff41;
        border-radius: 15px;
        padding: 25px;
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(20px, 6vw, 45px);
        font-weight: bold;
        text-align: center;
        margin: 30px 0;
        z-index: 10;
        position: relative;
        text-transform: uppercase;
        letter-spacing: 3px;
    }

    .terminal-text {
        font-family: 'Fira Code', monospace; 
        color: #00ff41; 
        font-size: 14px;
        background: rgba(0, 0, 0, 0.7); 
        padding: 10px; 
        border-left: 3px solid #00ff41; 
        margin-bottom: 5px;
    }

    /* Fireworks Canvas Full Screen */
    #fCanvasContainer {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 1; /* Sotto i testi ma sopra il fondo */
        pointer-events: none;
    }
    
    div.stButton > button {
        background-color: rgba(255, 0, 255, 0.1) !important; 
        color: #ff00ff !important; 
        border: 2px solid #ff00ff !important;
        font-family: 'Orbitron', sans-serif !important; 
        width: 100%; 
        box-shadow: 0 0 15px #ff00ff;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #ff00ff !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNZIONI CORE ---
def play_audio(file_name, loop=False):
    b64 = get_audio_b64(file_name)
    if b64:
        loop_attr = "loop" if loop else ""
        components.html(f"""<audio autoplay="true" {loop_attr}><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>""", height=0)

def show_party_visuals():
    # Matrix rain di simboli party
    chars = ["0", "1", "🥂", "🍸","🚬", "✨", "💎", "💰", "🍑", "🔞" , "2", "0", "2", "6"]
    rain_html = '<div style="position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:2; opacity:0.4;">'
    for i in range(25):
        left = random.randint(0, 100)
        dur = random.uniform(2, 6)
        rain_html += f'<div style="position:absolute; left:{left}%; top:-50px; color:#ff00ff; font-family:monospace; font-size:24px; animation: fall {dur}s linear infinite;">{random.choice(chars)}</div>'
    st.markdown(rain_html + '</div><style>@keyframes fall { to { transform: translateY(110vh); } }</style>', unsafe_allow_html=True)
    
    # Fireworks Javascript
    components.html("""
    <div id="fCanvasContainer"><canvas id="canvas"></canvas></div>
    <script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    let particles = [];
    let fireworks = [];

    class Firework {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = canvas.height;
            this.sx = Math.random() * 3 - 1.5;
            this.sy = Math.random() * -3 - 7; // Velocità verso l'alto
            this.size = 3;
            this.color = `hsl(${Math.random() * 360}, 100%, 50%)`;
            this.done = false;
        }
        update() {
            this.x += this.sx;
            this.y += this.sy;
            this.sy += 0.1; // Gravità
            if (this.sy >= -1) { // Esplosione al culmine
                this.explode();
                this.done = true;
            }
        }
        draw() {
            ctx.fillStyle = this.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
        explode() {
            for (let i = 0; i < 50; i++) {
                particles.push(new Particle(this.x, this.y, this.color));
            }
        }
    }

    class Particle {
        constructor(x, y, color) {
            this.x = x;
            this.y = y;
            this.color = color;
            this.angle = Math.random() * Math.PI * 2;
            this.speed = Math.random() * 6 + 2;
            this.friction = 0.95;
            this.gravity = 0.1;
            this.alpha = 1;
            this.decay = Math.random() * 0.015 + 0.015;
        }
        update() {
            this.speed *= this.friction;
            this.x += Math.cos(this.angle) * this.speed;
            this.y += Math.sin(this.angle) * this.speed + this.gravity;
            this.alpha -= this.decay;
        }
        draw() {
            ctx.globalAlpha = this.alpha;
            ctx.fillStyle = this.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, 2, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    function animate() {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.2)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        if (Math.random() < 0.05) fireworks.push(new Firework());

        fireworks.forEach((fw, i) => {
            fw.update();
            fw.draw();
            if (fw.done) fireworks.splice(i, 1);
        });

        particles.forEach((p, i) => {
            p.update();
            p.draw();
            if (p.alpha <= 0) particles.splice(i, 1);
        });

        requestAnimationFrame(animate);
    }
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
    animate();
    </script>
    <style>#fCanvasContainer { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; pointer-events: none; }</style>
    """, height=0)

# --- LOGICA APPLICAZIONE ---
def main():
    if 'state' not in st.session_state:
        st.session_state.state = 'login'

    main_placeholder = st.empty()

    if st.session_state.state == 'login':
        with main_placeholder.container():
            st.markdown("<div class='center-box'><div class='pink-neon'>THE BACKDOOR</div><div style='color:#00ffff; font-family:Orbitron; letter-spacing:3px;'>SECURE VIP ENTRANCE</div></div>", unsafe_allow_html=True)
            
            st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1fe56053-597e-45b3-a3b1-f26197574147/deb1dq7-6605a031-5944-49cc-8beb-dba5e8284c4a.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiIvZi8xZmU1NjA1My01OTdlLTQ1YjMtYTNiMS1mMjYxOTc1NzQxNDcvZGViMWRxNy02NjA1YTAzMS01OTQ0LTQ5Y2MtOGJlYi1kYmE1ZTgyODRjNGEuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.QauebzGlSfy161JK86WvKTuhXb3OfmoXKdV7rOy-I8Y", use_container_width=True)
            
            play_audio("scena1.mp3", loop=True)
            pwd = st.text_input("ACCESS KEY:", type="password")
            if st.button("AUTHORIZE ENTRANCE"):
                if pwd.lower().strip() == "locandieri":
                    st.session_state.state = 'hacking'
                    st.rerun()
                else: st.error("ACCESS DENIED")

    elif st.session_state.state == 'hacking':
        with main_placeholder.container():
            play_audio("scena2.mp3", loop=False)
            st.markdown("<div class='center-box'><div class='pink-neon'>OVERRIDING VIP SERVER...</div></div>", unsafe_allow_html=True)
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
            for text, delay in steps:
                full_log += f"<div class='terminal-text'>{text}</div>"
                log_area.markdown(full_log, unsafe_allow_html=True)
                time.sleep(delay)
            st.session_state.state = 'party'
            st.rerun()

    elif st.session_state.state == 'party':
        show_party_visuals()
        with main_placeholder.container():
            play_audio("musica.mp3", loop=True)
            
            # Titolo Unlocked Gigante
            st.markdown("<div class='unlocked-title'>2026<br>UNLOCKED</div>", unsafe_allow_html=True)
            
            # Box Buon Anno
            st.markdown("<div class='custom-success-box'>🥂 BUON ANNO, LOCANDIERI! 🥂</div>", unsafe_allow_html=True)
            
            if os.path.exists("foto.png"): 
                st.image("foto.png", use_container_width=True)
            
            if st.button("TERMINATE CONNECTION"):
                st.session_state.state = 'login'
                st.rerun()

if __name__ == "__main__":
    main()
