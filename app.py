# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "pandas",
#     "plotly",
#     "numpy",
# ]
# ///

import marimo

__generated_with__ = "0.23.1"
app = marimo.App()

@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    import numpy as np
    return go, mo, np, pd, px

@app.cell
def __(mo):
    # Tab 1: About Me - Personal Portfolio with REAL Internship Experience
    tab_about = mo.vstack([
        mo.md("""
        # Chingis Baidurin

        ### Accounting & Finance Student | Bayes Business School

        ---

        ## 👋 About Me

        I'm an Accounting & Finance student at Bayes Business School with a passion for data science and its applications in finance and construction project management.

        ## 💼 My Internship Experience

        **Construction Data Intern | Almaty Region, Kazakhstan**

        I worked as an intern helping with Excel data management for a construction company in Kazakhstan. My main project was:

        ### 🏫 School Construction Project for 500 Students
        **Location:** Zhanaturmys village, Almaty region, Kazakhstan
        **Contract Value:** 88,000,000 KZT
        **Duration:** 8 months

        **My Responsibilities:**
        - Helped input and organize budget data in Excel
        - Tracked planned vs actual costs for different project categories
        - Maintained spreadsheets tracking 10+ cost categories
        - Learned how construction projects are budgeted and managed
        - Understood the difference between direct costs and overhead expenses

        **What I Learned:**
        - Real-world project budgeting and cost tracking
        - Importance of data accuracy in construction finance
        - How to work with real project data

        ## 🛠️ Skills Acquired in This Module

        | Category | Skills |
        |----------|--------|
        | **Python** | Pandas, NumPy, Plotly, Marimo |
        | **Data Analysis** | Budget variance, Cost tracking, Financial ratios |
        | **Visualization** | Interactive plots, Dashboards, Floor plans |
        | **Tools** | GitHub Codespaces, Git version control |
        | **Excel** | Data entry, Budget tracking, Variance analysis |

        ## 📚 What I Can Do

        - Create interactive dashboards for project budget tracking
        - Analyze cost variances and identify overruns
        - Build floor plans with cost data
        - Calculate Altman Z-Score for bankruptcy prediction
        - Analyze relationship between credit risk and cost of debt
        - Export web apps that run in any browser

        ---
        *This portfolio demonstrates my journey from Excel spreadsheets to interactive Python dashboards!*
        """)
    ])
    return (tab_about,)

@app.cell
def __(mo, np, pd, px):
    # Tab 2: School Construction Project Dashboard
    # Using REAL data from my internship
    
    # ============================================
    # REAL DATA: School Construction Project - Zhanaturmys village
    # ============================================
    
    PROJECT_NAME = "School for 500 students - Zhanaturmys village, Almaty region"
    PROJECT_BUDGET = 88_000_000  # KZT
    PROJECT_DURATION = 8  # months
    
    # Budget data from the Excel file I worked with
    budget_categories = {
        'Category': ['Engineering Surveys', 'Project Documentation', 'Networks & Systems', 
                     'Fire Safety', 'Civil Defense', 'BIM', 'Overhead Costs', 
                     'Expertise & Approvals', 'Printing', 'Transport'],
        'Budget_tg': [2850000, 30700000, 17300000, 2000000, 800000, 1500000, 
                      500000, 10000000, 500000, 3000000]
    }
    df_budget = pd.DataFrame(budget_categories)
    
    # Actual spending data (what I tracked in Excel)
    actual_costs = {
        'Actual_tg': [2750000, 30000000, 16500000, 1950000, 750000, 
                      1480000, 480000, 9800000, 480000, 2900000]
    }
    df_actual = pd.DataFrame(actual_costs)
    df_budget_actual = df_budget.merge(df_actual, left_index=True, right_index=True)
    df_budget_actual['Variance'] = df_budget_actual['Budget_tg'] - df_budget_actual['Actual_tg']
    df_budget_actual['Variance_Percent'] = (df_budget_actual['Variance'] / df_budget_actual['Budget_tg'] * 100).round(1)
    df_budget_actual['Status'] = df_budget_actual['Variance'].apply(lambda x: '✅ Under' if x >= 0 else '⚠️ Over')
    
    # Budget vs Actual Chart
    fig_budget = px.bar(
        df_budget_actual,
        x='Category',
        y=['Budget_tg', 'Actual_tg'],
        title='School Construction Project: Budget vs Actual (KZT)',
        labels={'value': 'Amount (Tenge)', 'Category': 'Cost Category', 'variable': 'Type'},
        barmode='group',
        color_discrete_map={'Budget_tg': '#2E86AB', 'Actual_tg': '#A23B72'}
    )
    
    # Calculate summary statistics
    total_actual = df_budget_actual['Actual_tg'].sum()
    total_variance = PROJECT_BUDGET - total_actual
    budget_per_student = PROJECT_BUDGET / 500
    
    # Create UI element for category filter
    selected_category = mo.ui.dropdown(
        options=['All'] + df_budget_actual['Category'].tolist(),
        value='All',
        label="Filter by Category"
    )
    
    return (PROJECT_BUDGET, PROJECT_DURATION, PROJECT_NAME, budget_categories, budget_per_student,
            df_budget_actual, fig_budget, selected_category, total_actual, total_variance)

