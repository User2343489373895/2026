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

# --- CSS DEFINITIVO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Fira+Code&display=swap');
    
    .stApp { background-color: #050505 !important; overflow-x: hidden; }
    header, footer, #MainMenu {visibility: hidden;}
    
    /* Titoli Login */
    .pink-neon { 
        color: #ff00ff; 
        text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff; 
        font-family: 'Orbitron', sans-serif; 
        text-align: center; 
        font-size: clamp(28px, 8vw, 60px); 
        font-weight: 900; 
        margin-bottom: 5px;
    }

    .cyan-sub {
        color: #00ffff;
        text-shadow: 0 0 8px #00ffff;
        font-family: 'Orbitron', sans-serif;
        text-align: center;
        font-size: clamp(12px, 3.5vw, 20px);
        font-weight: bold;
        letter-spacing: 3px;
        text-transform: uppercase;
    }

    /* 2026 UNLOCKED - GIGANTE E PULSANTE */
    .unlocked-title {
        color: white; 
        font-family: 'Orbitron', sans-serif; 
        font-size: clamp(45px, 15vw, 120px); 
        font-weight: 900;
        text-align: center;
        margin: 10px 0;
        line-height: 1;
        text-shadow: 0 0 10px #fff, 0 0 30px #ff00ff, 0 0 50px #ff00ff;
        animation: pulse 2s infinite alternate;
        position: relative;
        z-index: 10;
    }

    @keyframes pulse {
        from { transform: scale(1); text-shadow: 0 0 10px #fff, 0 0 30px #ff00ff; }
        to { transform: scale(1.05); text-shadow: 0 0 20px #fff, 0 0 50px #ff00ff, 0 0 80px #ff00ff; }
    }

    /* BOX BUON ANNO - FULL WIDTH NO WRAP */
    .custom-success-box {
        background: rgba(0, 255, 65, 0.1);
        border: 3px solid #00ff41;
        box-shadow: 0 0 20px #00ff41;
        color: #00ff41;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(18px, 6vw, 42px);
        font-weight: 900;
        text-shadow: 0 0 15px #00ff41;
        margin: 20px auto;
        width: 100%;
        white-space: nowrap;
        position: relative;
        z-index: 10;
    }

    .terminal-text {
        font-family: 'Fira Code', monospace; color: #00ff41; font-size: clamp(12px, 3vw, 15px);
        background: rgba(0, 255, 65, 0.05); padding: 15px; border-left: 4px solid #00ff41; margin-bottom: 8px;
    }

    /* Matrix Rain */
    .matrix-rain { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 1; opacity: 0.2; }
    .bit { position: absolute; top: -30px; font-family: monospace; animation: fall linear infinite; }
    @keyframes fall { to { transform: translateY(110vh); } }
    
    div.stButton > button {
        background-color: transparent !important; color: #ff00ff !important; border: 2px solid #ff00ff !important;
        font-family: 'Orbitron', sans-serif !important; width: 100%; box-shadow: 0 0 15px #ff00ff; height: 50px;
        font-weight: bold;
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
    # Pioggia Matrix di emoji
    chars = ["0", "1", "🥂", "🍸","🚬", "✨", "💎", "💰", "🍑", "🔞" , "2", "0", "2", "6"]
    rain_html = '<div class="matrix-rain">'
    for i in range(30):
        left = i * 3.3
        rain_html += f'<div class="bit" style="left:{left}%; color:#ff00ff; font-size:20px; animation-duration:{random.uniform(2,5)}s;">{random.choice(chars)}</div>'
    st.markdown(rain_html + '</div>', unsafe_allow_html=True)
    
    # Fuochi d'Artificio (Height=0 per rimuovere lo spazio bianco)
    components.html("""
    <canvas id="f" style="position:fixed; top:0; left:0; width:100vw; height:100vh; pointer-events:none; z-index:5;"></canvas>
    <script>
    const c=document.getElementById('f'), ctx=c.getContext('2d');
    function resize() { c.width=window.innerWidth; c.height=window.innerHeight; }
    window.addEventListener('resize', resize); resize();
    
    let particles=[], fireworks=[];
    class Particle {
        constructor(x,y,color,sx,sy){this.x=x;this.y=y;this.color=color;this.sx=sx;this.sy=sy;this.life=1.0;}
        draw(){ctx.globalAlpha=this.life; ctx.fillStyle=this.color; ctx.beginPath(); ctx.arc(this.x,this.y,2.5,0,Math.PI*2); ctx.fill();}
        update(){this.x+=this.sx;this.y+=this.sy;this.sy+=0.07;this.life-=0.02;}
    }
    class Firework {
        constructor(){
            this.x=Math.random()*c.width; this.y=c.height;
            this.color=`hsl(${Math.random()*360},100%,60%)`;
            this.sy=Math.random()*-5-8; this.sx=Math.random()*2-1; this.ex=false;
        }
        draw(){ctx.fillStyle=this.color;ctx.beginPath();ctx.arc(this.x,this.y,3.5,0,Math.PI*2);ctx.fill();}
        update(){
            this.x+=this.sx; this.y+=this.sy; this.sy+=0.12;
            if(this.sy>=-0.5){
                this.ex=true;
                for(let i=0;i<40;i++){
                    const ang=Math.random()*Math.PI*2, spd=Math.random()*6+2;
                    particles.push(new Particle(this.x,this.y,this.color,Math.cos(ang)*spd,Math.sin(ang)*spd));
                }
            }
        }
    }
    function anim(){
        ctx.clearRect(0,0,c.width,c.height);
        if(Math.random()<0.04) fireworks.push(new Firework());
        fireworks.forEach((f,i)=>{f.update();f.draw();if(f.ex)fireworks.splice(i,1);});
        particles.forEach((p,i)=>{p.update();p.draw();if(p.life<=0)particles.splice(i,1);});
        requestAnimationFrame(anim);
    } anim();
    </script>""", height=0)

# --- LOGICA ---
def main():
    if 'state' not in st.session_state:
        st.session_state.state = 'login'

    main_placeholder = st.empty()

    if st.session_state.state == 'login':
        with main_placeholder.container():
            st.markdown("<div class='pink-neon'>THE BACKDOOR</div>", unsafe_allow_html=True)
            st.markdown("<div class='cyan-sub'>SECURE VIP ENTRANCE</div>", unsafe_allow_html=True)
            st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1fe56053-597e-45b3-a3b1-f26197574147/deb1dq7-6605a031-5944-49cc-8beb-dba5e8284c4a.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiIvZi8xZmU1NjA1My01OTdlLTQ1YjMtYTNiMS1mMjYxOTc1NzQxNDcvZGViMWRxNy02NjA1YTAzMS01OTQ0LTQ5Y2MtOGJlYi1kYmE1ZTgyODRjNGEuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.QauebzGlSfy161JK86WvKTuhXb3OfmoXKdV7rOy-I8Y", use_container_width=True)
            play_audio("scena1.mp3", loop=True)
            pwd = st.text_input("ACCESS KEY:", type="password", key="p_in")
            if st.button("AUTHORIZE ENTRANCE"):
                if pwd.lower().strip() == "locandieri":
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
        # Qui vengono chiamati gli effetti (ora non occupano spazio)
        show_party_visuals()
        
        with main_placeholder.container():
            play_audio("musica.mp3", loop=True)
            
            if os.path.exists("ascii.png"): 
                st.image("ascii.png", use_container_width=True)
            
            # Titolo Gigante
            st.markdown("<div class='unlocked-title'>2026 UNLOCKED</div>", unsafe_allow_html=True)
            
            # Box Buon Anno
            st.markdown("<div class='custom-success-box'>🥂 BUON ANNO, LOCANDIERI! 🥂</div>", unsafe_allow_html=True)
            
            if os.path.exists("foto.png"): 
                st.image("foto.png", use_container_width=True)
            
            if st.button("TERMINATE CONNECTION"):
                st.session_state.state = 'login'
                main_placeholder.empty()
                st.rerun()

if __name__ == "__main__":
    main()
