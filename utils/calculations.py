"""
Business logic and KPI calculation module
Contains all functions for calculating KPIs and aggregations
"""

import pandas as pd
import numpy as np


def calculate_revenue(df):
    """
    Calculate total revenue
    
    Args:
        df: Filtered DataFrame
        
    Returns:
        float: Total revenue in INR
    """
    return df['revenue_inr'].sum()


def calculate_units(df):
    """
    Calculate total units sold
    
    Args:
        df: Filtered DataFrame
        
    Returns:
        int: Total units sold
    """
    return int(df['units'].sum())


def calculate_aov(df):
    """
    Calculate Average Order Value (AOV)
    AOV = Total Revenue / Number of Unique Orders
    
    Args:
        df: Filtered DataFrame
        
    Returns:
        float: Average order value in INR
    """
    total_revenue = df['revenue_inr'].sum()
    unique_orders = df['order_id'].nunique()
    
    if unique_orders == 0:
        return 0
    
    return total_revenue / unique_orders


def calculate_gross_margin(df):
    """
    Calculate total gross margin
    
    Args:
        df: Filtered DataFrame
        
    Returns:
        float: Total gross margin in INR
    """
    return df['gross_margin_inr'].sum()


def calculate_gross_margin_percentage(df):
    """
    Calculate gross margin percentage
    Gross Margin % = (Total Gross Margin / Total Revenue) * 100
    
    Note: This is calculated at aggregate level, not by averaging row-level percentages
    
    Args:
        df: Filtered DataFrame
        
    Returns:
        float: Gross margin percentage
    """
    total_revenue = df['revenue_inr'].sum()
    total_margin = df['gross_margin_inr'].sum()
    
    if total_revenue == 0:
        return 0
    
    return (total_margin / total_revenue) * 100


def calculate_monthly_revenue(df):
    """
    Calculate revenue by month
    
    Args:
        df: Filtered DataFrame
        
    Returns:
        DataFrame with columns: month, month_name, revenue
        Sorted by month chronologically
    """
    monthly_data = df.groupby(['month', 'month_name'], as_index=False).agg({
        'revenue_inr': 'sum'
    })
    
    monthly_data.columns = ['month', 'month_name', 'revenue']
    monthly_data = monthly_data.sort_values('month')
    
    return monthly_data


def calculate_mom_growth(monthly_revenue_df):
    """
    Calculate Month-over-Month (MoM) revenue growth percentage
    MoM Growth % = ((Current Month - Previous Month) / Previous Month) * 100
    
    Args:
        monthly_revenue_df: DataFrame with monthly revenue (from calculate_monthly_revenue)
        
    Returns:
        DataFrame with additional mom_growth_pct column
    """
    df = monthly_revenue_df.copy()
    
    # Calculate previous month revenue
    df['prev_month_revenue'] = df['revenue'].shift(1)
    
    # Calculate growth percentage
    df['mom_growth_pct'] = ((df['revenue'] - df['prev_month_revenue']) / df['prev_month_revenue']) * 100
    
    # First month will have NaN for growth (no previous month)
    # This is expected and handled in visualization
    
    return df


def get_top_products(df, top_n=10):
    """
    Get top N products by revenue
    
    Args:
        df: Filtered DataFrame
        top_n: Number of top products to return (default: 10)
        
    Returns:
        DataFrame with product and revenue, sorted by revenue descending
    """
    product_revenue = df.groupby('product', as_index=False).agg({
        'revenue_inr': 'sum'
    })
    
    product_revenue.columns = ['product', 'revenue']
    product_revenue = product_revenue.sort_values('revenue', ascending=False).head(top_n)
    
    return product_revenue


def get_revenue_by_dimension(df, dimension):
    """
    Calculate revenue by any dimension (region, channel, category, etc.)
    
    Args:
        df: Filtered DataFrame
        dimension: Column name to group by (e.g., 'region', 'channel', 'category')
        
    Returns:
        DataFrame with dimension and revenue, sorted by revenue descending
    """
    if dimension not in df.columns:
        return pd.DataFrame()
    
    revenue_data = df.groupby(dimension, as_index=False).agg({
        'revenue_inr': 'sum'
    })
    
    revenue_data.columns = [dimension, 'revenue']
    revenue_data = revenue_data.sort_values('revenue', ascending=False)
    
    return revenue_data


