from GooglePage import SearchHelper


def test_google_search(browser):
    google_main_page = SearchHelper(browser)
    google_main_page.go_to_site()
    query_text = "QA Automation"
    google_main_page.text_input_and_search(query_text)
    assert query_text in browser.title
    google_main_page.assert_text_in_search_result(query_text)