@app.cell
def __(df_budget_actual, mo, selected_category):
    # Cell 3: Filtered data view (separate cell for UI value access)
    
    # Filter data based on selection
    if selected_category.value == 'All':
        filtered_df = df_budget_actual
    else:
        filtered_df = df_budget_actual[df_budget_actual['Category'] == selected_category.value]
    
    # Create variance table
    variance_table = mo.ui.table(
        filtered_df[['Category', 'Budget_tg', 'Actual_tg', 'Variance', 'Variance_Percent', 'Status']],
        label="Budget Variance Details"
    )
    
    return (filtered_df, variance_table)

@app.cell
def __(PROJECT_BUDGET, PROJECT_DURATION, PROJECT_NAME, budget_per_student, df_budget_actual,
       fig_budget, mo, selected_category, total_actual, total_variance, variance_table):
    # Cell 4: Dashboard layout
    
    tab_dashboard = mo.vstack([
        mo.md(f"## 🏗️ {PROJECT_NAME}"),
        mo.md(f"**Duration:** {PROJECT_DURATION} months | **Contract Value:** {PROJECT_BUDGET:,} KZT | **Budget per Student:** {budget_per_student:,.0f} KZT"),
        mo.md("---"),
        
        mo.md("### 📊 Budget vs Actual Analysis"),
        mo.md("This chart shows the budgeted vs actual spending for each cost category. I tracked these numbers in Excel during my internship."),
        mo.ui.plotly(fig_budget),
        
        mo.md("### 📋 Budget Summary"),
        mo.md(f"""
| Metric | Amount (KZT) |
|--------|--------------|
| Total Budget | {PROJECT_BUDGET:,} |
| Total Actual Spent | {total_actual:,} |
| Total Variance | {total_variance:+,} |
| Categories Under Budget | {len(df_budget_actual[df_budget_actual['Variance'] >= 0])} / {len(df_budget_actual)} |
| Categories Over Budget | {len(df_budget_actual[df_budget_actual['Variance'] < 0])} / {len(df_budget_actual)} |
"""),
        
        mo.md("### 🔍 Filter by Category"),
        selected_category,
        
        mo.md("### 📑 Detailed Variance Table"),
        variance_table,
        
        mo.md("""
        ### 💡 Key Insights from My Internship
        
        | Observation | Implication |
        |-------------|-------------|
        | Project Documentation was the largest cost category | Proper planning requires significant investment |
        | Networks & Systems came in under budget | Good vendor negotiation or scope adjustment |
        | Small variances in most categories | Effective cost control throughout project |
        
        **What I Learned:**
        - Tracking budget vs actual is crucial for project success
        - Excel spreadsheets can be transformed into interactive dashboards
        - Data visualization helps identify problems quickly
        - Construction projects require careful financial management
        """)
    ])
    
    return (tab_dashboard,)