def generate_insights(df, original_df):
    """
    Generate business insights from the filtered data
    
    Args:
        df: Filtered DataFrame
        original_df: Original unfiltered DataFrame for comparison
        
    Returns:
        List of insight strings
    """
    insights = []
    
    if len(df) == 0:
        return ["No data available for the selected filters."]
    
    # Total revenue insight
    total_revenue = calculate_revenue(df)
    insights.append(f"**Total Revenue:** ₹{format_currency(total_revenue)}")
    
    # Regional performance
    region_revenue = get_revenue_by_dimension(df, 'region')
    if len(region_revenue) > 0:
        top_region = region_revenue.iloc[0]
        region_contribution = (top_region['revenue'] / total_revenue) * 100
        insights.append(
            f"**Top Region:** {top_region['region']} generated ₹{format_currency(top_region['revenue'])} "
            f"({region_contribution:.1f}% of total revenue)"
        )
    
    # Channel performance
    channel_revenue = get_revenue_by_dimension(df, 'channel')
    if len(channel_revenue) > 0:
        top_channel = channel_revenue.iloc[0]
        channel_contribution = (top_channel['revenue'] / total_revenue) * 100
        insights.append(
            f"**Top Channel:** {top_channel['channel']} contributed ₹{format_currency(top_channel['revenue'])} "
            f"({channel_contribution:.1f}% of total revenue)"
        )
    
    # Category performance
    category_revenue = get_revenue_by_dimension(df, 'category')
    if len(category_revenue) > 0:
        top_category = category_revenue.iloc[0]
        category_contribution = (top_category['revenue'] / total_revenue) * 100
        insights.append(
            f"**Top Category:** {top_category['category']} generated ₹{format_currency(top_category['revenue'])} "
            f"({category_contribution:.1f}% of total revenue)"
        )
    
    # Product performance
    top_products = get_top_products(df, top_n=1)
    if len(top_products) > 0:
        top_product = top_products.iloc[0]
        product_contribution = (top_product['revenue'] / total_revenue) * 100
        insights.append(
            f"**Top Product:** {top_product['product']} generated ₹{format_currency(top_product['revenue'])} "
            f"({product_contribution:.1f}% of total revenue)"
        )
    
    # Profitability
    gm_pct = calculate_gross_margin_percentage(df)
    insights.append(f"**Gross Margin:** {gm_pct:.2f}%")
    
    if gm_pct > 35:
        insights.append("✓ Gross margin is healthy (above 35%)")
    elif gm_pct > 25:
        insights.append("⚠ Gross margin is moderate (25-35%). Consider cost optimization.")
    else:
        insights.append("⚠ Gross margin is below 25%. Cost optimization recommended.")
    
    # Month-over-month growth
    monthly_revenue = calculate_monthly_revenue(df)
    if len(monthly_revenue) >= 2:
        mom_data = calculate_mom_growth(monthly_revenue)
        # Get latest month growth
        latest_growth = mom_data.iloc[-1]
        if not pd.isna(latest_growth['mom_growth_pct']):
            if latest_growth['mom_growth_pct'] > 0:
                insights.append(
                    f"**Latest MoM Growth:** +{latest_growth['mom_growth_pct']:.1f}% "
                    f"in {latest_growth['month_name']}"
                )
            else:
                insights.append(
                    f"**Latest MoM Growth:** {latest_growth['mom_growth_pct']:.1f}% "
                    f"in {latest_growth['month_name']}"
                )
    
    return insights


def format_currency(value):
    """Format an INR amount using Lakhs (L) and Crores (Cr).

    Values from ₹1,00,000 use Lakhs and values from ₹1,00,00,000 use
    Crores. The rupee symbol is deliberately omitted so callers can place it
    appropriately in plain text, HTML, chart labels, or metrics.
    """
    try:
        numeric_value = float(value)
    except (TypeError, ValueError):
        return "0"

    if not np.isfinite(numeric_value):
        return "0"

    absolute_value = abs(numeric_value)
    sign = "-" if numeric_value < 0 else ""

    if absolute_value >= 10_000_000:  # ₹1 crore
        return f"{sign}{absolute_value / 10_000_000:.2f} Cr"
    if absolute_value >= 100_000:  # ₹1 lakh
        return f"{sign}{absolute_value / 100_000:.2f} L"
    return f"{numeric_value:,.0f}"


def format_number(value):
    """
    Format large numbers with commas
    
    Args:
        value: Numeric value to format
        
    Returns:
        Formatted string
    """
    return f"{value:,}"
