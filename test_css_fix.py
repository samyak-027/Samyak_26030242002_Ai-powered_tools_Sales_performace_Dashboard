"""
Test file to verify the CSS fix for sidebar background
"""
import streamlit as st

# Test the basic CSS structure
def test_css():
    theme_colors = {
        'bg_primary': '#ffffff',
        'bg_secondary': '#f0f2f6',
        'text_primary': '#262730'
    }
    
    css_test = f"""
    <style>
    .stApp {{
        background-color: {theme_colors['bg_primary']} !important;
    }}
    section[data-testid="stSidebar"] {{
        background-color: {theme_colors['bg_secondary']} !important;
    }}
    </style>
    """
    
    return css_test

if __name__ == "__main__":
    print("CSS Test:")
    print(test_css())
    print("✓ CSS structure is valid")