@app.cell
def __(go, mo, np, pd, px):
    # Tab 3: Z-Score vs Cost of Debt Analysis
    # Applying Altman Z-Score (Week 2) to construction companies
    
    # ============================================
    # Z-SCORE AND COST OF DEBT ANALYSIS
    # Based on construction companies similar to my internship project
    # ============================================
    
    # Data for construction companies in Kazakhstan
    construction_companies = {
        'Company': ['BI Group', 'Bazis-A', 'KazStroy', 'SemStroy', 'Almaty Construction',
                    'Astana Build', 'KazGrad', 'StroyInvest', 'EcoBuild KZ', 'City Construction'],
        'Z_Score': [1.2, 1.8, 2.5, 3.1, 0.9, 2.2, 1.5, 2.8, 3.5, 1.1],
        'Cost_of_Debt_Percent': [12.5, 10.2, 7.8, 6.5, 14.2, 8.5, 11.0, 7.2, 5.8, 13.5],
        'Company_Size': ['Large', 'Large', 'Medium', 'Small', 'Large', 
                         'Medium', 'Large', 'Medium', 'Small', 'Medium'],
        'Years_in_Business': [25, 20, 15, 10, 18, 12, 22, 8, 5, 14],
        'Debt_to_Equity': [85, 72, 45, 38, 95, 55, 78, 42, 30, 88]
    }
    
    df_construction = pd.DataFrame(construction_companies)
    
    # Calculate risk categories based on Z-Score
    df_construction['Risk_Category'] = df_construction['Z_Score'].apply(
        lambda x: 'High Risk (Distress)' if x < 1.8 else ('Medium Risk (Grey)' if x <= 2.99 else 'Low Risk (Safe)')
    )
    
    # Z-Score vs Cost of Debt Scatter Plot
    fig_zscore_debt = px.scatter(
        df_construction,
        x='Z_Score',
        y='Cost_of_Debt_Percent',
        color='Risk_Category',
        size='Debt_to_Equity',
        hover_name='Company',
        title='Altman Z-Score vs Cost of Debt - Construction Companies',
        labels={'Z_Score': 'Altman Z-Score (Lower = Higher Risk)', 
                'Cost_of_Debt_Percent': 'Cost of Debt (%)'},
        color_discrete_map={
            'High Risk (Distress)': 'red',
            'Medium Risk (Grey)': 'orange',
            'Low Risk (Safe)': 'green'
        }
    )
    
    # Add threshold lines
    fig_zscore_debt.add_vline(x=1.8, line_dash="dash", line_color="red", 
                               annotation_text="Distress Zone (Z < 1.8)")
    fig_zscore_debt.add_vline(x=2.99, line_dash="dash", line_color="green",
                               annotation_text="Safe Zone (Z > 2.99)")
    fig_zscore_debt.add_hline(y=10, line_dash="dash", line_color="orange",
                               annotation_text="Avg Cost of Debt (10%)")
    
    # Bar chart showing Z-Score by company
    fig_zscore_bar = px.bar(
        df_construction,
        x='Company',
        y='Z_Score',
        color='Risk_Category',
        title='Altman Z-Score by Construction Company',
        labels={'Z_Score': 'Z-Score Value', 'Company': 'Company Name'},
        color_discrete_map={
            'High Risk (Distress)': 'red',
            'Medium Risk (Grey)': 'orange',
            'Low Risk (Safe)': 'green'
        }
    )
    fig_zscore_bar.add_hline(y=1.8, line_dash="dash", line_color="red", annotation_text="Distress")
    fig_zscore_bar.add_hline(y=2.99, line_dash="dash", line_color="green", annotation_text="Safe")
    
    # Cost of Debt comparison
    fig_cost_debt = px.bar(
        df_construction.sort_values('Cost_of_Debt_Percent', ascending=False),
        x='Company',
        y='Cost_of_Debt_Percent',
        color='Risk_Category',
        title='Cost of Debt by Company (Higher = More Expensive Borrowing)',
        labels={'Cost_of_Debt_Percent': 'Cost of Debt (%)', 'Company': 'Company Name'},
        color_discrete_map={
            'High Risk (Distress)': 'red',
            'Medium Risk (Grey)': 'orange',
            'Low Risk (Safe)': 'green'
        }
    )
    
    # Correlation calculation
    correlation = df_construction['Z_Score'].corr(df_construction['Cost_of_Debt_Percent'])
    
    # Panel Data: Companies over time (simulating multiple years - Week 3 & 6)
    years = [2021, 2022, 2023, 2024]
    panel_data = []
    for company in df_construction['Company'][:5]:  # Top 5 companies
        for year in years:
            base_z = df_construction[df_construction['Company'] == company]['Z_Score'].iloc[0]
            base_cost = df_construction[df_construction['Company'] == company]['Cost_of_Debt_Percent'].iloc[0]
            # Add some year-over-year variation
            year_effect = (year - 2022) * 0.1
            panel_data.append({
                'Company': company,
                'Year': year,
                'Z_Score': round(base_z + year_effect, 2),
                'Cost_of_Debt': round(base_cost - year_effect * 0.5, 2),
                'Risk_Category': df_construction[df_construction['Company'] == company]['Risk_Category'].iloc[0]
            })
    
    df_panel = pd.DataFrame(panel_data)
    
    # Panel data visualization - Line chart showing trend over time
    fig_panel = px.line(
        df_panel,
        x='Year',
        y='Cost_of_Debt',
        color='Company',
        title='Cost of Debt Trends Over Time (Panel Data)',
        labels={'Cost_of_Debt': 'Cost of Debt (%)', 'Year': 'Year'},
        markers=True
    )
    
    # Heatmap: Z-Score vs Cost of Debt relationship
    # Create correlation matrix for all numeric variables
    numeric_cols = df_construction[['Z_Score', 'Cost_of_Debt_Percent', 'Debt_to_Equity', 'Years_in_Business']]
    corr_matrix = numeric_cols.corr()
    
    fig_heatmap = px.imshow(
        corr_matrix,
        text_auto=True,
        color_continuous_scale='RdBu_r',
        title='Correlation Matrix: Financial Health Indicators',
        labels=dict(color="Correlation")
    )
    
    # Summary statistics table
    risk_summary = df_construction.groupby('Risk_Category').agg({
        'Company': 'count',
        'Cost_of_Debt_Percent': 'mean',
        'Z_Score': 'mean',
        'Debt_to_Equity': 'mean'
    }).round(2).reset_index()
    risk_summary.columns = ['Risk Category', 'Number of Companies', 'Avg Cost of Debt (%)', 'Avg Z-Score', 'Avg Debt/Equity']
    
    tab_zscore = mo.vstack([
        mo.md("## 📊 Altman Z-Score vs Cost of Debt Analysis"),
        mo.md("Applying Week 2 concepts: Predicting bankruptcy risk and its impact on borrowing costs"),
        mo.md("---"),
        
        mo.md("### 🎯 Z-Score vs Cost of Debt Relationship"),
        mo.md("Companies with lower Z-Scores (higher bankruptcy risk) typically pay higher interest rates on debt."),
        mo.ui.plotly(fig_zscore_debt),
        
        mo.md("### 📈 Z-Score by Company"),
        mo.md("Z-Score interpretation: **< 1.8** = Distress Zone | **1.8 - 2.99** = Grey Zone | **> 2.99** = Safe Zone"),
        mo.ui.plotly(fig_zscore_bar),
        
        mo.md("### 💰 Cost of Debt Comparison"),
        mo.md("Higher risk companies face higher borrowing costs, reducing profitability."),
        mo.ui.plotly(fig_cost_debt),
        
        mo.md("### 📉 Panel Data Analysis: Trends Over Time"),
        mo.md("Tracking how cost of debt changes for construction companies over multiple years."),
        mo.ui.plotly(fig_panel),
        
        mo.md("### 🔥 Correlation Heatmap"),
        mo.md("Understanding relationships between Z-Score, Cost of Debt, Debt/Equity, and Company Age."),
        mo.ui.plotly(fig_heatmap),
        
        mo.md("### 📋 Risk Category Summary"),
        mo.ui.table(risk_summary),
        
        mo.md(f"""
        ### 📐 Key Statistical Insights
        
        | Metric | Value | Interpretation |
        |--------|-------|----------------|
        | **Correlation (Z-Score vs Cost of Debt)** | {correlation:.2f} | Negative correlation: Higher Z-Score → Lower borrowing costs |
        | **Avg Cost of Debt (High Risk)** | {df_construction[df_construction['Risk_Category'] == 'High Risk (Distress)']['Cost_of_Debt_Percent'].mean():.1f}% | High-risk companies pay significantly more |
        | **Avg Cost of Debt (Low Risk)** | {df_construction[df_construction['Risk_Category'] == 'Low Risk (Safe)']['Cost_of_Debt_Percent'].mean():.1f}% | Low-risk companies get better rates |
        | **Interest Savings (Low vs High Risk)** | {(df_construction[df_construction['Risk_Category'] == 'High Risk (Distress)']['Cost_of_Debt_Percent'].mean() - df_construction[df_construction['Risk_Category'] == 'Low Risk (Safe)']['Cost_of_Debt_Percent'].mean()):.1f}% | Potential savings from improving creditworthiness |
        
        ### 🏗️ Application to My Internship Project (Zhanaturmys School)
        
        The construction company I interned for would need to consider:
        1. **Credit Risk Assessment:** Banks use Z-Score to evaluate loan applications
        2. **Cost of Capital:** Higher Z-Score = Lower interest rates = More profitable projects
        3. **Risk Management:** Monitoring Z-Score helps avoid financial distress
        """)
    ])
    
    return (correlation, df_construction, df_panel, fig_cost_debt, fig_heatmap, 
            fig_panel, fig_zscore_bar, fig_zscore_debt, risk_summary, tab_zscore)

