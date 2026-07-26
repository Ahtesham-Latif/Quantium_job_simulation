# Quantium Software Engineering Job Simulation

**Author:** Ahtesham Latif  
**LinkedIn:** [ahtesham-latif](https://www.linkedin.com/in/ahtesham-latif)  

<br>

## 🏢 Project Overview

This documentation walks through exactly how I completed the **Quantium Software Engineering Job Simulation** on Forage. 

> [!NOTE]
> **The Goal:** A client named **Soul Foods** raised the price of their popular **"Pink Morsel"** candy bar. My job was to engineer an automated data pipeline and reactive web dashboard so they could easily visualize if the price increase drove profits up or scared customers away.

### 🛠️ What I Used:
- **Data Engineering:** Python, Pandas (ETL, Regex)
- **Frontend Development:** Plotly Dash, CSS (Component Callbacks)
- **Quality Assurance:** Pytest, Selenium WebDriver (DOM Verification)
- **DevOps:** Bash Scripting, Virtual Environments (CI/CD readiness)

---

## 💻 Task One: Getting Set Up

**Goal:** Establish an isolated local development environment to ensure strict dependency management before building out the client's solution.

### 📝 What I Did:

* **Checking the Runtime**  
  I verified the Python and pip installations.  
  *(Note: I ran this project on Python 3.14.6, but the codebase is fully compatible with Python 3.11).*

* **Cloning the Repository**  
  I cloned the starter boilerplate from Quantium into my local workspace.

* **Creating a Sandbox**  
  I initialized a virtual environment (`venv`). This ensures the project's dependencies remain strictly isolated from my global system packages.

* **Installing the Tech Stack**  
  I activated the environment and installed the necessary libraries, including `pandas` for data mutation and `dash` for the frontend application.

---

## 🧹 Task Two: Cleaning the Data (ETL)

**Goal:** Extract three fragmented, messy CSV files, transform them into a clean dataset, and load the output into a machine-readable format.

### 📝 What I Did:

* **Data Ingestion**  
  I used Python's `pandas` library to load the raw daily sales CSV files into memory.

* **Data Consolidation**  
  I concatenated all three dataframes into a single, unified structure and reset the index for clean iteration.

* **Data Filtering**  
  The client only cared about the Pink Morsel candy bar, so I filtered the dataframe to isolate only those specific product records.

* **Regex Sanitization**  
  The raw price column had string artifacts (dollar signs and commas). I wrote a regular expression filter to strip those out and cast the column into float values for arithmetic operations.

* **Metric Calculation**  
  I multiplied the cleaned `price` by the `quantity` sold to engineer a brand new `Sales` column.

* **Artifact Export**  
  I dropped the unnecessary columns and exported the final, sanitized dataframe as a new file called `pink_morsel_sales.csv`.

---

## 📈 Task Three & Four: Building the Reactive Dashboard

**Goal:** Build a frontend web application that visualizes the cleaned data, leveraging callbacks so the client can dynamically explore geographic sales trends.

### 📝 What I Did:

* **Loading & Formatting**  
  I wrote a server script to load the `pink_morsel_sales.csv` artifact and cast the dates into proper datetime objects for chronological plotting.

* **Data Aggregation**  
  I grouped the sales data by date to calculate total daily sales volume. I also programmed a comparative check to evaluate total sales before and after January 15, 2021 (the day the price increased).

* **Constructing the Graph**  
  I used Plotly to render a line chart tracking sales over time. I injected a bold red dashed line on January 15th to instantly provide visual context for the price hike.

* **Building the UI Components**  
  I used Dash to mount the chart onto a web layout. I added radio button components at the top to serve as regional filters (All, North, South, East, West). 

* **Implementing Callbacks**  
  I wrote a reactive callback function. Now, whenever the client interacts with a radio button, the application state updates, filters the underlying dataframe, and re-renders the graph live without a page refresh.

---

## 🧪 Task Five: Automated UI Testing

**Goal:** Engineer a robust automated test suite to verify the DOM elements and prevent regressions when pushing future changes to the codebase.

### 📝 What I Did:

* **WebDriver Configuration**  
  I installed `webdriver-manager` to dynamically handle the Chrome driver binaries.

* **Headless Testing Setup**  
  I configured `conftest.py` so the Selenium browser runs in "headless" mode. This allows the tests to execute silently in the background, which is crucial for CI/CD pipeline compatibility.

* **Test 1: Header Validation**  
  I wrote a test that mounts the app and asserts that the main `<h1>` element successfully renders the correct title.

* **Test 2: SVG Rendering**  
  I wrote a test that waits for the DOM to load and verifies that the Plotly SVG chart component is actually present on the screen.

* **Test 3: Component Interaction**  
  I wrote a test to assert that the regional radio selector component is mounted, visible, and ready for user interaction.

---

## 🤖 Task Six: Continuous Integration (CI) Scripting

**Goal:** Write a shell script to automate the execution of the test suite, simulating a basic CI pipeline step.

### 📝 What I Did:

* **Writing the Bash Script**  
  I created a shell script called `run_test.sh`. 

* **Environment Automation**  
  The script automatically activates the Python virtual environment and triggers the `pytest` runner. 

* **Handling Exit Codes**  
  I programmed the script to capture the system exit codes. If the suite passes (exit code 0), it logs a success message. If a test fails (exit code 1), it catches the failure. This ensures the script can easily plug into a larger automated deployment pipeline.

---

## 🏆 Final Result

> [!SUCCESS]
> **Tests passed successfully! Exit code: 0**

```text
============================= test session starts =============================
platform win32 -- Python 3.14.6, pytest-9.0.2, pluggy-1.6.0
rootdir: C:\Users\Admin\Desktop\Quantium JOB Simulation\quantium-starter-repo
plugins: dash-3.4.0
collected 3 items

test_app.py ...                                                          [100%]

============================= 3 passed in 38.93s ==============================
```

---

## 📁 Project Structure

Here is how all the project components fit together:

```text
quantium-starter-repo/
├── data/
│   ├── daily_sales_data_0.csv
│   ├── daily_sales_data_1.csv
│   ├── daily_sales_data_2.csv
│   └── pink_morsel_sales.csv     # The cleaned and aggregated artifact
├── venv/                         # Isolated Python environment
├── app.py                        # Task 2: The ETL processing script
├── App.ipynb                     # Scratchpad for initial exploration
├── Certificate.png               # Program completion certificate
├── DashBoard.png                 # Screenshot of the working UI
├── FlowDiagram.png               # System architecture diagram
├── Documentation.md              # You are reading this!
├── README.md                     # The executive overview page
├── CONTRIBUTING.md               # Guidelines for contributing
├── LICENSE                       # Project license
├── requirements.txt              # Project dependency list
├── task3.py                      # Task 3/4: The Dash application server
├── test_app.py                   # Task 5: The automated Pytest suite
├── conftest.py                   # Task 5: Headless WebDriver hooks
└── run_test.sh                   # Task 6: CI automation script
```
