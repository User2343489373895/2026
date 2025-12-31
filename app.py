import streamlit as st
import time
import os
import base64
import random
import streamlit.components.v1 as components

# 1. Configurazione (Deve essere la prima istruzione)
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

# --- CSS GLOBALE RESPONSIVE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Fira+Code&display=swap');
    
    .stApp { background-color: #050505 !important; overflow-x: hidden; }
    header, footer, #MainMenu {visibility: hidden;}
    
    /* Font che si adattano allo schermo */
    .pink-neon { 
        color: #ff00ff; 
        text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff; 
        font-family: 'Orbitron', sans-serif; 
        text-align: center; 
        font-size: clamp(28px, 8vw, 48px); /* Responsive: min 28px, ideale 8% larghezza, max 48px */
        font-weight: 900; 
        margin-bottom: 5px;
        width: 100%;
        display: block;
    }

    .cyan-sub {
        color: #00ffff;
        text-shadow: 0 0 8px #00ffff;
        font-family: 'Orbitron', sans-serif;
        text-align: center;
        font-size: clamp(14px, 4vw, 18px);
        font-weight: bold;
        margin-top: 0px;
        letter-spacing: 2px;
        width: 100%;
        display: block;
    }

    /* Box di Successo HTML (Mobile Friendly) */
    .custom-success-box {
        background-color: rgba(0, 255, 65, 0.1);
        border: 2px solid #00ff41;
        color: #00ff41;
        border-radius: 10px;
        padding: clamp(15px, 4vw, 30px);
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(16px, 5vw, 28px);
        font-weight: bold;
        text-shadow: 0 0 15px #00ff41;
        margin: 20px auto;
        width: 90%;
    }

    .terminal-text {
        font-family: 'Fira Code', monospace; color: #00ff41; font-size: clamp(12px, 3vw, 14px);
        background: rgba(0, 255, 65, 0.1); padding: 15px; border-left: 3px solid #00ff41; margin-bottom: 5px;
    }

    /* Matrix Rain */
    .matrix-rain { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 1; opacity: 0.3; }
    .bit { position: absolute; top: -30px; font-family: monospace; font-size: 18px; animation: fall linear infinite; }
    @keyframes fall { to { transform: translateY(110vh); } }
    
    /* Bottoni */
    div.stButton > button {
        background-color: transparent !important; color: #ff00ff !important; border: 2px solid #ff00ff !important;
        font-family: 'Orbitron', sans-serif !important; width: 100%; box-shadow: 0 0 10px #ff00ff; height: 50px;
    }

    /* Iframe Fuochi */
    iframe { position: fixed; top: 0; left: 0; width: 100vw !important; height: 100vh !important; border: none; pointer-events: none; z-index: 5; }
    
    /* Fix per centratura colonne Streamlit su Desktop */
    [data-testid="column"] {
        display: flex;
        justify-content: center;
        align-items: center;
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
    chars = ["$", "0", "1", "🥂", "✨", "💎", "🍑" , "2", "0", "2", "6"]
    rain_html = '<div class="matrix-rain">'
    for i in range(40): # Ridotto per mobile performance
        left = i * 2.5
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
        draw(){ctx.globalAlpha=this.life; ctx.fillStyle=this.color; ctx.beginPath(); ctx.arc(this.x,this.y,2,0,Math.PI*2); ctx.fill();}
        update(){this.x+=this.sx;this.y+=this.sy;this.sy+=0.05;this.life-=0.02;}
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
                for(let i=0;i<40;i++){
                    const ang=Math.random()*Math.PI*2, spd=Math.random()*5+2;
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
    </script>""", height=1000)

# --- MAIN ---
def main():
    if 'state' not in st.session_state:
        st.session_state.state = 'login'

    main_placeholder = st.empty()

    if st.session_state.state == 'login':
        with main_placeholder.container():
            # Titoli con classi Responsive
            st.markdown("<h1 class='pink-neon'>THE BACKDOOR</h1>", unsafe_allow_html=True)
            st.markdown("<p class='cyan-sub'>SECURE VIP ENTRANCE</p>", unsafe_allow_html=True)
            
            c1, c2, c3 = st.columns([0.1, 0.8, 0.1])
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
            st.markdown("<h2 class='pink-neon'>OVERRIDING VIP SERVER...</h2>", unsafe_allow_html=True)
            log_area = st.empty()
            full_log = ""
            steps = [
                ("> Initializing protocol...", 1.2), 
                ("> Bypassing IDS/IPS...", 1.5), 
                ("> Deep Packet Inspection...", 1.8), 
                ("> Escalating privileges...", 1.5), 
                ("> SUCCESS: Access granted.", 1.0)
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
            
            # 1. IMMAGINE ASCII PRIMA DEL TITOLO
            if os.path.exists("ascii.png"): 
                st.image("ascii.png", use_container_width=True)
            
            # 2. TITOLO 2026 UNLOCKED
            st.markdown("<div style='text-align: center; position: relative; z-index: 10;'><h1 style='color: white; font-family: Orbitron; font-size: clamp(30px, 10vw, 55px); text-shadow: 0 0 20px #ff00ff;'>2026 UNLOCKED</h1></div>", unsafe_allow_html=True)
            
            # 3. BOX SUCCESSO PERSONALIZZATO
            st.markdown("""
                <div class="custom-success-box">
                    🥂 BUON ANNO, LOCANDIERI! 🥂
                </div>
                """, unsafe_allow_html=True)
            
            # 4. FOTO FINALE
            if os.path.exists("foto.png"): 
                st.image("foto.png", use_container_width=True)
            
            if st.button("TERMINATE CONNECTION"):
                st.session_state.state = 'login'
                main_placeholder.empty()
                st.rerun()

if __name__ == "__main__":
    main()
