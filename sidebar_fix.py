"""
Additional CSS to fix sidebar background issue
Add this CSS to the existing app.py
"""

def get_sidebar_css(theme):
    """Get additional CSS to fix sidebar background"""
    return f"""
    <style>
    /* === STREAMLIT CORE BACKGROUND FIX === */
    
    /* Main Streamlit container */
    .stApp {{
        background-color: {theme['bg_primary']} !important;
    }}
    
    /* Sidebar - multiple selectors to ensure coverage */
    section[data-testid="stSidebar"] {{
        background-color: {theme['bg_secondary']} !important;
    }}
    
    section[data-testid="stSidebar"] > div:first-child {{
        background-color: {theme['bg_secondary']} !important;
    }}
    
    section[data-testid="stSidebar"] .css-ng1t4o {{
        background-color: {theme['bg_secondary']} !important;
    }}
    
    section[data-testid="stSidebar"] .css-1cypcdb {{
        background-color: {theme['bg_secondary']} !important;
    }}
    
    /* Sidebar text - ensure readability */
    section[data-testid="stSidebar"] * {{
        color: {theme['text_primary']} !important;
    }}
    
    /* Main content background */
    .main .block-container {{
        background-color: {theme['bg_primary']} !important;
    }}
    </style>
    """

# Test the CSS generation
if __name__ == "__main__":
    test_theme = {
        'bg_primary': '#ffffff',
        'bg_secondary': '#f0f2f6',
        'text_primary': '#262730'
    }
    
    print("Generated CSS:")
    print(get_sidebar_css(test_theme))