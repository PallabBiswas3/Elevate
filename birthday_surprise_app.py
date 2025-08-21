import streamlit as st
import datetime
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_drawable_canvas import st_canvas
import base64
import io
from PIL import Image
import math
import random

# Configure page
st.set_page_config(
    page_title="Happy Birthday My Dearest! 💚",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark green theme
st.markdown("""
<style>
    /* Import Bengali font */
    @import url('https://fonts.googleapis.com/css2?family=Kalam:wght@300;400;700&display=swap');
    
    .main {
        padding: 0rem 1rem;
        background: linear-gradient(135deg, #1a4429 0%, #2d5a3d 50%, #0f2e1a 100%);
        color: #ffffff;
    }
    
    .stApp {
        background: linear-gradient(135deg, #1a4429 0%, #2d5a3d 50%, #0f2e1a 100%);
    }
    
    .main-title {
        text-align: center;
        color: #ffd700;
        font-size: 3.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        font-family: 'Kalam', cursive;
    }
    
    .subtitle {
        text-align: center;
        color: #ffffff;
        font-size: 1.5rem;
        margin-bottom: 2rem;
        font-style: italic;
    }
    
    .countdown-container {
        background: rgba(255, 215, 0, 0.1);
        border: 2px solid #ffd700;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 8px 32px rgba(255, 215, 0, 0.3);
    }
    
    .countdown-number {
        font-size: 4rem;
        color: #ffd700;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    .countdown-label {
        font-size: 1.2rem;
        color: #ffffff;
        margin-top: -10px;
    }
    
    .section-header {
        color: #ffd700;
        font-size: 2.5rem;
        text-align: center;
        margin: 2rem 0;
        font-family: 'Kalam', cursive;
    }
    
    .timeline-item {
        background: rgba(255, 255, 255, 0.1);
        border-left: 4px solid #ffd700;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 10px;
        backdrop-filter: blur(10px);
    }
    
    .equation {
        background: rgba(255, 215, 0, 0.2);
        color: #ffd700;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        margin: 1rem 0;
        font-family: 'Courier New', monospace;
    }
    
    .quiz-question {
        background: rgba(255, 255, 255, 0.1);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 16px rgba(0,0,0,0.3);
    }
    
    .quiz-option {
        background: rgba(255, 215, 0, 0.1);
        border: 2px solid transparent;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .quiz-option:hover {
        border-color: #ffd700;
        background: rgba(255, 215, 0, 0.2);
    }
    
    .love-message {
        background: linear-gradient(45deg, #2d5a3d, #1a4429);
        color: #ffffff;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        border: 2px solid #ffd700;
    }
    
    .floating-hearts {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1000;
    }
    
    .heart {
        position: absolute;
        color: #ffd700;
        font-size: 2rem;
        animation: float 6s ease-in-out infinite;
        opacity: 0.7;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
        10%, 90% { opacity: 0.7; }
        50% { transform: translateY(-100px) rotate(180deg); opacity: 1; }
    }
    
    .gift-box {
        background: linear-gradient(45deg, #ffd700, #ffed4e);
        color: #2d5a3d;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 4px 16px rgba(255, 215, 0, 0.4);
        cursor: pointer;
        transition: transform 0.3s ease;
    }
    
    .gift-box:hover {
        transform: scale(1.05);
    }
    
    .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.1);
        color: #ffffff;
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #ffd700, #ffed4e);
        color: #2d5a3d;
        border: none;
        border-radius: 25px;
        font-weight: bold;
        padding: 0.75rem 2rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 16px rgba(255, 215, 0, 0.4);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Floating hearts animation
st.markdown("""
<div class="floating-hearts">
    <div class="heart" style="left: 10%; animation-delay: 0s;">💚</div>
    <div class="heart" style="left: 20%; animation-delay: 1s;">💚</div>
    <div class="heart" style="left: 30%; animation-delay: 2s;">💚</div>
    <div class="heart" style="left: 40%; animation-delay: 3s;">💚</div>
    <div class="heart" style="left: 50%; animation-delay: 4s;">💚</div>
    <div class="heart" style="left: 60%; animation-delay: 1.5s;">💚</div>
    <div class="heart" style="left: 70%; animation-delay: 2.5s;">💚</div>
    <div class="heart" style="left: 80%; animation-delay: 3.5s;">💚</div>
    <div class="heart" style="left: 90%; animation-delay: 0.5s;">💚</div>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_section' not in st.session_state:
    st.session_state.current_section = 'home'
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False

# Navigation
st.sidebar.markdown("## 💚 Navigation")
section = st.sidebar.selectbox(
    "Choose a section:",
    ['🏠 Home', '💕 Our Love Story', '🧠 Fun Quiz', '🎨 Art Gallery', 
     '✈️ Dream Travels', '📐 Mathematical Love', '🎁 Birthday Gifts']
)

def calculate_countdown():
    """Calculate countdown to birthday"""
    birthday = datetime.datetime(2025, 9, 4, 0, 0, 0)
    now = datetime.datetime.now()
    
    if now > birthday:
        # If birthday has passed, show celebratory message
        return None, "🎉 IT'S YOUR BIRTHDAY! 🎉"
    
    diff = birthday - now
    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return (days, hours, minutes, seconds), None

def create_love_equation_chart():
    """Create a mathematical love growth chart"""
    days = list(range(0, 365))
    love_growth = [math.log(day + 1) * 10 + random.uniform(-2, 2) for day in days]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=days,
        y=love_growth,
        mode='lines',
        line=dict(color='#ffd700', width=3),
        fill='tonexty',
        name='Our Love Growth'
    ))
    
    fig.update_layout(
        title="Mathematical Proof: Our Love Over Time",
        xaxis_title="Days Since December 2024",
        yaxis_title="Love Intensity (❤️ units)",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#ffffff'),
        title_font_color='#ffd700'
    )
    
    return fig

