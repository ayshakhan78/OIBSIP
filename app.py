import streamlit as st
import joblib
import re

# Load model & vectorizer
model = joblib.load("email_model.pkl")
tfidf = joblib.load("tfidf.pkl")

# ---------------- CUSTOM CSS ----------------
def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

    /* ── Base ── */
    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    .stApp {
        background: #0b0f1a;
        color: #e2e8f0;
    }

    /* ── Hide Streamlit chrome ── */
    #MainMenu, footer, header { visibility: hidden; }

    /* ── Top header bar ── */
    .email-header {
        background: linear-gradient(135deg, #1e2a45 0%, #141b2d 100%);
        border: 1px solid #2a3a5c;
        border-radius: 16px;
        padding: 36px 40px 28px;
        margin-bottom: 28px;
        position: relative;
        overflow: hidden;
    }
    .email-header::before {
        content: '';
        position: absolute;
        top: -40px; right: -40px;
        width: 200px; height: 200px;
        background: radial-gradient(circle, rgba(99,179,237,0.08) 0%, transparent 70%);
        border-radius: 50%;
    }
    .email-header h1 {
        font-size: 1.85rem;
        font-weight: 600;
        color: #f0f4ff;
        margin: 0 0 6px;
        letter-spacing: -0.5px;
    }
    .email-header p {
        color: #7a90b8;
        font-size: 0.93rem;
        margin: 0;
        font-weight: 300;
    }
    .header-icon {
        font-size: 2rem;
        margin-bottom: 12px;
        display: block;
    }

    /* ── Textarea ── */
    .stTextArea textarea {
        background: #111827 !important;
        border: 1px solid #2a3a5c !important;
        border-radius: 12px !important;
        color: #e2e8f0 !important;
        font-family: 'DM Mono', monospace !important;
        font-size: 0.88rem !important;
        padding: 16px !important;
        line-height: 1.65 !important;
        transition: border-color 0.2s ease !important;
    }
    .stTextArea textarea:focus {
        border-color: #4a90d9 !important;
        box-shadow: 0 0 0 3px rgba(74,144,217,0.12) !important;
    }
    .stTextArea label {
        color: #7a90b8 !important;
        font-size: 0.82rem !important;
        font-weight: 500 !important;
        letter-spacing: 0.05em !important;
        text-transform: uppercase !important;
    }

    /* ── Analyze button ── */
    .stButton > button {
        background: linear-gradient(135deg, #2563eb, #1e40af) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 32px !important;
        font-size: 0.9rem !important;
        font-weight: 500 !important;
        font-family: 'DM Sans', sans-serif !important;
        letter-spacing: 0.02em !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 20px rgba(37,99,235,0.35) !important;
    }

    /* ── Result cards ── */
    .result-card {
        background: #111827;
        border: 1px solid #1e2d4a;
        border-radius: 14px;
        padding: 22px 26px;
        margin-bottom: 16px;
        position: relative;
    }
    .result-card-accent {
        position: absolute;
        left: 0; top: 0; bottom: 0;
        width: 4px;
        border-radius: 14px 0 0 14px;
    }
    .accent-blue  { background: #3b82f6; }
    .accent-amber { background: #f59e0b; }
    .accent-green { background: #10b981; }
    .accent-red   { background: #ef4444; }
    .accent-violet{ background: #8b5cf6; }

    .card-label {
        font-size: 0.72rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #4a5568;
        margin-bottom: 6px;
    }
    .card-value {
        font-size: 1.25rem;
        font-weight: 600;
        color: #e2e8f0;
    }
    .card-sub {
        font-size: 0.83rem;
        color: #7a90b8;
        margin-top: 4px;
    }

    /* ── Probability bars ── */
    .prob-bar-wrap {
        margin-top: 10px;
    }
    .prob-row {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 10px;
    }
    .prob-label {
        width: 40px;
        font-size: 0.78rem;
        color: #7a90b8;
        font-family: 'DM Mono', monospace;
    }
    .prob-bar-bg {
        flex: 1;
        background: #1e2d4a;
        border-radius: 99px;
        height: 8px;
        overflow: hidden;
    }
    .prob-bar-fill {
        height: 100%;
        border-radius: 99px;
        transition: width 0.6s ease;
    }
    .fill-spam { background: linear-gradient(90deg, #ef4444, #f87171); }
    .fill-ham  { background: linear-gradient(90deg, #10b981, #34d399); }
    .prob-pct {
        width: 38px;
        text-align: right;
        font-size: 0.78rem;
        font-family: 'DM Mono', monospace;
        color: #94a3b8;
    }

    /* ── Keywords ── */
    .kw-pill {
        display: inline-block;
        background: rgba(245,158,11,0.15);
        border: 1px solid rgba(245,158,11,0.3);
        color: #fbbf24;
        font-size: 0.78rem;
        font-family: 'DM Mono', monospace;
        padding: 3px 10px;
        border-radius: 99px;
        margin: 3px 4px 3px 0;
    }

    /* ── Reply / Rewrite boxes ── */
    .text-box {
        background: #0d1424;
        border: 1px solid #1e2d4a;
        border-radius: 12px;
        padding: 18px 22px;
        font-family: 'DM Mono', monospace;
        font-size: 0.84rem;
        color: #94a3b8;
        line-height: 1.75;
        white-space: pre-wrap;
        margin-top: 10px;
    }

    /* ── Section headings ── */
    .section-title {
        font-size: 0.8rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #4a6080;
        margin: 28px 0 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .section-title::after {
        content: '';
        flex: 1;
        height: 1px;
        background: #1e2d4a;
    }

    /* ── Divider ── */
    hr { border-color: #1e2d4a !important; }

    /* ── Footer ── */
    .footer {
        text-align: center;
        color: #2d3f5a;
        font-size: 0.75rem;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #1a2236;
    }

    /* ── Warning ── */
    .stAlert {
        background: #1a1f2e !important;
        border: 1px solid #2a3a5c !important;
        border-radius: 10px !important;
        color: #94a3b8 !important;
    }
    </style>
    """, unsafe_allow_html=True)


# ---------------- CLEANING ----------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# ---------------- ML PREDICTION ----------------
def predict_email(text):
    text = clean_text(text)
    vec = tfidf.transform([text])
    pred = model.predict(vec)[0]
    proba = model.predict_proba(vec)[0]
    return pred, proba

# ---------------- CATEGORY LOGIC ----------------
def classify_email(text, spam_label,proba):
    text = text.lower()
    
    if spam_label == 1:
        return "Spam 🚨"
    if any(word in text for word in ["offer", "free", "win", "money", "prize", "reward", "claim", "winner"])and proba[1] > 0.4:
        return "Spam 🚨"
    if any(word in text for word in ["meeting", "project", "report", "deadline", "client", "update", "presentation", "review", "manager", "team", "office"]):
        return "Work 💼"
    if any(word in text for word in ["asap", "urgent", "immediately", "action required", "critical", "failure", "server"]):
        return "Urgent ⚡"
    personal_keywords = [
        "buddy", "friend", "catch up", "miss you",
        "long time", "how are you", "hope you", "get together", "nostalgia",
        "old friend", "free time", "let's meet", "take care", "how have you been",
        "nostalgic", "good to hear", "personal", "family", "vacation"
    ]
    if any(word in text for word in personal_keywords):
        return "Personal 👤"
    
    return "Personal 👤"

# ---------------- REPLY GENERATOR ----------------
def generate_reply(category):
    if "Spam" in category:
        return "This looks like a spam message. Avoid responding."
    if "Urgent" in category:
        return "I will address this immediately."
    if "Work" in category:
        return "Thank you for your email. I will review and respond soon."
    return "Thanks for your message. I will get back to you soon."

# ---------------- EMAIL REWRITER ----------------
def rewrite_email(text, category):
    text_lower = text.lower()
    if "urgent" in text_lower or "asap" in text_lower or "immediately" in text_lower:
        return """Subject: Urgent Request

Dear Sir/Madam,

I hope you are doing well. This is an urgent request. Kindly prioritize this matter.

Regards,"""
    if "meeting" in text_lower:
        return """Subject: Meeting Discussion

Dear Sir/Madam,

I hope you are doing well. I would like to schedule/discuss a meeting regarding the matter.

Please let me know your availability.

Regards,"""
    if "report" in text_lower:
        return """Subject: Report Request

Dear Sir/Madam,

I hope you are doing well. Kindly share the required report at your earliest convenience.

Thank you.

Regards,"""
    if any(word in text_lower for word in ["project", "deadline", "client"]):
        return f"""Subject: Work Update

Dear Sir/Madam,

{text.capitalize()}

Regards,"""
    return f"""Subject: General Communication

Dear Sir/Madam,

{text.capitalize()}

Regards,"""

# ---------------- IMPORTANT WORDS ----------------
def find_keywords(text):
    keywords = ["free", "win", "money", "urgent", "asap", "offer"]
    text = text.lower()
    return [word for word in keywords if word in text]

# ---------------- CATEGORY META ----------------
CATEGORY_META = {
    "Spam":     {"accent": "accent-red",    "icon": "🚨", "desc": "Potential spam detected"},
    "Urgent":   {"accent": "accent-amber",  "icon": "⚡", "desc": "Requires immediate attention"},
    "Work":     {"accent": "accent-blue",   "icon": "💼", "desc": "Professional communication"},
    "Personal": {"accent": "accent-green",  "icon": "👤", "desc": "Personal message"},
}

def get_meta(category):
    for key, meta in CATEGORY_META.items():
        if key in category:
            return meta
    return {"accent": "accent-violet", "icon": "📧", "desc": "Classified message"}

# ======================== UI ========================
st.set_page_config(
    page_title="Smart Email Assistant",
    page_icon="📧",
    layout="centered"
)

inject_css()

# Header
st.markdown("""
<div class="email-header">
    <span class="header-icon">📧</span>
    <h1>Smart Email Assistant</h1>
    <p>Paste any email below — get instant classification, confidence scores, and a suggested reply.</p>
</div>
""", unsafe_allow_html=True)

# Input
st.markdown('<p class="card-label">Email Content</p>', unsafe_allow_html=True)
user_input = st.text_area(
    label="Email Content",
    placeholder="Paste your email or message here…",
    height=180,
    label_visibility="collapsed"
)

analyze = st.button("Analyze Email")

# ── Results ──
if analyze:
    if not user_input.strip():
        st.warning("Please enter some text before analyzing.")
    else:
        pred, proba = predict_email(user_input)
        category    = classify_email(user_input, pred,proba)
        confidence  = max(proba)
        keywords    = find_keywords(user_input)
        meta        = get_meta(category)

        # ── Row 1: Category + Confidence ──
        col1, col2 = st.columns([1.4, 1])

        with col1:
            st.markdown(f"""
            <div class="result-card">
                <div class="result-card-accent {meta['accent']}"></div>
                <div class="card-label">Category</div>
                <div class="card-value">{category}</div>
                <div class="card-sub">{meta['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="result-card">
                <div class="result-card-accent accent-violet"></div>
                <div class="card-label">Confidence</div>
                <div class="card-value">{confidence:.0%}</div>
                <div class="card-sub">Model certainty</div>
            </div>
            """, unsafe_allow_html=True)

        # ── Probability breakdown ──
        spam_pct = int(proba[1] * 100)
        ham_pct  = int(proba[0] * 100)

        st.markdown(f"""
        <div class="result-card" style="margin-top:0">
            <div class="result-card-accent accent-blue"></div>
            <div class="card-label">Probability Breakdown</div>
            <div class="prob-bar-wrap">
                <div class="prob-row">
                    <span class="prob-label">Spam</span>
                    <div class="prob-bar-bg">
                        <div class="prob-bar-fill fill-spam" style="width:{spam_pct}%"></div>
                    </div>
                    <span class="prob-pct">{spam_pct}%</span>
                </div>
                <div class="prob-row">
                    <span class="prob-label">Ham</span>
                    <div class="prob-bar-bg">
                        <div class="prob-bar-fill fill-ham" style="width:{ham_pct}%"></div>
                    </div>
                    <span class="prob-pct">{ham_pct}%</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Keywords ──
        if keywords:
            pills = "".join(f'<span class="kw-pill">{kw}</span>' for kw in keywords)
            st.markdown(f"""
            <div class="result-card">
                <div class="result-card-accent accent-amber"></div>
                <div class="card-label">⚠️ Flagged Keywords</div>
                <div style="margin-top:10px">{pills}</div>
            </div>
            """, unsafe_allow_html=True)

        # ── Suggested Reply ──
        reply = generate_reply(category)
        st.markdown('<div class="section-title">Suggested Reply</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="text-box">{reply}</div>', unsafe_allow_html=True)

        # ── Rewritten Email ──
        if "Spam" not in category and "Personal" not in category:
            rewritten = rewrite_email(user_input, category)
            st.markdown('<div class="section-title">Rewritten Email</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="text-box">{rewritten}</div>', unsafe_allow_html=True)

        # Footer
        st.markdown("""
        <div class="footer">
            Built with NLP + Machine Learning · Smart Email Assistant
        </div>
        """, unsafe_allow_html=True)