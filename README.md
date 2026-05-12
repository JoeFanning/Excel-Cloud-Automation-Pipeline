# 📊 Cloud Sales Analysis & Excel Automation Pipeline

A serverless, cloud-based Python pipeline designed to automate the merging, analysis, and reporting of weekly sales data. This system transforms raw data into multi-tab executive reports and high-impact visual dashboards, deployed directly in the cloud.

## 🚀 Key Features

* **Serverless Cloud Execution:** Runs entirely in the cloud with automated Cron scheduling to clean and analyze data.
* **Data Consolidation:** Automatically merges multiple weekly Excel workbooks into a single master file.
* **Multi-Tab Reporting:** Generates a professional `.xlsx` file featuring dedicated sheets for core KPIs.
* **Visual Dashboards:** Automatically outputs a `.png` graphic dashboard for rapid executive review.
* **Direct Cloud Delivery:** Uses a built-in email module to securely deliver completed reports to stakeholders.

## 📈 Multi-Tab Report Structure

The generated Excel report (`sales_analysis_report.xlsx`) includes the following dedicated tabs:
1. **Executive Summary** - Core KPIs: Revenue, Units Sold, and Average Order Value.
2. **Sales by Location** - Regional performance across all store branches.
3. **Product Performance** - Analysis of Top 5 Best Sellers and Bottom 3 Performers.
4. **Payment Type Breakdown** - Revenue split across Cash, Card, Online, and Gift Cards.
5. **Time of Day** - Identifying peak sales hours (Morning, Afternoon, Evening).

## 🛠 Project Architecture

* `src/calculations.py`: The engine performing sales math and trend analysis.
* `src/io_manager.py`: Manages file merging and complex multi-sheet Excel writing.
* `src/visuals.py`: Generates graphical charts and dashboards.
* `src/mailer.py`: Handles secure SMTP email delivery with attachments.
* `main.py`: The central coordinator for the entire automation pipeline.

## 💻 Cloud Deployment Workflow

1. **Input:** Raw weekly Excel files are ingested into the pipeline via the designated cloud storage directory (`/input`).
2. **Process:** The automated cloud pipeline triggers, executing `main.py` on its set Cron schedule.
3. **Output:** The finalized dashboard and `.xlsx` report are generated (`/output`) and emailed directly to your distribution list.

## ⚙️ Setup & Requirements

1. **Clone the Repo:** 
   `git clone github.com`
2. **Install Dependencies:** 
   `pip install -r requirements.txt`
3. **Environment Variables:** 
   Configure your cloud server environment variables (e.g., SMTP credentials for email delivery).
and dashboard will be waiting in the `/output` folder.

---
