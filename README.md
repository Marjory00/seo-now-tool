# 🔍 SEO Now Tool — On-Page Analyzer

> **Portfolio Project** | A full-stack on-page SEO audit tool built with FastAPI and React.  
> Analyze any public URL for meta tags, keyword density, readability, link health, and crawlability — in seconds.

![License](https://img.shields.io/badge/license-Proprietary-red)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![React](https://img.shields.io/badge/React-18-61DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688)

---

## 📸 App Preview

![SEO Now Tool Dashboard](docs/image1.png)

![SEO Now Tool Main](docs/image2.png)

---

## 🧭 Overview

SEO Now Tool is a lightweight, self-hosted SEO auditing application. Paste any public URL and receive an instant breakdown of:

- **Meta Tags** — title length, meta description, Open Graph tags, canonical URL
- **Keywords** — heading structure (H1–H3), top keyword frequency and density
- **Link Audit** — internal vs. external link counts, broken link detection
- **Readability** — Flesch Reading Ease score, word/sentence counts
- **Crawlability** — presence of `sitemap.xml` and `robots.txt`

A composite **SEO score out of 100** aggregates all checks into a single actionable metric.

---

## 🧪 Case Study

### Problem

Running a proper on-page SEO audit is harder than it should be. Developers and content creators
are often stuck choosing between manually digging through page source code or signing up for
costly tools with features they'll never use. There was no simple, fast, self-hostable option
that just works — no account required, no paywalls, no bloat.

### Solution

Build a focused, fast, self-hosted on-page audit tool that runs locally with no external API keys
required. The tool fetches a page, parses its HTML, and runs five independent analyses in parallel,
returning results in a clean, scored dashboard.

### Technical Decisions

| Decision | Rationale |
|---|---|
| **FastAPI** | Async-native Python framework; ideal for concurrent HTTP requests during analysis |
| **BeautifulSoup + lxml** | Fast, reliable HTML parsing with broad compatibility |
| **React + Vite** | Lightweight SPA with instant HMR during development |
| **Tailwind CSS** | Utility-first CSS for rapid, consistent UI construction |
| **textstat** | Pure-Python readability scoring; no external API needed |
| **httpx** | Async HTTP client matching FastAPI's async model |

### Outcomes

- All five analyses run in parallel — full audit completes in ~2–4 seconds
- Modular architecture: each analysis is an independent FastAPI router
- Score algorithm is deterministic and documented, making it easy to extend
- Dark-mode-first UI designed for developer portfolios

---

## 🗂️ File & Folder Structure

```
seo-now-tool/
├── backend/                        # FastAPI Python backend
│   ├── main.py                     # App entry point, CORS, router registration
│   ├── requirements.txt            # Python dependencies
│   ├── .env.example                # Environment variable template
│   ├── api/                        # One router file per analysis module
│   │   ├── __init__.py
│   │   ├── meta.py                 # Meta tags analysis
│   │   ├── keywords.py             # Keyword & heading analysis
│   │   ├── links.py                # Link audit + broken link check
│   │   ├── readability.py          # Flesch / readability scoring
│   │   └── sitemap.py              # Sitemap & robots.txt checker
│   ├── core/                       # Shared business logic
│   │   ├── __init__.py
│   │   ├── scraper.py              # Async HTML fetcher (httpx + BeautifulSoup)
│   │   └── scorer.py               # Composite SEO score calculator
│   ├── utils/                      # Reserved for future helpers
│   └── tests/                      # Reserved for pytest unit tests
│
├── frontend/                       # React + Vite frontend
│   ├── index.html                  # HTML shell with Google Fonts
│   ├── vite.config.js              # Vite config + API proxy
│   ├── tailwind.config.js          # Tailwind theme config
│   ├── postcss.config.js           # PostCSS config
│   ├── package.json                # npm dependencies
│   └── src/
│       ├── main.jsx                # React entry point
│       ├── App.jsx                 # Router + layout shell
│       ├── index.css               # Global CSS variables + Tailwind
│       ├── pages/
│       │   ├── HomePage.jsx        # URL input + hero landing page
│       │   └── ResultsPage.jsx     # Audit results dashboard
│       ├── components/
│       │   ├── Navbar.jsx          # Top navigation bar
│       │   ├── ScoreGauge.jsx      # SVG circular score gauge
│       │   ├── IssuesList.jsx      # Aggregated issues list
│       │   ├── MetaCard.jsx        # Meta tag results card
│       │   ├── KeywordsCard.jsx    # Keywords & headings card
│       │   ├── LinksCard.jsx       # Link audit card
│       │   ├── ReadabilityCard.jsx # Readability metrics card
│       │   └── SitemapCard.jsx     # Crawlability card
│       └── utils/
│           ├── api.js              # Axios API call wrappers
│           └── score.js            # Client-side score calculator
│
├── docs/
│   ├── image1.png                  # Results dashboard screenshot
│   └── image2.png                  # Homepage screenshot
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│          React Frontend             │
│  (Vite + Tailwind + React Router)   │
│                                     │
│  HomePage     →  URL Input          │
│  ResultsPage  →  Dashboard          │
│  Components   →  Cards / Gauge      │
└──────────────┬──────────────────────┘
               │ HTTP POST /api/*
               │ (Vite proxy → localhost:8000)
               ▼
┌─────────────────────────────────────┐
│         FastAPI Backend             │
│                                     │
│  /api/meta         →  meta.py       │
│  /api/keywords     →  keywords.py   │
│  /api/links        →  links.py      │
│  /api/readability  →  readability   │
│  /api/sitemap      →  sitemap.py    │
│                                     │
│  core/scraper.py   ──►  httpx       │
│  core/scorer.py    ──►  scoring     │
└──────────────┬──────────────────────┘
               │
               ▼
       🌐 Target Website
  (fetched via httpx + parsed by BeautifulSoup)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Node.js 18+
- macOS (tested), Linux, or Windows WSL

### 1 — Clone the repository

```bash
git clone https://github.com/Marjory00/seo-now-tool.git
cd seo-now-tool
```

### 2 — Set up the backend

```bash
cd backend

# Create and activate a virtual environment
python3.11 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Start the FastAPI server
uvicorn main:app --reload --port 8000
```

The API will be live at `http://localhost:8000`.  
Interactive docs available at `http://localhost:8000/docs`.

### 3 — Set up the frontend

Open a new terminal tab:

```bash
cd frontend

# Install npm packages
npm install

# Start the Vite dev server
npm run dev
```

The app will be live at `http://localhost:5173`.

---

## 🛠️ VS Code Setup

Recommended extensions for this project:

- **Python** (Microsoft)
- **Pylance**
- **ES7+ React/Redux/React-Native snippets**
- **Tailwind CSS IntelliSense**
- **REST Client**

Recommended workspace settings (`.vscode/settings.json`):

```json
{
  "editor.formatOnSave": true,
  "python.defaultInterpreterPath": "./backend/venv/bin/python",
  "editor.tabSize": 2
}
```

---

## 📡 API Reference

All endpoints accept a `POST` request with JSON body `{ "url": "https://example.com" }`.

| Endpoint | Description |
|---|---|
| `POST /api/meta/analyze` | Meta tags, OG tags, canonical URL |
| `POST /api/keywords/analyze` | Headings, keyword density |
| `POST /api/links/analyze` | Internal / external / broken links |
| `POST /api/readability/analyze` | Flesch score, word count |
| `POST /api/sitemap/analyze` | sitemap.xml and robots.txt check |

---

## 🌐 Deploying to Production

### Backend (Railway, Render, or Fly.io)

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Update the `allow_origins` list in `main.py` to your frontend domain.

### Frontend (Vercel or Netlify)

```bash
npm run build
# Deploy the generated dist/ folder
```

Update `vite.config.js` proxy to point to your deployed backend URL.

---

## 🧰 Languages & Technologies

| Layer | Technology |
|---|---|
| Backend language | Python 3.11 |
| Backend framework | FastAPI |
| HTTP client | httpx (async) |
| HTML parsing | BeautifulSoup4 + lxml |
| Readability scoring | textstat |
| Data validation | Pydantic v2 |
| Frontend language | JavaScript (JSX) |
| Frontend framework | React 18 |
| Build tool | Vite 5 |
| Styling | Tailwind CSS 3 |
| Icons | Lucide React |
| Version control | Git + GitHub |
| IDE | Visual Studio Code |
| Platform | macOS |

---

## 📜 License

Copyright (c) 2024 **Marjory D. Marquez**. All Rights Reserved.

This project is published as part of a personal portfolio. It is **not open source**.  
You may view and study the code, but you may **not** use, distribute, or deploy it
commercially without explicit written permission from the author.

See [LICENSE](./LICENSE) for full terms.

---

## 👤 Author

**Marjory D. Marquez**

- 🌐 GitHub: [@Marjory00](https://github.com/Marjory00)
- 🎨 CodePen: [@Marjory00](https://codepen.io/Marjory00)
---

*Built with ☕ and Python on macOS.*