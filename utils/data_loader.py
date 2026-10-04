"""
Data loading and validation module
Handles Excel file loading, date parsing, and data validation
"""

import pandas as pd
import re
from pathlib import Path


def parse_date_with_timezone(date_str):
    """
    Parse date strings that may contain timezone information
    Example: "2024-01-15 GMT+0530 (India Standard Time)"
    
    Args:
        date_str: String representation of date
        
    Returns:
        Parsed datetime object
    """
    if pd.isna(date_str):
        return pd.NaT
    
    # If already a datetime object, return as is
    if isinstance(date_str, pd.Timestamp):
        return date_str
    
    # Convert to string
    date_str = str(date_str)
    
    # Remove timezone information using regex
    # Pattern matches GMT+XXXX or similar timezone patterns and text in parentheses
    cleaned_date = re.sub(r'\s*GMT[+-]\d{4}\s*\([^)]*\)', '', date_str)
    cleaned_date = re.sub(r'\s*[+-]\d{4}\s*', '', cleaned_date)
    cleaned_date = cleaned_date.strip()
    
    try:
        return pd.to_datetime(cleaned_date)
    except Exception as e:
        # Try default pandas parsing as fallback
        try:
            return pd.to_datetime(date_str)
        except:
            return pd.NaT


def load_sales_data(file_path):
    """
    Load sales data from Excel file
    
    Args:
        file_path: Path to the Excel file
        
    Returns:
        DataFrame with cleaned and processed sales data
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If required columns are missing
    """
    # Check if file exists
    if not Path(file_path).exists():
        raise FileNotFoundError(
            f"Sales data file not found: {file_path}\n"
            f"Please ensure the Excel file is in the correct location."
        )
    
    try:
        # Load the Excel file
        df = pd.read_excel(file_path, sheet_name='Sales')
        
        # Validate the data
        validate_data(df)
        
        # Parse order_date with timezone handling
        df['order_date'] = df['order_date'].apply(parse_date_with_timezone)
        
        # Remove rows with invalid dates
        invalid_dates = df['order_date'].isna().sum()
        if invalid_dates > 0:
            print(f"Warning: Removed {invalid_dates} rows with invalid dates")
            df = df.dropna(subset=['order_date'])
        
        # Create month column (YYYY-MM format for sorting)
        df['month'] = df['order_date'].dt.to_period('M')
        
        # Create month_name for display (e.g., "Jan 2024")
        df['month_name'] = df['order_date'].dt.strftime('%b %Y')
        
        # Ensure numeric columns are proper numeric types
        numeric_columns = ['units', 'unit_price_inr', 'discount_pct', 
                          'revenue_inr', 'cost_inr', 'gross_margin_inr']
        
        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Fill NaN values in numeric columns with 0
        df[numeric_columns] = df[numeric_columns].fillna(0)
        
        return df
        
    except Exception as e:
        raise ValueError(f"Error loading sales data: {str(e)}")


def validate_data(df):
    """
    Validate that the DataFrame contains all required columns
    
    Args:
        df: DataFrame to validate
        
    Raises:
        ValueError: If required columns are missing
    """
    required_columns = [
        'order_id', 'order_date', 'region', 'city', 'state', 
        'city_tier', 'channel', 'category', 'product', 
        'units', 'unit_price_inr', 'discount_pct', 
        'revenue_inr', 'cost_inr', 'gross_margin_inr'
    ]
    
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}\n"
            f"Available columns: {', '.join(df.columns.tolist())}"
        )
    
    # Validate that we have data
    if len(df) == 0:
        raise ValueError("The Sales sheet contains no data rows")
    
    return True
