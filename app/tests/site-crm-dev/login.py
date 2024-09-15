import re
from playwright.sync_api import Page, expect
from app.tests.record import record


def test_example(page: Page) -> None:
    page.goto("https://dev-crm01.ape11.com.br/")
    page.get_by_placeholder("email ou usuário").click()
    page.get_by_placeholder("email ou usuário").fill("douglas.ape11")
    page.get_by_placeholder("email ou usuário").press("Tab")
    page.get_by_placeholder("senha").fill("douglas123")
    page.get_by_role("button", name="Entrar").click()
    page.locator("#module-userActions").get_by_role("link").nth(2).click()
    
record(test_example)
