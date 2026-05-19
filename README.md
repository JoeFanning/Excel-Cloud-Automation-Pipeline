# 📊 Cloud Sales Analysis & Excel Automation Pipeline

A serverless, cloud-based Python pipeline designed to automate the merging, analysis, and reporting of weekly sales data. This system transforms raw data into multi-tab executive reports and visual dashboards, deployed directly in the cloud.

## 🚀 Key Features

* **Serverless Cloud Execution:** Runs entirely in the cloud on a weekly schedule using GitHub Actions.
* **Data Consolidation:** Automatically merges multiple weekly Excel workbooks into a master dataset.
* **Multi-Tab Reporting:** Generates a professional `.xlsx` file featuring dedicated sheets for core KPIs.
* **Visual Dashboards:** Automatically outputs a `.png` graphic dashboard for rapid executive review.
* **Direct Cloud SDK Delivery:** Integrates natively with the official Resend Python SDK(resend.com) to securely transmit reports without traditional SMTP overhead.

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
* `src/mailer.py`: Handles secure API email delivery using the official **Resend Python SDK** (resend.com)
* `main.py`: The central coordinator for the entire automation pipeline.
* `.github/workflows/main.yml`: The GitHub Actions runner script driving the automated cloud executions.

## ⚠ Data Ingestion & Spreadsheet Header Notice

The data pipeline relies on a specific, fixed file layout to process your metrics correctly. The application expects your uploaded Excel spreadsheets to contain exact column headers. If your source files use different names, spellings, or organizational structures, the system will not recognize the data.

### Required Spreadsheet Schema

For a seamless test run, please ensure your Excel column headers match this exact template:


| Required Column Header | Expected Data Type | Example Value | Description |
| :--- | :--- | :--- | :--- |
| **TransactionID** | Text / Integer | TX300667 | Unique identifier for the sale |
| **Date** | Date (YYYY-MM-DD) | 2024-02-27 | The date the transaction occurred |
| **Time** | Time (HH:MM) | 14:22 | The timestamp of the sale |
| **StoreID** | Text | S10 | Unique identifier for the retail store |
| **Location** | Text | Store B | Name or description of the store branch |
| **Product** | Text | Phone | Name of the item sold |
| **Quantity** | Integer | 4 | Number of units purchased |
| **UnitPrice** | Decimal / Float | 5.58 | The price per individual unit |
| **TotalPrice** | Decimal / Float | 22.32 | Gross price of the item sold (Quantity × UnitPrice) |
| **PaymentType** | Text | Credit Card | Method used to pay for the transaction |
| **Cashier** | Text | C1 | ID or name of the employee processing the sale |
| **StoreManager** | Text | Mia | Name of the manager running the store location |
| **TimeOfDay** | Text | Afternoon | Categorized period when the sale occurred |
| **DayOfWeek** | Text | Tuesday | Day name corresponding to the transaction date |

> [!NOTE]
> I am currently exploring alternative data ingestion methods to further optimize and refine this ingestion pipeline's functionality.

💡 **Tip:** A ready-to-use sample dataset file is included in the `input/` directory so you can test-run the pipeline immediately.

---
## 📥 Instant Desktop(Windows) Testing & Custom Routing

Instead of editing the raw Python code to route the final sales report to your inbox, you can use the pre-compiled standalone application layout. 

![Download App](https://shields.io)](https://github.com/JoeFanning/Excel-Cloud-Automation-Pipeline/releases/download/v1.0.0/sales_gui.exe)

> **How to Test:** Click the green link above to download the standalone `sales_gui.exe` application. Save it to your computer, open it, and type your personal email address into the input box. The application will instantly execute the pipeline data math and dispatch your sample Excel reports straight to your inbox! *(No local Python setup required).*

## ⚙️ Setup & Requirements

### 1. Clone the Repo
```bash
git clone [https://github.com](https://github.com/JoeFanning/Excel-Cloud-Automation-Pipeline.git)
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Environment Variables Configuration

#### Local Testing (PyCharm)
1. Navigate to **Run** -> **Edit Configurations...** -> **Environment variables**.
2. Add a variable with the Name `RESEND_API_KEY` and paste your raw token value.
3. Keep the file `sales_analysis_report.xlsx` closed locally to avoid `Permission Denied` execution errors.

#### Cloud Production (GitHub Actions)
1. Go to your repository **Settings** -> **Secrets and variables** -> **Actions**.
2. Click **New repository secret**.
3. Create a secret named exactly **`RESEND_API_KEY`** and paste your API key string.

## 📄 License
This project is open-source software created by **Joe Fanning** and is licensed under the [MIT License](LICENSE).

