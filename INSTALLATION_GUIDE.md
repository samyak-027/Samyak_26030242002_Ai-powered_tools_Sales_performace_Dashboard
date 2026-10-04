# 🚀 Installation and Running Guide

## Sales Performance Dashboard App

---

## ✅ Prerequisites Checklist

Before starting, ensure you have:

- [x] Python 3.11 or higher installed
- [x] pip (Python package manager)
- [x] Terminal/Command Prompt access
- [x] Excel file: `T01_Sales_performance_dashboard_app.xlsx`

---

## 📦 Installation Steps

### Step 1: Navigate to Project Directory

```bash
cd /Users/samyakacharya/scit_edu/sem-1/ai_powered_developer_tools/project
```

### Step 2: Activate Virtual Environment

The virtual environment `.venv` is already created. Activate it:

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

You should see `(.venv)` prefix in your terminal prompt.

### Step 3: Verify Installation

All required packages are already installed. Verify with:

```bash
python test_setup.py
```

**Expected Output:**
```
============================================================
✓ ALL TESTS PASSED - Dashboard is ready to run!
============================================================
```

If you see this, you're ready to proceed!

---

## ▶️ Running the Dashboard

### Start the Application

```bash
streamlit run app.py
```

### What Happens Next:

1. **Terminal Output**: You'll see something like:
   ```
   You can now view your Streamlit app in your browser.
   
   Local URL: http://localhost:8501
   Network URL: http://192.168.x.x:8501
   ```

2. **Browser**: The dashboard will automatically open in your default web browser

3. **If browser doesn't open**: Manually navigate to `http://localhost:8501`

---

## 🎮 Using the Dashboard

### 1. **Filters (Left Sidebar)**

- **Month**: Select specific months or "All"
- **Region**: Choose regions (North, South, East, West) or "All"
- **Channel**: Filter by sales channel or "All"
- **Category**: Select product categories or "All"

**Pro Tip**: Hold `Ctrl` (Windows) or `Cmd` (Mac) to select multiple items

### 2. **Reset Filters**

Click the "🔄 Reset Filters" button in the sidebar to clear all selections

### 3. **Interactive Charts**

- **Hover** over chart elements to see detailed information
- **Zoom** on line charts by clicking and dragging
- **Pan** by holding Shift and dragging

### 4. **KPI Cards**

View key metrics at the top:
- Total Revenue
- Units Sold
- Average Order Value (AOV)
- Gross Margin %

---

## 🛑 Stopping the Dashboard

Press `Ctrl + C` in the terminal where Streamlit is running

---

## 🔧 Troubleshooting

### Problem: "Module not found" errors

**Solution:**
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### Problem: "File not found: T01_Sales_performance_dashboard_app.xlsx"

**Solution:**
Verify the file location:
```bash
ls -la data/
```

The file should be in `data/T01_Sales_performance_dashboard_app.xlsx`

### Problem: Dashboard shows blank/no data

**Solution:**
1. Check if filters are too restrictive
2. Click "Reset Filters"
3. Verify data loaded: Check terminal for error messages

### Problem: Port 8501 already in use

**Solution:**
Run on a different port:
```bash
streamlit run app.py --server.port 8502
```

### Problem: Slow performance

**Solution:**
- Close other browser tabs
- Restart the Streamlit app
- Clear browser cache

---

## 📊 Testing the Dashboard

### Quick Validation Test

1. **Open dashboard** (no filters)
2. **Verify KPIs** match these benchmarks:
   - Total Revenue: ₹24,092,037.95 (or ₹24.09 Cr)
   - Units Sold: 12,001
   - AOV: ₹12,046.02
   - Gross Margin %: 33.39%

3. **Test Filters:**
   - Select "West" in Region filter
   - Verify all charts update
   - Click "Reset Filters"
   - Verify all data returns

4. **Test Visualizations:**
   - Hover over monthly revenue chart
   - Check if all 4 charts display correctly
   - Verify Top 10 Products shows

---

## 🎯 Dashboard Features to Explore

### 1. **Cross-Filtering**
Try: Select "West" (Region) + "Online Store" (Channel) + "Electronics" (Category)
Result: All KPIs and charts update to show only matching records

### 2. **Month-over-Month Analysis**
Look at the monthly revenue trend and the MoM growth metrics below it

### 3. **Regional Comparison**
Compare revenue across different regions in the horizontal bar chart

### 4. **Channel Distribution**
View the donut chart to see revenue split by sales channel

### 5. **Product Performance**
Check the Top 10 Products chart to identify best sellers

### 6. **Business Insights**
Scroll to the bottom to see automatically generated insights

---

## 📁 Project Files Overview

```
project/
├── app.py                    # Main dashboard application ⭐
├── test_setup.py             # Validation script
├── requirements.txt          # Dependencies list
├── README.md                 # Full documentation
├── INSTALLATION_GUIDE.md     # This file
│
├── data/
│   └── T01_Sales_performance_dashboard_app.xlsx
│
└── utils/
    ├── __init__.py           # Package initializer
    ├── data_loader.py        # Data loading functions
    └── calculations.py       # KPI calculation functions
```

---

## 💡 Tips for Best Experience

1. **Use Chrome or Firefox** for best compatibility
2. **Expand browser to full screen** for optimal layout
3. **Start with no filters** to see overall performance
4. **Then narrow down** using filters to drill into specifics
5. **Compare periods** by selecting different months
6. **Reset frequently** to avoid getting lost in filters

---

## 🎓 For Academic Presentation

### Demonstrating the Dashboard:

1. **Start with overview** (no filters)
   - Show all KPIs
   - Explain benchmark validation

2. **Show filter functionality**
   - Apply one filter at a time
   - Show how all charts update

3. **Highlight insights**
   - Point out top performing segments
   - Discuss MoM growth trends

4. **Demonstrate interactivity**
   - Hover over charts
   - Show Reset Filters

5. **Discuss architecture**
   - Modular code structure
   - Separation of concerns
   - Reusable functions

---

## 🆘 Getting Help

### If something doesn't work:

1. **Run validation script:**
   ```bash
   python test_setup.py
   ```

2. **Check terminal output** for error messages

3. **Verify virtual environment is activated:**
   Look for `(.venv)` in terminal prompt

4. **Reinstall packages:**
   ```bash
   pip install -r requirements.txt --force-reinstall
   ```

5. **Check Python version:**
   ```bash
   python --version
   ```
   Should be 3.11 or higher

---

## ✅ Quick Command Reference

| Task | Command |
|------|---------|
| Activate venv | `source .venv/bin/activate` |
| Test setup | `python test_setup.py` |
| Run dashboard | `streamlit run app.py` |
| Stop dashboard | `Ctrl + C` |
| Deactivate venv | `deactivate` |
| Reinstall packages | `pip install -r requirements.txt` |
| Check Python version | `python --version` |
| List packages | `pip list` |

---

## 🎉 Success Indicators

You know everything is working when:

- ✅ Test script shows "ALL TESTS PASSED"
- ✅ Dashboard opens in browser without errors
- ✅ KPIs match benchmark values (with no filters)
- ✅ All filters work and update charts
- ✅ Hover tooltips show on charts
- ✅ Business insights generate automatically
- ✅ Reset Filters button clears selections

---

**Dashboard Ready! 🚀**

Run: `streamlit run app.py`
