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

# --- CSS GLOBALE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Fira+Code&display=swap');
    
    /* Rimuove lo spazio bianco in alto */
    .block-container { padding-top: 0rem !important; }
    .stApp { background-color: #050505 !important; overflow-x: hidden; }
    header, footer, #MainMenu {visibility: hidden;}
    
    /* Login Titles */
    .pink-neon { 
        color: #ff00ff; text-shadow: 0 0 15px #ff00ff; 
        font-family: 'Orbitron', sans-serif; font-size: clamp(24px, 8vw, 60px); 
        font-weight: 900; line-height: 1.2; text-align: center;
    }
    .cyan-sub {
        color: #00ffff; text-shadow: 0 0 8px #00ffff;
        font-family: 'Orbitron', sans-serif; font-size: clamp(14px, 4vw, 22px);
        font-weight: bold; letter-spacing: 2px; text-transform: uppercase; text-align: center;
    }

    /* 2026 UNLOCKED - NON TOCCARE */
    .unlocked-title {
        color: white; 
        font-family: 'Orbitron', sans-serif; 
        font-size: clamp(40px, 15vw, 130px); 
        text-shadow: 0 0 20px #ff00ff, 0 0 50px #ff00ff;
        line-height: 1;
        margin: 20px 0;
        text-align: center;
    }

    /* BOX BUON ANNO - FIX MOBILE/DESKTOP */
    .custom-success-box {
        background-color: rgba(0, 255, 65, 0.1);
        border: 2px solid #00ff41;
        color: #00ff41;
        border-radius: 12px;
        padding: 20px;
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(18px, 6vw, 40px);
        font-weight: bold;
        text-shadow: 0 0 15px #00ff41;
        width: 100%;
        text-align: center;
        margin: 15px 0;
        white-space: nowrap; /* Desktop: non spezza */
        box-sizing: border-box;
    }
    @media (max-width: 600px) {
        .custom-success-box {
            white-space: normal; /* Mobile: permette adattamento se troppo stretto */
            font-size: clamp(16px, 5vw, 22px);
            line-height: 1.3;
        }
    }

    .terminal-text {
        font-family: 'Fira Code', monospace; 
        color: #00ff41; font-size: clamp(12px, 3vw, 15px);
        background: rgba(0, 255, 65, 0.1); padding: 12px; border-left: 3px solid #00ff41; 
        margin-bottom: 5px; text-align: left;
    }

    /* Matrix Rain FX */
    .matrix-rain { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 1; opacity: 0.3; }
    .bit { position: absolute; top: -30px; font-family: monospace; font-size: 18px; animation: fall linear infinite; }
    @keyframes fall { to { transform: translateY(110vh); } }
    
    div.stButton > button {
        background-color: transparent !important; color: #ff00ff !important; border: 2px solid #ff00ff !important;
        font-family: 'Orbitron', sans-serif !important; width: 100%; box-shadow: 0 0 10px #ff00ff; height: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

def play_audio(file_name, loop=False):
    b64 = get_audio_b64(file_name)
    if b64:
        loop_attr = "loop" if loop else ""
        components.html(f"""<audio autoplay="true" {loop_attr}><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>""", height=0)

# --- LOGICA NAVIGAZIONE ---
if 'state' not in st.session_state:
    st.session_state.state = 'login'

placeholder = st.empty()

# 1. LOGIN
if st.session_state.state == 'login':
    with placeholder.container():
        st.markdown("<div class='pink-neon'>THE BACKDOOR</div><div class='cyan-sub'>SECURE VIP ENTRANCE</div>", unsafe_allow_html=True)
        st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1fe56053-597e-45b3-a3b1-f26197574147/deb1dq7-6605a031-5944-49cc-8beb-dba5e8284c4a.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiIvZi8xZmU1NjA1My01OTdlLTQ1YjMtYTNiMS1mMjYxOTc1NzQxNDcvZGViMWRxNy02NjA1YTAzMS01OTQ0LTQ5Y2MtOGJlYi1kYmE1ZTgyODRjNGEuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.QauebzGlSfy161JK86WvKTuhXb3OfmoXKdV7rOy-I8Y", use_container_width=True)
        play_audio("scena1.mp3", loop=True)
        pwd = st.text_input("ACCESS KEY:", type="password")
        if st.button("AUTHORIZE ENTRANCE"):
            if pwd.lower().strip() == "locandieri":
                st.session_state.state = 'hacking'
                st.rerun() # Pulisce tutto e cambia pagina

# 2. HACKING
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

# 3. PARTY
elif st.session_state.state == 'party':
    # FUOCHI E PIOGGIA CARICATI SOLO QUI
    components.html("""
    <div style="position:fixed; top:0; left:0; width:100vw; height:100vh; pointer-events:none; z-index:9999;">
        <canvas id="f"></canvas>
    </div>
    <script>
    const c=document.getElementById('f'), x=c.getContext('2d');
    let w=c.width=window.innerWidth, h=c.height=window.innerHeight;
    let ps=[], fws=[];
    window.onresize=()=>{w=c.width=window.innerWidth; h=c.height=window.innerHeight;};
    class FW {
        constructor(){
            this.x=Math.random()*w; this.y=h; // Parte dal basso
            this.color=`hsl(${Math.random()*360},100%,60%)`;
            this.sy=Math.random()*-4-8; this.sx=Math.random()*2-1; this.ex=false;
        }
        update(){
            this.x+=this.sx; this.y+=this.sy; this.sy+=0.12;
            if(this.sy>=-0.5){
                this.ex=true;
                for(let i=0;i<40;i++){
                    const a=Math.random()*Math.PI*2, s=Math.random()*6+2;
                    ps.push({x:this.x,y:this.y,c:this.color,sx:Math.cos(a)*s,sy:Math.sin(a)*s,l:1});
                }
            }
        }
        draw(){ x.fillStyle=this.color; x.beginPath(); x.arc(this.x,this.y,3.5,0,7); x.fill(); }
    }
    function anim(){
        x.clearRect(0,0,w,h);
        if(Math.random()<0.05) fws.push(new FW());
        fws=fws.filter(f=>{f.update(); f.draw(); return !f.ex;});
        ps=ps.filter(p=>{
            x.globalAlpha=p.l; x.fillStyle=p.c; x.beginPath(); x.arc(p.x,p.y,2.5,0,7); x.fill();
            p.x+=p.sx; p.y+=p.sy; p.sy+=0.06; p.l-=0.02; return p.l>0;
        });
        requestAnimationFrame(anim);
    } anim();
    </script>
    """, height=0)

    with placeholder.container():
        # Pioggia Matrix Emoji
        chars = ["0", "1", "🥂", "🍸","🚬", "✨", "💎", "💰", "🍑", "🔞" , "2", "0", "2", "6"]
        rain_html = '<div class="matrix-rain">'
        for i in range(25):
            left = i * 4
            rain_html += f'<div class="bit" style="left:{left}%; color:#ff00ff; animation-duration:{random.uniform(2,5)}s;">{random.choice(chars)}</div>'
        st.markdown(rain_html + '</div>', unsafe_allow_html=True)

        play_audio("musica.mp3", loop=True)
        if os.path.exists("ascii.png"): st.image("ascii.png", use_container_width=True)
        
        # TITOLO 2026 - INVARIATO
        st.markdown("<div class='unlocked-title'>2026 UNLOCKED</div>", unsafe_allow_html=True)
        
        # BUON ANNO - FIXATO MOBILE
        st.markdown("<div class='custom-success-box'>🥂 BUON ANNO, LOCANDIERI! 🥂</div>", unsafe_allow_html=True)
        
        if os.path.exists("foto.png"): st.image("foto.png", use_container_width=True)
        
        if st.button("TERMINATE CONNECTION"):
            st.session_state.state = 'login'
            st.rerun()
