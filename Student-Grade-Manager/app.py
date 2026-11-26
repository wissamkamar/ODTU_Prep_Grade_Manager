"""ODTÜ Prep Grade Manager - Devamsızlık modülü (Streamlit).

Çalıştırma:  streamlit run app.py
"""


import streamlit as st

from attendance import LEVELS, TERMS, failed_terms, group_name, status
import add_exams
from add_exams import add_grade, delete_grade
from Calculation import calculate_final_grade

st.set_page_config(
    page_title="ODTÜ Prep Grade Manager",
    page_icon="🎓",
    layout="centered"
)

MAROON, GOLD, TINT, LINE = "#86143a", "#f0c35a", "#fde8ec", "#e6c3cc"

KISA = {
    "Quiz": "QZ",
    "Writing": "WA",
    "Speaking Assessment": "SA",
    "Midterm": "MT",
    "Speaking Examination": "SE",
}

# ---- TASARIM ----
st.markdown(
    f"""
<style>
.block-container {{
    max-width: 640px;
    padding-top: 1rem;
}}

.hdr {{
    background: {MAROON};
    color: white;
    text-align: center;
    padding: 1.2rem;
    border-radius: 12px;
    margin-bottom: 1.2rem;
}}

.hdr h1 {{
    margin: 0;
    font: 700 1.7rem Georgia, serif;
    color: {GOLD};
}}

.hdr p {{
    margin: .3rem 0 0;
}}

.card {{
    background: {TINT};
    border: 1px solid {LINE};
    border-radius: 14px;
    padding: 1rem;
}}

div.stButton > button {{
    background: {MAROON};
    color: white;
    border: 0;
    border-radius: 10px;
}}

div.stButton > button:hover {{
    background: #6a0f2e;
    color: white;
}}

[data-testid="stDataFrame"] {{
    border: 1px solid {LINE};
    border-radius: 10px;
}}

</style>
""",
    unsafe_allow_html=True,
)

# ---- ÜST BAŞLIK ----
st.markdown(
    """
    <div class="hdr">
        <h1>ODTÜ Prep Grade Manager</h1>
        <p>Akademik İlerleme Takip Sistemi</p>
    </div>
    """,
    unsafe_allow_html=True,
)

genel = st.container()

# ---- VERİLER ----
if "data" not in st.session_state:
    st.session_state.data = {
        t: {"level": 1, "used": 0} for t in TERMS
    }

data = st.session_state.data


def add_hours():
    term = st.session_state.term
    data[term]["used"] += int(st.session_state.hours)


def reset_term(term):
    data[term]["used"] = 0


# ---- KUR SEÇİMİ ----
st.subheader("Kur Seçimi")

term = st.radio(
    "Dönem",
    TERMS,
    horizontal=True,
    key="term"
)

level = st.radio(
    "Kur",
    LEVELS,
    index=data[term]["level"] - 1,
    format_func=lambda l: group_name(l, term),
    horizontal=True,
    key=f"level_{term}",
)

data[term]["level"] = level

s = status(level, term, data[term]["used"])

lost = failed_terms({
    t: (data[t]["level"], data[t]["used"])
    for t in TERMS
})

if lost:
    st.error(
        f"{' ve '.join(lost)} döneminde devamsızlık limiti aşıldı: "
        "EPE'ye giremezsin ve sınıfta kalırsın."
    )

# ---- DEVAMSIZLIK ----
st.subheader("Devamsızlık Bilgileri")

c1, c2 = st.columns([3, 1], vertical_alignment="bottom")

c1.number_input(
    "Devamsızlık Saati",
    min_value=1,
    max_value=200,
    value=1,
    step=1,
    key="hours"
)

c2.button(
    "+ Ekle",
    on_click=add_hours,
    use_container_width=True
)

hdr = st.columns([2, 2, 2, 2, 2])

for col, name in zip(
    hdr,
    ["Dönem", "Kullanılan Saat", "Kalan Saat", "Toplam Saat", "İşlem"]
):
    col.markdown(f"**{name}**")

