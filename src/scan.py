from requests import get
response =  None
def status_code(url):
    response = get(url)
    return response.status_code

#CMS Detection
def detect_cms(url):
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
