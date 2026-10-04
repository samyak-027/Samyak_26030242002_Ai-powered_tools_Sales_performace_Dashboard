#!/usr/bin/env python3

print("Testing Python environment...")

try:
    import streamlit as st
    print("✓ Streamlit imported successfully")
except ImportError as e:
    print(f"✗ Streamlit import failed: {e}")

try:
    import pandas as pd
    print("✓ Pandas imported successfully")
except ImportError as e:
    print(f"✗ Pandas import failed: {e}")

try:
    import plotly.express as px
    print("✓ Plotly imported successfully")
except ImportError as e:
    print(f"✗ Plotly import failed: {e}")

print("\nEnvironment test complete.")