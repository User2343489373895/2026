import streamlit as st
import time
import os
import base64
import random
import streamlit.components.v1 as components

# 1. Configurazione Iniziale
st.set_page_config(page_title="Exclusive VIP Lounge 2026", page_icon="🔞", layout="centered")

# --- CACHE AUDIO ---
@st.cache_data
def get_audio_b64(file_path):
    if file_path and os.path.exists(file_path):
        try:
            with open(file_path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        except: return None
    return None

# --- CSS GLOBALE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Fira+Code&display=swap');
    
    .stApp { background-color: #050505 !important; }
    header, footer, #MainMenu {visibility: hidden;}

    /* Box Titoli */
    .pink-neon { 
        color: #ff00ff; 
        text-shadow: 0 0 15px #ff00ff; 
        font-family: 'Orbitron', sans-serif; 
        font-size: clamp(22px, 6vw, 50px); 
        font-weight: 900; 
        text-align: center;
        margin-bottom: 10px;
    }

    /* 2026 UNLOCKED - Ridimensionato per non rompere il layout */
    .unlocked-title {
        color: white; 
        font-family: 'Orbitron', sans-serif; 
        font-size: clamp(30px, 10vw, 75px); 
        text-shadow: 0 0 20px #ff00ff;
        text-align: center;
        font-weight: 900;
        margin: 10px 0;
        line-height: 1.2;
    }

    /* BOX BUON ANNO - Più largo e font adattivo per stare su una riga */
    .custom-success-box {
        background-color: rgba(0, 255, 65, 0.15);
        border: 2px solid #00ff41;
        color: #00ff41;
        border-radius: 8px;
        padding: 15px;
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(14px, 4vw, 28px);
        font-weight: bold;
        text-shadow: 0 0 10px #00ff41;
        width: 100%;
        text-align: center;
        white-space: nowrap; /* Impedisce di andare a capo */
        margin: 20px 0;
    }

    .terminal-text {
        font-family: 'Fira Code', monospace; 
        color: #00ff41; 
        font-size: 14px;
        background: rgba(0, 255, 65, 0.05); 
        padding: 8px; 
        border-left: 3px solid #00ff41; 
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- EFFETTI VISIVI (Solo per la fase Party) ---
def show_fireworks_and_rain():
    # Matrix rain di simboli
    chars = ["0", "1", "🥂", "🍸","🚬", "✨", "💎", "💰", "🍑", "🔞" , "2", "0", "2", "6"]
    rain_html = '<div style="position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:1; opacity:0.3;">'
    for i in range(20):
        left = i * 5
        rain_html += f'<div style="position:absolute; left:{left}%; top:-50px; color:#ff00ff; font-size:20px; animation: fall {random.uniform(2,5)}s linear infinite;">{random.choice(chars)}</div>'
    st.markdown(rain_html + '</div><style>@keyframes fall { to { transform: translateY(110vh); } }</style>', unsafe_allow_html=True)
    
    # Fuochi d'artificio JS (Canvas Overlay)
    components.html("""
    <canvas id="f" style="position:fixed; top:0; left:0; width:100vw; height:100vh; pointer-events:none; z-index:999;"></canvas>
    <script>
    const c = document.getElementById('f');
    const x = c.getContext('2d');
    let w = c.width = window.innerWidth;
    let h = c.height = window.innerHeight;
    let dots = [];

    class Firework {
        constructor() {
            this.x = Math.random() * w;
            this.y = h;
            this.targetY = Math.random() * (h/2);
            this.speed = Math.random() * 3 + 5;
            this.color = `hsl(${Math.random()*360}, 100%, 50%)`;
            this.exploded = false;
        }
        update() {
            if(!this.exploded) {
                this.y -= this.speed;
                if(this.y <= this.targetY) {
                    this.exploded = true;
                    this.createParticles();
                }
            }
        }
        createParticles() {
            for(let i=0; i<30; i++) {
                dots.push(new Particle(this.x, this.y, this.color));
            }
        }
    }

    class Particle {
        constructor(x,y,color) {
            this.x = x; this.y = y; this.color = color;
            this.vx = Math.random() * 4 - 2;
            this.vy = Math.random() * 4 - 2;
            this.alpha = 1;
        }
        update() {
            this.x += this.vx; this.y += this.vy;
            this.vy += 0.05; this.alpha -= 0.02;
        }
    }

    let fws = [];
    function anim() {
        x.clearRect(0,0,w,h);
        if(Math.random() < 0.05) fws.push(new Firework());
        fws.forEach((f,i) => {
            f.update();
            x.fillStyle = f.color;
            if(!f.exploded) x.fillRect(f.x, f.y, 3, 3);
            else fws.splice(i,1);
        });
        dots.forEach((d,i) => {
            d.update();
            x.globalAlpha = d.alpha;
            x.fillStyle = d.color;
            x.fillRect(d.x, d.y, 2, 2);
            if(d.alpha <= 0) dots.splice(i,1);
        });
        requestAnimationFrame(anim);
    }
    anim();
    </script>
    """, height=0)

# --- LOGICA APPLICAZIONE ---
def main():
    if 'state' not in st.session_state:
        st.session_state.state = 'login'

    # Placeholder principale per evitare sovrapposizioni
    placeholder = st.empty()

    if st.session_state.state == 'login':
        with placeholder.container():
            st.markdown("<div class='pink-neon'>THE BACKDOOR</div>", unsafe_allow_html=True)
            st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1fe56053-597e-45b3-a3b1-f26197574147/deb1dq7-6605a031-5944-49cc-8beb-dba5e8284c4a.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiIvZi8xZmU1NjA1My01OTdlLTQ1YjMtYTNiMS1mMjYxOTc1NzQxNDcvZGViMWRxNy02NjA1YTAzMS01OTQ0LTQ5Y2MtOGJlYi1kYmE1ZTgyODRjNGEuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.QauebzGlSfy161JK86WvKTuhXb3OfmoXKdV7rOy-I8Y", use_container_width=True)
            
            play_audio("scena1.mp3", loop=True)
            pwd = st.text_input("ACCESS KEY:", type="password", key="login_pwd")
            if st.button("AUTHORIZE ENTRANCE"):
                if pwd.lower().strip() == "locandieri":
                    st.session_state.state = 'hacking'
                    st.rerun()
                else: st.error("ACCESS DENIED")

    elif st.session_state.state == 'hacking':
        with placeholder.container():
            play_audio("scena2.mp3")
            st.markdown("<div class='pink-neon'>OVERRIDING SYSTEM...</div>", unsafe_allow_html=True)
            log_area = st.empty()
            lines = [
                ("> Initializing 'Seductive_Handshake' protocol...", 1.2), 
                ("> Bypassing IDS/IPS (Intrusion Desire System)...", 1.5), 
                ("> Deep Packet Inspection of 'Private_Area'...", 1.8), 
                ("> Escalating privileges: Root granted.", 1.5), 
                ("> Extracting 'Secret_Payload.bin'...", 2.0), 
                ("> SUCCESS: Access granted.", 1.2), 
                ("> WELCOME!", 1.5)
            ]
            full_text = ""
            for line in lines:
                full_text += f"<div class='terminal-text'>{line}</div>"
                log_area.markdown(full_text, unsafe_allow_html=True)
                time.sleep(0.8)
            st.session_state.state = 'party'
            st.rerun()

    elif st.session_state.state == 'party':
        # Qui chiamiamo i visual (fuochi e rain)
        show_fireworks_and_rain()
        
        with placeholder.container():
            play_audio("musica.mp3", loop=True)
            
            # Titolo Ridimensionato
            st.markdown("<div class='unlocked-title'>2026 UNLOCKED</div>", unsafe_allow_html=True)
            
            # Box Buon Anno che non va a capo
            st.markdown("<div class='custom-success-box'>🥂 BUON ANNO, LOCANDIERI! 🥂</div>", unsafe_allow_html=True)
            
            # Immagine finale se esiste
            if os.path.exists("foto.png"):
                st.image("foto.png", use_container_width=True)
            else:
                st.info("Aggiungi 'foto.png' per vederla qui!")

            if st.button("LOGOUT"):
                st.session_state.state = 'login'
                st.rerun()

# Funzione Audio helper
def play_audio(file_name, loop=False):
    b64 = get_audio_b64(file_name)
    if b64:
        loop_attr = "loop" if loop else ""
        components.html(f"""<audio autoplay="true" {loop_attr}><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>""", height=0)

if __name__ == "__main__":
    main()
