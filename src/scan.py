from requests import get
from rich.table import Table

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

    table = Table(title="Security Headers Report", show_lines=True)
    table.add_column("Header", style="cyan", justify="left")
    table.add_column("Status", style="green", justify="center")

    for header in expected_headers:
        if header in headers:
            table.add_row(header, "[green]✅ Detected")
        else:
            table.add_row(header, "[bold red]⚠️ Not Found")

    return table
