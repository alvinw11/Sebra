"""
Authentication utilities for the Clinical Trial Analysis Platform.
"""

import streamlit as st
from .translations import get_translation

def check_password(username: str, password: str) -> bool:
    """
    Verify user credentials.
    
    Args:
        username (str): The username to check
        password (str): The password to verify
        
    Returns:
        bool: True if credentials are valid, False otherwise
    """
    # TODO: Replace with actual authentication logic
    return username == "admin" and password == "password"

def render_login_page(language: str) -> bool:
    """
    Render the login page and handle authentication.
    
    Args:
        language (str): Current language code
        
    Returns:
        bool: True if login successful, False otherwise
    """
    st.title(get_translation('login_title', language))
    
    with st.form("login_form"):
        username = st.text_input(get_translation('username_prompt', language))
        password = st.text_input(get_translation('password_prompt', language), type="password")
        submitted = st.form_submit_button(get_translation('sign_in', language))
        
        if submitted:
            if check_password(username, password):
                st.session_state.authenticated = True
                return True
            st.error("Invalid username or password")
    
    return False 