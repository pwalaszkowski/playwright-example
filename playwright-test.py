import datetime
import platform
from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    start_time = datetime.datetime.now()

    # Go to https://www.wikipedia.org/
    page.goto("https://www.wikipedia.org/")

    # Click input[name="search"]
    page.locator("input[name=\"search\"]").click()

    # Fill input[name="search"]
    page.locator("input[name=\"search\"]").fill("Boeing")

    # Click button:has-text("Search")
    page.locator("button:has-text(\"Search\")").click()

    # Click #Further_reading
    page.locator("#Further_reading").click()

    end_time = datetime.datetime.now()
    # ---------------------
    context.close()
    browser.close()

    print('Duration: {} [seconds]'.format(end_time - start_time))


def main():
    with sync_playwright() as playwright:
        run(playwright)


print(platform.system())  # e.g. Windows, Linux, Darwin
print(platform.architecture())  # e.g. 64-bit
print(platform.machine())  # e.g. x86_64
print(platform.node())  # Hostname
print(platform.processor())  # e.g. i386
main()
