from selene import browser, by, be, have


def test_selene():
    browser.open_url('https://google.com/ncr')
    browser.element(by.name('q')).should(be.blank)\
        .type('selenium').press_enter()
    browser.all('#rso>div').should(have.size(4))\
        .first.should(have.text('Selenium automates browsers'))

