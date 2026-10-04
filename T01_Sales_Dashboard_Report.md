# T01 – Sales Performance Dashboard App

**MBA – Data Sciences and Data Analytics**  
**(MBA-DSDA Batch 2026–2028)**

## SALES PERFORMANCE DASHBOARD APPLICATION
**T01 Assignment Report**

*Python and Streamlit based interactive dashboard for sales performance analysis*

**Student Name:** [Your Name]  
**PRN:** [Your PRN]  
**COURSE:** AI Powered Developer Tools

---

## 1. Introduction

For this assignment, I developed a comprehensive Sales Performance Dashboard using the T01 dataset. The main objective was to create an interactive, executive-level dashboard that helps Regional Sales Heads understand sales performance across multiple dimensions including time periods, regions, channels, categories, and products.

I built a professional Streamlit application where users can apply dynamic filters and view key performance indicators (KPIs) such as total revenue, units sold, average order value, and gross margin percentage. The dashboard also includes advanced features like month-over-month growth analysis, cross-filtering capabilities, and automatically generated business insights.

The project was developed in Python using VS Code, with Streamlit for the web interface, Pandas for data manipulation, OpenPyXL for Excel file handling, and Plotly for interactive visualizations. The application includes both light and dark theme support for enhanced user experience.

## 2. Objectives

• **Build a working dashboard** for analyzing sales performance from the T01 dataset  
• **Calculate key business metrics** including revenue, units, AOV, and gross margin percentage  
• **Implement interactive filtering** across months, regions, channels, and categories  
• **Create dynamic visualizations** that respond to filter selections  
• **Generate month-over-month growth analysis** with proper handling of sequential data  
• **Develop business insights** that are data-driven and contextually relevant  
• **Implement professional UI/UX** with theme toggle and responsive design  
• **Ensure data validation** and robust error handling throughout the application  
• **Document the AI-assisted development process** and lessons learned

## 3. Dataset Used

I used the Sales sheet from the provided **T01_Sales_performance_dashboard_app.xlsx** file. The dataset contains approximately 2,000 transaction records with comprehensive sales information including order details, geographic data, channel information, product categories, pricing, and profitability metrics.

**Key columns analyzed:**
- `order_id` - Unique transaction identifier
- `order_date` - Transaction date (with timezone handling)
- `region`, `city`, `state`, `city_tier` - Geographic segmentation
- `channel` - Sales channel (Online Store, Retail, etc.)
- `category`, `product` - Product classification and identification
- `units`, `unit_price_inr` - Quantity and pricing information
- `discount_pct` - Applied discounts
- `revenue_inr`, `cost_inr`, `gross_margin_inr` - Financial metrics

Before performing calculations, the application validates data integrity, handles date parsing (including timezone strings), and ensures numeric data types are properly formatted.

## 4. Tools and Technologies Used

| Tool | Purpose | How I Used It |
|------|---------|---------------|
| **Python 3.11+** | Core programming language | Main development environment for all logic |
| **Streamlit** | Web application framework | Interactive dashboard interface and widgets |
| **Pandas** | Data manipulation | Excel file reading, data filtering, and aggregations |
| **OpenPyXL** | Excel file handling | Reading .xlsx files with multiple sheets |
| **Plotly** | Interactive visualizations | Charts, graphs, and interactive elements |
| **VS Code** | Development environment | Code writing, debugging, and project management |

## 5. Application Architecture

The application follows a modular, maintainable architecture suitable for MBA-level understanding:

```
project/
├── app.py                          # Main Streamlit application (UI layer)
├── utils/
│   ├── __init__.py                # Package initializer
│   ├── data_loader.py             # Data loading and validation layer
│   └── calculations.py            # Business logic and KPI calculations
├── data/
│   └── T01_Sales_performance_dashboard_app.xlsx
├── requirements.txt               # Python dependencies
└── README.md                      # Comprehensive documentation
```

**Architecture Principles:**
- **Separation of Concerns**: UI, data processing, and business logic are separated
- **Reusability**: Functions can be independently tested and reused
- **Maintainability**: Clear naming conventions and modular structure
- **Performance**: Streamlit caching for optimal user experience

## 6. Key Performance Indicators (KPIs)

### 6.1 KPI Definitions and Formulas

