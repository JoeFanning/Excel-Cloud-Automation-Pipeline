# Resend Email Integration & SDK Documentation

This document explains how our automation pipeline connects to the Resend Email Platform, why we use their official SDK tool, and how to manage the environment security.

---

## 1. What is Resend?
Resend is a cloud-based email delivery service built for developers. Instead of managing a slow, traditional SMTP email server, our script sends data packets over a fast, secure Web API gateway.

* **Target Account:** joespirial@hotmail.com
* **Sender Alias:** Automation Engine <onboarding@resend.dev>

---

## 2. Why We Use the Official Resend Python SDK
Instead of building manual network requests using Python's general `requests` library, we use the official custom wrapper package (`pip install resend`). 

### Key Benefits of the SDK:
* **Hidden URL Routing:** We do not type any web address strings in our code. The package automatically knows to target the exact endpoint (`https://resend.com`) in the background.
* **Auto-Formatted Headers:** Security rules, payload encryption, and strict browser `User-Agent` strings are handled natively by the library.
* **Typo Protection:** Code editors can read the built-in dictionary requirements, helping prevent spelling mistakes before the script runs.
* **Cleaner Maintenance:** If Resend upgrades their cloud servers, we only have to update the package rather than rewriting our script logic.

---

## 3. How the Code Works (`src/mailer.py`)
Our mailer module converts local binary Excel files into text-based **Base64 strings** to match Resend's attachment structure.

```python
import resend

# The SDK automatically finds the backend servers
resend.api_key = os.environ.get("RESEND_API_KEY")

email_params = {
    "from": "Automation Engine <onboarding@resend.dev>",
    "to": ["joespirial@hotmail.com"],
    "subject": "Weekly Report",
    "html": "<strong>Pipeline Complete!</strong>",
    "attachments": [{"filename": "report.xlsx", "content": "BASE64_STRING_HERE"}]
}

resend.Emails.send(email_params)
```

---

## 4. Local Setup & Security Rules

### ⚠️ Rule 1: Never Hardcode the API Key
Never type your raw `re_c34b...` key directly into your Python files. If a raw key is pushed to GitHub, it will instantly leak, and Resend will automatically deactivate it for security.

### Rule 2: Local Testing in PyCharm
To test the script locally without exposing the secret key to Git:
1. Open PyCharm -> **Run** -> **Edit Configurations...**
2. Select your active run script profile.
3. Click **Environment variables**.
4. Add a new row:
   * **Name:** `RESEND_API_KEY`
   * **Value:** *Paste your raw token string here (no quotes, no brackets)*
5. Click **Apply** and run the project.

### Rule 3: Cloud Deployment (GitHub Actions)
When running automatically on a weekly schedule, the cloud runner gets its key from **GitHub Repository Secrets**. The `main.yml` file maps the secret token to the script using the exact same variable name (`RESEND_API_KEY`).
