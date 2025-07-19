import pytest


@pytest.mark.tc_id("TC_02.001_06")
@pytest.mark.parametrize("new_item_page_and_name", ["duplicate"], indirect=True)
def test_duplicate_item_name(new_item_page_and_name):
    item_page, _ = new_item_page_and_name
    error_text = item_page.error_message_text()

    assert error_text is not None, "Expected an error message, but got None"
    assert "A job already exists with the name" in error_text, f"Unexpected error text: {error_text}"
    assert item_page.is_ok_button_disabled(), "OK button should be disabled for duplicate item"
