from playwright.sync_api import Page

def scroll_down(page: Page, url): # -> html(str)
    # """Scroll down the page until all comments are loaded"""
    page.goto(url)
    page.wait_for_load_state("networkidle")

    # manual scrolling xD
    input("Manually scroll to the bottom, then press `Enter` to continue...")

    # maximum comment count after srolling
    comment_count = page.locator("div.list_wrap > div.list_item").count() 
    print(f"Total comments loaded: {comment_count}")

    return page.locator("div.list_wrap").inner_html() 
