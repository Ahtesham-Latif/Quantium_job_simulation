# Quantium starter repo
Pink Morsel Sales VisualizerA data engineering and visualization suite designed to analyze sales trends for the "Pink Morsel" product. This tool was developed to investigate the impact of a significant price increase on January 15, 2021, providing stakeholders with a clear, interactive way to view performance across different geographical regions.✨ FeaturesAutomated Data ETLConsolidates fragmented data from multiple CSV sources.Sanitizes and cleans financial data for accurate calculation.Filters specifically for the "Pink Morsel" product line.Interactive Analytics DashboardTrend Visualization: High-fidelity line charts showing daily sales volume.Regional Selectors: Filter data by North, South, East, West, or All regions.Price Increase Impact: Visual markers (crimson dashed lines) pinpointing the exact date of price changes.Peak/Trough Detection: Automatic identification of highest and lowest sales days.Robust Quality AssuranceAutomated test suite using Selenium and Pytest.Headless browser configuration for CI/CD compatibility.Single-command execution via Shell scripting.🛠 Installation1. Clone the RepositoryBashgit clone https://github.com/vagabond-systems/quantium-starter-repo.git
cd quantium-starter-repo
2. Setup Virtual EnvironmentBash# Initialize the environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
3. Install DependenciesBashpip install pandas dash[testing] plotly webdriver-manager selenium
🚀 How to Run the ProjectPhase 1: Data ProcessingRun the ETL script to generate the formatted sales data from the raw input files:Bashpython app.py
Output: data/pink_morsel_sales.csvPhase 2: Start the DashboardLaunch the Dash application:Bashpython task3.py
Access the app: Open your browser and navigate to http://127.0.0.1:8050Phase 3: Automation & TestingTo ensure the system is running correctly, execute the automated test suite:Bash# Make script executable (Git Bash/Linux)
chmod +x run_test.sh

# Run the tests
./run_test.sh
🧪 Logic & CapabilitiesETL Logic: Uses Python's pandas library to perform regex-based cleaning of currency strings ($5.00 -> 5.0) and aggregate sales ($Sales = Price \times Quantity$).Reactive UI: Built with Dash callbacks; when a user selects a region, the backend re-calculates the idxmax() and idxmin() for sales to update the graph markers dynamically.Headless Testing: The conftest.py setup allows the Selenium WebDriver to run without a GUI, making it ideal for server environments.

👨‍💻 AuthorAhtesham LatifLinkedIn: linkedin.com/in/ahtesham-latif 
GitHub: github.com/Ahtesham-Latif
📜 LicenseThis project is licensed for educational and professional simulation use.
