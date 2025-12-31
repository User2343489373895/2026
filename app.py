import streamlit as st
import time
import os
import base64
import random
import streamlit.components.v1 as components

# 1. Configurazione
st.set_page_config(page_title="NEON_OVERRIDE_2026", page_icon="📟", layout="centered")

# --- CSS GLOBALE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Fira+Code&display=swap');
    .stApp { background-color: #050505 !important; }
    header, footer, #MainMenu {visibility: hidden;}
    
    .neon-text { font-family: 'Orbitron', sans-serif; color: #00ffff; text-shadow: 0 0 10px #00ffff; text-align: center; position: relative; z-index: 10; }
    .pink-neon { color: #ff00ff; text-shadow: 0 0 10px #ff00ff; font-family: 'Orbitron', sans-serif; text-align: center; font-size: 24px; position: relative; z-index: 10; }
    
    .terminal-text {
        font-family: 'Fira Code', monospace; color: #00ff41; font-size: 14px;
        background: rgba(0, 255, 65, 0.1); padding: 15px; border-left: 3px solid #00ff41; margin-bottom: 5px;
    }
    
    /* Pioggia di Bit */
    .matrix-rain { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 1; opacity: 0.3; }
    .bit { position: absolute; top: -30px; font-family: monospace; font-size: 20px; animation: fall linear infinite; }
    @keyframes fall { to { transform: translateY(110vh); } }
    
    /* Bottone */
    div.stButton > button {
        background-color: transparent !important; color: #ff00ff !important; border: 2px solid #ff00ff !important;
        font-family: 'Orbitron', sans-serif !important; width: 100%; box-shadow: 0 0 10px #ff00ff; height: 50px;
        position: relative; z-index: 100;
    }

    /* FIX DEFINITIVO PER I FUOCHI A TUTTO SCHERMO */
    .fireworks-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 5; /* Sopra la pioggia di bit, sotto il testo */
        pointer-events: none;
    }
    iframe {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw !important;
        height: 100vh !important;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNZIONE FUOCHI D'ARTIFICIO "PRO" ---
def show_real_fireworks():
    # JavaScript per creare un sistema di fuochi d'artificio su Canvas
    components.html(
        """
        <canvas id="fireworksCanvas"></canvas>
        <style>
            body { margin: 0; overflow: hidden; background: transparent; }
            canvas { display: block; background: transparent; }
        </style>
        <script>
            const canvas = document.getElementById('fireworksCanvas');
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;

            class Firework {
                constructor() {
                    this.x = Math.random() * canvas.width;
                    this.y = canvas.height;
                    this.sx = Math.random() * 3 - 1.5;
                    this.sy = Math.random() * -3 - 7;
                    this.size = 2;
                    this.color = `hsl(${Math.random() * 360}, 100%, 50%)`;
                    this.shouldExplode = false;
                }
                update() {
                    this.x += this.sx;
                    this.y += this.sy;
                    this.sy += 0.1; // Gravità
                    if (this.sy >= -1) this.shouldExplode = true;
                }
                draw() {
                    ctx.fillStyle = this.color;
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                    ctx.fill();
                }
            }

            class Particle {
                constructor(x, y, color) {
                    this.x = x;
                    this.y = y;
                    this.sx = Math.random() * 6 - 3;
                    this.sy = Math.random() * 6 - 3;
                    this.life = 100;
                    this.color = color;
                }
                update() {
                    this.x += this.sx;
                    this.y += this.sy;
                    this.life -= 1.5;
                }
                draw() {
                    ctx.globalAlpha = this.life / 100;
                    ctx.fillStyle = this.color;
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, 2, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.globalAlpha = 1;
                }
            }

            let fireworks = [];
            let particles = [];

            function animate() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                if (Math.random() < 0.05) fireworks.push(new Firework());

                fireworks.forEach((f, i) => {
                    f.update();
                    f.draw();
                    if (f.shouldExplode) {
                        for (let j = 0; j < 50; j++) particles.push(new Particle(f.x, f.y, f.color));
                        fireworks.splice(i, 1);
                    }
                });

                particles.forEach((p, i) => {
                    p.update();
                    p.draw();
                    if (p.life <= 0) particles.splice(i, 1);
                });

                requestAnimationFrame(animate);
            }
            animate();
        </script>
        """,
        height=1000, # Valore alto per forzare l'altezza dell'iframe
    )

def play_audio(file_name):
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            md = f"""<audio autoplay="true" style="display:none;"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>"""
            components.html(md, height=0, width=0)

def start_cyber_rain():
    chars = ["$", "0", "1", "🥂", "🍑", "✨"]
    html_bits = '<div class="matrix-rain">'
    for i in range(80):
        left = i * 1.25
        duration = random.uniform(2, 5)
        color = "#ff00ff" if i % 2 == 0 else "#00ffff"
        char = random.choice(chars)
        html_bits += f'<div class="bit" style="left:{left}%; color:{color}; animation-duration:{duration}s;">{char}</div>'
    html_bits += '</div>'
    st.markdown(html_bits, unsafe_allow_html=True)

# --- LOGICA PRINCIPALE ---
if 'state' not in st.session_state:
    st.session_state.state = 'login'

placeholder = st.empty()

# FASE 1: LOGIN
if st.session_state.state == 'login':
    with placeholder.container():
        st.markdown("<h1 class='neon-text'>THE BACKDOOR</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#ff00ff; text-align:center; font-family:Orbitron;'>SECURE VIP ENTRANCE // 2026</p>", unsafe_allow_html=True)
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3ZidW5pZ3MwaHh6OHZidW5pZ3MwaHh6OHZidW5pZ3MwaHh6OHZidW5pZ3MmZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PWc/3o7TKVUn7iM8FMEU24/giphy.gif")
        pwd = st.text_input("ACCESS KEY:", type="password")
        if st.button("BYPASS FIREWALL"):
            if pwd.lower().strip() == "locandieri":
                st.session_state.state = 'hacking'
                placeholder.empty()
                st.rerun()
            else:
                st.error("ACCESS DENIED")

# FASE 2: HACKING
elif st.session_state.state == 'hacking':
    with placeholder.container():
        play_audio("modem.mp3")
        st.markdown("<h2 class='pink-neon'>OVERRIDING VIP SERVER...</h2>", unsafe_allow_html=True)
        log_area = st.empty()
        full_log = ""
        steps = [
            ("> Initializing 'Seductive_Handshake' protocol...", 1.2),
            ("> Bypassing IDS/IPS (Intrusion Desire System)...", 1.5),
            ("> Deep Packet Inspection of 'Private_Area'...", 1.8),
            ("> Escalating privileges to 'GOD_MODE'...", 1.5),
            ("> Extracting 'Secret_Payload_2026.bin'...", 2.0),
            ("> SUCCESS: System compromised.", 1.0),
        ]
        for text, delay in steps:
            full_log += f"<div class='terminal-text'>{text}</div>"
            log_area.markdown(full_log, unsafe_allow_html=True)
            time.sleep(delay)
        st.session_state.state = 'party'
        placeholder.empty()
        st.rerun()

# FASE 3: PARTY FINALE
elif st.session_state.state == 'party':
    with placeholder.container():
        # L'ordine è importante: i fuochi devono essere renderizzati
        show_real_fireworks()
        start_cyber_rain()
        play_audio("musica.mp3")

        st.markdown("""
            <div style='text-align: center;'>
                <h1 style='color: white; font-family: Orbitron; font-size: 50px; text-shadow: 0 0 20px #ff00ff;'>2026 UNLOCKED</h1>
                <p style='color: #00ffff; font-family: Orbitron; font-size: 20px;'>The backdoor is open. Enjoy the show.</p>
            </div>
            """, unsafe_allow_html=True)

        if os.path.exists("ascii.png"):
            st.image("ascii.png", use_container_width=True)
        
        st.success("BUON ANNO, LOCANDIERI! 🥂🔥")

        if os.path.exists("foto.png"):
            st.image("foto.png", caption="THE CREW", use_container_width=True)
        
        if st.button("TERMINATE CONNECTION"):
            st.session_state.state = 'login'
            placeholder.empty()
            st.rerun()
