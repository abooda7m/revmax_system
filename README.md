# RevMax - Business Intelligence System

RevMax is a full-scale business intelligence system built using real retail sales data. The project provides actionable insights to support strategic decision-making, improve profitability, and enhance customer satisfaction.

---

## Project Overview

This application analyzes historical sales data using advanced data science techniques. It features a modern interactive dashboard, predictive analytics, and business recommendations powered by Python and cloud technologies.

---

## Key Features

- Cloud-based data storage using **Supabase**
- Data processing and transformation using **pandas**
- Interactive web interface built with **Streamlit** and **Plotly**
- Customer segmentation and product analysis
- Statistical testing for performance validation
- Predictive models for sales forecasting (Prophet, Linear Regression)
- Automated business recommendations
- Deployed on **Google Cloud VM**

---

## Main Components

- **Main Dashboard**: High-level metrics for sales, profit, and regional performance
- **Customer Analytics**: Segments customers and analyzes purchasing behavior
- **Product Insights**: Highlights top-selling and underperforming products
- **Sales Forecasting**: Projects future revenue trends using time series models
- **Recommendation Engine**: Suggests actions to increase revenue and efficiency

---

## Folder Structure

```
RevMax/
├── data/                  # Cleaned and raw data files
├── scripts/               # Python scripts for analysis and modeling
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
```

---

## Requirements

- Python 3.10+
- pandas  
- streamlit  
- plotly  
- prophet  
- scikit-learn  
- supabase-py  
- statsmodels  

Install dependencies:

```bash
uv venv env
env\Scripts\activate  # On Windows
uv pip install -r requirements.txt
```

---

## How to Run

1. Make sure your data files are in the `/data` directory.
2. Activate your virtual environment.
3. Run the Streamlit app:

```bash
streamlit run app.py
```

The dashboard will open in your browser for real-time interaction and exploration.

---

## Deployment

The app is deployed on a Google Cloud VM instance for remote access and scalability. Ensure proper firewall settings and VM configurations are applied for public access.
