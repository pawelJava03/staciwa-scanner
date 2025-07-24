from requests import get
from rich.table import Table
import requests

response =  None
def status_code(url):
    response = get(url)
    if response.status_code == 200:
        return f'[green] {response.status_code}'
    else:
        return f'[bold red] {response.status_code}'

#CMS Detection
def detect_cms(url: str) -> str | None:
    response = get(url)
    html = response.text
    if 'wp-content' in html:
        return('WordPress')
    elif 'cdn.shopify.com' in html:
        return('Shopify')
    elif 'Joomla' in html or '/media/system/js/' in html:
        return('Joomla')
    elif 'content=/"Drupal"' in html:
        return('Drupal')
    elif 'cmp-container' in html or 'cmp-text' in html or '/content/' in html:
        return('AEM')
    else:
        return('Unknown/None')

#Framework Detection
def detect_framework(url):
    response = get(url)
    html = response.text
    if 'jquery' in html:
        return('jQuery')
    elif 'bootstrap' in html:
        return('Bootstrap')
    elif 'angular' in html:
        return('Angular')
    elif 'react' in html:
        return('React')
    elif 'vue' in html:
        return('Vue')
    elif '__NEXT_DATA__' in html:
        return('Next.js')
    else:
        return('Unknown/None')

# Security Detection
def detect_security(url):
    response = get(url)
    headers = response.headers

    expected_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Content-Type-Options",
        "X-Frame-Options",
        "X-XSS-Protection",
        "Referrer-Policy",
        "Permissions-Policy"
    ]

    table = Table(show_lines=True)
    table.add_column("Header", style="cyan", justify="left")
    table.add_column("Status", style="green", justify="center")

    for header in expected_headers:
        if header in headers:
            table.add_row(header, "[green]✅ Detected")
        else:
            table.add_row(header, "[bold red]⚠️ Not Found")

    return table

def check_https_redirect(url):

    test_url = url.replace("https://", "http://") if url.startswith("https://") else "http://" + url

    try:
        response = requests.get(test_url, allow_redirects=True, timeout=5)
        if response.url.startswith("https://"):
            return "[green]✅ Site redirects to HTTPS"
        else:
            return "[red]❌ No HTTPS redirect"
    except requests.RequestException:
        return "[yellow]⚠️ Failed to check HTTPS redirect"

def exposed_files(url):
    common_paths = [
        '.env', 'backup.zip', 'phpinfo.php', 'config.php',
        'admin.php', 'wp-config.php', 'wp-content', 'wp-includes', 'wp-admin'
    ]

    findings = []

    for path in common_paths:
        full_url = url.rstrip('/') + '/' + path
        try:
            response = requests.get(full_url, timeout=5)
            if response.status_code == 200 and len(response.text) > 10:
                findings.append(f"[bold red]❌ Exposed file or folder: {path}")
        except requests.RequestException:
            findings.append(f"[yellow]⚠️ Could not check: {path}")

    if not findings:
        findings.append("[green]✅ No exposed files found")

    return findings


def check_cors(url):
    r = requests.get(url, headers={'Origin': 'https://example.com'})
    if r.status_code == 200:
        return "[green]✅ CORS enabled"
    elif r.status_code == 403:
        return "[red]❌ CORS disabled"
    else:
        return "[yellow]⚠️ Failed to check CORS"