# HOME SECTION
if section == '🏠 Home':
    st.markdown('<h1 class="main-title">Happy Birthday My Dearest! 🌟</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">For the most amazing artist and mathematician in my heart</p>', unsafe_allow_html=True)
    
    # Background music note
    st.markdown("""
    <div class="love-message">
        🎵 <strong>Playing in my heart:</strong> Our special 80s Bengali love song<br>
        <em>Tumi Je Amar - The melody that brought us together</em>
        <br><br>
        <a href="https://www.youtube.com/watch?v=S82bAkqqwX4" target="_blank" 
           style="color: #ffd700; text-decoration: none;">🎶 Listen to Our Song 🎶</a>
    </div>
    """, unsafe_allow_html=True)
    
    # Countdown
    countdown_data, birthday_msg = calculate_countdown()
    
    if birthday_msg:
        st.markdown(f'<div class="countdown-container"><h2 style="color: #ffd700;">{birthday_msg}</h2></div>', 
                    unsafe_allow_html=True)
    else:
        days, hours, minutes, seconds = countdown_data
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f'<div class="countdown-container"><div class="countdown-number">{days}</div><div class="countdown-label">Days</div></div>', 
                        unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="countdown-container"><div class="countdown-number">{hours}</div><div class="countdown-label">Hours</div></div>', 
                        unsafe_allow_html=True)
        with col3:
            st.markdown(f'<div class="countdown-container"><div class="countdown-number">{minutes}</div><div class="countdown-label">Minutes</div></div>', 
                        unsafe_allow_html=True)
        with col4:
            st.markdown(f'<div class="countdown-container"><div class="countdown-number">{seconds}</div><div class="countdown-label">Seconds</div></div>', 
                        unsafe_allow_html=True)
    
    st.markdown("""
    <div class="love-message">
        <h3>💚 A Message From Your Heart</h3>
        <p>Even though we're miles apart, you're always in my heart. This website is a small token of my love for you - 
        celebrating your artistic soul, your brilliant mathematical mind, and the beautiful journey we've shared.</p>
        <p><em>From the boy who turned a proposal into an interview, to the man who found his romantic side through you ✨</em></p>
    </div>
    """, unsafe_allow_html=True)

# LOVE STORY SECTION
elif section == '💕 Our Love Story':
    st.markdown('<h2 class="section-header">Our Beautiful Journey 💕</h2>', unsafe_allow_html=True)
    
    # Timeline events
    timeline_events = [
        {
            "date": "3-4 Years Ago",
            "title": "First Connection ✨",
            "description": "When two souls found each other across the distance. A studious boy and an artistic village girl - destiny had its own mathematical equation planned.",
            "equation": "Stranger + Stranger = Friends"
        },
        {
            "date": "December 2024",
            "title": "Everything Changed 💚",
            "description": "From friends to something magical. Your heart discovered what your mind had been analyzing - this was love, pure and infinite.",
            "equation": "Friendship + Time = Love"
        },
        {
            "date": "The Legendary Proposal",
            "title": "World's Most Unique Proposal 😅",
            "description": "When romance meets logic - you turned our beautiful moment into an interview! But even that couldn't hide the love in your heart. It became our most precious memory.",
            "equation": "Heart + Brain = Unforgettable Memory"
        },
        {
            "date": "The Discovery",
            "title": "Finding His Romantic Side 💖",
            "description": "You saw beyond the logical exterior and discovered a heart full of love, poetry, and dreams. You taught him that being studious doesn't mean being unromantic.",
            "equation": "Logic + Love = Perfect Balance"
        }
    ]
    
    for event in timeline_events:
        st.markdown(f"""
        <div class="timeline-item">
            <h3 style="color: #ffd700;">{event['date']}: {event['title']}</h3>
            <p>{event['description']}</p>
        </div>
        <div class="equation">{event['equation']}</div>
        """, unsafe_allow_html=True)