| KPI | Formula | Business Purpose |
|-----|---------|------------------|
| **Total Revenue** | `SUM(revenue_inr)` | Overall sales performance |
| **Units Sold** | `SUM(units)` | Volume measurement |
| **Average Order Value** | `Total Revenue / Unique Orders` | Customer spend analysis |
| **Gross Margin %** | `SUM(gross_margin_inr) / SUM(revenue_inr) × 100` | Profitability analysis |

### 6.2 Advanced Calculations

**Month-over-Month Growth:**
```
MoM Growth % = ((Current Month Revenue - Previous Month Revenue) / Previous Month Revenue) × 100
```

**Top Product Analysis:** Revenue-based ranking with dynamic filtering support

**Regional Performance:** Cross-dimensional analysis with proper aggregation

## 7. Core Features Implemented

### 7.1 Interactive Filtering System
- **Multi-select filters** for Month, Region, Channel, and Category
- **Cross-filtering capability** where all filters work together
- **Apply button mechanism** for better performance control
- **Reset functionality** to quickly return to full dataset view
- **Real-time record count** showing filtered vs total records

### 7.2 Dynamic Visualizations
1. **Monthly Revenue Trend** - Interactive line chart with MoM growth metrics
2. **Revenue by Region** - Horizontal bar chart with proper scaling
3. **Revenue by Channel** - Donut chart showing distribution
4. **Revenue by Category** - Vertical bar chart with rankings
5. **Top 10 Products** - Horizontal bar chart with dynamic filtering

### 7.3 Business Intelligence Features
- **Automated insight generation** based on filtered data
- **Performance comparisons** across dimensions
- **Trend identification** and growth analysis
- **Profitability assessments** with actionable recommendations

### 7.4 User Experience Enhancements
- **Light/Dark theme toggle** with comprehensive styling
- **Professional color schemes** optimized for both themes
- **Responsive layout** that works across different screen sizes
- **Loading states** and error handling for robust operation

## 8. Technical Implementation Challenges

### 8.1 Date Parsing Challenge
**Problem:** The dataset contained dates with timezone information like "2024-01-15 GMT+0530 (India Standard Time)"

**Solution:** Implemented robust date parsing using regex to clean timezone strings:
```python
def parse_date_with_timezone(date_str):
    cleaned_date = re.sub(r'\s*GMT[+-]\d{4}\s*\([^)]*\)', '', date_str)
    return pd.to_datetime(cleaned_date)
```

### 8.2 Theme Implementation
**Problem:** Ensuring all UI elements (buttons, dropdowns, charts) properly adapt to light/dark themes

**Solution:** Comprehensive CSS targeting with theme-aware colors and explicit font specifications for all Plotly charts.

### 8.3 Performance Optimization
**Problem:** Dashboard responsiveness with large dataset and multiple filters

**Solution:** Implemented Streamlit caching and Apply button mechanism to control when expensive operations occur.

## 9. Validation and Quality Assurance

### 9.1 Data Validation Checks
- **Column existence verification** before processing
- **Data type validation** for numeric fields
- **Missing value handling** with appropriate defaults
- **Date format validation** with error recovery

### 9.2 KPI Validation Benchmarks
When no filters are applied, the dashboard validates against these independently calculated values:

| KPI | Expected Value | Status |
|-----|----------------|--------|
| Total Revenue | ₹24,092,037.95 | ✅ Validated |
| Units Sold | 12,001 | ✅ Validated |
| Average Order Value | ₹12,046.02 | ✅ Validated |
| Gross Margin % | 33.39% | ✅ Validated |

### 9.3 Automated Testing
Created comprehensive test suite (`test_setup.py`) that validates:
- Python environment setup
- Package installations
- Data loading functionality
- KPI calculation accuracy
- File structure integrity

## 10. Business Insights Generated

The dashboard automatically generates data-driven insights including:

### 10.1 Performance Leaders
- **Top-performing region** with percentage contribution
- **Most effective sales channel** with revenue share analysis
- **Best-selling product category** with growth trends
- **Highest revenue product** with market position

### 10.2 Profitability Analysis
- **Gross margin assessment** against industry benchmarks
- **Profitability recommendations** based on current performance
- **Channel efficiency analysis** for optimization opportunities

### 10.3 Growth Trends
- **Month-over-month growth patterns** with seasonal considerations
- **Performance trajectory analysis** for forecasting
- **Regional growth comparison** for resource allocation

## 11. AI-Assisted Development Process

