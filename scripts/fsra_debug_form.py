"""Quick debug — find all form elements and try submitting."""
import time
from playwright.sync_api import sync_playwright

BASE_URL = "https://alias2a.fsco.gov.on.ca/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
    page = browser.new_context(viewport={"width": 1280, "height": 900}).new_page()

    page.goto(BASE_URL, wait_until="networkidle", timeout=30000)
    print(f"Title: {page.title()}")
    print(f"URL: {page.url}")

    # Dump ALL form elements
    form_info = page.evaluate("""
        () => {
            const els = document.querySelectorAll('input, select, button, a, form');
            return Array.from(els).map(el => ({
                tag: el.tagName,
                id: el.id,
                name: el.name,
                type: el.type || '',
                value: el.value ? el.value.substring(0,40) : '',
                text: el.innerText ? el.innerText.trim().substring(0,40) : '',
                visible: el.offsetParent !== null,
                href: el.href || ''
            }));
        }
    """)
    print(f"\nAll form elements ({len(form_info)} total):")
    for el in form_info:
        if el['visible'] or el['tag'] in ['INPUT','BUTTON','SELECT']:
            print(f"  {el['tag']:<8} id={el['id']:<20} name={el['name']:<20} type={el['type']:<10} value='{el['value']}' text='{el['text']}'")

    # Fill city
    page.evaluate("""
        () => {
            const inputs = document.querySelectorAll('input[type=text], input:not([type])');
            inputs.forEach(i => { if (i.offsetParent !== null) i.value = 'Peterborough'; });
        }
    """)
    print("\nFilled city fields")

    # Screenshot before submit
    page.screenshot(path="/home/maximus/.openclaw/workspace/scripts/before_submit.png")
    print("Screenshot: before_submit.png")

    # Try clicking all submit-like elements and see what changes URL
    submits = page.evaluate("""
        () => {
            const els = document.querySelectorAll('input[type=submit], button[type=submit], input[type=button]');
            return Array.from(els).map(el => ({
                tag: el.tagName, id: el.id, value: el.value, text: el.innerText
            }));
        }
    """)
    print(f"\nSubmit buttons: {submits}")

    # Try clicking first submit
    if submits:
        btn_id = submits[0]['id']
        print(f"Clicking #{btn_id}...")
        try:
            with page.expect_navigation(wait_until="networkidle", timeout=15000):
                page.click(f"#{btn_id}" if btn_id else "input[type=submit]")
            print(f"After click URL: {page.url}")
        except Exception as e:
            print(f"Navigation error: {e}")
            page.wait_for_load_state("networkidle", timeout=10000)
            print(f"After wait URL: {page.url}")

    page.screenshot(path="/home/maximus/.openclaw/workspace/scripts/after_submit.png")
    print("Screenshot: after_submit.png")
    print(f"Rows after submit: {page.evaluate('() => document.querySelectorAll(\"table tr\").length')}")

    browser.close()