# QUIZ SECTION
elif section == '🧠 Fun Quiz':
    st.markdown('<h2 class="section-header">How Well Do You Know Your Studious Boyfriend? 🤓</h2>', unsafe_allow_html=True)
    
    questions = [
        {
            "question": "What did your boyfriend accidentally turn your proposal into?",
            "options": ["A presentation", "An interview", "A lecture", "A debate"],
            "correct": 1,
            "explanation": "Even in love, his studious nature shined through! 😄"
        },
        {
            "question": "Complete the equation: Study + Love = ?",
            "options": ["Stress", "You!", "Confusion", "Sleepless nights"],
            "correct": 1,
            "explanation": "The most beautiful solution to any equation! 💚"
        },
        {
            "question": "What did people think about him before you discovered his romantic side?",
            "options": ["Too funny", "Too romantic", "Unromantic and logical", "Too talkative"],
            "correct": 2,
            "explanation": "Little did they know about the heart behind the brain! ❤️"
        },
        {
            "question": "What's the distance formula for your love?",
            "options": ["Distance² + Time²", "Love grows with distance", "Distance = 0 in heart", "All of the above"],
            "correct": 3,
            "explanation": "Love transcends all mathematical limitations! 🌟"
        }
    ]
    
    if not st.session_state.quiz_completed:
        if st.session_state.current_question < len(questions):
            current_q = questions[st.session_state.current_question]
            
            st.markdown(f"""
            <div class="quiz-question">
                <h3>Question {st.session_state.current_question + 1}: {current_q['question']}</h3>
            </div>
            """, unsafe_allow_html=True)
            
            selected_answer = st.radio(
                "Choose your answer:",
                current_q['options'],
                key=f"q_{st.session_state.current_question}"
            )
            
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                if st.button("Submit Answer", key=f"submit_{st.session_state.current_question}"):
                    if current_q['options'].index(selected_answer) == current_q['correct']:
                        st.session_state.quiz_score += 1
                        st.success(f"Correct! {current_q['explanation']}")
                    else:
                        st.error(f"Oops! {current_q['explanation']}")
                    
                    st.session_state.current_question += 1
                    time.sleep(2)
                    st.rerun()
        else:
            st.session_state.quiz_completed = True
    
    if st.session_state.quiz_completed:
        score_percentage = (st.session_state.quiz_score / len(questions)) * 100
        
        st.markdown(f"""
        <div class="love-message">
            <h2>Quiz Complete! 🎉</h2>
            <h3>Your Score: {st.session_state.quiz_score}/{len(questions)} ({score_percentage:.0f}%)</h3>
        """, unsafe_allow_html=True)
        
        if score_percentage >= 75:
            st.markdown("<p>You know him so well! His heart is truly yours 💚</p>", unsafe_allow_html=True)
        elif score_percentage >= 50:
            st.markdown("<p>Pretty good! You're learning more about his quirky side 😊</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p>There's still so much to discover about each other! 💕</p>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.button("Retake Quiz"):
            st.session_state.quiz_score = 0
            st.session_state.current_question = 0
            st.session_state.quiz_completed = False
            st.rerun()

# ART GALLERY SECTION
elif section == '🎨 Art Gallery':
    st.markdown('<h2 class="section-header">For My Beautiful Artist 🎨</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="love-message">
        <h3>Your Creative Space</h3>
        <p>This is for the artist in you - create something beautiful, just like how you've painted colors in my black and white world.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Drawing Canvas
    st.markdown("### 🖌️ Digital Sketchbook")
    
    # Canvas settings
    drawing_mode = st.selectbox("Drawing tool:", ["freedraw", "line", "rect", "circle"])
    stroke_width = st.slider("Stroke width: ", 1, 25, 3)
    stroke_color = st.color_picker("Stroke color: ", "#ffd700")
    
    # Create canvas
    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 0.1)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color="#2d5a3d",
        height=400,
        width=600,
        drawing_mode=drawing_mode,
        key="canvas",
    )
    
    # Shayari Corner
    st.markdown("### ✍️ Your Shayari Corner")
    shayari = st.text_area(
        "Write a beautiful shayari or poem:",
        placeholder="तेरी मोहब्बत में हमने जो खुशियां पाई हैं,\nवो किसी किताब में नहीं, तेरी आंखों में पढ़ी हैं...",
        height=150
    )
    
    if shayari:
        st.markdown(f"""
        <div class="love-message">
            <h4>Your Beautiful Words:</h4>
            <p style="font-style: italic; font-size: 1.2rem; line-height: 1.8;">{shayari}</p>
        </div>
        """, unsafe_allow_html=True)

