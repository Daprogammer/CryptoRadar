# 📈 CryptoRadar — Cryptocurrency Forecasting & Market Sentiment Platform

<p align="center">

**A data-driven cryptocurrency intelligence platform combining market data, macroeconomic indicators, financial news, and social sentiment to identify bullish and bearish market trends.**

</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge\&logo=mysql\&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-UI-06B6D4?style=for-the-badge\&logo=tailwindcss\&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Web_Scraping-43B02A?style=for-the-badge\&logo=selenium\&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-NLP-09A3D5?style=for-the-badge)

</p>

---

## 📌 Overview

**CryptoRadar** is a full-stack cryptocurrency forecasting and market intelligence platform designed to combine **quantitative market data with qualitative market sentiment**.

Traditional cryptocurrency analysis often relies heavily on historical price charts and technical indicators. However, crypto markets are also strongly influenced by:

* Community sentiment
* Financial news
* Market narratives
* Macroeconomic conditions
* Sudden changes in investor psychology

CryptoRadar addresses this by building an automated data pipeline that collects **OHLCV market data, macroeconomic indicators, Reddit discussions, and financial news**, processes textual information using NLP, and presents the resulting information through an interactive web dashboard.

The platform provides users with:

* Current cryptocurrency market information
* Historical price data
* Forecast ratings
* Bullish/Bearish sentiment indicators
* News sentiment
* Reddit community sentiment
* Interactive price charts
* Historical CSV exports
* Personalized dashboard preferences

---

# 🎯 Problem Statement

Cryptocurrency markets are highly volatile and are influenced by more than historical price movement.

A price-only forecasting system can overlook important information such as:

* A sudden shift in community sentiment
* Major cryptocurrency news
* Macroeconomic pressure from the US Dollar
* Negative narratives surrounding a particular asset
* Positive accumulation or breakout narratives

Therefore, CryptoRadar follows a multi-source approach:

```text
             Historical Market Data
                     │
                     ▼
              Quantitative Signals
                     │
                     │
Social Sentiment ────┼──── Financial News
                     │
                     │
             Macro Indicators
                     │
                     ▼
             ┌───────────────┐
             │   CryptoRadar │
             │ Intelligence  │
             └───────┬───────┘
                     │
                     ▼
           Market Outlook & Signals
              Bullish / Bearish
```

The objective is not to rely on a single source of information, but to create a more comprehensive market perspective by combining multiple independent signals.

---

# 💡 Solution

CryptoRadar implements an automated data-processing pipeline that:

1. Collects cryptocurrency OHLCV data from Binance.
2. Collects the US Dollar Index (DXY) using Yahoo Finance data.
3. Retrieves cryptocurrency-related discussions from Reddit through RSS.
4. Scrapes financial headlines from CoinDesk.
5. Cleans and lemmatizes textual data using spaCy.
6. Calculates sentiment using a customized VADER lexicon.
7. Stores processed information in MySQL.
8. Presents the resulting market information through a responsive frontend dashboard.

---

# 🏗️ System Architecture

CryptoRadar follows a modular data-pipeline architecture consisting of a client-side dashboard, automated ingestion layer, NLP processing engine, and relational database.

```text
                         ┌─────────────────────┐
                         │        USER         │
                         └──────────┬──────────┘
                                    │
                                    ▼
                    ┌───────────────────────────┐
                    │     Frontend Dashboard    │
                    │                           │
                    │ HTML5                     │
                    │ Vanilla JavaScript        │
                    │ Tailwind CSS / Bootstrap   │
                    │ Chart.js                  │
                    └─────────────┬─────────────┘
                                  │
                                  │
                                  ▼
                    ┌───────────────────────────┐
                    │     Data / Application    │
                    │         Pipeline          │
                    │       extractor.py        │
                    └─────────────┬─────────────┘
                                  │
                ┌─────────────────┼──────────────────┐
                │                 │                  │
                ▼                 ▼                  ▼
        ┌──────────────┐  ┌──────────────┐  ┌───────────────┐
        │    Binance   │  │ Yahoo Finance│  │    Reddit     │
        │     API      │  │     DXY      │  │     RSS       │
        └──────┬───────┘  └──────┬───────┘  └───────┬───────┘
               │                 │                  │
               │                 │                  │
               └─────────────────┼──────────────────┘
                                 │
                                 ▼
                       ┌──────────────────┐
                       │   CoinDesk       │
                       │ Selenium +       │
                       │ BeautifulSoup    │
                       └────────┬─────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │    NLP Processing      │
                    │                        │
                    │ spaCy                  │
                    │ Lemmatization          │
                    │ Custom VADER Lexicon   │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │       MySQL             │
                    │                         │
                    │ coin_prices              │
                    │ macro_indicators         │
                    │ posts_logs               │
                    │ news_logs                │
                    │ _migrations              │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │  Dashboard & Analytics  │
                    │                        │
                    │ Prices                 │
                    │ Forecasts              │
                    │ Sentiment              │
                    │ Charts                 │
                    │ CSV Export             │
                    └────────────────────────┘
```

