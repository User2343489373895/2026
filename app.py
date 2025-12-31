import streamlit as st
import time
import os
import base64
import random
import streamlit.components.v1 as components

# 1. Configurazione (Deve essere la prima)
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

# --- CSS ORIGINALE RIPRISTINATO E FIXATO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Fira+Code&display=swap');
    
    .stApp { background-color: #050505 !important; }
    header, footer, #MainMenu {visibility: hidden;}
    
    .center-box { text-align: center; width: 100%; display: block; margin: 0 auto; }

    .pink-neon { 
        color: #ff00ff; 
        text-shadow: 0 0 15px #ff00ff; 
        font-family: 'Orbitron', sans-serif; 
        font-size: clamp(24px, 8vw, 60px); 
        font-weight: 900; 
        line-height: 1.2;
        margin-bottom: 5px;
    }

    .cyan-sub {
        color: #00ffff;
        text-shadow: 0 0 8px #00ffff;
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(14px, 4vw, 22px);
        font-weight: bold;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    /* 2026 UNLOCKED - Ridotto leggermente per non rompere tutto */
    .unlocked-title {
        color: white; 
        font-family: 'Orbitron', sans-serif; 
        font-size: clamp(35px, 12vw, 100px); /* Ridotto il max da 160 a 100 */
        text-shadow: 0 0 20px #ff00ff, 0 0 50px #ff00ff;
        line-height: 1;
        margin: 20px 0;
        text-align: center;
    }

    /* BOX BUON ANNO - White-space nowrap per non spezzarlo */
    .custom-success-box {
        background-color: rgba(0, 255, 65, 0.1);
        border: 2px solid #00ff41;
        color: #00ff41;
        border-radius: 12px;
        padding: 20px;
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(16px, 5vw, 35px);
        font-weight: bold;
        text-shadow: 0 0 15px #00ff41;
        width: 100%;
        text-align: center;
        margin: 15px 0;
        white-space: nowrap; /* EVITA CHE VENGA SPEZZATO */
    }

    .terminal-text {
        font-family: 'Fira Code', monospace; 
        color: #00ff41; 
        font-size: 14px;
        background: rgba(0, 255, 65, 0.1); 
        padding: 10px; 
        border-left: 3px solid #00ff41; 
        margin-bottom: 5px;
    }

    /* Matrix Rain Anim */
    @keyframes fall { to { transform: translateY(110vh); } }
    </style>
    """, unsafe_allow_html=True)

# --- EFFETTI PARTY (FUOCHI D'ARTIFICIO E RAIN) ---
def show_party_visuals():
    # Rain di emoji (Solo fase party)
    chars = ["0", "1", "🥂", "🍸","🚬", "✨", "💎", "💰", "🍑", "🔞" , "2", "0", "2", "6"]
    rain_html = '<div style="position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:1; opacity:0.3;">'
    for i in range(30):
        left = i * 3.3
        rain_html += f'<div style="position:absolute; left:{left}%; top:-50px; color:#ff00ff; font-family:monospace; animation: fall {random.uniform(2,5)}s linear infinite;">{random.choice(chars)}</div>'
    st.markdown(rain_html + '</div>', unsafe_allow_html=True)
    
    # Fuochi d'Artificio Migliorati
    components.html("""
    <canvas id="fireworks" style="position:fixed; top:0; left:0; width:100vw; height:100vh; pointer-events:none; z-index:9999;"></canvas>
    <script>
    const canvas = document.getElementById('fireworks');
    const ctx = canvas.getContext('2d');
    let w = canvas.width = window.innerWidth;
    let h = canvas.height = window.innerHeight;
    let particles = [];
    let fw = [];

    class Firework {
        constructor() {
            this.x = Math.random() * w;
            this.y = h;
            this.sx = Math.random() * 2 - 1;
            this.sy = Math.random() * -3 - 7;
            this.color = `hsl(${Math.random()*360}, 100%, 60%)`;
        }
        update() {
            this.x += this.sx; this.y += this.sy;
            this.sy += 0.1;
            if(this.sy >= 0) {
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
        constructor(x,y,color) {
            this.x = x; this.y = y; this.color = color;
            this.dx = Math.random() * 6 - 3;
            this.dy = Math.random() * 6 - 3;
            this.life = 1.0;
        }
        update() {
            this.x += this.dx; this.y += this.dy;
            this.dy += 0.05; this.life -= 0.02;
        }
        draw() {
            ctx.globalAlpha = this.life;
            ctx.fillStyle = this.color;
            ctx.beginPath(); ctx.arc(this.x, this.y, 2, 0, Math.PI*2); ctx.fill();
        }
    }

    function loop() {
        ctx.clearRect(0,0,w,h);
        if(Math.random() < 0.04) fw.push(new Firework());
        fw = fw.filter(f => {
            f.draw();
            return f.update();
        });
        particles = particles.filter(p => {
            p.draw();
            p.update();
            return p.life > 0;
        });
        requestAnimationFrame(loop);
    }
    loop();
    window.addEventListener('resize', () => { w = canvas.width = window.innerWidth; h = canvas.height = window.innerHeight; });
    </script>
    """, height=0)

# --- AUDIO ---
def play_audio(file_name, loop=False):
    b64 = get_audio_b64(file_name)
    if b64:
        loop_attr = "loop" if loop else ""
        components.html(f"""<audio autoplay="true" {loop_attr}><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>""", height=0)

# --- LOGICA NAVIGAZIONE ---
if 'state' not in st.session_state:
    st.session_state.state = 'login'

# Questo container serve a svuotare la pagina ad ogni cambio stato
main_container = st.empty()

if st.session_state.state == 'login':
    with main_container.container():
        st.markdown("<div class='center-box'><div class='pink-neon'>THE BACKDOOR</div><div class='cyan-sub'>SECURE VIP ENTRANCE</div></div>", unsafe_allow_html=True)
        st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1fe56053-597e-45b3-a3b1-f26197574147/deb1dq7-6605a031-5944-49cc-8beb-dba5e8284c4a.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiIvZi8xZmU1NjA1My01OTdlLTQ1YjMtYTNiMS1mMjYxOTc1NzQxNDcvZGViMWRxNy02NjA1YTAzMS01OTQ0LTQ5Y2MtOGJlYi1kYmE1ZTgyODRjNGEuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.QauebzGlSfy161JK86WvKTuhXb3OfmoXKdV7rOy-I8Y", use_container_width=True)
        play_audio("scena1.mp3", loop=True)
        
        pwd = st.text_input("ACCESS KEY:", type="password")
        if st.button("AUTHORIZE ENTRANCE"):
            if pwd.lower().strip() == "locandieri":
                st.session_state.state = 'hacking'
                st.rerun()
            else:
                st.error("ACCESS DENIED")

elif st.session_state.state == 'hacking':
    with main_container.container():
        play_audio("scena2.mp3")
        st.markdown("<div class='pink-neon'>OVERRIDING VIP SERVER...</div>", unsafe_allow_html=True)
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
    # 1. Fuochi e pioggia (vengono renderizzati come componenti separati)
    show_party_visuals()
    
    with main_container.container():
        play_audio("musica.mp3", loop=True)
        
        # ASCII IMAGE
        if os.path.exists("ascii.png"):
            st.image("ascii.png", use_container_width=True)
        
        # TITOLO 2026 UNLOCKED
        st.markdown("<div class='unlocked-title'>2026 UNLOCKED</div>", unsafe_allow_html=True)
        
        # BOX BUON ANNO (Ora non si spezza)
        st.markdown("<div class='custom-success-box'>🥂 BUON ANNO, LOCANDIERI! 🥂</div>", unsafe_allow_html=True)
        
        # FOTO FINALE
        if os.path.exists("foto.png"):
            st.image("foto.png", use_container_width=True)
            
        if st.button("TERMINATE CONNECTION"):
            st.session_state.state = 'login'
            st.rerun()
