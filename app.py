
import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="TechBridge",
    page_icon="🚀",
    layout="wide"
)

# =========================
# BACKGROUND & GLOBAL CSS
# =========================

st.markdown(
    """
    <style>

    /* =========================
       MAIN BLACK + GREY + GOLD THEME
       ========================= */

    .stApp {
        background:
            radial-gradient(circle at top right, rgba(212, 175, 55, 0.08), transparent 28%),
            radial-gradient(circle at bottom left, rgba(100, 100, 100, 0.08), transparent 30%),
            #080808;
        color: #ffffff;
    }

    [data-testid="stHeader"] {
        background-color: #080808;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* =========================
       MAIN HEADINGS
       ========================= */

    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
        font-weight: 700 !important;
        letter-spacing: 0.3px;
    }

    h1 {
        text-shadow: 0 0 18px rgba(212, 175, 55, 0.12);
    }

    p {
        color: #d0d0d0;
    }

    /* =========================
       GOLD ACCENT
       ========================= */

    .stCaption {
        color: #bdbdbd !important;
    }

    hr {
        border: none !important;
        height: 1px !important;
        background: linear-gradient(
            90deg,
            transparent,
            #555555,
            #d4af37,
            #555555,
            transparent
        ) !important;
        margin: 28px 0 !important;
    }

    /* =========================
       TEAM CARDS
       ========================= */

    .team-card {
        background:
            linear-gradient(
                145deg,
                #151515,
                #0d0d0d
            );
        border: 1px solid #3d3d3d;
        border-radius: 18px;
        padding: 28px;
        min-height: 470px;

        box-shadow:
            0px 8px 30px rgba(0, 0, 0, 0.55),
            inset 0 1px 0 rgba(255, 255, 255, 0.03);

        transition:
            transform 0.25s ease,
            border-color 0.25s ease,
            box-shadow 0.25s ease;
    }

    .team-card:hover {
        transform: translateY(-5px);
        border-color: #d4af37;

        box-shadow:
            0px 12px 35px rgba(0, 0, 0, 0.65),
            0 0 22px rgba(212, 175, 55, 0.08);
    }

    .team-card h3 {
        color: #ffffff !important;
        margin-bottom: 8px;
    }

    .team-role {
        color: #d4af37;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 18px;
        letter-spacing: 0.2px;
    }

    .team-card p {
        color: #d2d2d2;
        line-height: 1.75;
        font-size: 15px;
    }

    /* =========================
       SERVICE CARDS
       ========================= */

    .service-card {
        background:
            linear-gradient(
                145deg,
                #151515,
                #0d0d0d
            );

        border: 1px solid #3b3b3b;
        border-radius: 18px;
        padding: 25px;
        min-height: 220px;

        box-shadow:
            0px 7px 25px rgba(0, 0, 0, 0.5),
            inset 0 1px 0 rgba(255, 255, 255, 0.025);

        transition:
            transform 0.25s ease,
            border-color 0.25s ease,
            box-shadow 0.25s ease;
    }

    .service-card:hover {
        transform: translateY(-5px);
        border-color: #d4af37;

        box-shadow:
            0px 10px 30px rgba(0, 0, 0, 0.6),
            0 0 20px rgba(212, 175, 55, 0.08);
    }

    .service-card h3 {
        color: #ffffff !important;
        margin-bottom: 12px;
    }

    .service-card p {
        color: #cfcfcf;
        line-height: 1.7;
    }

    /* =========================
       BUTTONS
       ========================= */

    .stButton > button,
    .stLinkButton > a {
        background: linear-gradient(
            135deg,
            #d4af37,
            #b9962e
        ) !important;

        color: #080808 !important;

        border: 1px solid #d4af37 !important;
        border-radius: 10px !important;

        font-weight: 700 !important;
        letter-spacing: 0.2px;

        box-shadow:
            0 4px 15px rgba(212, 175, 55, 0.12);

        transition:
            all 0.25s ease;
    }

    .stButton > button:hover,
    .stLinkButton > a:hover {
        background: linear-gradient(
            135deg,
            #e2c35a,
            #d4af37
        ) !important;

        color: #000000 !important;

        border-color: #f0d878 !important;

        transform: translateY(-2px);

        box-shadow:
            0 7px 22px rgba(212, 175, 55, 0.2);
    }

    /* =========================
       METRIC BOX
       ========================= */

    [data-testid="stMetric"] {
        background:
            linear-gradient(
                145deg,
                #171717,
                #0d0d0d
            );

        border: 1px solid #3d3d3d;
        border-radius: 18px;
        padding: 25px;

        box-shadow:
            0 8px 28px rgba(0, 0, 0, 0.5);
    }

    [data-testid="stMetricLabel"] {
        color: #bcbcbc !important;
    }

    [data-testid="stMetricValue"] {
        color: #d4af37 !important;
        font-weight: 800 !important;
    }

    /* =========================
       INFO / SUCCESS BOX
       ========================= */

    [data-testid="stAlert"] {
        background-color: #151515 !important;
        border: 1px solid #3e3e3e !important;
        color: #dddddd !important;
        border-radius: 12px !important;
    }

    /* =========================
       LINKS
       ========================= */

    a {
        color: #d4af37 !important;
    }

    a:hover {
        color: #f0d878 !important;
    }

    /* =========================
       FOOTER
       ========================= */

    [data-testid="stCaptionContainer"] {
        color: #999999;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# NAVBAR
# =========================

st.title("TechBridge")

st.caption("AI • Web Development • Digital Marketing")

st.divider()

# =========================
# HERO
# =========================

left, right = st.columns(2)

with left:

    st.header("Building The")
    st.header("Digital Future")

    st.write(
        "TechBridge is a modern technology and digital marketing "
        "company focused on AI, web development and digital "
        "marketing solutions."
    )

    if st.button("🚀 Explore Services"):
        st.success("Our services are below!")

    # =========================
    # CONTACT US
    # =========================

    if st.button("📞 Contact Us"):

        st.info("Choose who you want to contact:")

        contact1, contact2 = st.columns(2)

        with contact1:

            st.link_button(
                "👨‍💻 Contact Mohammad Hunza",
                "https://wa.me/923192200926",
                use_container_width=True
            )

        with contact2:

            st.link_button(
                "👨‍💼 Contact Syed Khizar",
                "https://wa.me/923146864935",
                use_container_width=True
            )

with right:

    st.metric(
        label="TechBridge",
        value="TB"
    )

# =========================
# SERVICES
# =========================

st.divider()

st.header("Our Services")

st.write(
    "Professional digital solutions for modern businesses."
)

service1, service2, service3 = st.columns(3)

with service1:

    st.markdown(
        """
        <div class="service-card">

        <h3>🤖 AI Solutions</h3>

        <p>
        Smart AI-powered solutions and automation systems
        designed to make businesses more efficient and
        productive.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

with service2:

    st.markdown(
        """
        <div class="service-card">

        <h3>💻 Web Development</h3>

        <p>
        Modern, responsive and user-friendly websites
        for businesses, brands and startups.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

with service3:

    st.markdown(
        """
        <div class="service-card">

        <h3>📈 Digital Marketing</h3>

        <p>
        Digital marketing and social media strategies
        designed to help businesses build their online
        presence and grow.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# ABOUT
# =========================

st.divider()

st.header("About TechBridge")

st.write(
    "TechBridge is a modern technology and digital marketing "
    "company focused on creating useful digital solutions "
    "for businesses."
)

st.write(
    "Our goal is to combine technology, creativity and "
    "digital strategy to help businesses grow."
)

st.write(
    "We provide high-quality digital solutions at affordable, "
    "low-budget prices, making professional technology "
    "accessible to businesses of all sizes."
)

# =========================
# MISSION
# =========================

st.subheader("🎯 Our Mission")

st.info(
    "To provide innovative, reliable and affordable "
    "digital solutions that help businesses grow."
)

# =========================
# TEAM
# =========================

st.divider()

st.header("Meet Our Team")

st.write(
    "Meet the people behind TechBridge, combining technology, "
    "AI, web development and digital marketing to create "
    "modern digital solutions."
)

team1, team2 = st.columns(2)

# =========================
# MOHAMMAD HUNZA
# =========================

with team1:

    st.markdown(
        """
        <div class="team-card">

        <h3>👨‍💻 Mohammad Hunza</h3>

        <div class="team-role">
        CEO & AI / Web Developer
        </div>

        <p>
        Mohammad Hunza is the CEO of TechBridge and a passionate
        learner in AI, programming and modern Web Development.
        He focuses on building modern websites, AI-powered
        applications and useful digital solutions for businesses.
        </p>

        <p>
        He has completed his Matriculation in Computer Science
        and has completed his First Year in Computer Science.
        He is currently a Second Year student and is continuing
        to develop his knowledge in technology and programming.
        </p>

        <p>
        He has also completed an English Language Diploma and
        holds a CIIT certificate. Along with his studies, he is
        continuously learning Python, Streamlit, Artificial
        Intelligence and modern Web Development technologies.
        </p>

        <p>
        His goal is to combine technology, creativity and AI
        to build innovative and useful digital solutions through
        TechBridge.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# SYED KHIZAR
# =========================

with team2:

    st.markdown(
        """
        <div class="team-card">

        <h3>👨‍💼 Syed Khizar</h3>

        <div class="team-role">
        Digital Marketing Specialist
        </div>

        <p>
        Syed Khizar is a Digital Marketing Specialist and an
        important part of the TechBridge team. He has around
        1 year of experience in digital marketing and focuses
        on helping businesses improve their online presence.
        </p>

        <p>
        His areas of interest include digital marketing,
        social media strategy, online promotion and developing
        effective digital growth strategies for businesses.
        </p>

        <p>
        He has completed his Matriculation and has also
        completed an English Language course from Infotics,
        which supports his communication and professional skills.
        </p>

        <p>
        At TechBridge, he works alongside the development team
        to combine digital marketing strategies with modern
        technology and help businesses build their brand,
        reach more people and grow online.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# CONTACT
# =========================

st.divider()

st.header("Let's Work Together")

st.write(
    "Have a project in mind? Let's build something amazing."
)

if st.button("📩 Start a Project"):

    st.info("Choose who you want to contact:")

    contact1, contact2 = st.columns(2)

    with contact1:

        st.link_button(
            "👨‍💻 Contact Mohammad Hunza",
            "https://wa.me/923192200926",
            use_container_width=True
        )

    with contact2:

        st.link_button(
            "👨‍💼 Contact Syed Khizar",
            "https://wa.me/923146864935",
            use_container_width=True
        )

# =========================
# FOOTER
# =========================
    
st.divider()

st.caption("© 2026 TechBridge • All Rights Reserved")