---

# ✨ Key Features

## 🖥️ Frontend Dashboard

The frontend is built using **HTML5, Vanilla JavaScript, Tailwind CSS, Bootstrap 5, and Chart.js**.

### 🔐 Authentication

The application provides client-side authentication functionality through:

* Login
* Signup
* Session persistence
* `localStorage`-based session handling

---

### 📊 Market Dashboard

The main dashboard provides a high-level overview of supported cryptocurrencies.

Users can view:

* Current prices
* Price-related information
* Forecast ratings
* Bullish/Bearish indicators
* Market information

---

### 📈 Interactive Historical Charts

The cryptocurrency detail page uses **Chart.js** to visualize historical price information.

Features include:

* Interactive price charts
* Historical market data
* Dynamic chart rendering
* Historical dataset export

---

### 📥 CSV Data Export

Users can export historical cryptocurrency datasets in CSV format for:

* Further analysis
* Data science workflows
* Spreadsheet analysis
* External visualization tools

---

### 🔎 Real-Time Cryptocurrency Search

The search interface provides instant filtering based on:

* Cryptocurrency name
* Cryptocurrency symbol

This allows users to quickly locate supported assets.

---

### 🎨 Personalization

CryptoRadar includes a personalization page where users can manage their profile preferences.

The frontend also supports persistent:

* Light mode
* Dark mode

Theme preferences are retained using client-side storage.

---

# ⚙️ Automated Data Extraction Pipeline

The primary data ingestion workflow is implemented in:

```text
extractor.py
```

The pipeline aggregates information from multiple sources.

---

## 🟡 Binance Market Data

CryptoRadar uses the **Binance public API** to retrieve cryptocurrency market information.

The pipeline collects OHLCV data:

| Field      | Meaning                |
| ---------- | ---------------------- |
| **Open**   | Opening price          |
| **High**   | Highest recorded price |
| **Low**    | Lowest recorded price  |
| **Close**  | Closing price          |
| **Volume** | Trading volume         |

The pipeline supports multiple candle intervals for historical market analysis.

---

## 💵 US Dollar Index — DXY

The project uses **Yahoo Finance data through `yfinance`** to retrieve the US Dollar Index.

The DXY provides a macroeconomic signal that can be incorporated into cryptocurrency market analysis.

Conceptually:

```text
US Dollar Strength
        │
        ▼
Macro Market Pressure
        │
        ▼
Cryptocurrency Market Context
```

---

## 🔴 Reddit Community Sentiment

CryptoRadar retrieves cryptocurrency discussions from:

```text
r/CryptoMarkets
```

The project uses **`feedparser`** to consume the subreddit RSS feed.

Extracted information can then be processed by the NLP pipeline to identify the sentiment expressed within community discussions.

---

## 📰 CoinDesk News Extraction

CryptoRadar also incorporates financial news through an automated web scraping pipeline.

The scraper uses:

* Selenium
* BeautifulSoup4

Selenium provides browser automation while BeautifulSoup4 is used to parse and extract relevant information from the retrieved pages.

The resulting headlines are passed into the sentiment analysis pipeline.

---

# 🧠 Natural Language Processing Engine

CryptoRadar uses NLP to convert unstructured financial and social text into quantitative sentiment information.

```text
Raw Text
   │
   ▼
Text Cleaning
   │
   ▼
spaCy Processing
   │
   ▼
Lemmatization
   │
   ▼
Custom VADER Lexicon
   │
   ▼
Sentiment Score
   │
   ▼
Normalized Market Signal
```

---

## 🔤 spaCy Text Processing

The project uses:

```text
en_core_web_sm
```

from spaCy.

The NLP pipeline uses spaCy primarily for text processing and **lemmatization**, allowing different grammatical forms of words to be normalized into their base forms.

For example:

```text
accumulating
accumulated
accumulation
```

can be normalized toward a common linguistic representation.

---

## 📊 Custom VADER Sentiment Analysis

CryptoRadar uses VADER sentiment analysis with a customized lexicon for cryptocurrency terminology.

The lexicon accounts for terms that have specific meanings in crypto markets.

Examples include:

* `breakout`
* `liquidation`
* `moon`
* `rug pull`
* `accumulation`

The resulting sentiment is normalized to a:

```text
[0, 1]
```

scale.

Conceptually:

```text
0.0 ─────────────────────────────── 1.0
│                                    │
Extreme Bearish                 Extreme Bullish
```

This allows textual sentiment to be represented numerically and incorporated into the project's broader market analysis.

