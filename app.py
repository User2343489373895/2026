import streamlit as st
import time
import os
import base64
import random
import streamlit.components.v1 as components

# --- 1. Configurazione ---
st.set_page_config(page_title="Exclusive VIP Lounge 💎", page_icon="🔞", layout="centered")

# --- CACHE AUDIO ---
@st.cache_data
def get_audio_b64(file_path):
    if file_path and os.path.exists(file_path):
        try:
            with open(file_path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        except: 
            return None
    return None

# --- CSS GLOBALE ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Fira+Code&display=swap');
.stApp { background-color: #050505 !important; }
header, footer, #MainMenu {visibility: hidden;}

/* Titoli Neon */
.pink-neon { 
    color: #ff00ff; text-shadow: 0 0 15px #ff00ff, 0 0 30px #ff00ff; 
    font-family: 'Orbitron', sans-serif; font-size: clamp(24px, 8vw, 60px); 
    font-weight: 900; text-align: center; margin-top: 20px;
    line-height: 1.2;
}
.cyan-sub {
    color: #00ffff; text-shadow: 0 0 8px #00ffff;
    font-family: 'Orbitron', sans-serif; font-size: clamp(12px, 4vw, 22px);
    font-weight: bold; text-align: center; letter-spacing: 4px; 
    text-transform: uppercase; margin-bottom: 20px;
}

/* 2026 UNLOCKED */
.unlocked-title {
    color: white; font-family: 'Orbitron', sans-serif; 
    font-size: clamp(38px, 12vw, 90px); 
    text-shadow: 0 0 20px #ff00ff, 0 0 40px #ff00ff;
    font-weight: 900; text-align: center;
    width: 100%; margin: 20px 0; line-height: 1.1;
}

/* Box Buon Anno Custom */
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
    margin: 20px auto;
    text-align: center;
}

.terminal-text {
    font-family: 'Fira Code', monospace; color: #00ff41; font-size: 14px;
    background: rgba(0, 255, 65, 0.1); padding: 15px; border-left: 3px solid #00ff41; margin-bottom: 5px;
}

.matrix-rain { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 1; opacity: 0.3; }
.bit { position: absolute; top: -30px; font-family: monospace; font-size: 20px; animation: fall linear infinite; }
@keyframes fall { to { transform: translateY(110vh); } }

div.stButton > button {
    background-color: transparent !important; color: #ff00ff !important; border: 2px solid #ff00ff !important;
    font-family: 'Orbitron', sans-serif !important; width: 100%; box-shadow: 0 0 10px #ff00ff; height: 50px;
}

iframe { position: fixed; top: 0; left: 0; width: 100vw !important; height: 100vh !important; border: none; pointer-events: none; z-index: 5; }
</style>
""", unsafe_allow_html=True)

# --- FUNZIONI CORE ---

def play_audio(file_name, loop=False):
    b64 = get_audio_b64(file_name)
    if b64:
        loop_attr = "loop" if loop else ""
        # Script migliorato per forzare l'attivazione dopo il primo click dell'utente
        components.html(f"""
            <audio id="audio-player" {loop_attr}>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            <script>
                const audio = document.getElementById('audio-player');
                // Prova a farlo partire subito
                audio.play().catch(e => {{
                    console.log("Autoplay bloccato. In attesa di interazione.");
                    // Se bloccato, parte al primo click sulla pagina
                    window.parent.document.addEventListener('click', () => {{
                        audio.play();
                    }}, {{ once: true }});
                }});
            </script>
        """, height=0)

def show_party_visuals():
    chars = ["0", "1", "🥂", "🍸","🚬", "✨", "💎", "💰", "🍑", "🔞" , "2", "0", "2", "6"]
    rain_html = '<div class="matrix-rain">'
    for i in range(50):
        left = i * 2
        rain_html += f'<div class="bit" style="left:{left}%; color:#ff00ff; animation-duration:{random.uniform(2,5)}s;">{random.choice(chars)}</div>'
    st.markdown(rain_html + '</div>', unsafe_allow_html=True)

    components.html("""
    <canvas id="f"></canvas>
    <script>
    const c=document.getElementById('f'), ctx=c.getContext('2d');
    c.width=window.innerWidth; c.height=window.innerHeight;
    let particles=[], fireworks=[];

    class Particle {
        constructor(x,y,color,sx,sy){this.x=x;this.y=y;this.color=color;this.sx=sx;this.sy=sy;this.life=1.0;}
        draw(){
            ctx.globalAlpha=this.life; ctx.fillStyle=this.color; ctx.beginPath();
            ctx.arc(this.x,this.y,2,0,Math.PI*2); ctx.fill();
        }
        update(){this.x+=this.sx;this.y+=this.sy;this.sy+=0.05;this.life-=0.015;}
    }

    class Firework {
        constructor(){
            this.x=Math.random()*c.width; this.y=c.height;
            this.color=`hsl(${Math.random()*360},100%,60%)`;
            this.sy=Math.random()*-4-7; this.sx=Math.random()*2-1; this.ex=false;
        }
        draw(){ctx.fillStyle=this.color;ctx.beginPath();ctx.arc(this.x,this.y,3,0,Math.PI*2);ctx.fill();}
        update(){
            this.x+=this.sx; this.y+=this.sy; this.sy+=0.1;
            if(this.sy>=-0.5){
                this.ex=true;
                for(let i=0;i<50;i++){
                    const ang=Math.random()*Math.PI*2, spd=Math.random()*5+2;
                    particles.push(new Particle(this.x,this.y,this.color,Math.cos(ang)*spd,Math.sin(ang)*spd));
                }
            }
        }
    }

    function anim(){
        ctx.clearRect(0,0,c.width,c.height);
        if(Math.random()<0.06) fireworks.push(new Firework());
        fireworks.forEach((f,i)=>{f.update();f.draw();if(f.ex)fireworks.splice(i,1);});
        particles.forEach((p,i)=>{p.update();p.draw();if(p.life<=0)particles.splice(i,1);});
        requestAnimationFrame(anim);
    } anim();
    </script>""", height=1000)

# --- MAIN ---

def main():
    if 'state' not in st.session_state:
        st.session_state.state = 'login'

    main_placeholder = st.empty()

    if st.session_state.state == 'login':
        with main_placeholder.container():
            st.markdown("<div class='pink-neon'>THE BACKDOOR</div>", unsafe_allow_html=True)
            st.markdown("<div class='cyan-sub'>SECURE VIP ENTRANCE</div>", unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns([1, 3, 1])
            with c2:
                st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1fe56053-597e-45b3-a3b1-f26197574147/deb1dq7-6605a031-5944-49cc-8beb-dba5e8284c4a.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiIvZi8xZmU1NjA1My01OTdlLTQ1YjMtYTNiMS1mMjYxOTc1NzQxNDcvZGViMWRxNy02NjA1YTAzMS01OTQ0LTQ5Y2MtOGJlYi1kYmE1ZTgyODRjNGEuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.QauebzGlSfy161JK86WvKTuhXb3OfmoXKdV7rOy-I8Y", use_container_width=True)
            
            play_audio("scena1.mp3", loop=True)
            pwd = st.text_input("ACCESS KEY:", type="password", key="p_in")
            if st.button("AUTHORIZE ENTRANCE"):
                if pwd.lower().strip() == "locanda2026":
                    st.session_state.state = 'hacking'
                    main_placeholder.empty()
                    st.rerun()
                else: st.error("ACCESS DENIED")

    elif st.session_state.state == 'hacking':
        with main_placeholder.container():
            play_audio("scena2.mp3", loop=False)
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
            main_placeholder.empty()
            st.rerun()

    elif st.session_state.state == 'party':
        with main_placeholder.container():
            play_audio("musica.mp3", loop=False)
            show_party_visuals()
            
            if os.path.exists("ascii2.png"): 
                st.image("ascii2.png", use_container_width=True)
            
            st.markdown("<div class='unlocked-title'>2026 UNLOCKED</div>", unsafe_allow_html=True)
            st.markdown("<div class='custom-success-box'>🥂 BUON ANNO, LOCANDIERI! 🥂</div>", unsafe_allow_html=True)
            
            if os.path.exists("foto.png"): 
                st.image("foto.png", use_container_width=True)
                
            if st.button("TERMINATE CONNECTION"):
                st.session_state.state = 'login'
                main_placeholder.empty()
                st.rerun()

if __name__ == "__main__":
    main()
