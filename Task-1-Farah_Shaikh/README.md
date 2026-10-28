# Data Analytics Project 1 — Data Cleaning & Preparation

## Project Overview

This project focuses on cleaning and preparing an order-related dataset using Microsoft Excel as part of the Data Analytics Internship at DecodeLabs.

The main objective was to identify and handle missing values, check duplicate records, verify data formats, and validate numerical calculations to improve data quality and consistency.

## Project Information

- **Project:** Project 1 — Data Cleaning & Preparation
- **Organization:** DecodeLabs
- **Tool:** Microsoft Excel
- **Dataset:** Dataset for Data Analytics
- **Total Records:** 1,200
- **Total Columns:** 14

## Dataset Description

The dataset contains order-related information, including:

- Order IDs and order dates
- Customer details
- Product information
- Quantities and prices
- Payment methods
- Order statuses
- Coupon codes

## Tasks Performed

### 1. Missing Value Handling

- Identified 309 blank cells in the `CouponCode` column.
- Replaced blank values with `No Coupon Used` to improve consistency.

### 2. Duplicate Record Checking

- Checked the dataset for exact duplicate rows.
- No duplicate complete rows were found.

### 3. Duplicate ID Validation

- Checked the `OrderID` column for duplicate values.
- Confirmed that all OrderIDs were unique.

### 4. Date and Number Formatting

- Verified the `OrderDate` column and standardized its display format to `YYYY-MM-DD`.
- Checked `Quantity` and `ItemsInCart` for valid numeric values and displayed them as whole numbers.
- Verified `UnitPrice` and `TotalPrice` and standardized their display to two decimal places.

### 5. Text Data Review

- Reviewed categorical columns, including `Product`, `PaymentMethod`, `OrderStatus`, and `ReferralSource`.
- Checked for inconsistent text values and unnecessary spaces.

### 6. Price Calculation Validation

- Compared `TotalPrice` with `Quantity × UnitPrice`.
- All 1,200 records matched the expected calculation when rounded to two decimal places.

## Final Results

| Validation Check | Result |
|---|---|
| Total Records | 1,200 |
| Total Columns | 14 |
| Missing CouponCode Values Handled | 309 |
| Exact Duplicate Rows | 0 |
| Duplicate OrderIDs | 0 |
| Price Calculations Matched | 1,200 |

## Project Files

- **`Data_Analytics_Cleaned.xlsx`** — Cleaned dataset.
- **`PROJECT 1 DOCUMENTATION.docx`** — Detailed project documentation and cleaning process.

## Key Learnings

Through this project, I gained practical experience in:

- Handling missing values in Excel
- Checking duplicate records and unique identifiers
- Verifying date and numeric formats
- Reviewing text consistency
- Validating calculations
- Preparing datasets for further analysis

## Conclusion

This project strengthened my understanding of data cleaning and preparation using Microsoft Excel. By handling missing values and performing data quality checks, I prepared the dataset for more reliable analysis.

---

**Author:** Farah Shaikh  
**Project:** Data Analytics Internship — Project 1  
**Organization:** DecodeLabs

