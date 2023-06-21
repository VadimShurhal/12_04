import time


def test_run(playwright):
    browser = playwright.chromium.launch(headless=False, devtools=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://github.com/")
    page.get_by_role("link", name="Sign in").click()
    time.sleep(4)
    page.get_by_label("Username or email address").fill("karpovolegggg@gmail.com")
    page.get_by_label("Password").fill("Hillel2023!")
    page.get_by_role("button", name="Sign in").click()

    page.get_by_role("link", name="New").click()
    page.get_by_role("textbox", name="Repository").fill("Playwright_repo")
    page.get_by_test_id("description").fill("Description for playwriht repo")
    page.get_by_label("Add a README file").check()
    page.get_by_role("button", name="Create repository").click()

    context.close()
    browser.close()
