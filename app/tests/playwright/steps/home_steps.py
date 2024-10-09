import pytest
import json
from playwright.sync_api import sync_playwright
from pytest_bdd import scenarios, given, then, parsers

# Importar cenários do arquivo .feature
scenarios('features/site1.feature')

# Carregar dados do arquivo JSON
with open('test_data.json') as f:
    test_data = json.load(f)

@given(parsers.parse('I open the page "{url}"'))
def open_page(url, page):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        return page

@then(parsers.parse('I should see the title "{expected_title}"'))
def check_page_title(expected_title, page):
    assert page.title() == expected_title
    page.close()