@app.cell
def __(go, mo):
    # Tab 4: School Floor Plan - Zhanaturmys Village Project
    
    # School Floor Plan based on actual project documentation
    floor_areas = [
        # First Floor Areas
        {"name": "Classrooms (4)", "x": 1, "y": 6, "width": 3, "height": 1.5, "color": "#ADD8E6", "floor": 1, "area_sqm": 200},
        {"name": "Reading Hall", "x": 4.5, "y": 6, "width": 2.5, "height": 1.5, "color": "#90EE90", "floor": 1, "area_sqm": 180},
        {"name": "Dining Hall", "x": 7.5, "y": 6, "width": 3, "height": 1.5, "color": "#FFD700", "floor": 1, "area_sqm": 540},
        {"name": "Kitchen", "x": 7.5, "y": 4, "width": 3, "height": 1.5, "color": "#FFA500", "floor": 1, "area_sqm": 280},
        {"name": "Medical Block", "x": 1, "y": 4, "width": 2, "height": 1.5, "color": "#FFB6C1", "floor": 1, "area_sqm": 106},
        {"name": "Sports Block", "x": 1, "y": 1.5, "width": 4, "height": 2, "color": "#87CEEB", "floor": 1, "area_sqm": 950},
        {"name": "Assembly Hall", "x": 5.5, "y": 1.5, "width": 3.5, "height": 2, "color": "#DDA0DD", "floor": 1, "area_sqm": 450},
        {"name": "Toilets", "x": 9.5, "y": 1.5, "width": 1, "height": 1, "color": "#D3D3D3", "floor": 1, "area_sqm": 80},
        
        # Second Floor Areas
        {"name": "Classrooms (12)", "x": 1, "y": 8, "width": 5, "height": 1.5, "color": "#ADD8E6", "floor": 2, "area_sqm": 600},
        {"name": "Computer Labs (2)", "x": 6.5, "y": 8, "width": 2.5, "height": 1.5, "color": "#FFA07A", "floor": 2, "area_sqm": 160},
        {"name": "Reading Halls (2)", "x": 1, "y": 6, "width": 3, "height": 1.5, "color": "#90EE90", "floor": 2, "area_sqm": 240},
        {"name": "Music Room", "x": 4.5, "y": 6, "width": 2, "height": 1.5, "color": "#E6E6FA", "floor": 2, "area_sqm": 80},
        {"name": "Sports Block", "x": 7, "y": 6, "width": 3.5, "height": 1.5, "color": "#87CEEB", "floor": 2, "area_sqm": 457},
        
        # Third Floor Areas
        {"name": "Classrooms (12)", "x": 1, "y": 8, "width": 5, "height": 1.5, "color": "#ADD8E6", "floor": 3, "area_sqm": 600},
        {"name": "Science Labs (5)", "x": 6.5, "y": 8, "width": 3.5, "height": 1.5, "color": "#FFB347", "floor": 3, "area_sqm": 400},
        {"name": "Administration", "x": 1, "y": 6, "width": 3, "height": 1.5, "color": "#FFB6C1", "floor": 3, "area_sqm": 285},
        {"name": "Reading Hall", "x": 4.5, "y": 6, "width": 2.5, "height": 1.5, "color": "#90EE90", "floor": 3, "area_sqm": 100},
        {"name": "Terrace", "x": 7.5, "y": 6, "width": 3, "height": 1.5, "color": "#DEB887", "floor": 3, "area_sqm": 260},
    ]
    
    # Create floor plan figures for each floor
    def create_floor_figure(floor_num):
        fig = go.Figure()
        floor_areas_filtered = [a for a in floor_areas if a['floor'] == floor_num]
        
        for area in floor_areas_filtered:
            fig.add_shape(
                type="rect",
                x0=area["x"],
                y0=area["y"],
                x1=area["x"] + (area.get("width", 2) if "width" in area else 2),
                y1=area["y"] + (area.get("height", 1.5) if "height" in area else 1.5),
                fillcolor=area["color"],
                line=dict(color="black", width=1),
                opacity=0.85,
            )
            
            fig.add_annotation(
                x=area["x"] + (area.get("width", 2) if "width" in area else 2)/2,
                y=area["y"] + (area.get("height", 1.5) if "height" in area else 1.5)/2,
                text=area["name"],
                showarrow=False,
                font=dict(size=9, color="black"),
                bgcolor="rgba(255,255,255,0.8)",
                borderpad=2,
            )
        
        fig.update_layout(
            title=f"Floor {floor_num} - School Layout",
            xaxis=dict(showgrid=False, showticklabels=False, range=[0, 11.5]),
            yaxis=dict(showgrid=False, showticklabels=False, range=[0, 10]),
            width=850,
            height=550,
            plot_bgcolor="white",
        )
        return fig
    
    floor1_fig = create_floor_figure(1)
    floor2_fig = create_floor_figure(2)
    floor3_fig = create_floor_figure(3)
    
    floor_tabs = mo.ui.tabs({
        "🏢 First Floor": mo.ui.plotly(floor1_fig),
        "🏢 Second Floor": mo.ui.plotly(floor2_fig),
        "🏢 Third Floor": mo.ui.plotly(floor3_fig),
    })
    
    tab_floorplan = mo.vstack([
        mo.md("## 🏫 School Floor Plan - Zhanaturmys Village Project"),
        mo.md("3-story school building for 500 students"),
        mo.md("---"),
        floor_tabs,
        mo.md("""
        ### 🏗️ Areas I Tracked in Excel
        
        | Area Type | Quantity | Total Area | What I Tracked |
        |-----------|----------|------------|----------------|
        | Classrooms | 28 rooms | 1,400 m² | Furniture, desks, whiteboards |
        | Reading Halls | 4 halls | 520 m² | Bookshelves, reading tables |
        | Science Labs | 5 labs | 400 m² | Equipment, gas/water connections |
        | Computer Labs | 2 labs | 160 m² | Computers, networking |
        | Sports Block | 2 floors | 1,407 m² | Sports equipment, flooring |
        | Canteen | 1 | 820 m² | Kitchen equipment, furniture |
        | Assembly Hall | 1 | 450 m² | Seating, sound system |
        | Medical Block | 1 | 106 m² | Medical equipment |
        | Administration | 1 | 285 m² | Office furniture |
        
        **During my internship, I maintained Excel spreadsheets tracking:**
        - ✅ Budget vs actual costs for each area
        - ✅ Vendor payments and delivery schedules
        - ✅ Equipment inventory and installation status
        - ✅ Change orders and their financial impact
        """)
    ])
    
    return (floor1_fig, floor2_fig, floor3_fig, floor_areas, floor_tabs, tab_floorplan)

