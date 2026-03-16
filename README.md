# DA-and-ML-PJT1
Our team is "Uncles"
--

# 📊EST Team: Data Analytics & Machine Learning Project 

1. Subject: Data Analytics - Machine Learning
2. Content: Project Plan Submission
3. Deadline: February 11th
4. Submission Method: Write the plan on your team leader's GitHub and share the GitHub URL on this Telegram.


## 👥 Team Members & Roles

| Role | Name | Student ID |
| :--- | :--- | :--- |
| **Project Manager** | Hamidov Qudrat | `202490125` |
| **System Analyst** | Yuldashev Dilshodbek | `202490381` |
| **Database Architect** | Rihsitillayev Azizbek | `202490271` |
| **UI/UX Designer** | Karamatov Farid | `202490160` |

---

## Course Name
---
Data Analytics – Machine Learning


## Project Title
---
Customer Purchase Behavior Analysis in Online Retail

Clear.
Business related.
Easy for Pandas.
Professors love it.

## Dataset Information
-
Dataset Title: Online Retail Dataset
Source:
https://archive.ics.uci.edu/ml/datasets/online+retail


#### Description:
Transactions of an online store.
Includes invoice number, product, quantity, price, customer, country, date.
Why this dataset:
Real business data.
Good for grouping, filtering, time analysis.
Perfect for future ML predictions.
Size:
~500,000 rows
8 columns


## Project Objectives
---
You will try to understand customers and sales.

#### Main goals:
Find top selling products.
Identify best customers.
Analyze which countries buy more.
Discover sales trends by time.
Questions you answer:
Which products bring most revenue?
Who are VIP customers?
When do people buy more?
What patterns exist in returns?

#### Expected insight:
Help company improve marketing.
Support better stock planning.

## Data Preparation (Pandas)
---
Loading dataset
import pandas as pd

df = pd.read_csv("online_retail.csv")
df.head()

## Cleaning
-
#### remove missing customer IDs
df = df.dropna(subset=['CustomerID'])

#### remove duplicates
df = df.drop_duplicates()

#### correct data types
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

Feature creation
df['Revenue'] = df['Quantity'] * df['UnitPrice']


Now you are ready for analysis.

## Data Analysis Tasks
---
Top products
top_products = df.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(10)


You will see which items earn the most money.

Best customers
top_customers = df.groupby('CustomerID')['Revenue'].sum().sort_values(ascending=False).head(10)


This helps find loyal buyers.

Sales by country
country_sales = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False)


You can identify strong markets.

Monthly trend
df['Month'] = df['InvoiceDate'].dt.month
monthly_sales = df.groupby('Month')['Revenue'].sum()


You understand seasonality.

## Key Findings and Insights
---
Example of what you might discover:
Few products generate most revenue.
Small group of customers are responsible for large sales.
UK dominates purchases.
Sales increase during holidays.
Business meaning:
Focus marketing on VIP customers.
Promote top products.
Prepare stock for busy months.

## Project Timeline
---
Week 1 → find dataset, define goals

Week 2 → clean data

Week 3 → explore patterns

Week 4 → visualization & deeper analysis

Week 5 → report & slides

## Outcome of the Project
---
You will gain:
Real experience with messy data
Strong Pandas skills
Business thinking
Team collaboration
GitHub workflow

## Conclusion
---
This project shows how raw data becomes useful information.
You will support decision making using numbers instead of guessing.

## References
---
Dataset:
https://archive.ics.uci.edu/ml/datasets/online+retail
Pandas documentation:
https://pandas.pydata.org/docs/
Scikit-learn:
https://scikit-learn.org/

## Appendix
---
Extra code
Additional charts
Tables
Experiments
