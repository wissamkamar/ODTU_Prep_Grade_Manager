"""ODTÜ Prep Grade Manager - Devamsızlık modülü (Streamlit).
 
Çalıştırma:  streamlit run app.py
"""
import streamlit as st
 
from attendance import LEVELS, TERMS, failed_terms, group_name, status
 
st.set_page_config(page_title="ODTÜ Prep Grade Manager", page_icon="🎓", layout="centered")
 
MAROON, GOLD, TINT, LINE = "#86143a", "#f0c35a", "#fde8ec", "#e6c3cc"
 
st.markdown(
    f"""
<style>
.block-container {{ max-width: 640px; padding-top: 1rem; }}
.hdr {{ background:{MAROON}; color:#fff; text-align:center; padding:1rem; border-radius:12px; margin-bottom:1rem; }}
.hdr h1 {{ margin:0; font: 700 1.7rem Georgia, serif; color:{GOLD}; padding:0; }}
.hdr p {{ margin:.2rem 0 0; }}
.card {{ background:{TINT}; border:1px solid {LINE}; border-radius:14px; padding:1rem; }}
.card h3 {{ margin:0 0 .6rem; font-size:1.1rem; }}
.ring-row {{ display:flex; align-items:center; gap:1.2rem; }}
.ring {{ width:110px; height:110px; border-radius:50%; flex:none; position:relative; }}
.ring::after {{ content:""; position:absolute; inset:14px; background:{TINT}; border-radius:50%; }}
.pct {{ font-size:2.2rem; font-weight:800; line-height:1.1; }}
.sub {{ color:#6b5a60; }}
.ok {{ color:#1f8a4c; font-weight:600; margin:.7rem 0 0; }}
.bad {{ color:#c0172f; font-weight:600; margin:.7rem 0 0; }}
div.stButton > button {{ background:{MAROON}; color:#fff; border:0; border-radius:10px; }}
div.stButton > button:hover {{ background:#6a0f2e; color:#fff; }}
</style>
<div class="hdr"><h1>ODTÜ Prep Grade Manager</h1><p>Akademik İlerleme Takip Sistemi</p></div>
""",
    unsafe_allow_html=True,
)
 
# Her dönemin kur seçimi ve devamsızlığı ayrı tutulur (dönem sonunda sıfırlanır).
if "data" not in st.session_state:
    st.session_state.data = {t: {"level": 1, "used": 0} for t in TERMS}
data = st.session_state.data
 
 
def add_hours():
    term = st.session_state.term
    data[term]["used"] += int(st.session_state.hours)
 
 
def reset_term(term):
    data[term]["used"] = 0
 
 
# ---- Kur seçimi (önce seçilir, özet kartı ona göre çizilir) ----
st.subheader("Kur Seçimi")
term = st.radio("Dönem", TERMS, horizontal=True, key="term")
level = st.radio(
    "Kur",
    LEVELS,
    index=data[term]["level"] - 1,
    format_func=lambda l: group_name(l, term),
    horizontal=True,
    key=f"level_{term}",
)
data[term]["level"] = level
 
# ---- Özet kartı ----
s = status(level, term, data[term]["used"])
color = "#c0172f" if s.exceeded else MAROON
deg = s.remaining_percent * 3.6
msg = (
    f'<p class="bad">{term} dönemi limiti {s.over_by} saat aşıldı. EPE\'ye giremezsin ve sınıfta kalırsın.</p>'
    if s.exceeded
    else f'<p class="ok">{s.remaining} saat devamsızlık hakkın kaldı.</p>'
)
st.markdown(
    f"""
<div class="card"><h3>Devamsızlık Oranı</h3>
<div class="ring-row">
  <div class="ring" style="background:conic-gradient({color} {deg}deg, #f1c4cd 0)"></div>
  <div><div class="pct">%{s.remaining_percent}</div><div class="sub">({s.used} / {s.total} saat)</div></div>
</div>{msg}</div>
""",
    unsafe_allow_html=True,
)
 
# İki dönemden herhangi birinde limit aşıldıysa genel uyarı
lost = failed_terms({t: (data[t]["level"], data[t]["used"]) for t in TERMS})
if lost:
    st.error(f"{' ve '.join(lost)} döneminde devamsızlık limiti aşıldı: EPE'ye giremezsin ve sınıfta kalırsın.")
 
# ---- Devamsızlık bilgileri ----
st.subheader("Devamsızlık Bilgileri")
c1, c2 = st.columns([3, 1], vertical_alignment="bottom")
c1.number_input("Devamsızlık Saati", min_value=1, max_value=200, value=1, step=1, key="hours")
c2.button("+ Ekle", on_click=add_hours, use_container_width=True)
 
hdr = st.columns([2, 2, 2, 2, 2])
for col, name in zip(hdr, ["Dönem", "Kullanılan Saat", "Kalan Saat", "Toplam Saat", "İşlem"]):
    col.markdown(f"**{name}**")
for t in TERMS:
    lvl, used = data[t]["level"], data[t]["used"]
    st_t = status(lvl, t, used)
    row = st.columns([2, 2, 2, 2, 2])
    row[0].write(f"{t} ({group_name(lvl, t)})")
    row[1].write(used)
    row[2].write(f"Aşıldı (+{st_t.over_by})" if st_t.exceeded else st_t.remaining)
    row[3].write(st_t.total)
    row[4].button("Sıfırla", key=f"reset_{t}", on_click=reset_term, args=(t,))
