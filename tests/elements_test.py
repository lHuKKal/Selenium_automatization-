import time
import pytest
from pages.base_page import BasePage
from pages.element_page import TextBoxPage, CheckBoxPage, RadioButtonPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_per_adr = text_box_page.check_filled_form()

            assert full_name == output_name, "the full name don't match"
            assert email == output_email, "the email don't match"
            assert current_address == output_current_address, "the current address don't match"
            assert permanent_address == output_per_adr, "the permanent address don't match"

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list_checkbox()
            check_box_page.click_random_checkbox()
            input_check_box = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print("Selected check boxes " + str(input_check_box))
            print("Output " + str(output_result))
            assert input_check_box == output_result, "checkboxes has not been selected"

    class TestRadioButtons:

        def test_radio_button_click(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()

            radio_button_page.click_radio_button("yes")
            output_radio_button_yes = radio_button_page.get_result_radio_button()
            assert 'Yes' == output_radio_button_yes, "YES radio button is not selected"

            radio_button_page.click_radio_button("impressive")
            output_radio_button_impressive = radio_button_page.get_result_radio_button()
            assert 'Impressive' == output_radio_button_impressive, "IMPRESSIVE radio button is not selected"

            input_radio_button_no = radio_button_page.click_radio_button("no")
            output_radio_button_no = radio_button_page.get_result_radio_button()
            assert "No" != output_radio_button_no, "There is bug"