for t in TERMS:
    lvl, used = data[t]["level"], data[t]["used"]
    st_t = status(lvl, t, used)

    row = st.columns([2, 2, 2, 2, 2])

    row[0].write(f"{t} ({group_name(lvl, t)})")
    row[1].write(used)
    row[2].write(
        f"Aşıldı (+{st_t.over_by})"
        if st_t.exceeded else st_t.remaining
    )
    row[3].write(st_t.total)

    row[4].button(
        "🗑️",
        key=f"reset_{t}",
        on_click=reset_term,
        args=(t,)
    )

# ---- NOT HESAPLAMA ----
st.subheader("Not Hesaplama")

if "grades" not in st.session_state:
    st.session_state.grades = []

add_exams.grades[:] = st.session_state.grades

semester = st.radio(
    "Not Dönemi",
    ["Fall", "Spring"],
    horizontal=True
)

exam_type = st.selectbox(
    "Sınav",
    [
        "Quiz",
        "Writing",
        "Speaking Assessment",
        "Midterm",
        "Speaking Examination"
    ]
)

exam_no = st.text_input("Sınav no (örn. 01)", value="01")

grade = st.number_input(
    "Not",
    min_value=0.0,
    max_value=100.0
)

if st.button("Notu Ekle"):

    zaten_var = any(
        g["Exam Type"] == exam_type
        and g["Exam No"] == exam_no
        and g["semester"] == semester
        for g in st.session_state.grades
    )

    if zaten_var:
        st.error("Bu sınav zaten eklenmiş!")

    else:
        result = add_grade(
            exam_type,
            exam_no,
            semester,
            grade
        )

        if isinstance(result, str):
            st.error(result)
        else:
            st.session_state.grades = list(add_exams.grades)
            st.rerun()


# ---- HESAPLAMA ----
final = calculate_final_grade()

# ---- GENEL DURUM ----
with genel:

    st.subheader("📊 Genel Durum")

    k1, k2, k3 = st.columns([1, 1, 1], gap="small")

    with k1.container(border=True):
        st.caption("🕒 Devamsızlık Hakkı")
        st.metric(
            "Kalan hak",
            f"{s.remaining} saat",
            delta=f"{s.over_by} saat aşıldı" if s.exceeded else None,
            delta_color="inverse"
        )
        st.caption(f"{s.used} / {s.total} saat kullanıldı")

    with k2.container(border=True):
        st.caption("🎓 Not Ortalaması")
        st.metric(
            "Genel ortalama",
            f"{final:.2f}"
        )
        st.caption("100 üzerinden")

    with k3.container(border=True):
        st.caption("🏆 EPE Durumu")

        if final >= 64.5 and not lost:
            st.success("Hak Kazandın")
        else:
            st.error("Hak Kazanmadın")

        st.caption("Gerekli not: 64.5")


# ---- SINAV NOTLARI TABLOSU ----
st.markdown("---")
st.subheader("Sınav Notları Tablosu")

hdr = st.columns([3, 2, 2, 1])

for col, name in zip(hdr, ["Sınav", "Dönem", "Not", "İşlem"]):
    col.markdown(f"**{name}**")

if st.session_state.grades:

    for i, g in enumerate(st.session_state.grades):
        row = st.columns([3, 2, 2, 1])

        exam_short = KISA[g["Exam Type"]]
        exam_name = f"{exam_short}{g['Exam No']}"

        row[0].write(exam_name)
        row[1].write(g["semester"])
        row[2].write(f"{g['Grade']:g}")

        if row[3].button("🗑️", key=f"delete_exam_{i}"):
            delete_grade(
                g["Exam Type"],
                g["Exam No"],
                g["semester"]
            )
            st.session_state.grades = add_exams.grades.copy()
            st.rerun()

else:
    st.info("Henüz sınav notu eklenmedi.")

        st.caption("Gerekli not: 64.5")