---

# 🗄️ Database Architecture

CryptoRadar uses **MySQL** as its relational database.

The database is designed to store market data, macroeconomic information, social posts, financial news, and migration history.

---

## 📋 Database Tables

### `coin_prices`

Stores historical cryptocurrency market information.

Primary data includes:

* Cryptocurrency information
* OHLCV values
* Time intervals
* Historical timestamps

---

### `macro_indicators`

Stores macroeconomic indicators used by the application.

Current implementation includes:

* US Dollar Index (DXY)

---

### `posts_logs`

Stores processed Reddit community information.

Data includes:

* Community posts
* Processed text
* Sentiment polarity
* Related metadata
* Upvote-related information

---

### `news_logs`

Stores financial news information extracted from CoinDesk.

Data includes:

* News headlines
* Processed information
* Normalized sentiment scores

---

### `_migrations`

Tracks database migration execution.

The migration system records:

* Migration filename
* Execution status
* Execution timestamp

This prevents the same migration from being executed repeatedly.

---

# 🔄 Database Migration System

Database schema management is handled through:

```text
migrate.py
```

SQL schema changes are stored as sequential migration files.

Example:

```text
migration/
├── 001_create_tables.sql
├── 002_add_...
├── 003_add_...
└── ...
```

The migration runner:

1. Reads available SQL migration files.
2. Checks the `_migrations` tracking table.
3. Identifies migrations that have already been executed.
4. Executes pending migrations sequentially.
5. Records successfully executed migrations.

This provides a lightweight and automated schema versioning mechanism.

---

# 🛡️ Data Integrity

The database layer uses techniques such as:

* Composite keys
* Unique constraints
* `INSERT IGNORE`

These mechanisms help prevent duplicate market and sentiment records from being inserted during repeated extraction runs.

---

# 🛠️ Technology Stack

| Layer                       | Technologies                         |
| --------------------------- | ------------------------------------ |
| **Frontend**                | HTML5, CSS3, Vanilla JavaScript ES6+ |
| **UI Frameworks**           | Tailwind CSS, Bootstrap 5            |
| **Visualization**           | Chart.js                             |
| **Backend / Data Pipeline** | Python 3.10+                         |
| **Market Data**             | Binance Public API                   |
| **Macro Data**              | `yfinance`                           |
| **Social Data**             | Reddit RSS, `feedparser`             |
| **News Extraction**         | Selenium, BeautifulSoup4             |
| **NLP**                     | spaCy, `en_core_web_sm`              |
| **Sentiment Analysis**      | VADER Sentiment Analysis             |
| **Database**                | MySQL                                |
| **Database Driver**         | `mysql-connector-python`             |
| **Environment Management**  | `python-dotenv`                      |

---

# 📁 Project Structure

```text
CryptoRadar/
│
├── migration/
│   ├── 001_create_tables.sql
│   ├── ...
│   └── ...
│
├── database/
│   └── migrate.py
│
├── frontend/
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── detail.html
│   ├── search.html
│   └── personalize.html
│
├── extractor.py
├── requirements.txt
├── .env.example
├── LICENSE
└── README.md
```

---

# 📦 Installation & Setup

## Prerequisites

Before running CryptoRadar locally, make sure the following software is installed.

### Required

* Python **3.10+**
* MySQL Server
* Google Chrome
* Git

Chrome is required for the Selenium-based CoinDesk extraction workflow.

---

# 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/CryptoRadar.git
cd CryptoRadar
```

Replace `your-username` with the GitHub account containing the repository.

---

# 2️⃣ Create a Python Virtual Environment

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After activation, your terminal should indicate that the virtual environment is active.

---

# 3️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

If the spaCy language model has not been installed automatically, install it manually:

```bash
python -m spacy download en_core_web_sm
```

---

# 4️⃣ Configure MySQL

Create a MySQL database for the application.

For example:

```sql
CREATE DATABASE cryptoradar_db;
```

Make sure the MySQL server is running before starting the application.

---

# 5️⃣ Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=cryptoradar_db

INTERVAL=4h
LIMIT=500
```

### Environment Variables

| Variable      | Description                          |
| ------------- | ------------------------------------ |
| `DB_HOST`     | MySQL server hostname                |
| `DB_USER`     | MySQL username                       |
| `DB_PASSWORD` | MySQL password                       |
| `DB_NAME`     | CryptoRadar database name            |
| `INTERVAL`    | Market-data extraction interval      |
| `LIMIT`       | Number of market records to retrieve |

> **Security:** Never commit your real `.env` file or database credentials to GitHub. Use `.env.example` for repository documentation.

---

# 6️⃣ Run Database Migrations

Execute the migration system before populating the database:

```bash
python database/migrate.py
```

The migration runner will execute pending SQL migration files and record their completion in the `_migrations` table.

