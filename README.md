# 🛠️ Log Analysis Tool — User Manual

## 📍 Purpose
This tool helps identify and visualize abnormal traffic patterns from server logs. It detects potential bots by analyzing request frequency and generates charts to support decision-making.

---

## 🧰 Requirements

### 1. 🧑‍💻 Code Editor (VS Code)

- Download Visual Studio Code: 👉 (https://code.visualstudio.com/)
- Install and open it. (Optional but recommended for editing and debugging Python files)

---

### 2. 🐍 Python Installation

- Download Python 3.10 or higher: 👉 (https://www.python.org/downloads/)
- Make sure to check “Add Python to PATH” during installation
- Verify installation:
  ```bash
  python --version
  ```

---

### 3. 🧪 Create a Virtual Environment

Inside your project folder:

```bash
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate.bat      # Windows
```

---

### 4. 📦 Install Project Dependencies

Inside your virtual environment, run:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Your `requirements.txt` should include:

```
matplotlib
python-dateutil
```

---

## 📂 Project Structure

```
project-root/
├── logs/
│   └── sample-log.log             # Your raw web server log
├── src/
│   └── parser.py                  # Log parsing logic
├── logs-analysis.py               # Main entry point
├── requirements.txt
```

---

## 🚀 How to Run the Analysis

Once your environment is ready:

```bash
python analysis.py
```

This will:

✅ Parse and analyze your log file  
✅ Count total requests per IP  
✅ Detect burst traffic from bots  
✅ Generate 2 charts in your root folder:

| File                      | What it shows                           |
|---------------------------|------------------------------------------|
| `ip_requests.png`         | Top IPs by total request volume          |
| `hourly_distribution.png` | Request volume across hours of the day |

---

## 🔎 Key Features

- **Regex-based parser** customized for extended Apache-style logs
- **Bot detection** via total requests and burst activity
- **Visualizations** using Matplotlib
- **Configurable thresholds** to adjust sensitivity based on your traffic baseline