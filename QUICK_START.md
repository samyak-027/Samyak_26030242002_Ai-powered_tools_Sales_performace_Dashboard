# ⚡ Quick Start Guide

## Sales Performance Dashboard - Get Running in 2 Minutes

---

## 🎯 Three Simple Steps

### 1️⃣ Activate Virtual Environment

```bash
cd /Users/samyakacharya/scit_edu/sem-1/ai_powered_developer_tools/project
source .venv/bin/activate
```

### 2️⃣ Verify Setup (Optional but Recommended)

```bash
python test_setup.py
```

Expected output: `✓ ALL TESTS PASSED`

### 3️⃣ Run Dashboard

```bash
streamlit run app.py
```

**That's it!** The dashboard opens in your browser automatically. 🎉

---

## 🎮 First Steps in Dashboard

1. **Look at KPI cards** at the top (should show ₹24.09 Cr revenue)
2. **Try filters** in the left sidebar
3. **Click "Reset Filters"** to return to full view
4. **Hover over charts** for detailed info
5. **Scroll down** to see Business Insights

---

## 📚 Need More Info?

- **Full Documentation**: See `README.md`
- **Installation Help**: See `INSTALLATION_GUIDE.md`
- **Development Details**: See `AI_DEVELOPMENT_ITERATIONS.md`

---

## 🆘 Quick Troubleshooting

**Problem**: Module not found  
**Fix**: `pip install -r requirements.txt`

**Problem**: No data showing  
**Fix**: Click "Reset Filters" button

**Problem**: Port in use  
**Fix**: `streamlit run app.py --server.port 8502`

---

## ✅ Validation

With no filters, you should see:
- Revenue: ₹24.09 Cr
- Units: 12,001
- AOV: ₹12,046
- Gross Margin: 33.39%

---

**Happy Analyzing! 📊**
