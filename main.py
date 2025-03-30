from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
from scroll import scroll_down
from comment import parse, write_csv


base_url = "https://m.ctrip.com/webapp/you/commentWeb/commentList?businessId={}&businessType=sight"
ids = {
    # "武夷山": 126481,
    # "五指山": 3211,
    "尖峰岭": 3233,
    # "呀诺达": 55820,
    # "水满河": 110178,
    # "七仙岭": 145186,
    # "大熊猫": 145412216,
}
urls = {sight: base_url.format(i) for sight, i in ids.items()}

# homepage = "https://m.ctrip.com/webapp/you/sight/981/{}.html" 
# homepages = {sight: homepage.format(i) for sight, i in ids.items()}


with sync_playwright() as p:
    iphone_13 = p.devices['iPhone 13']
    browser = p.webkit.launch(headless=False)
    context = browser.new_context(**iphone_13,)
    page = context.new_page()
    page.set_default_navigation_timeout(0)
    
    for sight, url in urls.items():
        print(f"Visiting {sight} homepage...")
        # manually scroll down
        html = scroll_down(page, url)
        results = list(parse(HTMLParser(html)))
        write_csv(sight, results)
        print(f"Extracted {len(results)} comments.")

    context.close()
    browser.close()
