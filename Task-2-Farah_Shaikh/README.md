# DecodeLabs Internship – Project 2: Exploratory Data Analysis (EDA)

## Project Overview
This project was completed as part of the DecodeLabs Data Analytics Internship (Batch 2026). The objective was to perform Exploratory Data Analysis (EDA) on a cleaned dataset to understand data patterns, analyze trends, identify potential outliers, and summarize key observations.

## Tools and Technologies
- Python
- Pandas
- Matplotlib
- Microsoft Excel

## Dataset Overview
- **Total Records:** 1,200
- **Total Columns:** 14
- **Missing Values:** 0

The dataset contains order-related information, including dates, products, quantities, unit prices, order statuses, and total prices.

## Tasks Performed

### 1. Data Inspection
- Loaded the Excel dataset using Pandas.
- Examined the first five rows and dataset dimensions.
- Checked column information and missing values.

### 2. Descriptive Statistics
Calculated the mean, median, and count for:
- Quantity
- UnitPrice
- TotalPrice

### 3. Monthly Trend Analysis
- Converted the Date column into datetime format.
- Grouped records by month.
- Calculated monthly total prices.
- Created a line chart using Matplotlib.

**Key Findings:**
- Highest monthly total: June 2024 — 68,068.54
- Lowest monthly total: April 2023 — 27,751.71

### 4. Outlier Detection
Applied the Interquartile Range (IQR) method to identify potential outliers in Quantity, UnitPrice, and TotalPrice.

**Results:**
- Quantity: 0 potential outliers
- UnitPrice: 0 potential outliers
- TotalPrice: 8 potential outliers

The potential outliers were retained because they may represent valid transactions and require further investigation before removal.

### 5. Key Observations
- Average Quantity: 2.95
- Average UnitPrice: 356.41
- Average TotalPrice: 1,053.97
- Most common product: Printer
- Most frequent order status: Cancelled, with 250 records
- Least frequent order status: Delivered, with 231 records

## Project Files
- `main.py` – Python script used for the analysis.
- `Cleaned dataset.xlsx` – Cleaned dataset used as input.
- `DECODELABS.docx` – Project report documenting the methodology and findings.
- `Monthly_Total_Price_Trend.png` – Monthly trend visualization, if included.

## How to Run the Project

1. Clone or download this repository.
2. Install the required Python libraries:

   ```bash
   pip install pandas matplotlib openpyxl
   ```

3. Place `main.py` and the cleaned Excel dataset in the same folder.
4. Ensure the filename in `pd.read_excel()` matches the actual dataset filename.
5. Run the script:

   ```bash
   python main.py
   ```

The script displays dataset information, descriptive statistics, monthly trend results, outlier analysis, and key observations. It also generates a monthly trend graph.

## Conclusion
This project demonstrates the use of Python, Pandas, and Matplotlib for basic data inspection, descriptive statistical analysis, monthly trend visualization, and potential outlier detection. The analysis provides an initial understanding of the dataset and highlights areas for further investigation.

## Author
**Farah Shaikh**  
Data Analytics Intern | DecodeLabs Internship – Batch 2026

