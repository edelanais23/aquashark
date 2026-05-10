import streamlit as st
import datetime
import random

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AQUASHARK",
    page_icon="🦈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
# GLOBAL CSS  — deep-ocean noir + electric cyan accents
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:wght@300;400;600&display=swap');

:root {
  --bg:        #020d18;
  --bg2:       #061828;
  --bg3:       #0a2035;
  --cyan:      #00e5ff;
  --cyan2:     #00b4cc;
  --gold:      #f0a500;
  --green:     #00ff9d;
  --red:       #ff4560;
  --text:      #cce8f4;
  --muted:     #5a8aa0;
  --border:    rgba(0,229,255,0.15);
}

html, body, [class*="css"], .stApp {
  font-family: 'Exo 2', sans-serif;
  background: var(--bg) !important;
  color: var(--text);
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none !important; }

.nav-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: linear-gradient(90deg, #020d18 0%, #061828 60%, #020d18 100%);
  border-bottom: 1px solid var(--border);
  padding: 0 2rem;
  height: 64px;
}
.nav-logo {
  font-family: 'Orbitron', sans-serif;
  font-size: 1.5rem;
  font-weight: 900;
  color: var(--cyan);
  letter-spacing: 4px;
  text-shadow: 0 0 20px rgba(0,229,255,0.5);
}
.nav-slogan { font-size: .72rem; color: var(--muted); letter-spacing: 2px; text-transform: uppercase; }

.hero {
  text-align: center;
  padding: 2.5rem 2rem 1.5rem;
  background: radial-gradient(ellipse at 50% 0%, rgba(0,229,255,0.07) 0%, transparent 70%);
}
.hero h1 {
  font-family: 'Orbitron', sans-serif;
  font-size: clamp(2rem, 5vw, 4rem);
  font-weight: 900;
  color: var(--cyan);
  letter-spacing: 8px;
  text-shadow: 0 0 40px rgba(0,229,255,0.4), 0 0 80px rgba(0,229,255,0.15);
  margin: 0;
}
.hero-sub { font-size: .9rem; color: var(--muted); letter-spacing: 3px; text-transform: uppercase; margin-top: .5rem; }

.section-title {
  font-family: 'Orbitron', sans-serif;
  font-size: 1rem;
  font-weight: 700;
  color: var(--cyan);
  letter-spacing: 3px;
  text-transform: uppercase;
  padding: 1.5rem 2rem .5rem;
  display: flex;
  align-items: center;
  gap: .6rem;
}
.section-title::after {
  content: '';
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, var(--border), transparent);
  margin-left: .5rem;
}

.glass-card {
  background: rgba(6,24,40,0.85);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1.3rem 1.4rem;
  margin-bottom: 1rem;
  backdrop-filter: blur(8px);
}
.glass-card:hover { border-color: rgba(0,229,255,0.3); box-shadow: 0 0 18px rgba(0,229,255,0.07); }
.glass-card h4 {
  font-family: 'Orbitron', sans-serif;
  font-size: .8rem;
  color: var(--cyan);
  letter-spacing: 2px;
  margin: 0 0 .9rem;
}

.badge { display: inline-block; padding: 3px 11px; border-radius: 20px; font-size: .72rem; font-family: 'Orbitron', sans-serif; letter-spacing: 1px; font-weight: 700; }
.badge-ok   { background: rgba(0,255,157,0.12); color: var(--green); border: 1px solid rgba(0,255,157,0.3); }
.badge-warn { background: rgba(240,165,0,0.12); color: var(--gold);  border: 1px solid rgba(240,165,0,0.3); }
.badge-ban  { background: rgba(255,69,96,0.12);  color: var(--red);   border: 1px solid rgba(255,69,96,0.3); }

.stat-row { display: flex; gap: 1rem; flex-wrap: wrap; padding: 0 2rem 1.5rem; }
.stat-box { flex: 1; min-width: 120px; background: var(--bg2); border: 1px solid var(--border); border-radius: 10px; padding: 1rem; text-align: center; }
.stat-box .val { font-family: 'Orbitron', sans-serif; font-size: 1.6rem; font-weight: 700; color: var(--cyan); }
.stat-box .lbl { font-size: .68rem; color: var(--muted); letter-spacing: 1.5px; text-transform: uppercase; margin-top: .2rem; }

.fish-row { display: grid; grid-template-columns: 2.5fr 1.2fr 1fr 2fr; gap: .5rem; align-items: center; padding: .6rem .8rem; border-bottom: 1px solid rgba(255,255,255,0.04); font-size: .83rem; }
.fish-row:hover { background: rgba(0,229,255,0.04); }
.fish-row.header { font-family: 'Orbitron', sans-serif; font-size: .62rem; color: var(--muted); letter-spacing: 2px; border-bottom: 1px solid var(--border); }

