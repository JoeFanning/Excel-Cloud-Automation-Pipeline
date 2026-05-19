# 📊 Cloud Sales Analysis & Excel Automation Pipeline

## 📥 Instant Desktop Testing
[![Download App](https://shields.io)](https://github.com/JoeFanning/Excel-Cloud-Automation-Pipeline/releases/download/v1.0.0/sales_gui.exe)

> **How to Test:** Click the green badge above to download the standalone `sales_gui.exe` application [GitHub Cloud Upload]. Save it to your computer, open it, and type your email address to instantly run the automation pipeline and receive your sample Excel reports! *(No Python or PyCharm installation required).*

---

A serverless, cloud-based Python pipeline designed to automate the merging, analysis, and reporting of weekly sales data [GitHub Cloud Upload]. This system transforms raw data into multi-tab executive reports and visual dashboards, deployed directly in the cloud.

## 🚀 Key Features

* **Serverless Cloud Execution:** Runs entirely in the cloud on a weekly schedule using GitHub Actions [GitHub Cloud Upload].
* **Data Consolidation:** Automatically merges multiple weekly Excel workbooks into a master dataset.
* **Multi-Tab Reporting:** Generates a professional `.xlsx` file featuring dedicated sheets for core KPIs.
* **Visual Dashboards:** Automatically outputs a `.png` graphic dashboard for rapid executive review.
* **Direct Cloud SDK Delivery:** Integrates natively with the official Resend Python SDK to securely transmit reports without traditional SMTP overhead [Resend API].

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
* `src/mailer.py`: Handles secure API email delivery using the official **Resend Python SDK** [Resend API].
* `main.py`: The central coordinator for the entire automation pipeline.
* `.github/workflows/main.yml`: The GitHub Actions runner script driving the automated cloud executions [GitHub Cloud Upload].

## ⚠️ Important: Input Data & Header Constraints

The calculation engine relies on a strict database schema. If you load raw data files into the `/input` directory, you must ensure your columns match our format perfectly.

* **Header Mapping:** The script looks for explicit, case-sensitive columns (e.g., `Revenue`, `Location`, `Product_ID`, `Timestamp`).
* **Mismatched Headers:** If another developer imports data with different column names (such as `Total_Sales` instead of `Revenue`), **the calculation engine will throw a key error and crash**.
* **Fixing Layout Changes:** If your source data layout changes, you must update the column tracking keys inside `src/clean_sort_data.py` and `src/calculations.py` to match your new headers.

## ✉️ Customizing Email Recipients

By default, the automated report routes directly to a pre-configured stakeholder address. If you are a developer forks this project and want the email directed to your own inbox, follow these steps:

1. Open `main.py` in your code editor.
2. Scroll down to **Step 5 (Send ONE Final Email)** inside the `main()` function block.
3. Replace the target email string with your own address:
   ```python
   send_email_report(
       "Weekly Sales Dashboard Report",
       summary_text,
       "your-custom-email@example.com",  # <-- Change this to your address!
       attachments,
       logger
   )
   ```
4. *Note on Testing:* If you are using Resend's default free test tier, your custom address **must** be registered as a verified recipient inside your personal Resend Dashboard, or the transmission will be blocked.

## 🚧 Road Map: Upcoming GUI Desktop App

* **In Development:** A native Graphical User Interface (GUI) wrapper application is currently being built for this engine.
* **The Goal:** Once completed, non-technical users will be able to launch a desktop application, paste their target email addresses into a simple text box, click a button, and handle cloud deployments without editing a single line of Python code.

## ⚙️ Setup & Requirements

### 1. Clone the Repo
```bash
git clone https://github.com
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
1. Go to your repository **Settings** -> **Secrets and variables** -> **Actions** [GitHub Cloud Upload].
2. Click **New repository secret** [GitHub Cloud Upload].
3. Create a secret named exactly **`RESEND_API_KEY`** and paste your API key string [GitHub Cloud Upload].
