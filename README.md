<img width="1919" height="971" alt="Screenshot 2026-10-11 224354" src="https://github.com/user-attachments/assets/8b9efb26-79dd-4bd5-b3e6-328bdd68bd62" />




# Packet-Sentinels
Packet Sentinels is a lightweight, high-performance web application built with Flask and Pandas designed to analyze network capture data. It processes uploaded network logs in CSV format and immediately generates visual, interactive insights using Chart.js.



# 🛡️ Packet Sentinels: Network Traffic Analyzer

**Packet Sentinels** is a lightweight, high-performance web application built with **Flask** and **Pandas** designed to analyze network capture data. It processes uploaded network logs in CSV format and immediately generates visual, interactive insights using **Chart.js**. 

The user interface features a retro-modern **Cyberpunk Hacker Terminal** theme, optimized for high-speed data parsing, clear visual segregation, and fully responsive layouts.

---

## 🚀 Key Features

*   **Instant Data Ingestion:** Processes network capture CSV files dynamically directly from memory streams without slow disk-write operations.
*   **Memory-Optimized Parsing:** Uses selective Pandas stream-reading (`usecols`) to pull only required metrics (`Source` and `Protocol`), minimizing RAM usage on large capture logs.
*   **Top-5 Analytical Dashboard:** Instantly isolates, ranks, and maps the top 5 most active Source IP addresses and network protocols.
*   **Interactive Data Graphics:** Displays live data metrics using high-contrast Chart.js bar graphs equipped with automatic lifecycle cleanup to prevent hover-ghosting on sequential file uploads.
*   **Robust Server-Side Validation:** Hardened structural error trapping shields against invalid extensions, empty states, or missing data fields, rendering graceful JSON error alerts on the interface.

---

## 🛠️ Tech Stack & Components

### Backend (Python)
*   **Flask:** Handles lightweight routing, content length restrictions, and clean JSON endpoints.
*   **Pandas:** Drives high-speed tabular data processing, frequency distribution calculations, and column filtering.
*   **Werkzeug:** Reinforces secure file handling standards.

### Frontend (Modern UI)
*   **HTML5 / CSS3:** Structured with modern CSS variables, Flexbox layouts, and responsive grid patterns matching an obsidian-green terminal aesthetic.
*   **JavaScript (ES6):** Utilizes the asynchronous Fetch API to stream file uploads smoothly without breaking page workflows or requiring hard reloads.
*   **Chart.js (CDN):** Generates fast, animated, and responsive vector graphs natively in the browser.

---

## 📂 Project Structure

```text
packet-sentinels/
│
├── app.py                 # Memory-optimized Flask backend service
├── README.md              # Project documentation and setup guide
│
├── templates/
│   └── index.html         # Responsive hacker dashboard & AJAX chart logic
│
└── static/
    └── style.css          # Cyberpunk grid layout and neon visual accents
```

---

## ⚡ Getting Started

Follow these instructions to get the application up and running on your local machine.

### Prerequisites
Make sure you have Python 3.8+ installed. Check your version with:
```bash
python --version
```

### 1. Clone the Repository
```bash
git clone https://github.com
cd Packet-Sentinels
```

### 2. Install Required Packages
Install the essential analytical and web server dependencies:
```bash
pip install flask pandas
```

### 3. Run the Application
Start your local deployment server:
```bash
python app.py
```

Open your web browser and navigate to:
```text
http://127.0.0.1:5000
```

---

## 📊 CSV File Format Requirement

To ensure accurate analysis, your uploaded `.csv` file must contain at least the following two column names (case-sensitive):

| Column Name | Sample Data | Description |
| :--- | :--- | :--- |
| `Source` | `192.168.1.1` or `Device-Alpha` | The originating IP address or host hardware identifier. |
| `Protocol` | `TCP`, `UDP`, `HTTP`, `TLSv1.2` | The network transfer layer protocol used for the packet. |

---