---

# 7️⃣ Run the Data Pipeline

Start the primary extraction pipeline:

```bash
python extractor.py
```

The pipeline is responsible for collecting and processing the project's external data sources.

Conceptually:

```text
extractor.py
    │
    ├── Binance OHLCV
    │
    ├── DXY / Yahoo Finance
    │
    ├── Reddit RSS
    │
    ├── CoinDesk
    │
    └── NLP Sentiment
             │
             ▼
           MySQL
```

---

# 8️⃣ Launch the Frontend

The project uses static HTML pages for the client interface.

You can open the pages directly in a browser or use a development server such as the **VS Code Live Server extension**.

Start with:

```text
frontend/login.html
```

Main pages include:

```text
login.html          → User login
signup.html         → Registration
dashboard.html      → Market dashboard
search.html         → Cryptocurrency search
detail.html         → Coin details & historical charts
personalize.html    → Profile & theme preferences
```

---

# 🔄 Typical Application Workflow

```text
             User
              │
              ▼
        Login / Signup
              │
              ▼
       Dashboard Access
              │
              ▼
       Market Information
              │
      ┌───────┼────────┐
      ▼       ▼        ▼
   Prices   News    Sentiment
      │       │        │
      └───────┼────────┘
              ▼
        Market Outlook
              │
       ┌──────┴──────┐
       ▼             ▼
    Bullish        Bearish
              │
              ▼
        Coin Details
              │
              ▼
       Historical Chart
              │
              ▼
          CSV Export
```

---

# 📊 Data Processing Overview

CryptoRadar processes information from multiple independent sources:

| Source            | Data                | Processing                     |
| ----------------- | ------------------- | ------------------------------ |
| **Binance**       | OHLCV               | Market data ingestion          |
| **Yahoo Finance** | DXY                 | Macro indicator                |
| **Reddit**        | Community posts     | RSS + NLP                      |
| **CoinDesk**      | Financial headlines | Selenium + BeautifulSoup + NLP |

This architecture allows the project to combine quantitative and qualitative market information.

---

# 🔬 Technical Highlights

### Multi-Source Data Fusion

Rather than depending exclusively on historical cryptocurrency prices, CryptoRadar incorporates:

```text
Price Data
    +
Macro Data
    +
Social Sentiment
    +
Financial News
    =
Broader Market Context
```

---

### Domain-Specific Sentiment

The customized VADER lexicon is designed around cryptocurrency terminology instead of treating all financial text as generic sentiment.

This enables terms such as:

```text
breakout
liquidation
moon
rug pull
accumulation
```

to contribute appropriately to the sentiment calculation.

---

### Automated Data Pipeline

The extraction process minimizes manual data collection by automating:

* Market-data retrieval
* Macro-data ingestion
* Reddit extraction
* Financial-news scraping
* Text processing
* Sentiment scoring
* Database insertion

---

# ⚠️ Important Notes

### Selenium

The CoinDesk extraction component requires Google Chrome and Selenium-compatible browser automation.

If scraping fails, verify that:

* Chrome is installed.
* Selenium dependencies are installed.
* Network access is available.
* The target website has not changed its HTML structure.

---

### External Data Sources

CryptoRadar depends on external services such as Binance, Yahoo Finance, Reddit, and CoinDesk.

Changes to their:

* APIs
* RSS feeds
* Website structure
* Access policies
* Rate limits

may require corresponding changes to the extraction pipeline.

---

# 🚧 Limitations

Current limitations include:

* Dependence on external data providers.
* Web scraping can break when website structures change.
* Sentiment analysis is dependent on the quality and coverage of the custom lexicon.
* Cryptocurrency markets are highly volatile and inherently difficult to forecast.
* Sentiment should be treated as an analytical signal rather than a guaranteed prediction.
* Client-side authentication using `localStorage` is appropriate for the current project architecture but should not be considered equivalent to a production-grade server-side authentication system.

---

# 🔮 Future Scope

Potential improvements include:

* Machine-learning-based price forecasting models.
* More advanced technical indicators.
* Additional macroeconomic indicators.
* X/Twitter sentiment integration.
* More cryptocurrency news sources.
* Transformer-based financial NLP models.
* Real-time WebSocket market updates.
* Server-side authentication.
* REST API backend.
* Cloud deployment.
* Scheduled background data ingestion.
* Advanced portfolio analytics.
* Backtesting and model evaluation dashboards.

---

# 📄 License

This project is distributed under the **MIT License**.

See the `LICENSE` file for more information.

---

# 👨‍💻 Author

**Dhairya Amit Shah**

GitHub: **Daprogammer**

---

<p align="center">

**CryptoRadar — Combining market data, macroeconomic signals, news, and community sentiment for a broader view of cryptocurrency markets.**

</p>