# DREAM TRAVELS SECTION
elif section == '✈️ Dream Travels':
    st.markdown('<h2 class="section-header">Places We\'ll Visit Together ✈️</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="love-message">
        <h3>From Your Village to the World 🌍</h3>
        <p>Every journey starts with a dream. Here are the places where we'll create beautiful memories together.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Dream destinations
    destinations = [
        {"name": "Darjeeling 🍃", "distance": "~450 km", "description": "Tea gardens, mountain views, and our first trip together"},
        {"name": "Kashmir 🏔️", "distance": "~1200 km", "description": "Paradise on earth for our love story"},
        {"name": "Goa 🏖️", "distance": "~1800 km", "description": "Beach walks, sunsets, and romantic dinners"},
        {"name": "Kerala 🌴", "distance": "~2000 km", "description": "Backwaters, boat rides, and peaceful moments"},
        {"name": "Rajasthan 🏰", "distance": "~800 km", "description": "Royal palaces, desert adventures, and fairy tale moments"},
        {"name": "Paris 🗼", "distance": "~7000 km", "description": "City of love - for our first international adventure"}
    ]
    
    for dest in destinations:
        st.markdown(f"""
        <div class="timeline-item">
            <h3 style="color: #ffd700;">{dest['name']}</h3>
            <div class="equation">Mathematical Distance: {dest['distance']}</div>
            <p>{dest['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Travel savings calculator
    st.markdown("### 💰 Our Travel Savings Goal")
    monthly_savings = st.slider("Monthly savings for our trips (₹):", 1000, 10000, 3000)
    trip_cost = st.slider("Dream trip budget (₹):", 20000, 100000, 50000)
    
    months_needed = trip_cost / monthly_savings
    
    st.markdown(f"""
    <div class="equation">
    Travel Equation:<br>
    ₹{trip_cost:,.0f} ÷ ₹{monthly_savings:,.0f} = {months_needed:.1f} months<br>
    <em>Our next adventure is just {months_needed:.0f} months away! 💚</em>
    </div>
    """, unsafe_allow_html=True)

# MATHEMATICAL LOVE SECTION
elif section == '📐 Mathematical Love':
    st.markdown('<h2 class="section-header">Love in Mathematical Terms 📐</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="love-message">
        <h3>For My Mathematics Student 🧮</h3>
        <p>Since you study mathematics, here's our love story expressed in equations and graphs!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Love equations
    love_equations = [
        {
            "equation": "Distance² + Time² = Love∞",
            "meaning": "No distance can measure our infinite love"
        },
        {
            "equation": "You + Me = Perfect Solution",
            "meaning": "Together we solve life's greatest equation"
        },
        {
            "equation": "lim(our love) as time→∞ = ∞",
            "meaning": "Our love approaches infinity over time"
        },
        {
            "equation": "∫(happiness)dt = You in my life",
            "meaning": "You are the integral of all my joy"
        },
        {
            "equation": "d/dt(my love) > 0",
            "meaning": "My love for you is always increasing"
        }
    ]
    
    for eq in love_equations:
        st.markdown(f"""
        <div class="equation">{eq['equation']}</div>
        <div class="timeline-item">
            <p><em>{eq['meaning']}</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    # Love growth chart
    st.markdown("### 📊 Our Love Growth Over Time")
    fig = create_love_equation_chart()
    st.plotly_chart(fig, use_container_width=True)
    
    # Romantic calculator
    st.markdown("### 💚 Love Calculator")
    st.markdown("*This calculator only gives romantic answers!*")
    
    col1, col2, col3 = st.columns([2, 1, 2])
    with col1:
        num1 = st.text_input("First number:", placeholder="Any number")
    with col2:
        operation = st.selectbox("Operation:", ["+", "-", "×", "÷", "^"])
    with col3:
        num2 = st.text_input("Second number:", placeholder="Any number")
    
    if st.button("Calculate Love"):
        love_answers = [
            "= You (the most beautiful answer) 💚",
            "= Infinite Love ∞",
            "= Our Perfect Future Together ✨",
            "= The Solution to My Heart 💕",
            "= Forever and Always 💖",
            "= The Best Equation Ever! 🌟",
            "= Pure Magic ✨",
            "= Love Beyond Numbers 💚"
        ]
        result = random.choice(love_answers)
        st.markdown(f'<div class="equation">{num1} {operation} {num2} {result}</div>', unsafe_allow_html=True)

# BIRTHDAY GIFTS SECTION
elif section == '🎁 Birthday Gifts':
    st.markdown('<h2 class="section-header">Virtual Birthday Gifts for You! 🎁</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="love-message">
        <h3>🎂 Happy Birthday My Dearest!</h3>
        <p>While I can't be there physically, these virtual gifts come straight from my heart to yours.</p>
    </div>
    """, unsafe_allow_html=True)
    
    gifts = [
        {
            "title": "🎨 A Digital Sketchbook",
            "description": "For all the beautiful art you create. May your creativity always flow like our love!",
            "icon": "🎨",
            "content": "This represents all the drawings you'll create, the sketches that capture your beautiful mind, and the art that makes you who you are."
        },
        {
            "title": "📐 Mathematical Love Theorem", 
            "description": "Scientific proof that our love equals infinity ∞",
            "icon": "📐",
            "content": "Theorem: Given two hearts H₁ and H₂, if they beat in synchronization across any distance d, then Love(H₁,H₂) = ∞. Q.E.D. ✨"
        },
        {
            "title": "✈️ Virtual Travel Tickets",
            "description": "For all our future adventures together around the world!",
            "icon": "✈️", 
            "content": "Destination: Everywhere together. Departure: Soon. Return: Never, because every place becomes home with you."
        },
        {
            "title": "🎵 Bengali Love Song Collection",
            "description": "Starting with our special 80s melody that brought us together",
            "icon": "🎵",
            "content": "Our playlist begins with 'Tumi Je Amar' and will grow with every song that reminds us of our beautiful moments together."
        },
        {
            "title": "💚 Promise of Forever",
            "description": "The most precious gift - my commitment to love you always",
            "icon": "💚",
            "content": "No matter the distance, no matter the time, no matter the challenges - you have my heart, my love, and my forever."
        }
    ]
    
    cols = st.columns(2)
    for i, gift in enumerate(gifts):
        with cols[i % 2]:
            with st.expander(f"{gift['icon']} {gift['title']}", expanded=False):
                st.markdown(f"""
                <div class="gift-box">
                    <h4>{gift['description']}</h4>
                    <p>{gift['content']}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Special birthday message
    st.markdown("""
    <div class="love-message">
        <h3>💝 A Special Birthday Message</h3>
        <p>My dearest,</p>
        <p>Today marks another year of your beautiful existence, another year of the joy you bring to this world, 
        and another year closer to when we'll finally be together.</p>
        <p>You've taught this logical, studious boy that love isn't just an equation to be solved - 
        it's a beautiful poem to be lived. You found the romantic hidden behind all the books and formulas.</p>
        <p>Even though we haven't met face to face yet, you've touched my soul in ways I never thought possible. 
        Your sketches color my dreams, your shayari fills my heart with melody, and your love gives my life meaning.</p>
        <p>This website is just a small token of the infinite love I have for you. 
        Every line of code written with love, every feature designed thinking of your smile.</p>
        <p><strong>Happy Birthday, my beautiful artist, my brilliant mathematician, my everything. 
        May this new year of your life be filled with all the colors of happiness! 🌈💚</strong></p>
        <p>With all my love and a promise of forever,<br>Your devoted (and now romantic) boyfriend 💕</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Final countdown for today
    countdown_data, birthday_msg = calculate_countdown()
    if countdown_data:
        days, hours, minutes, seconds = countdown_data
        st.markdown(f"""
        <div class="countdown-container">
            <h3>Time until your special day:</h3>
            <h2 style="color: #ffd700;">{days} days, {hours} hours, {minutes} minutes!</h2>
        </div>
        """, unsafe_allow_html=True)

# Auto-refresh countdown every minute
if section == '🏠 Home':
    time.sleep(60)
    st.rerun()