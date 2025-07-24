# staciwa-scan

A lightweight CLI tool for website scanning: HTTP status, CMS/framework detection, security headers, CORS policy, exposed files, HTTPS redirect check, and a Lighthouse report (Performance, SEO, Accessibility, Best Practices) displayed in a Rich table.

---

## 🔧 Requirements

- Python ≥ 3.7
- Google PageSpeed Insights API key (for Lighthouse module)
- Installable via pip:

  ```bash
  pip install staciwa-scan
🚀 Installation
Install the package:

bash

pip install staciwa-scan
Set up your API key
Create a .env file in your project or home directory with:

dotenv

LIGHTHOUSE_API_KEY=your_google_pagespeed_api_key
💻 Usage
bash
Kopiuj
Edytuj
staciwa-scan scan <URL>
Example
bash

$ staciwa-scan scan https://example.com
🔍 Scanning https://example.com...

Status code: 200
Detected CMS: WordPress
Detected Framework: React
🛡️ Security headers OK
Detected CORS: ✓ permissive
🔍 Detected Files:
  • /wp-admin/
  • /readme.html
🔒 HTTPS redirect: https://example.com

┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ Category              ┃ Score   ┃
┡━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━┩
│ Performance           │ 85 / 100 │
│ SEO                   │ 92 / 100 │
│ Accessibility         │ 78 / 100 │
│ Best Practices        │ 90 / 100 │
└───────────────────────┴─────────┘
⚙️ Configuration
Timeouts & Retries
You can adjust default timeout and retry settings in scan.py to suit your environment.

Logging
rich supports multiple output styles—modify Console() in cli.py if you want to log to a file or change verbosity.

🛠️ Development & Contributing
Fork the repository

Create a feature branch: git checkout -b feature/your-feature

Implement your changes and add tests (using pytest)

Submit a Pull Request to main

After review and merge, a GitHub Actions workflow will publish a new release to PyPI

📄 License
MIT License © 2025 Paweł Staciwa
See LICENSE for details.

Happy scanning! 🚀
