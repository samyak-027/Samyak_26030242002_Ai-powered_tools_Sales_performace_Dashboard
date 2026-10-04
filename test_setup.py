"""
Quick test script to validate the dashboard setup
Run this before launching the main app
"""

import sys
from pathlib import Path

print("=" * 60)
print("Sales Performance Dashboard - Setup Validation")
print("=" * 60)

# Test 1: Check Python version
print("\n1. Python Version Check...")
if sys.version_info >= (3, 11):
    print(f"   ✓ Python {sys.version_info.major}.{sys.version_info.minor} (Recommended)")
else:
    print(f"   ⚠ Python {sys.version_info.major}.{sys.version_info.minor} (3.11+ recommended)")

# Test 2: Import required packages
print("\n2. Package Import Check...")
required_packages = ['pandas', 'streamlit', 'plotly', 'openpyxl']
missing_packages = []

for package in required_packages:
    try:
        __import__(package)
        print(f"   ✓ {package}")
    except ImportError:
        print(f"   ✗ {package} - NOT INSTALLED")
        missing_packages.append(package)

if missing_packages:
    print(f"\n   ⚠ Missing packages: {', '.join(missing_packages)}")
    print("   Run: pip install -r requirements.txt")
    sys.exit(1)

# Test 3: Check file structure
print("\n3. File Structure Check...")
required_files = [
    'app.py',
    'requirements.txt',
    'README.md',
    'utils/__init__.py',
    'utils/data_loader.py',
    'utils/calculations.py'
]

for file in required_files:
    if Path(file).exists():
        print(f"   ✓ {file}")
    else:
        print(f"   ✗ {file} - MISSING")

# Test 4: Check data file
print("\n4. Data File Check...")
data_paths = [
    'data/T01_Sales_performance_dashboard_app.xlsx',
    'T01_Sales_performance_dashboard_app.xlsx'
]

data_file_found = False
for path in data_paths:
    if Path(path).exists():
        print(f"   ✓ Found: {path}")
        data_file_found = True
        break

if not data_file_found:
    print("   ✗ Data file not found!")
    print("   Expected: data/T01_Sales_performance_dashboard_app.xlsx")
    sys.exit(1)

# Test 5: Load and validate data
print("\n5. Data Loading Test...")
try:
    from utils.data_loader import load_sales_data
    
    # Find the data file
    if Path('data/T01_Sales_performance_dashboard_app.xlsx').exists():
        df = load_sales_data('data/T01_Sales_performance_dashboard_app.xlsx')
    else:
        df = load_sales_data('T01_Sales_performance_dashboard_app.xlsx')
    
    print(f"   ✓ Data loaded successfully")
    print(f"   ✓ Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    
    # Test KPI calculations
    from utils.calculations import (
        calculate_revenue,
        calculate_units,
        calculate_aov,
        calculate_gross_margin_percentage
    )
    
    revenue = calculate_revenue(df)
    units = calculate_units(df)
    aov = calculate_aov(df)
    gm_pct = calculate_gross_margin_percentage(df)
    
    print(f"\n6. KPI Calculation Test (No Filters)...")
    print(f"   Total Revenue: ₹{revenue:,.2f}")
    print(f"   Total Units: {units:,}")
    print(f"   Average Order Value: ₹{aov:,.2f}")
    print(f"   Gross Margin %: {gm_pct:.2f}%")
    
    # Validate against benchmarks
    print(f"\n7. Benchmark Validation...")
    
    expected_revenue = 24092037.95
    expected_units = 12001
    expected_aov = 12046.02
    expected_gm_pct = 33.39
    
    tolerance = 0.01  # 1% tolerance
    
    def check_value(actual, expected, name):
        diff_pct = abs(actual - expected) / expected * 100
        if diff_pct <= tolerance:
            print(f"   ✓ {name}: PASS (within {tolerance}%)")
            return True
        else:
            print(f"   ⚠ {name}: {diff_pct:.2f}% deviation (expected ₹{expected:,.2f}, got ₹{actual:,.2f})")
            return False
    
    validations = [
        check_value(revenue, expected_revenue, "Revenue"),
        check_value(units, expected_units, "Units"),
        check_value(aov, expected_aov, "AOV"),
        check_value(gm_pct, expected_gm_pct, "Gross Margin %")
    ]
    
    if all(validations):
        print("\n" + "=" * 60)
        print("✓ ALL TESTS PASSED - Dashboard is ready to run!")
        print("=" * 60)
        print("\nRun the dashboard with:")
        print("  streamlit run app.py")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("⚠ Some validations failed - Check calculations")
        print("=" * 60)
        
except Exception as e:
    print(f"   ✗ Error: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
