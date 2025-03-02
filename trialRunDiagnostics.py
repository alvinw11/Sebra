"""
Main application file for the Clinical Trial Analysis Platform.
"""

import os
import sys
import streamlit as st

# Add the current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from utils import (
    get_translation,
    SUPPORTED_LANGUAGES,
    render_login_page,
    render_medical_info_page,
    render_analysis_page
)

def initialize_session_state():
    """Initialize session state variables."""
    if 'language' not in st.session_state:
        st.session_state.language = 'en'
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'
    if 'show_login' not in st.session_state:
        st.session_state.show_login = False
    if "saved_data" not in st.session_state:
        st.session_state.saved_data = ""
        
    # Initialize medical section data
    if "demographics_data" not in st.session_state:
        st.session_state.demographics_data = {}
    if "vital_signs_data" not in st.session_state:
        st.session_state.vital_signs_data = {}
    if "medical_history_data" not in st.session_state:
        st.session_state.medical_history_data = {}
    if "medications_data" not in st.session_state:
        st.session_state.medications_data = {}
    if "lab_results_data" not in st.session_state:
        st.session_state.lab_results_data = {}
    if "imaging_data" not in st.session_state:
        st.session_state.imaging_data = {}
    if "procedures_data" not in st.session_state:
        st.session_state.procedures_data = {}
    if "lifestyle_data" not in st.session_state:
        st.session_state.lifestyle_data = {}
    if "family_history_data" not in st.session_state:
        st.session_state.family_history_data = {}
    if "rare_diseases_data" not in st.session_state:
        st.session_state.rare_diseases_data = {}
    if "genetic_data" not in st.session_state:
        st.session_state.genetic_data = {}
    if "clinical_notes_data" not in st.session_state:
        st.session_state.clinical_notes_data = {}

def save_section_data(section_name, data):
    """Save data for a specific section."""
    session_key = f"{section_name.lower().replace(' ', '_')}_data"
    st.session_state[session_key] = data
    st.success(f"{section_name} data saved successfully!")

def get_section_data(section_name):
    """Get saved data for a specific section."""
    session_key = f"{section_name.lower().replace(' ', '_')}_data"
    return st.session_state.get(session_key, {})

def render_homepage():
    """Render the homepage with login button."""
    # Create a container for the login button at the top
    header = st.container()
    
    # Add the login button to the top right using columns
    with header:
        cols = st.columns([5, 1])
        with cols[1]:
            if st.button("Login →", use_container_width=True):
                st.session_state.show_login = True
                st.rerun()

    # Add homepage content here
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://plus.unsplash.com/premium_photo-1661830629991-01950d3eba34?q=80&w=3274&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        min-height: 100vh;
    }

    [data-testid="stHeader"] {
        background-color: transparent;
    }

    [data-testid="stToolbar"] {
        right: 2rem;
    }

    /* Custom Login Button Styling */
    button[kind="secondary"] {
        background-color: rgba(255, 255, 255, 0.1) !important;
        border: 0.5px solid white !important;
        border-radius: 20px !important;
        color: white !important;
        font-size: 16px !important;
        padding: 10px 20px !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(5px) !important;
        margin-right: 10px !important;
        margin-top: 20px !important;
        background-image: url('https://plus.unsplash.com/premium_photo-1661830629991-01950d3eba34?q=80&w=3274&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') !important;
    }

    button[kind="secondary"]:hover {
        background-color: rgba(255, 255, 255, 0.2) !important;
        transform: scale(1.05) !important;
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.3) !important;
    }

    /* Cloud Styling */
    .cloud {
        position: absolute;
        width: 200px;
        height: 120px;
        background-image: url('https://www.citypng.com/public/uploads/preview/transparent-hd-white-painting-realistic-cloud-704081694963701vtfd1xzbpm.png');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        opacity: 0.8;
    }

    /* Cloud Animation */
    @keyframes moveClouds {
        0% { transform: translateX(-250px); }
        100% { transform: translateX(100vw); }
    }

    /* Individual Clouds */
    .cloud1 {
        top: 20%;
        left: -250px;
        animation: moveClouds 25s linear infinite;
        transform: scale(1);
    }

    .cloud2 {
        top: 40%;
        left: -300px;
        animation: moveClouds 30s linear infinite;
        transform: scale(0.8);
        background-image: url('https://www.citypng.com/public/uploads/preview/transparent-hd-white-painting-realistic-cloud-704081694963701vtfd1xzbpm.png');
    }

    .cloud3 {
        top: 60%;
        left: -280px;
        animation: moveClouds 35s linear infinite;
        transform: scale(1.2);
        background-image: url('https://www.citypng.com/public/uploads/preview/transparent-hd-white-painting-realistic-cloud-704081694963701vtfd1xzbpm.png');
    }
    </style>

    <div class="sky">
        <div class="cloud cloud1"></div>
        <div class="cloud cloud2"></div>
        <div class="cloud cloud3"></div>
    </div>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    # You can add more homepage content here

def render_login_with_back():
    """Render the login page with a back button."""
    # Create a container for the back button at the top
    header = st.container()
    
    # Add the back button to the top left using columns
    with header:
        cols = st.columns([1, 5])
        with cols[0]:
            if st.button("← Back", use_container_width=True):
                st.session_state.show_login = False
                st.rerun()

    # Language Selector
    language_options = list(SUPPORTED_LANGUAGES.keys())
    current_language_index = language_options.index(
        next(k for k, v in SUPPORTED_LANGUAGES.items() if v == st.session_state.language)
    )
    
    selected_language = st.selectbox(
        get_translation('language_selector', st.session_state.language),
        options=language_options,
        index=current_language_index,
        key='language_select'
    )
    
    # Update language if changed
    new_language = SUPPORTED_LANGUAGES[selected_language]
    if new_language != st.session_state.language:
        st.session_state.language = new_language
        st.rerun()
    
    # Display login page
    render_login_page(st.session_state.language)

def main():
    """Main application function."""
    initialize_session_state()
    
    if not st.session_state.show_login and not st.session_state.authenticated:
        render_homepage()
        return

    if not st.session_state.authenticated:
        render_login_with_back()
        return
    
    # Main navigation
    tabs = st.tabs([
        get_translation('medical_info_title', st.session_state.language),
        get_translation('results_title', st.session_state.language)
    ])
    
    with tabs[0]:
        render_medical_info_page(st.session_state.language)
    
    with tabs[1]:
        render_analysis_page(st.session_state.language)

if __name__ == "__main__":
    main()