from playwright.sync_api import sync_playwright

def record(test):
    with sync_playwright() as p:
        browser = p.firefox.launch()

        context = browser.new_context(record_video_dir='midia')

        page = context.new_page()

        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        test(page)

        context.tracing.stop(path="trace.zip")

        page.close()
        context.close()
        browser.close()