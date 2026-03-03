def apply_style(bg1, bg2, bg3, bg4):
    return f"""
    <style>

    /* ===== ANNOUNCEMENT BAR ===== */
    .announce {{
        background: #1e40af;
        color: white;
        text-align: center;
        padding: 8px;
        font-size: 14px;
    }}

    /* ===== NAVBAR ===== */
    .navbar {{
        background: white;
        padding: 18px 60px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    }}

    .nav-logo {{
        font-size: 24px;
        font-weight: 800;
        color: #1e3a8a;
    }}

    /* ===== HERO ===== */
    .hero {{
        background-size: cover;
        background-position: center;
        position: relative;
        padding: 160px 20px;
        text-align: center;
        color: white;
        border-radius: 0 0 40px 40px;
        animation: slideBg 40s infinite;
    }}

    @keyframes slideBg {{
        0%,24% {{
            background-image: url("data:image/jpg;base64,{bg1}");
        }}
        25%,49% {{
            background-image: url("data:image/jpg;base64,{bg2}");
        }}
        50%,74% {{
            background-image: url("data:image/jpg;base64,{bg3}");
        }}
        75%,100% {{
            background-image: url("data:image/jpg;base64,{bg4}");
        }}
    }}

    .hero::before {{
        content: "";
        position: absolute;
        inset: 0;
        background: rgba(0,0,0,0.55);
        border-radius: 0 0 40px 40px;
    }}

    .hero-content {{
        position: relative;
        z-index: 2;
    }}

    .hero h1 {{
        font-size: 72px;
        font-weight: 800;
        margin: 0;
    }}

    .hero p {{
        font-size: 24px;
        margin-top: 20px;
    }}

    /* ===== BUTTON ===== */
    .stButton>button {{
        border-radius: 14px;
        height: 52px;
        font-weight: 600;
        background: white;
        color: #1e3a8a;
        border: none;
        transition: 0.3s ease;
    }}

    .stButton>button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }}

    /* ===== CONTACT CARD ===== */
    .contact-box {{
        margin-top: 60px;
        padding: 30px;
        background: white;
        border-radius: 20px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.08);
        font-size: 18px;
        text-align: center;
    }}

    /* ===== EXAM CARD ===== */
    .exam-box {{
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }}

    </style>
    """