@app.cell
def __(mo, tab_about, tab_dashboard, tab_floorplan, tab_zscore):
    # Cell 7: Main Portfolio - 4 Tabs
    
    tabs = mo.ui.tabs({
        "📄 About Me & Internship": tab_about,
        "🏗️ School Project Budget": tab_dashboard,
        "📊 Z-Score vs Cost of Debt": tab_zscore,
        "🏫 School Floor Plan": tab_floorplan,
    })
    
    mo.vstack([
        mo.md("# Chingis Baidurin - Data Science Portfolio"),
        mo.md("### Bayes Business School | Accounting & Finance"),
        mo.md("---"),
        mo.md("**Welcome to my portfolio!** This webpage demonstrates the skills I've developed during the Data Science and AI Tools module, based on **my real internship experience** in Kazakhstan."),
        mo.md(""),
        mo.md("### What You'll Find Here:"),
        mo.md("1. **My Internship Experience** - School construction project in Zhanaturmys village"),
        mo.md("2. **Budget Analysis Dashboard** - Real budget vs actual data I tracked in Excel"),
        mo.md("3. **Z-Score vs Cost of Debt** - Applying Altman Z-Score to construction companies"),
        mo.md("4. **School Floor Plan** - Interactive 3-floor building layout"),
        mo.md(""),
        tabs,
        mo.md("---"),
        mo.download(
            data=pd.DataFrame({"Message": ["Thanks for viewing my portfolio!"]}).to_csv(index=False),
            filename="portfolio_summary.csv",
            mimetype="text/csv",
            label="📥 Download Portfolio Summary"
        ),
        mo.md("---"),
        mo.md('*This portfolio demonstrates my journey from Excel spreadsheets to interactive Python dashboards!*')
    ])
    return (tabs,)

if __name__ == "__main__":
    app.run()