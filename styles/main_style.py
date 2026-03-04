def apply_style(bg1, bg2, bg3, bg4):
    return f"""
    <style>

/* ===== Fade content when popup active ===== */
.dimmed {{
    opacity: 0.25;
    pointer-events: none;
    transition: 0.3s ease;
}}

/* ===== Center wrapper ===== */
.password-wrapper {{
    display: flex;
    justify-content: center;
    margin-top: 8vh;
    transition: 0.3s ease;
}}

/* ===== Modal Box ===== */
.password-box {{
    background: white;
    padding: 40px;
    width: 420px;
    border-radius: 24px;
    box-shadow: 0 30px 80px rgba(0,0,0,0.25);
    animation: popUp 0.25s ease-out;
}}

/* ===== Title ===== */
.password-title {{
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 20px;
    text-align: center;
}}

/* ===== Buttons ===== */
.stButton > button {{
    border-radius: 14px;
    font-weight: 500;
    padding: 10px;
    transition: 0.2s;
}}

.stButton > button:hover {{
    transform: translateY(-2px);
}}

/* ===== Animation ===== */
@keyframes popUp {{
    from {{opacity:0; transform: scale(0.95);}}
    to {{opacity:1; transform: scale(1);}}
}}

/* ===== Mobile Responsive ===== */
@media (max-width: 768px) {{
    .password-box {{
        width: 92%;
        padding: 28px;
        border-radius: 18px;
    }}
}}


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

    /* Social item */
    .contact-item {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        padding: 4px 10px;
        border-radius: 4px;
        text-decoration: none;
        font-weight: 300;
        color: #1e3a8a;
        transition: 0.3s ease;
    }}

    /* Logo size */
    .contact-item img {{
        width: 34px;
    }}

    /* Hover effect */
    .contact-item:hover {{
        background: #f3f6ff;
        transform: translateY(-2px);
    }}
    
    /* ===== FOOTER ===== */
    .footer {{
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: rgba(30, 64, 175, 0.95);
        backdrop-filter: blur(8px);
        padding: 22px 0;  
        z-index: 999;
    }}

    .footer-content {{
        max-width: 1400px;
        margin: auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 50px;
        color: white;
    }}

    .footer-title {{
        font-weight: 700;
        font-size: 24px;  
        color: white;
    }}

    .footer-links {{
        display: flex;
        gap: 40px;
    }}

    .footer-item {{
        display: flex;
        align-items: center;
        gap: 14px;
        text-decoration: none;
        color: #ffffff !important;
        font-weight: 600;
        font-size: 18px;
        transition: 0.3s ease;
    }}

    .footer-item img {{
        width: 32px;
        filter: brightness(0) invert(1);
    }}

    .footer-item:hover {{
        transform: translateY(-3px);
    }}

    /* ===== MOBILE ===== */
    @media (max-width: 768px) {{

        .footer {{
            padding: 1px 0;   
        }}

        .footer-content {{
            flex-direction: column;
            gap: 1px;
            padding: 0 1px;
            text-align: center;
        }}

        .footer-title {{
            font-size: 10px;  
            font-weight: 500;
        }}

        .footer-links {{
            flex-direction: column;
            gap: 3px;
        }}

        .footer-item {{
            justify-content: center;
            font-size: 7px;   
            gap: 3px;
            font-weight: 300;
        }}

        .footer-item img {{
            width: 10px;  
        }}
    }}

    /* Prevent content from hiding */
    .main .block-container {{
        padding-bottom: 50px;
    }}

    </style>
    """

