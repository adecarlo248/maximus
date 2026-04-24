"""Debug: find all links after search."""
import time
from playwright.sync_api import sync_playwright

BASE_URL  = "https://alias2a.fsco.gov.on.ca/"
CITY_ID   = "MainPlaceHolder_Content4_aliascity"
SEARCH_ID = "MainPlaceHolder_Content4_srButton"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
    page = browser.new_context(viewport={"width": 1280, "height": 900}).new_page()

    page.goto(BASE_URL, wait_until="networkidle", timeout=30000)
    page.fill(f"#{CITY_ID}", "Peterborough")
    page.click(f"#{SEARCH_ID}")

    # Wait a few seconds for postback
    time.sleep(4)

    print(f"URL after search: {page.url}")
    print(f"Total <a> tags: {page.evaluate('() => document.querySelectorAll(\"a\").length')}")

    # Dump all links
    links = page.evaluate("""
        () => Array.from(document.querySelectorAll('a')).map(a => ({
            text: a.innerText.trim().substring(0, 40),
            href: a.href.substring(0, 80)
        })).filter(a => a.href || a.text)
    """)

    print("\nAll links:")
    for lnk in links:
        print(f"  text='{lnk['text']}'  href='{lnk['href']}'")

    # Also check page text snippet
    body = page.inner_text("body")
    print(f"\nBody snippet (first 500 chars):\n{body[:500]}")

    page.screenshot(path="/home/maximus/.openclaw/workspace/scripts/fsra_after_search.png")
    print("\nScreenshot saved: fsra_after_search.png")
    browser.close()
