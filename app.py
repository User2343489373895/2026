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
    
    .stApp { background-color: #050505 !important; }
    header, footer, #MainMenu {visibility: hidden;}
    
    /* Contenitore per centratura forzata di tutti i testi */
    .centered-wrapper {
        width: 100%;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .pink-neon-title { 
        color: #ff00ff; 
        text-shadow: 0 0 15px #ff00ff; 
        font-family: 'Orbitron', sans-serif; 
        font-size: clamp(30px, 8vw, 65px); 
        font-weight: 900; 
        margin: 0;
        line-height: 1.1;
    }

    .cyan-neon-subtitle {
        color: #00ffff;
        text-shadow: 0 0 8px #00ffff;
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(14px, 4vw, 22px);
        font-weight: bold;
        letter-spacing: 2px;
        margin: 5px 0 20px 0;
    }

    .unlocked-title {
        color: white; 
        font-family: 'Orbitron', sans-serif; 
        /* GIGANTE SU DESKTOP (160px), ADATTABILE SU MOBILE */
        font-size: clamp(35px, 15vw, 160px); 
        text-shadow: 0 0 20px #ff00ff, 0 0 50px #ff00ff;
        line-height: 1;
        margin: 20px 0;
    }

    /* BOX BUON ANNO - FULL WIDTH E CENTRATO */
    .brindisi-box {
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
        margin: 20px 0;
    }

    .terminal-text {
        font-family: 'Fira Code', monospace; 
        color: #00ff41; 
        font-size: clamp(12px, 3vw, 15px);
        background: rgba(0, 255, 65, 0.1); 
        padding: 12px; 
        border-left: 3px solid #00ff41; 
        margin-bottom: 5px;
        text-align: left;
        width: 100%;
    }

    .matrix-rain { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 1; opacity: 0.3; }
    .bit { position: absolute; top: -30px; font-family: monospace; font-size: 18px; animation: fall linear infinite; }
    @keyframes fall { to { transform: translateY(110vh); } }
    
    div.stButton > button {
        background-color: transparent !important; color: #ff00ff !important; border: 2px solid #ff00ff !important;
        font-family: 'Orbitron', sans-serif !important; width: 100%; box-shadow: 0 0 10px #ff00ff; height: 50px;
    }

    /* Overlay per Fuochi */
    #canvas-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        pointer-events: none;
        z-index: 5;
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
    # Pioggia di bit (Streamlit Native)
    chars = ["0", "1", "🥂", "🍸","🚬", "✨", "💎", "💰", "🍑", "🔞" , "2", "0", "2", "6"]
    rain_html = '<div class="matrix-rain">'
    for i in range(35):
        left = i * 2.8
        rain_html += f'<div class="bit" style="left:{left}%; color:#ff00ff; animation-duration:{random.uniform(2,5)}s;">{random.choice(chars)}</div>'
    st.markdown(rain_html + '</div>', unsafe_allow_html=True)
    
    # Fuochi d'Artificio (Componente dedicato)
    components.html("""
    <canvas id="f" style="position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:5;"></canvas>
    <script>
    const c=document.getElementById('f'), x=c.getContext('2d');
    c.width=window.innerWidth; c.height=window.innerHeight;
    let ps=[], fws=[];
    class P {
        constructor(x,y,c,sx,sy){this.x=x;this.y=y;this.c=c;this.sx=sx;this.sy=sy;this.l=1.0;}
        draw(){x.globalAlpha=this.l; x.fillStyle=this.c; x.beginPath(); x.arc(this.x,this.y,2.5,0,Math.PI*2); x.fill();}
        up(){this.x+=this.sx;this.y+=this.sy;this.sy+=0.06;this.l-=0.025;}
    }
    class FW {
        constructor(){
            this.x=Math.random()*c.width; this.y=c.height;
            this.color=`hsl(${Math.random()*360},100%,60%)`;
            this.sy=Math.random()*-4-8; this.sx=Math.random()*2-1; this.ex=false;
        }
        draw(){x.fillStyle=this.color;x.beginPath();x.arc(this.x,this.y,3.5,0,Math.PI*2);x.fill();}
        up(){
            this.x+=this.sx; this.y+=this.sy; this.sy+=0.12;
            if(this.sy>=-0.5){
                this.ex=true;
                for(let i=0;i<45;i++){
                    const a=Math.random()*Math.PI*2, s=Math.random()*6+2;
                    ps.push(new P(this.x,this.y,this.color,Math.cos(a)*s,Math.sin(a)*s));
                }
            }
        }
    }
    function anim(){
        x.clearRect(0,0,c.width,c.height);
        if(Math.random()<0.05) fws.push(new FW());
        fws.forEach((f,i)=>{f.up();f.draw();if(f.ex)fws.splice(i,1);});
        ps.forEach((p,i)=>{p.up();p.draw();if(p.l<=0)ps.splice(i,1);});
        requestAnimationFrame(anim);
    } anim();
    </script>""", height=0)

# --- LOGICA MAIN ---
def main():
    if 'state' not in st.session_state:
        st.session_state.state = 'login'

    main_placeholder = st.empty()

    if st.session_state.state == 'login':
        with main_placeholder.container():
            # LOGIN HEADER - Centratura forzata
            st.markdown("""
                <div class="centered-wrapper">
                    <h1 class="pink-neon-title">THE BACKDOOR</h1>
                    <p class="cyan-neon-subtitle">SECURE VIP ENTRANCE</p>
                </div>
            """, unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns([0.05, 0.9, 0.05])
            with c2:
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
            # HACKING HEADER - Centratura forzata
            st.markdown("""
                <div class="centered-wrapper">
                    <h1 class="pink-neon-title">OVERRIDING VIP SERVER...</h1>
                </div>
            """, unsafe_allow_html=True)
            
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
            
            # Immagine ASCII Sopra
            if os.path.exists("ascii.png"): 
                st.image("ascii.png", use_container_width=True)
            
            # Titolo 2026 UNLOCKED
            st.markdown(f"<div class='centered-wrapper'><h1 class='unlocked-title'>2026 UNLOCKED</h1></div>", unsafe_allow_html=True)
            
            # Box Buon Anno
            st.markdown("""
                <div class="centered-wrapper">
                    <div class="brindisi-box">🥂 BUON ANNO, LOCANDIERI! 🥂</div>
                </div>
                """, unsafe_allow_html=True)
            
            # Foto Finale
            if os.path.exists("foto.png"): 
                st.image("foto.png", use_container_width=True)
            
            if st.button("TERMINATE CONNECTION"):
                st.session_state.state = 'login'
                main_placeholder.empty()
                st.rerun()

if __name__ == "__main__":
    main()
