# T01 – Sales Performance Dashboard App

Name: Samyak Acharya

PRN: 26030242002

Batch : 2026-2028 (M.B.A. DS & DA)

🚀 **Live Demo**: [https://sales-performance-dashboard-dotx.streamlit.app/](https://sales-performance-dashboard-dotx.streamlit.app/)

## 📋 Project Overview

An interactive Sales Performance Dashboard built with Python and Streamlit for analyzing sales data across multiple dimensions. This dashboard helps Regional Sales Heads understand performance trends, identify opportunities, and make data-driven decisions.

**Academic Context:** This project demonstrates AI-assisted development practices for the "AI Powered Developer Tools" subject in an MBA Data Science program.

---

## 🎯 Business Objective

The dashboard enables Regional Sales Heads to:

1. Monitor overall sales performance through key metrics
2. Analyze revenue trends over time
3. Compare performance across regions, channels, and categories
4. Identify top-performing products
5. Track profitability metrics
6. Calculate month-over-month revenue growth
7. Make data-driven strategic decisions

---

## ✨ Features

### Interactive Filters
- **Month**: Filter by specific months or view all periods
- **Region**: Analyze specific regions or compare all regions
- **Channel**: Focus on specific sales channels
- **Category**: Drill down into product categories
- **Cross-filtering**: All filters work together dynamically
- **Reset Filters**: One-click reset to view all data

### Key Performance Indicators (KPIs)
1. **Total Revenue**: Sum of all revenue in INR
2. **Units Sold**: Total units sold across all transactions
3. **Average Order Value (AOV)**: Total Revenue / Number of Unique Orders
4. **Gross Margin %**: (Total Gross Margin / Total Revenue) × 100

### Visualizations
1. **Monthly Revenue Trend**: Interactive line chart showing revenue over time
2. **Month-over-Month Growth**: Growth percentage metrics for each month
3. **Revenue by Region**: Horizontal bar chart comparing regional performance
4. **Revenue by Channel**: Donut chart showing channel distribution
5. **Revenue by Category**: Bar chart comparing category performance
6. **Top 10 Products**: Horizontal bar chart of best-selling products

### Business Insights
Automatically generated insights including:
- Top-performing region, channel, category, and product
- Profitability assessment
- Latest month-over-month growth trends
- Actionable recommendations

---

## 🛠️ Tech Stack

- **Python 3.11+**: Programming language
- **Streamlit**: Web application framework for interactive dashboards
- **Pandas**: Data manipulation and analysis
- **OpenPyXL**: Excel file handling
- **Plotly**: Interactive data visualizations

---

## 📊 Dataset Description

**File**: `T01_Sales_performance_dashboard_app.xlsx`  
**Sheet**: `Sales`  
**Records**: ~2,000 transactions

### Columns:
| Column | Description |
|--------|-------------|
| `order_id` | Unique order identifier |
| `order_date` | Date of the transaction |
| `region` | Geographic region (North, South, East, West) |
| `city` | City name |
| `state` | State name |
| `city_tier` | Tier classification (1, 2, 3) |
| `channel` | Sales channel (e.g., Online Store, Retail) |
| `category` | Product category (e.g., Electronics, Clothing) |
| `product` | Product name |
| `units` | Quantity sold |
| `unit_price_inr` | Price per unit in INR |
| `discount_pct` | Discount percentage applied |
| `revenue_inr` | Total revenue in INR |
| `cost_inr` | Total cost in INR |
| `gross_margin_inr` | Gross margin in INR (revenue - cost) |

---

## 📐 KPI Definitions

### Revenue
```
Total Revenue = SUM(revenue_inr)
```

### Units Sold
```
Total Units = SUM(units)
```

### Average Order Value (AOV)
```
AOV = Total Revenue / Number of Unique Orders
```

### Gross Margin
```
Total Gross Margin = SUM(gross_margin_inr)
```

### Gross Margin Percentage
```
Gross Margin % = (SUM(gross_margin_inr) / SUM(revenue_inr)) × 100
```
**Note**: This is calculated at aggregate level, NOT by averaging row-level percentages.

### Month-over-Month (MoM) Growth
```
MoM Growth % = ((Current Month Revenue - Previous Month Revenue) / Previous Month Revenue) × 100
```
**Note**: The first month has no previous month, so MoM growth is not calculated.

---

## 📁 Project Structure

```
project/
│
├── app.py                          # Main Streamlit application
├── requirements.txt                 # Python dependencies
├── README.md                        # Documentation (this file)
│
├── data/
│   └── T01_Sales_performance_dashboard_app.xlsx  # Source data
│
└── utils/
    ├── __init__.py                 # Package initializer
    ├── data_loader.py              # Data loading and validation
    └── calculations.py             # Business logic and KPI calculations
```

### Module Descriptions

**app.py**: Main Streamlit application containing:
- Page configuration and styling
- Filter widgets in sidebar
- KPI card displays
- Visualization layouts
- Main application flow

**utils/data_loader.py**: Data loading module with:
- Excel file loading
- Date parsing (handles timezone strings)
- Data validation
- Month column creation

**utils/calculations.py**: Business logic module with:
- KPI calculation functions
- Monthly aggregation
- MoM growth calculations
- Top products analysis
- Insight generation
- Formatting utilities

---

## 🚀 Installation Instructions

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone or download the project**
   ```bash
   cd /path/to/project
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Verify data file location**
   Ensure `T01_Sales_performance_dashboard_app.xlsx` is in one of these locations:
   - Project root directory
   - `data/` subdirectory

---

## ▶️ How to Run

1. **Activate virtual environment** (if not already activated)
   ```bash
   source .venv/bin/activate  # macOS/Linux
   # or
   .venv\Scripts\activate  # Windows
   ```

2. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

3. **Open in browser**
   - The app will automatically open in your default browser
   - Default URL: http://localhost:8501
   - If it doesn't open automatically, navigate to the URL shown in terminal

4. **Stop the app**
   - Press `Ctrl+C` in the terminal

---

## ✅ Testing Checklist

### Data Loading
- [ ] Application starts without errors
- [ ] Excel file is loaded successfully
- [ ] All required columns are present
- [ ] Date parsing handles timezone strings correctly
- [ ] No missing critical data

### Filters
- [ ] Month filter works correctly
- [ ] Region filter works correctly
- [ ] Channel filter works correctly
- [ ] Category filter works correctly
- [ ] Multiple filters work together (cross-filtering)
- [ ] "Reset Filters" button clears all selections
- [ ] Empty state message shows when no data matches filters

### KPIs
- [ ] Total Revenue displays correctly
- [ ] Units Sold displays correctly
- [ ] Average Order Value calculates correctly
- [ ] Gross Margin % calculates correctly (aggregate level)

### Visualizations
- [ ] Monthly revenue trend chart displays
- [ ] MoM growth metrics display (except first month)
- [ ] Revenue by Region chart displays
- [ ] Revenue by Channel chart displays
- [ ] Revenue by Category chart displays
- [ ] Top 10 Products chart displays
- [ ] All charts update when filters change
- [ ] Hover tooltips work on all charts

### Business Insights
- [ ] Insights generate automatically
- [ ] Insights update based on filters
- [ ] No hard-coded values in insights
- [ ] Recommendations are data-driven

---

## 🔍 KPI Validation

### Benchmark Values (No Filters Applied)

Use these independently calculated values to validate the dashboard:

| KPI | Expected Value |
|-----|----------------|
| Total Orders | 2,000 |
| Total Revenue | ₹24,092,037.95 |
| Total Units | 12,001 |
| Average Order Value | ₹12,046.02 |
| Gross Margin | ₹8,044,916.66 |
| Gross Margin % | 33.39% |

**Validation Steps:**
1. Open the dashboard with no filters applied (select "All" for each filter)
2. Compare displayed KPIs with benchmark values above
3. Values should match within rounding precision
4. If values don't match, check:
   - Data file is correct and complete
   - No rows were filtered out during loading
   - Calculation formulas are correct

---

## 🔄 AI-Assisted Development Iterations

This project demonstrates iterative AI-assisted development across 15+ iterations:

1. **Requirements Analysis**: Understanding business needs and KPI definitions
2. **Architecture Design**: Modular structure with separation of concerns
3. **Data Loading**: Excel file handling and validation
4. **Date Parsing**: Robust handling of timezone strings
5. **KPI Calculations**: Implementing business formulas correctly
6. **Filter Implementation**: Interactive multi-select filters
7. **Cross-Filtering**: Ensuring all filters work together
8. **Monthly Aggregation**: Time-based grouping and sorting
9. **MoM Growth Calculation**: Handling sequential calculations
10. **Visualization Design**: Creating appropriate chart types
11. **Top Products**: Ranking and limiting results
12. **Insight Generation**: Dynamic, data-driven recommendations
13. **Error Handling**: Graceful handling of edge cases
14. **UI/UX Polish**: Professional styling and layout
15. **Validation**: Testing against benchmarks

Each iteration improved specific aspects of the application, demonstrating how AI tools can accelerate development while maintaining code quality.

---

## 🎓 Validation Methodology

### Data Validation
- Column existence checks
- Data type validation
- Missing value handling
- Date format parsing
- Numeric value verification

### Calculation Validation
- KPIs calculated at aggregate level (not row averages)
- MoM growth uses proper sequential logic
- AOV uses unique order count
- Gross margin % uses correct formula

### Filter Validation
- Each filter affects the entire dataset
- Filters work independently and together
- Empty results handled gracefully
- Reset functionality clears all selections

---

## ⚠️ Limitations

1. **Dataset**: Uses synthetic data for demonstration purposes
2. **Insights**: Descriptive only; correlation ≠ causation
3. **Scale**: Optimized for datasets up to 100K records
4. **Real-time**: Data is static; refresh requires reloading Excel file
5. **Authentication**: No user authentication or access control
6. **Export**: No built-in data export functionality
7. **Drill-down**: Limited to predefined aggregation levels

---

## 🔮 Future Enhancements

1. **Data Export**: Add CSV/Excel export of filtered data
2. **Advanced Filters**: Date range picker, numeric range filters
3. **Custom KPIs**: User-defined metrics and calculations
4. **Drill-down**: Click charts to filter and explore deeper
5. **Comparative Analysis**: Year-over-year, period-over-period comparisons
6. **Forecasting**: Predictive analytics for future trends
7. **Database Integration**: Connect to SQL databases instead of Excel
8. **User Authentication**: Multi-user support with role-based access
9. **Scheduled Refresh**: Automatic data updates
10. **Mobile Responsive**: Optimized layout for mobile devices
11. **PDF Reports**: Generate and download PDF reports
12. **Email Alerts**: Automated alerts for significant changes

---

## 👥 Contributors

**MBA Data Science Project**  
Subject: AI Powered Developer Tools  
Academic Year: FY 2025-26

---

## 📄 License

This project is for educational purposes as part of an MBA Data Science program.

---

## 📞 Support

For questions or issues:
1. Review this README thoroughly
2. Check the Testing Checklist
3. Validate KPIs against benchmarks
4. Verify data file location and format

---

## 📝 Notes

- **Dataset Disclaimer**: This dashboard uses synthetic sales data. All insights are for demonstration purposes only.
- **Academic Integrity**: This project demonstrates AI-assisted development practices. Code was iteratively developed with AI guidance while maintaining understanding of all components.
- **Responsible AI**: The dashboard avoids unsupported causal claims and clearly labels correlational insights.

---

**Built with ❤️ using Python, Streamlit, and AI-Powered Development Tools**
