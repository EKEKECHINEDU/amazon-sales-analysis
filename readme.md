# Amazon Retail Sales Analysis

## Project Overview
This project analyzes an Amazon retail sales dataset to uncover trends in customer purchases. The analysis focuses on product popularity, pricing strategies, and the impact of discounts on customer ratings.

## Features
- **Data Cleaning**: Converts price, discount, and rating values from text to numeric format.
- **Exploratory Data Analysis (EDA)**:
  - Identifies the top product categories by count.
  - Finds the best-selling products based on the number of reviews.
  - Analyzes the relationship between discount percentages and product ratings.
- **Data Visualization**:
  - Bar charts for top product categories and best-selling products.
  - Scatter plot to examine the effect of discounts on ratings.
- **Summary Statistics**:
  - Computes average discount percentage and product rating.
  - Displays the top five product categories by product count.

## Technologies Used
- **Python**: Data processing and analysis
- **Pandas**: Data manipulation
- **Matplotlib & Seaborn**: Data visualization

## How to Run the Project
1. Install required libraries if not already installed:
   ```bash
   pip install pandas matplotlib seaborn
   ```
2. Place the dataset (`amazon.csv`) in the project directory.
3. Run the analysis script:
   ```bash
   python amazon_sales_analysis.py
   ```
4. View the generated visualizations and insights in the console.

## Insights & Findings
- Certain product categories dominate the marketplace in terms of listings.
- The number of reviews can serve as an indicator of best-selling products.
- Higher discount percentages do not always correlate with higher ratings.

## Future Improvements
- Incorporate time-based trends if timestamps are available.
- Extend analysis to include customer sentiment from reviews.
- Predict sales trends using machine learning techniques.

## Dataset Source
This dataset was obtained from Amazon's product listings and contains information on pricing, ratings, reviews, and categories.

