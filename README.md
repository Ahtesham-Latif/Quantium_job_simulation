# 📊 Pink Morsel Sales Visualizer

A data engineering and visualization suite that processes fragmented sales data to analyze the impact of a price increase on the **"Pink Morsel"** product.  

It features an interactive Dash dashboard with regional filtering and a robust, automated Selenium testing pipeline.

---

## ✨ Features

### 🔄 Automated Data ETL
- Consolidates fragmented data from multiple CSV sources into a unified dataset  
- Sanitizes and cleans financial data (currency formatting) for accurate calculation  
- Filters specifically for the **"Pink Morsel"** product line  

### 📈 Interactive Analytics Dashboard
- **Trend Visualization**: High-fidelity line charts showing daily sales volume  
- **Regional Selectors**: Filter data by North, South, East, West, or All regions via radio buttons  
- **Price Increase Impact**: Visual markers (crimson dashed lines) pinpointing the exact date of price changes  
- **Peak/Trough Detection**: Automatic identification of highest and lowest sales days  

### 🧪 Robust Quality Assurance
- Automated test suite using Selenium and Pytest  
- Headless browser configuration for CI/CD compatibility  
- Single-command execution via Shell scripting  

---

## 🛠 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/vagabond-systems/quantium-starter-repo.git
cd quantium-starter-repo
2️⃣ Setup Virtual Environment
# Initialize the environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
3️⃣ Install Dependencies
pip install pandas dash[testing] plotly webdriver-manager selenium
🚀 How to Run the Project
Phase 1: Data Processing
Run the ETL script to generate the formatted sales data from the raw input files:

python app.py
Output:

data/pink_morsel_sales.csv
Phase 2: Start the Dashboard
Launch the Dash application:

python task3.py
Access the app in your browser:

http://127.0.0.1:8050
Phase 3: Automation & Testing
To ensure the system is running correctly, execute the automated test suite:

# Make script executable (Git Bash/Linux)
chmod +x run_test.sh

# Run the tests
./run_test.sh
🧠 Logic & Capabilities
ETL Logic
Uses Python's pandas library

Performs regex-based cleaning of currency strings

Example: $5.00 → 5.0

Aggregates sales using:

Sales = Price × Quantity
Reactive UI
Built with Dash callbacks

When a user selects a region:

Backend recalculates idxmax() and idxmin() for sales

Graph markers update dynamically

Headless Testing
conftest.py configuration enables Selenium WebDriver to run without a GUI

Ideal for CI/CD pipelines and server environments

👨‍💻 Author
Ahtesham Latif

LinkedIn: https://linkedin.com/in/ahtesham-latif

GitHub: https://github.com/Ahtesham-Latif