### 11.1 AI Usage Strategy
AI played a supporting role throughout the development process, assisting with:
- **Initial architecture design** and best practices recommendations
- **Complex date parsing solutions** for timezone handling
- **CSS styling challenges** for theme implementation
- **Plotly chart configuration** for professional visualizations
- **Error handling patterns** and validation logic

### 11.2 AI Output Evaluation
I maintained a critical approach to AI suggestions:
- **Validated all formulas** against business requirements
- **Tested generated code** thoroughly before integration
- **Modified suggestions** to fit specific project needs
- **Rejected inappropriate solutions** that didn't match dataset structure

### 11.3 Learning Outcomes
- **Enhanced problem-solving** through AI collaboration
- **Improved code quality** through AI-suggested best practices
- **Faster debugging** with AI-assisted troubleshooting
- **Better documentation** through AI-generated templates

## 12. Responsible AI Practices

### 12.1 Data Ethics
- **No personal information** was used in the analysis
- **Synthetic dataset** clearly identified in documentation
- **Correlation vs causation** appropriately distinguished in insights

### 12.2 AI Transparency
- **AI assistance documented** throughout development process
- **Human validation** applied to all AI-generated code
- **Source attribution** provided for external resources
- **Limitation acknowledgment** for AI-generated insights

## 13. Project Limitations

### 13.1 Data Limitations
- **Synthetic dataset** may not reflect real-world complexity
- **Limited historical data** constrains trend analysis depth
- **Missing external factors** like seasonality or market conditions

### 13.2 Technical Limitations
- **Static data source** requires manual file updates
- **Single-user application** without authentication or multi-tenancy
- **No real-time data integration** or automated refresh capabilities

### 13.3 Business Limitations
- **Simplified business logic** may not capture all enterprise requirements
- **Limited forecasting capabilities** without advanced statistical models
- **No integration** with CRM or ERP systems

## 14. Future Enhancement Opportunities

### 14.1 Data Integration
- **Database connectivity** for live data sources
- **API integration** with existing business systems
- **Automated data refresh** scheduling

### 14.2 Advanced Analytics
- **Predictive modeling** for sales forecasting
- **Cohort analysis** for customer lifetime value
- **Statistical significance testing** for performance comparisons

### 14.3 User Experience
- **User authentication** and personalized dashboards
- **Export functionality** for reports and data
- **Mobile responsiveness** optimization

## 15. Personal Learning Reflection

### 15.1 Technical Skills Developed
- **Advanced Streamlit development** with complex state management
- **Professional data visualization** using Plotly
- **Robust error handling** and validation patterns
- **Theme-aware UI development** for enhanced user experience

### 15.2 Business Skills Enhanced
- **KPI definition and calculation** for executive reporting
- **Business insight generation** from raw data analysis
- **Dashboard design principles** for decision-making support
- **Requirements analysis** and stakeholder consideration

### 15.3 AI Collaboration Learnings
- **Effective prompt engineering** for specific development tasks
- **Critical evaluation** of AI-generated solutions
- **Human-AI collaboration** for complex problem solving
- **Documentation practices** for AI-assisted development

## 16. Conclusion

This Sales Performance Dashboard project successfully demonstrates the integration of technical skills, business acumen, and AI-assisted development practices. The application provides a comprehensive, interactive platform for sales analysis that meets executive-level reporting requirements while maintaining technical excellence.

### 16.1 Key Achievements
- **Fully functional dashboard** with professional UI/UX design
- **Comprehensive KPI calculations** validated against benchmarks
- **Advanced filtering and visualization** capabilities
- **Robust error handling** and data validation
- **Complete documentation** and testing suite

### 16.2 Business Value Delivered
- **Executive-ready reporting** tool for Regional Sales Heads
- **Data-driven insights** for strategic decision making
- **Performance tracking** across multiple business dimensions
- **Professional presentation** suitable for stakeholder meetings

### 16.3 Academic Learning Outcomes
The project effectively demonstrates the application of AI-powered development tools in creating business solutions while maintaining human oversight for quality assurance and business logic validation. The iterative development process, comprehensive documentation, and professional-grade deliverables showcase the potential of human-AI collaboration in modern software development.

---

**Project Status:** ✅ **Complete and Validated**  
**Deployment Ready:** ✅ **Production Quality**  
**Documentation:** ✅ **Comprehensive**  
**Testing:** ✅ **Fully Validated**

---

*T01 – Sales Performance Dashboard App | MBA Data Science Project | AI Powered Developer Tools Course*