.stButton > button {
  background: linear-gradient(135deg, #004d6e, #00b4cc) !important;
  color: #020d18 !important;
  font-family: 'Orbitron', sans-serif !important;
  font-size: .7rem !important;
  letter-spacing: 2px !important;
  border: none !important;
  border-radius: 6px !important;
  padding: .55rem 1.4rem !important;
  font-weight: 700 !important;
  box-shadow: 0 0 14px rgba(0,180,204,0.25) !important;
}
.stButton > button:hover { box-shadow: 0 0 26px rgba(0,229,255,0.45) !important; }

.stSelectbox > div > div,
.stMultiSelect > div > div,
.stDateInput > div > div { background: var(--bg2) !important; border: 1px solid var(--border) !important; border-radius: 6px !important; }

label { color: var(--muted) !important; font-size: .78rem !important; letter-spacing: 1px !important; }

.tip-item { display: flex; gap: .75rem; align-items: flex-start; padding: .55rem 0; border-bottom: 1px solid rgba(255,255,255,0.04); font-size: .84rem; }
.tip-icon { color: var(--cyan); font-size: .95rem; flex-shrink: 0; margin-top: .1rem; }

.result-header {
  background: linear-gradient(90deg, rgba(0,229,255,0.1), transparent);
  border-left: 3px solid var(--cyan);
  border-radius: 0 8px 8px 0;
  padding: .75rem 1.2rem;
  margin-bottom: 1rem;
  font-family: 'Orbitron', sans-serif;
  font-size: .82rem;
  color: var(--cyan);
  letter-spacing: 2px;
}

.zone-btn { margin-bottom: .4rem; }

hr { border-color: var(--border) !important; margin: .5rem 0 !important; }
.padded { padding: 0 2rem 2rem; }
.stAlert { border-radius: 8px !important; font-size: .84rem !important; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────────────────────────────────────

ZONES = {
    "Calanques National Park": {
        "lat": 43.215, "lon": 5.432,
        "depth": "5–40 m",
        "best_season": ["Spring", "Autumn"],
        "species": ["Loup / Bar", "Daurade royale", "Sar commun"],
        "restrictions": "Pas de pêche dans les zones MPA centrales. Vérifier les limites avant le départ.",
        "tip": "L'ancrage est interdit sur les herbiers de Posidonie. Utiliser les bouées.",
        "color": "#00e5ff",
        "difficulty": "Intermédiaire",
        "rating": "★★★★☆",
        "icon": "🏔️",
    },
    "Île de Riou": {
        "lat": 43.165, "lon": 5.385,
        "depth": "10–60 m",
        "best_season": ["Summer", "Autumn"],
        "species": ["Mérou brun", "Rascasse", "Congre"],
        "restrictions": "MPA partielle. Pas de chasse sous-marine dans les zones restreintes.",
        "tip": "Les tombants rocheux à l'est de Riou sont très productifs le matin.",
        "color": "#f0a500",
        "difficulty": "Expert",
        "rating": "★★★★★",
        "icon": "🏝️",
    },
    "Cap Couronne": {
        "lat": 43.328, "lon": 5.053,
        "depth": "3–25 m",
        "best_season": ["Spring", "Summer"],
        "species": ["Daurade royale", "Sar commun", "Loup / Bar"],
        "restrictions": "Réserve marine à proximité — vérifier les limites.",
        "tip": "Les zones sableuses entre les rochers retiennent les daurades tout l'été.",
        "color": "#00ff9d",
        "difficulty": "Débutant",
        "rating": "★★★☆☆",
        "icon": "⚓",
    },
    "Large Marseille (offshore)": {
        "lat": 43.10, "lon": 5.30,
        "depth": "50–300 m",
        "best_season": ["Summer"],
        "species": ["Thon rouge", "Corb"],
        "restrictions": "Carte quota thon rouge obligatoire. Radio VHF requise.",
        "tip": "Départ à l'aube pour le thon — mer calme indispensable.",
        "color": "#ff4560",
        "difficulty": "Expert",
        "rating": "★★★★★",
        "icon": "🌊",
    },
    "Côte Bleue – Port de Bouc": {
        "lat": 43.40, "lon": 5.10,
        "depth": "5–30 m",
        "best_season": ["Spring", "Autumn", "Winter"],
        "species": ["Rascasse", "Congre", "Sar commun"],
        "restrictions": "Réglementation générale de pêche applicable.",
        "tip": "La pêche hivernale est sous-estimée ici — moins de pression, de bonnes prises.",
        "color": "#b48aff",
        "difficulty": "Débutant",
        "rating": "★★★☆☆",
        "icon": "🏖️",
    },
}

SPECIES_DB = {
    "Mérou brun (Grouper)": {
        "status": "restricted", "min_size_cm": 45,
        "season_closed": "Toute l'année (quota)",
        "notes": "Protégé en zones MPA. Max 1/jour hors MPA.", "emoji": "🐟",
    },
    "Loup / Bar (Sea Bass)": {
        "status": "allowed", "min_size_cm": 42,
        "season_closed": "Jan–Fév (ponte)",
        "notes": "Commun sur les côtes rocheuses. Meilleur à l'aube.", "emoji": "🐠",
    },
    "Daurade royale (Gilt-head Bream)": {
        "status": "allowed", "min_size_cm": 20,
        "season_closed": "Aucune",
        "notes": "Très populaire. Abondante printemps–automne.", "emoji": "🐡",
    },
    "Rascasse (Scorpionfish)": {
        "status": "allowed", "min_size_cm": 25,
        "season_closed": "Aucune",
        "notes": "Épineuse — manipuler avec précaution! Fonds rocheux.", "emoji": "🐠",
    },
    "Grande Nacre (Noble Pen Shell)": {
        "status": "protected", "min_size_cm": None,
        "season_closed": "Toute l'année",
        "notes": "En danger critique. Signaler les observations.", "emoji": "🐚",
    },
    "Corb (Brown Meagre)": {
        "status": "restricted", "min_size_cm": 30,
        "season_closed": "Avril–Juin",
        "notes": "Espèce vulnérable. Envisager la remise à l'eau.", "emoji": "🐟",
    },
    "Thon rouge (Bluefin Tuna)": {
        "status": "restricted", "min_size_cm": 115,
        "season_closed": "Quota annuel DPMA",
        "notes": "Carte quota requise. Règles très strictes.", "emoji": "🐟",
    },
    "Sar commun (White Seabream)": {
        "status": "allowed", "min_size_cm": 23,
        "season_closed": "Aucune",
        "notes": "Abondant dans les Calanques. Idéal débutants.", "emoji": "🐡",
    },
    "Congre (European Conger)": {
        "status": "allowed", "min_size_cm": 58,
        "season_closed": "Aucune",
        "notes": "Pêche nocturne près des rochers. Hameçons solides.", "emoji": "🐍",
    },
    "Grande cigale (Slipper Lobster)": {
        "status": "protected", "min_size_cm": None,
        "season_closed": "Toute l'année",
        "notes": "Totalement protégée en France. Zéro prélèvement.", "emoji": "🦞",
    },
}

SEASON_TIPS = {
    "Spring":  ["Les daurades et bars remontent vers la côte — cibler les récifs à 5–15 m.",
                "Eau qui se réchauffe : les poissons sont actifs et s'alimentent.",
                "Éviter de déranger les regroupements de ponte près des herbiers."],
    "Summer":  ["Aube et crépuscule sont les meilleures fenêtres — la chaleur de mi-journée ralentit.",
                "Saison thon rouge offshore : vérifier la validité de votre carte quota.",
                "Hydratation et protection solaire. Vérifier les conditions avant le départ."],
    "Autumn":  ["Meilleure saison globale en Méditerranée. Nombreuses espèces à leur pic de poids.",
                "Les mérous sont plus actifs — pêcher les structures rocheuses profondes.",
                "Vent Mistral : vérifier les prévisions, les conditions peuvent changer vite."],
    "Winter":  ["Le congre et la rascasse sont des cibles fiables toute l'année.",
                "Moins de pêcheurs = moins de pression sur les populations de poissons.",
                "Vêtements en couches. Eau <14 °C : vigilance si vous tombez à l'eau."],
}

WEATHER_LABELS = {
    "Calme (< 2 Bft)":         ("ok",   "✅ Excellent — toutes zones accessibles."),
    "Brise légère (2–3 Bft)":  ("ok",   "✅ Bon — idéal côtier et offshore."),
    "Modéré (4 Bft)":          ("warn", "⚠️ Prudence offshore. Zones côtières OK."),
    "Frais / Mistral (5 Bft)": ("ban",  "❌ Offshore déconseillé. Rester dans les criques."),
    "Fort / Tempête (6+ Bft)": ("ban",  "❌ Ne pas sortir. Sécurité avant tout."),
}

SUSTAINABLE_TIPS = [
    "Utiliser des hameçons sans ardillon si possible — remise à l'eau facilitée.",
    "Mesurer chaque poisson avant de le garder. Remettre les individus trop petits à l'eau.",
    "Ne jamais jeter du fil monofilament en mer — il tue les oiseaux et tortues.",
    "Limiter votre prise à ce que vous consommerez réellement.",
    "Éviter de mouiller l'ancre sur les herbiers de Posidonie — une décennie à se remettre.",
    "Signaler la pêche illégale au ☎️ 17 ou à la DDTM.",
    "Photographier et relâcher les spécimens rares ou de grande taille.",
    "Ramener vos déchets à terre — zéro plastique en mer.",
]

def get_season():
    m = datetime.date.today().month
    if m in (3,4,5):   return "Spring"
    if m in (6,7,8):   return "Summer"
    if m in (9,10,11): return "Autumn"
    return "Winter"

def badge(status):
    d = {
        "allowed":    ("badge-ok",   "✅ AUTORISÉ"),
        "restricted": ("badge-warn", "⚠️ RESTREINT"),
        "protected":  ("badge-ban",  "🚫 PROTÉGÉ"),
    }
    cls, lbl = d.get(status, ("badge-ok", "?"))
    return f'<span class="badge {cls}">{lbl}</span>'

# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
if "page"       not in st.session_state: st.session_state.page       = "Carte"
if "sel_zone"   not in st.session_state: st.session_state.sel_zone   = None
if "sp_checked" not in st.session_state: st.session_state.sp_checked = None

# ─────────────────────────────────────────────────────────────────────────────
# NAV BAR (visual only)
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="nav-bar">
  <div>
    <div class="nav-logo">🦈 AQUASHARK</div>
    <div class="nav-slogan">Fish better · Protect more · Thanks to AI</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# TAB NAV (functional)
# ─────────────────────────────────────────────────────────────────────────────
pages      = ["Carte", "Planificateur", "Espèces", "Conseiller IA"]
page_icons = {"Carte": "🗺️", "Planificateur": "📋", "Espèces": "🐟", "Conseiller IA": "🤖"}

tab_cols = st.columns(len(pages))
for i, p in enumerate(pages):
    with tab_cols[i]:
        if st.button(f"{page_icons[p]} {p}", use_container_width=True, key=f"nav_{p}"):
            st.session_state.page = p
            st.rerun()

page = st.session_state.page

# ─────────────────────────────────────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div style="font-size:2.5rem">🦈</div>
  <h1>AQUASHARK</h1>
  <div class="hero-sub">Fish better &nbsp;·&nbsp; Protect more &nbsp;·&nbsp; Thanks to AI</div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# STATS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stat-row">
  <div class="stat-box"><div class="val">5</div><div class="lbl">Zones de pêche</div></div>
  <div class="stat-box"><div class="val">10</div><div class="lbl">Espèces référencées</div></div>
  <div class="stat-box"><div class="val">3</div><div class="lbl">Espèces protégées</div></div>
  <div class="stat-box"><div class="val">4</div><div class="lbl">Saisons couvertes</div></div>
  <div class="stat-box"><div class="val">∞</div><div class="lbl">Conseils IA</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ═════════════════════════════════════════════════════════════════════════════
# PAGE : CARTE
# ═════════════════════════════════════════════════════════════════════════════
if page == "Carte":
    st.markdown('<div class="section-title">🗺️ Carte interactive des zones de pêche</div>', unsafe_allow_html=True)

    map_col, info_col = st.columns([3, 2], gap="medium")

    with map_col:
        try:
            import folium
            from streamlit_folium import st_folium

            m = folium.Map(
                location=[43.25, 5.28],
                zoom_start=11,
                tiles="CartoDB dark_matter",
            )

            for zname, z in ZONES.items():
                c = z["color"]
                popup_html = f"""
                <div style='font-family:sans-serif;min-width:210px;background:#061828;
                            color:#cce8f4;padding:12px;border-radius:8px;border:1px solid {c}'>
                  <b style='color:{c};font-size:14px'>{z['icon']} {zname}</b><br><br>
                  <span style='color:#5a8aa0;font-size:12px'>🌊 Profondeur : {z['depth']}</span><br>
                  <span style='color:#5a8aa0;font-size:12px'>📊 Difficulté : {z['difficulty']}</span><br>
                  <span style='color:#5a8aa0;font-size:12px'>⭐ {z['rating']}</span><br><br>
                  <span style='font-size:12px'>🐟 {', '.join(z['species'])}</span><br><br>
                  <span style='color:#f0a500;font-size:11px'>⚠️ {z['restrictions'][:70]}...</span>
                </div>"""

                # Outer glow ring
                folium.CircleMarker(
                    location=[z["lat"], z["lon"]],
                    radius=22,
                    color=c,
                    fill=True,
                    fill_color=c,
                    fill_opacity=0.12,
                    weight=1.5,
                    popup=folium.Popup(popup_html, max_width=290),
                    tooltip=folium.Tooltip(
                        f"<span style='font-family:sans-serif;color:{c};font-size:13px'>"
                        f"{z['icon']} <b>{zname}</b><br>"
                        f"<span style='color:#cce8f4;font-size:11px'>{z['rating']} · {z['difficulty']}</span></span>",
                        sticky=False,
                    ),
                ).add_to(m)

                # Middle ring
                folium.CircleMarker(
                    location=[z["lat"], z["lon"]],
                    radius=12,
                    color=c,
                    fill=True,
                    fill_color=c,
                    fill_opacity=0.2,
                    weight=2,
                ).add_to(m)

                # Centre dot
                folium.CircleMarker(
                    location=[z["lat"], z["lon"]],
                    radius=5,
                    color=c,
                    fill=True,
                    fill_color=c,
                    fill_opacity=1.0,
                    weight=0,
                ).add_to(m)

                # Zone label
                folium.Marker(
                    location=[z["lat"] + 0.012, z["lon"]],
                    icon=folium.DivIcon(
                        html=f"""<div style='font-family:sans-serif;font-size:11px;font-weight:700;
                                 color:{c};text-shadow:0 0 6px #020d18,0 0 3px #020d18;
                                 white-space:nowrap;text-align:center'>{z['icon']} {zname}</div>""",
                        icon_size=(200, 20),
                        icon_anchor=(100, 10),
                    ),
                ).add_to(m)

            map_data = st_folium(m, width="100%", height=540,
                                 returned_objects=["last_object_clicked_tooltip"])

            # Detect zone click via tooltip text
            if map_data and map_data.get("last_object_clicked_tooltip"):
                tip = map_data["last_object_clicked_tooltip"]
                for zname in ZONES:
                    if zname in tip:
                        st.session_state.sel_zone = zname
                        break

        except ImportError:
            st.warning("📦 **Carte non disponible.** Ajouter `folium` et `streamlit-folium` à requirements.txt, puis redéployer.")
            sel = st.selectbox("Sélectionner une zone manuellement", list(ZONES.keys()))
            if st.button("Voir cette zone"):
                st.session_state.sel_zone = sel
                st.rerun()

    with info_col:
        st.markdown("#### 📍 Sélectionner une zone")
        for zname, z in ZONES.items():
            if st.button(f"{z['icon']} {zname}  {z['rating']}", key=f"zone_{zname}", use_container_width=True):
                st.session_state.sel_zone = zname
                st.rerun()

        if st.session_state.sel_zone:
            z     = ZONES[st.session_state.sel_zone]
            zname = st.session_state.sel_zone
            c     = z["color"]
            st.markdown("---")
            st.markdown(f"""
            <div class="glass-card" style="border-left:3px solid {c}">
              <h4>{z['icon']} {zname.upper()}</h4>
              <table style="width:100%;font-size:.81rem;border-collapse:collapse">
                <tr>
                  <td style="color:var(--muted);padding:5px 0;width:45%">📊 Difficulté</td>
                  <td style="color:var(--text)">{z['difficulty']}</td>
                </tr>
                <tr>
                  <td style="color:var(--muted);padding:5px 0">🌊 Profondeur</td>
                  <td style="color:var(--text)">{z['depth']}</td>
                </tr>
                <tr>
                  <td style="color:var(--muted);padding:5px 0">📅 Meilleures saisons</td>
                  <td style="color:var(--text)">{', '.join(z['best_season'])}</td>
                </tr>
                <tr>
                  <td style="color:var(--muted);padding:5px 0">⭐ Note</td>
                  <td style="color:#f0a500">{z['rating']}</td>
                </tr>
              </table>

              <div style="margin-top:.9rem;padding-top:.9rem;border-top:1px solid var(--border)">
                <span style="color:var(--muted);font-size:.72rem;letter-spacing:1px">🐟 ESPÈCES PRÉSENTES</span><br>
                <span style="font-size:.83rem">{' &nbsp;·&nbsp; '.join(z['species'])}</span>
              </div>

              <div style="margin-top:.8rem;padding:.7rem;background:rgba(255,69,96,0.07);border-radius:6px;border:1px solid rgba(255,69,96,0.2)">
                <span style="color:#ff4560;font-size:.7rem;letter-spacing:1px">⚠️ RÉGLEMENTATION</span><br>
                <span style="font-size:.8rem">{z['restrictions']}</span>
              </div>

              <div style="margin-top:.7rem;padding:.7rem;background:rgba(0,229,255,0.05);border-radius:6px;border:1px solid var(--border)">
                <span style="color:var(--cyan);font-size:.7rem;letter-spacing:1px">💡 CONSEIL LOCAL</span><br>
                <span style="font-size:.8rem">{z['tip']}</span>
              </div>
            </div>
            """, unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════════════════════
# PAGE : PLANIFICATEUR
# ═════════════════════════════════════════════════════════════════════════════
elif page == "Planificateur":
    st.markdown('<div class="section-title">📋 Planificateur de sortie</div>', unsafe_allow_html=True)
    st.markdown('<div class="padded">', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        season  = st.selectbox("🌿 Saison", ["Spring","Summer","Autumn","Winter"],
                               index=["Spring","Summer","Autumn","Winter"].index(get_season()))
        weather = st.selectbox("🌬️ Conditions de mer", list(WEATHER_LABELS.keys()))
    with c2:
        zone   = st.selectbox("📍 Zone de pêche", list(ZONES.keys()))
        target = st.multiselect("🎯 Espèces ciblées (optionnel)", list(SPECIES_DB.keys()))
    with c3:
        experience = st.selectbox("🎓 Niveau", ["Débutant","Intermédiaire","Expert"])
        trip_date  = st.date_input("📅 Date de sortie", datetime.date.today())

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🚀 GÉNÉRER MON PLAN DE SORTIE", use_container_width=False):
        z              = ZONES[zone]
        w_type, w_msg  = WEATHER_LABELS[weather]

        st.markdown("---")
        st.markdown(f'<div class="result-header">📋 VOTRE PLAN — {zone.upper()}</div>', unsafe_allow_html=True)

        if w_type == "ok":    st.success(w_msg)
        elif w_type == "warn": st.warning(w_msg)
        else:                  st.error(w_msg)

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"""
            <div class="glass-card">
              <h4>📍 INFORMATIONS DE ZONE</h4>
              <div class="tip-item"><span class="tip-icon">🌊</span><span>Profondeur : <b>{z['depth']}</b></span></div>
              <div class="tip-item"><span class="tip-icon">📅</span><span>Meilleures saisons : <b>{', '.join(z['best_season'])}</b></span></div>
              <div class="tip-item"><span class="tip-icon">⚠️</span><span>{z['restrictions']}</span></div>
              <div class="tip-item"><span class="tip-icon">💡</span><span>{z['tip']}</span></div>
            </div>""", unsafe_allow_html=True)

        with col_b:
            sp_html = '<div class="glass-card"><h4>🐟 ESPÈCES EN ZONE</h4>'
            for sp_short in z["species"]:
                full = next((k for k in SPECIES_DB if sp_short in k), None)
                if full:
                    info = SPECIES_DB[full]
                    b    = badge(info["status"])
                    sz   = f"{info['min_size_cm']} cm" if info["min_size_cm"] else "N/A"
                    sp_html += f'<div class="tip-item"><span>{info["emoji"]} {full}</span>&nbsp;{b}&nbsp;<span style="color:var(--muted);font-size:.78rem">min {sz}</span></div>'
            sp_html += "</div>"
            st.markdown(sp_html, unsafe_allow_html=True)

        if target:
            st.markdown("#### 🎯 Vérification de vos espèces cibles")
            for sp in target:
                info = SPECIES_DB[sp]
                if info["status"] == "protected":
                    st.error(f"🚫 **{sp}** — Totalement protégée. Ne pas cibler ni conserver.")
                elif info["status"] == "restricted":
                    st.warning(f"⚠️ **{sp}** — Restreinte. Fermeture : {info['season_closed']}. {info['notes']}")
                else:
                    st.success(f"✅ **{sp}** — Autorisée. Taille min : {info['min_size_cm']} cm. {info['notes']}")

        tips_html = f'<div class="glass-card"><h4>🌿 CONSEILS {season.upper()}</h4>'
        for tip in SEASON_TIPS[season]:
            tips_html += f'<div class="tip-item"><span class="tip-icon">›</span><span>{tip}</span></div>'
        tips_html += "</div>"
        st.markdown(tips_html, unsafe_allow_html=True)

        if experience == "Débutant":
            st.info("🎓 **Conseil débutant :** Commencez par la Daurade ou le Sar dans des zones côtières calmes. Montage de fond simple avec ver ou crevette. Ayez toujours votre licence de pêche.")

        st.markdown(f'<div class="glass-card"><h4>♻️ CONSEIL DU JOUR</h4><div class="tip-item"><span class="tip-icon">🌱</span><span>{random.choice(SUSTAINABLE_TIPS)}</span></div></div>', unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════════════════════
# PAGE : ESPÈCES
# ═════════════════════════════════════════════════════════════════════════════
elif page == "Espèces":
    st.markdown('<div class="section-title">🐟 Espèces & Réglementation</div>', unsafe_allow_html=True)
    st.markdown('<div class="padded">', unsafe_allow_html=True)

    col_sel, col_info = st.columns([1, 2])
    with col_sel:
        sel = st.selectbox("Choisir une espèce", list(SPECIES_DB.keys()))
        if st.button("🔍 VÉRIFIER LES RÈGLES", use_container_width=True):
            st.session_state.sp_checked = sel

    if st.session_state.sp_checked:
        sp   = st.session_state.sp_checked
        info = SPECIES_DB[sp]
        with col_info:
            b = badge(info["status"])
            st.markdown(f"""
            <div class="glass-card">
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:.8rem">
                <span style="font-size:2.2rem">{info['emoji']}</span>
                {b}
              </div>
              <div style="font-family:'Orbitron',sans-serif;font-size:1rem;color:var(--cyan);margin-bottom:1rem;letter-spacing:1px">{sp}</div>
              <div class="tip-item"><span class="tip-icon">📏</span><span>Taille min. légale : <b>{f"{info['min_size_cm']} cm" if info['min_size_cm'] else "Ne pas prélever"}</b></span></div>
              <div class="tip-item"><span class="tip-icon">📅</span><span>Fermeture : <b>{info['season_closed']}</b></span></div>
              <div class="tip-item"><span class="tip-icon">📝</span><span>{info['notes']}</span></div>
            </div>""", unsafe_allow_html=True)
            if info["status"] == "protected":
                st.error("🚫 Totalement protégée. Toute capture, détention ou vente est illégale. Remise à l'eau immédiate si capture accidentelle.")
            elif info["status"] == "restricted":
                st.warning("⚠️ Espèce restreinte. Règles spéciales applicables. Vérifier la réglementation en vigueur.")
            else:
                st.success("✅ Pêche récréative autorisée dans les limites légales indiquées.")

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<div class="section-title">📋 Tableau de référence complet</div>', unsafe_allow_html=True)
    st.markdown('<div class="padded">', unsafe_allow_html=True)

    st.markdown('<div class="fish-row header"><span>Espèce</span><span>Statut</span><span>Taille min.</span><span>Fermeture</span></div>', unsafe_allow_html=True)
    for sp, info in SPECIES_DB.items():
        b  = badge(info["status"])
        sz = f"{info['min_size_cm']} cm" if info["min_size_cm"] else "—"
        st.markdown(f"""
        <div class="fish-row">
          <span>{info['emoji']} {sp}</span>
          <span>{b}</span>
          <span>{sz}</span>
          <span style="color:var(--muted);font-size:.78rem">{info['season_closed']}</span>
        </div>""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ═════════════════════════════════════════════════════════════════════════════
# PAGE : CONSEILLER IA
# ═════════════════════════════════════════════════════════════════════════════
elif page == "Conseiller IA":
    st.markdown('<div class="section-title">🤖 Conseiller IA personnalisé</div>', unsafe_allow_html=True)
    st.markdown('<div class="padded">', unsafe_allow_html=True)

    with st.form("advisor"):
        c1, c2 = st.columns(2)
        with c1:
            a_season  = st.selectbox("🌿 Saison actuelle", ["Spring","Summer","Autumn","Winter"],
                                     index=["Spring","Summer","Autumn","Winter"].index(get_season()))
            a_weather = st.selectbox("🌬️ Conditions", list(WEATHER_LABELS.keys()))
            a_exp     = st.selectbox("🎓 Niveau", ["Débutant","Intermédiaire","Expert"])
        with c2:
            a_goal = st.selectbox("🎯 Objectif principal", [
                "Bonne quantité de prises", "Trophée / grand poisson",
                "Sortie en famille", "Apprendre la pêche durable", "Pêche de nuit"])
            a_gear = st.multiselect("🎣 Équipement disponible",
                ["Canne de bord / rocher","Bateau","Kayak","Canne à lancer","Bas de ligne fond","Pêche aux leurres"],
                default=["Canne de bord / rocher","Bas de ligne fond"])
            a_time = st.selectbox("⏱️ Temps disponible", ["Demi-journée (<4h)","Journée complète","Nuit"])
        go = st.form_submit_button("🤖 OBTENIR MA RECOMMANDATION", use_container_width=True)

    if go:
        # Score zones
        scored = []
        for zname, z in ZONES.items():
            s = 0
            if a_season in z["best_season"]:                                          s += 3
            if "Bateau" in a_gear or "Kayak" in a_gear:                              s += 1
            if a_exp == "Débutant" and "Calanques" in zname:                         s += 2
            if a_exp == "Expert"   and "offshore" in zname.lower():                  s += 2
            if a_goal == "Trophée / grand poisson" and "offshore" in zname.lower():  s += 2
            if a_goal == "Sortie en famille"       and "offshore" not in zname.lower(): s += 2
            if a_goal == "Pêche de nuit"           and "Bouc" in zname:              s += 2
            if "offshore" in zname.lower() and "Mistral" in a_weather:               s -= 5
            if "offshore" in zname.lower() and "Tempête" in a_weather:               s -= 5
            scored.append((s, zname))
        scored.sort(reverse=True)
        best_name = scored[0][1]
        best      = ZONES[best_name]
        w_type, w_msg = WEATHER_LABELS[a_weather]

        st.markdown("---")
        st.markdown(f'<div class="result-header">🤖 RECOMMANDATION IA — {best_name.upper()}</div>', unsafe_allow_html=True)

        if w_type == "ok":    st.success(w_msg)
        elif w_type == "warn": st.warning(w_msg)
        else:                  st.error(w_msg)

        col_r1, col_r2 = st.columns(2)
        with col_r1:
            match = "✅ En saison" if a_season in best["best_season"] else "⚠️ Hors saison optimale"
            st.markdown(f"""
            <div class="glass-card" style="border-left:3px solid {best['color']}">
              <h4>{best['icon']} ZONE RECOMMANDÉE</h4>
              <div class="tip-item"><span class="tip-icon">📅</span><span>Saison : <b>{match}</b></span></div>
              <div class="tip-item"><span class="tip-icon">🌊</span><span>Profondeur : <b>{best['depth']}</b></span></div>
              <div class="tip-item"><span class="tip-icon">⭐</span><span>Note : <b style="color:#f0a500">{best['rating']}</b></span></div>
              <div class="tip-item"><span class="tip-icon">⚠️</span><span>{best['restrictions']}</span></div>
              <div class="tip-item"><span class="tip-icon">💡</span><span>{best['tip']}</span></div>
            </div>""", unsafe_allow_html=True)

        with col_r2:
            sp_html2 = '<div class="glass-card"><h4>🎯 ESPÈCES À CIBLER</h4>'
            for sp_short in best["species"]:
                full = next((k for k in SPECIES_DB if sp_short in k), None)
                if full:
                    info = SPECIES_DB[full]
                    b2   = badge(info["status"])
                    note = "→ Ne pas cibler" if info["status"] == "protected" else f"min {info['min_size_cm']} cm" if info["min_size_cm"] else ""
                    col_note = "color:var(--red)" if info["status"] == "protected" else "color:var(--muted)"
                    sp_html2 += f'<div class="tip-item"><span>{info["emoji"]} {full}</span>&nbsp;{b2}&nbsp;<span style="{col_note};font-size:.78rem">{note}</span></div>'
            sp_html2 += "</div>"
            st.markdown(sp_html2, unsafe_allow_html=True)

        # Gear tips
        gear_tips = []
        if "Bas de ligne fond"   in a_gear: gear_tips.append("🪝 Bas de ligne fond : hameçons 2–4 avec ver, crevette ou encornet.")
        if "Pêche aux leurres"   in a_gear: gear_tips.append("🎣 Leurres souples en couleurs naturelles (brun, olive) — efficaces sur bar et daurade.")
        if "Canne à lancer"      in a_gear: gear_tips.append("🎯 Lancer le long des bords rocheux et récupération lente — idéal pour le bar.")
        if gear_tips:
            g_html = '<div class="glass-card"><h4>🎣 CONSEILS ÉQUIPEMENT</h4>'
            for gt in gear_tips:
                g_html += f'<div class="tip-item"><span class="tip-icon">›</span><span>{gt}</span></div>'
            g_html += "</div>"
            st.markdown(g_html, unsafe_allow_html=True)

        time_map = {
            "Demi-journée (<4h)": "Arriver à l'aube, pêcher les 3 premières heures de lumière — fenêtre la plus productive.",
            "Journée complète":   "Pêcher intensément à l'aube et au crépuscule. Repos ou changement de zone en milieu de journée.",
            "Nuit":               "Monter les lignes nocturnes pour congre et rascasse. Lampe frontale et vêtements chauds obligatoires.",
        }
        st.markdown(f'<div class="glass-card"><h4>⏱️ PLAN HORAIRE</h4><div class="tip-item"><span class="tip-icon">›</span><span>{time_map[a_time]}</span></div></div>', unsafe_allow_html=True)

        s_html = f'<div class="glass-card"><h4>🌿 CONSEILS {a_season.upper()}</h4>'
        for t in SEASON_TIPS[a_season]:
            s_html += f'<div class="tip-item"><span class="tip-icon">›</span><span>{t}</span></div>'
        s_html += "</div>"
        st.markdown(s_html, unsafe_allow_html=True)

        alt_html = '<div class="glass-card"><h4>🗺️ ZONES ALTERNATIVES</h4>'
        for _, zn in scored[1:3]:
            alt_html += f'<div class="tip-item"><span class="tip-icon">{ZONES[zn]["icon"]}</span><span><b>{zn}</b> — {ZONES[zn]["tip"]}</span></div>'
        alt_html += "</div>"
        st.markdown(alt_html, unsafe_allow_html=True)

        picks    = random.sample(SUSTAINABLE_TIPS, 3)
        su_html  = '<div class="glass-card"><h4>♻️ ENGAGEMENTS DURABLES</h4>'
        for p in picks:
            su_html += f'<div class="tip-item"><span class="tip-icon">🌱</span><span>{p}</span></div>'
        su_html += "</div>"
        st.markdown(su_html, unsafe_allow_html=True)

        st.success("✅ Recommandation générée. Bonne pêche et protégez la Méditerranée !")

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<div class="section-title">♻️ Charte de pêche durable</div>', unsafe_allow_html=True)
    st.markdown('<div class="padded">', unsafe_allow_html=True)
    ch_html = '<div class="glass-card">'
    for tip in SUSTAINABLE_TIPS:
        ch_html += f'<div class="tip-item"><span class="tip-icon">🌱</span><span>{tip}</span></div>'
    ch_html += "</div>"
    st.markdown(ch_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:2rem;color:#2a5070;font-size:.72rem;
            letter-spacing:1.5px;border-top:1px solid rgba(0,229,255,0.08);margin-top:2rem">
  AQUASHARK © 2025 &nbsp;·&nbsp; Basé sur la réglementation française & UE 2024
  &nbsp;·&nbsp; Vérifier toujours auprès des sources officielles avant de pêcher
</div>
""", unsafe_allow_html=True)
