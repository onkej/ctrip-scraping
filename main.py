from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
from scroll import scroll_down
from comment import parse, write_csv


base_url = "https://m.ctrip.com/webapp/you/commentWeb/\
    commentList?businessId={}&businessType=sight"

# sight_name: sight_id, # sight_comment_count
ids = {
    # "五指山": 3211, # 79
    # "尖峰岭": 3233, # 81
    # "呀诺达": 55820, # 13760
    # "水满河": 110178, # 1903
    # "七仙岭": 145186, # 1288
    # "霸王岭": 1730760, # 127
    # "霸王岭_白石潭": 143748445, # 1
    # "霸王岭_雅加": 143727908,  # 8
    # "鹦哥岭": 145248513, # 0
    "黎母山": 18195, # 17
    # "吊罗山": 21835, # 164
    # "三江源_chindu": 50054, # 28
    # "三江源_madoi1": 4575908, # 8
    # "三江源_madoi2": 5718131, # 8
    # "三江源_zadoi": 145694557, 
    # "三江源_qumarleb": 145572672,
    # "大熊猫": 145412216,
    # "武夷山": 126481, 
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
