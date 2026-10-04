"""
Sales Performance Dashboard App
A Streamlit-based interactive dashboard for analyzing sales performance

Author: MBA Data Science Project
Subject: AI Powered Developer Tools
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# Import utility functions
from utils.data_loader import load_sales_data
from utils.calculations import (
    calculate_revenue,
    calculate_units,
    calculate_aov,
    calculate_gross_margin,
    calculate_gross_margin_percentage,
    calculate_monthly_revenue,
    calculate_mom_growth,
    get_top_products,
    get_revenue_by_dimension,
    generate_insights,
    format_currency,
    format_number
)

# Page configuration
st.set_page_config(
    page_title="Sales Performance Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for theme and filters
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

if 'applied_filters' not in st.session_state:
    st.session_state.applied_filters = {
        'month': ['All'],
        'region': ['All'],
        'channel': ['All'],
        'category': ['All']
    }

if 'temp_filters' not in st.session_state:
    st.session_state.temp_filters = {
        'month': ['All'],
        'region': ['All'],
        'channel': ['All'],
        'category': ['All']
    }


def get_theme_colors():
    """
    Get color scheme based on current theme
    """
    if st.session_state.theme == 'dark':
        return {
            'bg_primary': '#0e1117',
            'bg_secondary': '#262730',
            'text_primary': '#fafafa',
            'text_secondary': '#b0b0b0',
            'accent': '#4da6ff',
            'accent_light': '#66b3ff',
            'border': '#4da6ff',
            'card_bg': '#1e1e1e',
            'insight_bg': '#1a2332',
            'chart_bg': '#262730',
            'grid_color': '#404040'
        }
    else:
        return {
            'bg_primary': '#ffffff',
            'bg_secondary': '#f0f2f6',
            'text_primary': '#262730',
            'text_secondary': '#555555',
            'accent': '#1f77b4',
            'accent_light': '#5ba3d0',
            'border': '#1f77b4',
            'card_bg': '#f0f2f6',
            'insight_bg': '#e8f4f8',
            'chart_bg': '#ffffff',
            'grid_color': '#e0e0e0'
        }


# Get current theme colors
theme = get_theme_colors()

# Custom CSS for better styling with theme support
st.markdown(f"""
    <style>
    /* === CORE STREAMLIT STYLING === */
    
    /* Main Streamlit App Container */
    .stApp {{
        background-color: {theme['bg_primary']} !important;
    }}
    
    /* Main content area */
    .main .block-container {{
        background-color: {theme['bg_primary']} !important;
        padding-top: 1rem;
    }}
    
    /* === SIDEBAR STYLING === */
    
    /* Sidebar container */
    section[data-testid="stSidebar"] {{
        background-color: {theme['bg_secondary']} !important;
    }}
    
    /* Sidebar content */
    section[data-testid="stSidebar"] > div {{
        background-color: {theme['bg_secondary']} !important;
    }}
    
    /* Sidebar text elements */
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] div,
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {{
        color: {theme['text_primary']} !important;
    }}
    
    /* === CUSTOM COMPONENT STYLING === */
    
    /* Headers */
    .main-header {{
        font-size: 2.5rem;
        font-weight: 700;
        color: {theme['accent']};
        text-align: center;
        margin-bottom: 0.5rem;
    }}
    .sub-header {{
        font-size: 1.2rem;
        color: {theme['text_secondary']};
        text-align: center;
        margin-bottom: 2rem;
    }}
    
    /* KPI Cards */
    .kpi-card {{
        background-color: {theme['card_bg']};
        padding: 1.5rem;
        border-radius: 0.5rem;
        text-align: center;
        border: 1px solid {theme['grid_color']};
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    .kpi-value {{
        font-size: 2rem;
        font-weight: 700;
        color: {theme['accent']};
    }}
    .kpi-label {{
        font-size: 0.9rem;
        color: {theme['text_secondary']};
        margin-top: 0.5rem;
    }}
    
    /* Insight Box */
    .insight-box {{
        background-color: {theme['insight_bg']};
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid {theme['border']};
        color: {theme['text_primary']};
    }}
    
    .insight-box li {{
        color: {theme['text_primary']};
    }}
    
    /* Section Headers */
    .section-header {{
        font-size: 1.5rem;
        font-weight: 600;
        color: {theme['text_primary']};
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid {theme['border']};
        padding-bottom: 0.5rem;
    }}
    
    /* === TEXT ELEMENTS === */
    
    /* All text in main area */
    .element-container h1, .element-container h2, .element-container h3,
    .element-container h4, .element-container h5, .element-container h6,
    .element-container p, .element-container span, .element-container div,
    .element-container strong, .element-container b {{
        color: {theme['text_primary']} !important;
    }}
    
    /* Metric components */
    [data-testid="stMetricLabel"] {{
        color: {theme['text_primary']} !important;
    }}
    
    [data-testid="stMetricValue"] {{
        color: {theme['accent']} !important;
    }}
    
    /* === BUTTON STYLING === */
    
    /* Sidebar buttons */
    section[data-testid="stSidebar"] .stButton > button {{
        background-color: {theme['accent']} !important;
        color: white !important;
        border: none !important;
        border-radius: 0.3rem !important;
        font-weight: 600 !important;
    }}
    
    /* Theme toggle button */
    .stButton > button {{
        border-radius: 0.3rem !important;
    }}
    
    /* === ADDITIONAL ELEMENTS === */
    
    /* Alert boxes */
    .stAlert {{
        background-color: {theme['card_bg']} !important;
        color: {theme['text_primary']} !important;
    }}
    
    /* Header area */
    header[data-testid="stHeader"] {{
        background-color: {theme['bg_primary']} !important;
    }}
    </style>
    """, unsafe_allow_html=True)


@st.cache_data
def load_data():
    """
    Load sales data with caching for performance
    """
    # Try multiple possible file locations
    possible_paths = [
        'T01_Sales_performance_dashboard_app.xlsx',
        'data/T01_Sales_performance_dashboard_app.xlsx',
        '../T01_Sales_performance_dashboard_app.xlsx'
    ]
    
    for file_path in possible_paths:
        if Path(file_path).exists():
            return load_sales_data(file_path)
    
    # If no file found, raise error
    raise FileNotFoundError(
        "Could not find T01_Sales_performance_dashboard_app.xlsx\n"
        "Please ensure the file is in the project root or data/ directory"
    )


def apply_filters(df, month_filter, region_filter, channel_filter, category_filter):
    """
    Apply selected filters to the DataFrame
    
    Args:
        df: Original DataFrame
        month_filter: Selected month(s)
        region_filter: Selected region(s)
        channel_filter: Selected channel(s)
        category_filter: Selected category(ies)
        
    Returns:
        Filtered DataFrame
    """
    filtered_df = df.copy()
    
    if month_filter and 'All' not in month_filter:
        filtered_df = filtered_df[filtered_df['month_name'].isin(month_filter)]
    
    if region_filter and 'All' not in region_filter:
        filtered_df = filtered_df[filtered_df['region'].isin(region_filter)]
    
    if channel_filter and 'All' not in channel_filter:
        filtered_df = filtered_df[filtered_df['channel'].isin(channel_filter)]
    
    if category_filter and 'All' not in category_filter:
        filtered_df = filtered_df[filtered_df['category'].isin(category_filter)]
    
    return filtered_df


def main():
    """
    Main application function
    """
    
    # Theme colors
    theme = get_theme_colors()
    
    # Header with theme toggle
    col_header1, col_header2, col_header3 = st.columns([1, 3, 1])
    
    with col_header1:
        st.write("")  # Spacer
    
    with col_header2:
        st.markdown('<div class="main-header">📊 Sales Performance Dashboard</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">FY 2025-26 | Regional Sales Analytics</div>', unsafe_allow_html=True)
    
    with col_header3:
        # Theme toggle button
        if st.session_state.theme == 'light':
            if st.button("🌙 Dark Mode", key="theme_toggle"):
                st.session_state.theme = 'dark'
                st.rerun()
        else:
            if st.button("☀️ Light Mode", key="theme_toggle"):
                st.session_state.theme = 'light'
                st.rerun()
    
    # Load data
    try:
        df = load_data()
    except FileNotFoundError as e:
        st.error(str(e))
        st.stop()
    except ValueError as e:
        st.error(f"Data validation error: {str(e)}")
        st.stop()
    except Exception as e:
        st.error(f"Unexpected error loading data: {str(e)}")
        st.stop()
    
    # Sidebar - Filters
    st.sidebar.header("🔍 Filters")
    
    # Get unique values for filters (sorted)
    months = ['All'] + sorted(df['month_name'].unique().tolist(), 
                               key=lambda x: pd.to_datetime(x, format='%b %Y'))
    regions = ['All'] + sorted(df['region'].unique().tolist())
    channels = ['All'] + sorted(df['channel'].unique().tolist())
    categories = ['All'] + sorted(df['category'].unique().tolist())
    
    # Filter widgets (storing in temp state)
    st.session_state.temp_filters['month'] = st.sidebar.multiselect(
        "Month",
        options=months,
        default=st.session_state.applied_filters['month'],
        help="Select one or more months",
        key="month_filter"
    )
    
    st.session_state.temp_filters['region'] = st.sidebar.multiselect(
        "Region",
        options=regions,
        default=st.session_state.applied_filters['region'],
        help="Select one or more regions",
        key="region_filter"
    )
    
    st.session_state.temp_filters['channel'] = st.sidebar.multiselect(
        "Channel",
        options=channels,
        default=st.session_state.applied_filters['channel'],
        help="Select one or more channels",
        key="channel_filter"
    )
    
    st.session_state.temp_filters['category'] = st.sidebar.multiselect(
        "Category",
        options=categories,
        default=st.session_state.applied_filters['category'],
        help="Select one or more categories",
        key="category_filter"
    )
    
    # Apply and Reset buttons
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        if st.button("✅ Apply Filters", use_container_width=True, type="primary"):
            # Copy temp filters to applied filters
            st.session_state.applied_filters = st.session_state.temp_filters.copy()
            st.rerun()
    
    with col2:
        if st.button("🔄 Reset", use_container_width=True):
            # Reset all filters to 'All'
            st.session_state.applied_filters = {
                'month': ['All'],
                'region': ['All'],
                'channel': ['All'],
                'category': ['All']
            }
            st.session_state.temp_filters = {
                'month': ['All'],
                'region': ['All'],
                'channel': ['All'],
                'category': ['All']
            }
            st.rerun()
    
    # Apply filters using applied_filters state
    filtered_df = apply_filters(
        df, 
        st.session_state.applied_filters['month'],
        st.session_state.applied_filters['region'],
        st.session_state.applied_filters['channel'],
        st.session_state.applied_filters['category']
    )
    
    # Check if filtered data is empty
    if len(filtered_df) == 0:
        st.warning("⚠️ No data available for the selected filters. Please adjust your selection.")
        st.stop()
    
    # Display filter info
    st.sidebar.markdown("---")
    st.sidebar.info(f"**Showing:** {len(filtered_df):,} of {len(df):,} records")
    
    # KPI Cards
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        revenue = calculate_revenue(filtered_df)
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-value">₹{format_currency(revenue)}</div>
                <div class="kpi-label">Total Revenue</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        units = calculate_units(filtered_df)
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-value">{format_number(units)}</div>
                <div class="kpi-label">Units Sold</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        aov = calculate_aov(filtered_df)
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-value">₹{aov:,.0f}</div>
                <div class="kpi-label">Average Order Value</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col4:
        gm_pct = calculate_gross_margin_percentage(filtered_df)
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-value">{gm_pct:.2f}%</div>
                <div class="kpi-label">Gross Margin %</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Monthly Revenue Trend
    st.markdown('<div class="section-header">📈 Monthly Revenue Trend</div>', unsafe_allow_html=True)
    
    monthly_data = calculate_monthly_revenue(filtered_df)
    
    if len(monthly_data) > 0:
        mom_data = calculate_mom_growth(monthly_data)
        
        # Create line chart with MoM growth
        fig_trend = go.Figure()
        
        # Revenue line
        fig_trend.add_trace(go.Scatter(
            x=mom_data['month_name'],
            y=mom_data['revenue'],
            mode='lines+markers',
            name='Revenue',
            line=dict(color=theme['accent'], width=3),
            marker=dict(size=8),
            hovertemplate='<b>%{x}</b><br>Revenue: ₹%{y:,.0f}<extra></extra>'
        ))
        
        fig_trend.update_layout(
            xaxis_title="Month",
            yaxis_title="Revenue (INR)",
            hovermode='x unified',
            height=400,
            showlegend=False,
            plot_bgcolor=theme['chart_bg'],
            paper_bgcolor=theme['chart_bg'],
            font=dict(color=theme['text_primary']),
            xaxis=dict(gridcolor=theme['grid_color'], color=theme['text_primary']),
            yaxis=dict(gridcolor=theme['grid_color'], color=theme['text_primary'])
        )
        
        st.plotly_chart(fig_trend, use_container_width=True)
        
        # Show MoM growth metrics
        if len(mom_data) > 1:
            st.markdown(f'<p style="color: {theme["text_primary"]}; font-weight: bold;">Month-over-Month Growth:</p>', unsafe_allow_html=True)
            mom_cols = st.columns(min(len(mom_data), 6))
            for idx, row in mom_data.iterrows():
                col_idx = idx % 6
                with mom_cols[col_idx]:
                    if pd.notna(row['mom_growth_pct']):
                        growth_color = "green" if row['mom_growth_pct'] > 0 else "red"
                        st.metric(
                            label=row['month_name'],
                            value=f"₹{format_currency(row['revenue'])}",
                            delta=f"{row['mom_growth_pct']:.1f}%"
                        )
                    else:
                        st.metric(
                            label=row['month_name'],
                            value=f"₹{format_currency(row['revenue'])}"
                        )
    else:
        st.info("No monthly data available for the selected filters.")
    
    # Secondary Analysis
    st.markdown('<div class="section-header">📊 Performance by Dimensions</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    # Revenue by Region
    with col1:
        st.markdown(f'<p style="color: {theme["text_primary"]}; font-weight: bold;">Revenue by Region</p>', unsafe_allow_html=True)
        region_data = get_revenue_by_dimension(filtered_df, 'region')
        
        if len(region_data) > 0:
            fig_region = px.bar(
                region_data,
                x='revenue',
                y='region',
                orientation='h',
                text='revenue',
                color='revenue',
                color_continuous_scale='Blues' if st.session_state.theme == 'light' else 'Teal'
            )
            fig_region.update_traces(
                texttemplate='₹%{text:,.0f}',
                textposition='outside'
            )
            fig_region.update_layout(
                xaxis_title="Revenue (INR)",
                yaxis_title="Region",
                showlegend=False,
                height=300,
                plot_bgcolor=theme['chart_bg'],
                paper_bgcolor=theme['chart_bg'],
                font=dict(color=theme['text_primary']),
                xaxis=dict(gridcolor=theme['grid_color'], color=theme['text_primary']),
                yaxis=dict(categoryorder='total ascending', color=theme['text_primary'])
            )
            st.plotly_chart(fig_region, use_container_width=True)
        else:
            st.info("No data available")
    
    # Revenue by Channel
    with col2:
        st.markdown(f'<p style="color: {theme["text_primary"]}; font-weight: bold;">Revenue by Channel</p>', unsafe_allow_html=True)
        channel_data = get_revenue_by_dimension(filtered_df, 'channel')
        
        if len(channel_data) > 0:
            fig_channel = px.pie(
                channel_data,
                values='revenue',
                names='channel',
                hole=0.4,
                color_discrete_sequence=px.colors.qualitative.Set2 if st.session_state.theme == 'light' else px.colors.qualitative.Pastel
            )
            fig_channel.update_traces(
                textposition='inside',
                textinfo='percent+label',
                hovertemplate='<b>%{label}</b><br>Revenue: ₹%{value:,.0f}<br>Share: %{percent}<extra></extra>'
            )
            fig_channel.update_layout(
                showlegend=True,
                height=300,
                paper_bgcolor=theme['chart_bg'],
                font=dict(color=theme['text_primary']),
                legend=dict(font=dict(color=theme['text_primary']))
            )
            st.plotly_chart(fig_channel, use_container_width=True)
        else:
            st.info("No data available")
    
    col3, col4 = st.columns(2)
    
    # Revenue by Category
    with col3:
        st.markdown(f'<p style="color: {theme["text_primary"]}; font-weight: bold;">Revenue by Category</p>', unsafe_allow_html=True)
        category_data = get_revenue_by_dimension(filtered_df, 'category')
        
        if len(category_data) > 0:
            fig_category = px.bar(
                category_data,
                x='category',
                y='revenue',
                text='revenue',
                color='revenue',
                color_continuous_scale='Greens' if st.session_state.theme == 'light' else 'Mint'
            )
            fig_category.update_traces(
                texttemplate='₹%{text:,.0f}',
                textposition='outside'
            )
            fig_category.update_layout(
                xaxis_title="Category",
                yaxis_title="Revenue (INR)",
                showlegend=False,
                height=300,
                plot_bgcolor=theme['chart_bg'],
                paper_bgcolor=theme['chart_bg'],
                font=dict(color=theme['text_primary']),
                xaxis=dict(gridcolor=theme['grid_color'], color=theme['text_primary']),
                yaxis=dict(gridcolor=theme['grid_color'], color=theme['text_primary'])
            )
            st.plotly_chart(fig_category, use_container_width=True)
        else:
            st.info("No data available")
    
    # Top 10 Products
    with col4:
        st.markdown(f'<p style="color: {theme["text_primary"]}; font-weight: bold;">Top 10 Products</p>', unsafe_allow_html=True)
        top_products = get_top_products(filtered_df, top_n=10)
        
        if len(top_products) > 0:
            fig_products = px.bar(
                top_products,
                x='revenue',
                y='product',
                orientation='h',
                text='revenue',
                color='revenue',
                color_continuous_scale='Oranges' if st.session_state.theme == 'light' else 'Peach'
            )
            fig_products.update_traces(
                texttemplate='₹%{text:,.0f}',
                textposition='outside'
            )
            fig_products.update_layout(
                xaxis_title="Revenue (INR)",
                yaxis_title="Product",
                showlegend=False,
                height=300,
                plot_bgcolor=theme['chart_bg'],
                paper_bgcolor=theme['chart_bg'],
                font=dict(color=theme['text_primary']),
                xaxis=dict(gridcolor=theme['grid_color'], color=theme['text_primary']),
                yaxis=dict(categoryorder='total ascending', color=theme['text_primary'])
            )
            st.plotly_chart(fig_products, use_container_width=True)
        else:
            st.info("No data available")
    
    # Business Insights
    st.markdown('<div class="section-header">💡 Business Insights</div>', unsafe_allow_html=True)
    
    insights = generate_insights(filtered_df, df)
    
    insights_html = '<div class="insight-box"><ul style="list-style-type: none; padding-left: 0;">'
    for insight in insights:
        insights_html += f'<li style="color: {theme["text_primary"]}; margin-bottom: 0.5rem;">• {insight}</li>'
    insights_html += '</ul></div>'
    
    st.markdown(insights_html, unsafe_allow_html=True)
    
    # Dataset Note
    st.markdown("---")
    st.markdown(
        f'<p style="color: {theme["text_secondary"]}; font-size: 0.9rem;">'
        '<strong>Note:</strong> This dashboard uses synthetic sales data for demonstration purposes. '
        'Insights are descriptive and based on the filtered dataset. '
        'Correlation does not imply causation.</p>',
        unsafe_allow_html=True
    )
    
    # Footer
    st.markdown(
        f"""
        <div style="text-align: center; color: {theme['text_secondary']}; margin-top: 2rem; padding: 1rem;">
            <small>Sales Performance Dashboard | MBA Data Science Project | AI Powered Developer Tools</small>
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
