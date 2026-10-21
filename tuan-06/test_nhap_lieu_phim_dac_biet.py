"""
Học phần: Kiểm thử phần mềm - Thực hành kiểm thử tự động
Tuần 6: Báo cáo chuyên đề tài liệu + Chức năng 1 (Nhóm W1)
Chức năng: Nhập liệu & phím đặc biệt
Trang kiểm thử:
  - https://the-internet.herokuapp.com/key_presses
  - https://the-internet.herokuapp.com/inputs

Các hàm và phương thức bắt buộc sử dụng theo phân công:
  - get, find_element, By.ID, send_keys, Keys.ENTER, Keys.TAB, Keys.ARROW_UP,
    clear, get_attribute, text, unittest.TestCase, setUp, tearDown
"""

import os
import unittest
from typing import Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Đường dẫn URL và hằng số cấu hình
BASE_URL = "https://the-internet.herokuapp.com"
URL_KEY_PRESSES = f"{BASE_URL}/key_presses"
URL_INPUTS = f"{BASE_URL}/inputs"

# Định danh phần tử (Locators theo By.ID)
ID_TARGET_INPUT = "target"
ID_RESULT_TEXT = "result"

# Kết quả mong đợi cho trang Key Presses
EXPECTED_RESULT_ENTER = "You entered: ENTER"
EXPECTED_RESULT_TAB = "You entered: TAB"
EXPECTED_RESULT_ARROW_UP = "You entered: UP"

# Dữ liệu kiểm thử cho trang Inputs
INPUT_NUMBER_VALUE = "50"
EXPECTED_INCREMENTED_VALUE = "51"
EMPTY_STRING_VALUE = ""
EXPECTED_INPUT_TYPE = "number"

# Thư mục lưu ảnh chụp màn hình minh chứng
OUTPUT_IMAGE_DIR = os.path.join(os.path.dirname(__file__), "anh")


class TestNhapLieuVaPhimDacBiet(unittest.TestCase):
    """
    Bộ kiểm thử cho chức năng Nhập liệu & phím đặc biệt (Tuần 6 - Nhóm W1).
    Kế thừa từ unittest.TestCase theo đúng tài liệu Selenium Python (mục 2.3 & 2.4).
    """

    driver: Optional[webdriver.Chrome] = None

    @classmethod
    def setUpClass(cls) -> None:
        """
        Khởi tạo trình duyệt một lần cho toàn bộ test suite để tối ưu hiệu năng
        và tránh khởi động lại trình duyệt nhiều lần gây nghẽn phiên mạng.
        """
        os.makedirs(OUTPUT_IMAGE_DIR, exist_ok=True)

        chrome_options = Options()
        if os.environ.get("HEADLESS", "true").lower() == "true":
            chrome_options.add_argument("--headless=new")

        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1280,800")
        chrome_options.page_load_strategy = "eager"

        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Đóng trình duyệt sau khi hoàn thành toàn bộ các ca kiểm thử trong lớp.
        """
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None

    def setUp(self) -> None:
        """
        Phương thức setUp: Chạy trước mỗi ca kiểm thử (theo yêu cầu bắt buộc môn học).
        Đảm bảo phiên WebDriver luôn sẵn sàng trước khi thực thi ca kiểm thử.
        """
        self.assertIsNotNone(
            self.driver,
            "WebDriver chưa được khởi tạo thành công."
        )

    def tearDown(self) -> None:
        """
        Phương thức tearDown: Chạy sau mỗi ca kiểm thử (theo yêu cầu bắt buộc môn học).
        Dọn dẹp trạng thái giữa các ca kiểm thử.
        """
        # Đã hoàn thành ghi nhận kết quả và lưu ảnh của ca kiểm thử hiện tại
        pass

    def test_01_key_presses_enter(self) -> None:
        """
        TC01: Kiểm tra gõ phím đặc biệt ENTER trên trang /key_presses.
        Sử dụng: get, find_element, By.ID, send_keys, Keys.ENTER, text.
        """
        assert self.driver is not None
        # 1. Điều hướng đến trang kiểm thử bằng hàm get
        self.driver.get(URL_KEY_PRESSES)

        # 2. Tìm ô nhập liệu bằng By.ID
        target_input = self.driver.find_element(By.ID, ID_TARGET_INPUT)

        # Ngăn form HTML tự reload để kiểm tra phản hồi tức thời của trang
        prevent_submit_script = (
            "document.querySelector('form').onsubmit = function(e){ "
            "e.preventDefault(); return false; };"
        )
        self.driver.execute_script(prevent_submit_script)

        # 3. Gửi phím đặc biệt ENTER vào ô input bằng send_keys và Keys.ENTER
        target_input.send_keys(Keys.ENTER)

        # 4. Tìm phần tử kết quả bằng By.ID và trích xuất nội dung văn bản bằng thuộc tính .text
        result_element = self.driver.find_element(By.ID, ID_RESULT_TEXT)
        actual_text = result_element.text

        # 5. Xác minh kết quả hiển thị khớp với thông báo mong đợi
        self.assertEqual(
            actual_text,
            EXPECTED_RESULT_ENTER,
            f"Thông báo hiển thị không đúng: kỳ vọng '{EXPECTED_RESULT_ENTER}', thực tế '{actual_text}'"
        )

        # 6. Chụp ảnh màn hình minh chứng
        screenshot_path = os.path.join(OUTPUT_IMAGE_DIR, "tc01_key_presses_enter.png")
        self.driver.save_screenshot(screenshot_path)

    def test_02_key_presses_tab(self) -> None:
        """
        TC02: Kiểm tra gõ phím đặc biệt TAB trên trang /key_presses.
        Sử dụng: get, find_element, By.ID, send_keys, Keys.TAB, text.
        """
        assert self.driver is not None
        # 1. Mở trang key_presses bằng get
        self.driver.get(URL_KEY_PRESSES)

        # 2. Định vị ô input target bằng By.ID
        target_input = self.driver.find_element(By.ID, ID_TARGET_INPUT)

        # 3. Gửi phím TAB vào ô input bằng Keys.TAB
        target_input.send_keys(Keys.TAB)

        # 4. Đọc kết quả hiển thị thông qua thuộc tính .text
        result_element = self.driver.find_element(By.ID, ID_RESULT_TEXT)
        actual_text = result_element.text

        # 5. So sánh kết quả
        self.assertEqual(
            actual_text,
            EXPECTED_RESULT_TAB,
            f"Thông báo hiển thị không đúng: kỳ vọng '{EXPECTED_RESULT_TAB}', thực tế '{actual_text}'"
        )

        # 6. Chụp ảnh minh chứng
        screenshot_path = os.path.join(OUTPUT_IMAGE_DIR, "tc02_key_presses_tab.png")
        self.driver.save_screenshot(screenshot_path)

    def test_03_key_presses_arrow_up(self) -> None:
        """
        TC03: Kiểm tra gõ phím đặc biệt ARROW_UP (mũi tên lên) trên trang /key_presses.
        Sử dụng: get, find_element, By.ID, send_keys, Keys.ARROW_UP, text.
        """
        assert self.driver is not None
        # 1. Điều hướng đến trang bằng hàm get
        self.driver.get(URL_KEY_PRESSES)

        # 2. Tìm ô nhập bằng By.ID
        target_input = self.driver.find_element(By.ID, ID_TARGET_INPUT)

        # 3. Gửi phím mũi tên lên bằng Keys.ARROW_UP
        target_input.send_keys(Keys.ARROW_UP)

        # 4. Lấy text kết quả từ phần tử By.ID
        result_element = self.driver.find_element(By.ID, ID_RESULT_TEXT)
        actual_text = result_element.text

        # 5. Khẳng định kết quả
        self.assertEqual(
            actual_text,
            EXPECTED_RESULT_ARROW_UP,
            f"Thông báo hiển thị không đúng: kỳ vọng '{EXPECTED_RESULT_ARROW_UP}', thực tế '{actual_text}'"
        )

        # 6. Chụp ảnh minh chứng
        screenshot_path = os.path.join(OUTPUT_IMAGE_DIR, "tc03_key_presses_arrow_up.png")
        self.driver.save_screenshot(screenshot_path)

    def test_04_inputs_send_keys_and_get_attribute(self) -> None:
        """
        TC04: Kiểm tra nhập dữ liệu số và lấy giá trị thuộc tính trên trang /inputs.
        Sử dụng: get, find_element, send_keys, get_attribute.
        """
        assert self.driver is not None
        # 1. Mở trang inputs bằng hàm get
        self.driver.get(URL_INPUTS)

        # 2. Tìm phần tử input số bằng selector CSS
        number_input = self.driver.find_element(By.CSS_SELECTOR, ".example input")

        # 3. Kiểm tra kiểu của ô nhập bằng get_attribute('type')
        input_type = number_input.get_attribute("type")
        self.assertEqual(input_type, EXPECTED_INPUT_TYPE, "Kiểu trường dữ liệu không phải dạng number")

        # 4. Nhập dữ liệu số vào ô input bằng hàm send_keys
        number_input.send_keys(INPUT_NUMBER_VALUE)

        # 5. Đọc giá trị thực tế của ô input bằng get_attribute('value')
        actual_value = number_input.get_attribute("value")

        # 6. Xác nhận giá trị đã nhập hiển thị chính xác
        self.assertEqual(
            actual_value,
            INPUT_NUMBER_VALUE,
            f"Giá trị ô input không khớp: kỳ vọng '{INPUT_NUMBER_VALUE}', thực tế '{actual_value}'"
        )

        # 7. Chụp ảnh minh chứng
        screenshot_path = os.path.join(OUTPUT_IMAGE_DIR, "tc04_inputs_send_keys.png")
        self.driver.save_screenshot(screenshot_path)

    def test_05_inputs_arrow_up_increment(self) -> None:
        """
        TC05: Kiểm tra dùng phím ARROW_UP để tăng giá trị số trong ô input.
        Sử dụng: get, find_element, send_keys, Keys.ARROW_UP, get_attribute.
        """
        assert self.driver is not None
        # 1. Mở trang inputs
        self.driver.get(URL_INPUTS)

        # 2. Tìm ô input
        number_input = self.driver.find_element(By.CSS_SELECTOR, ".example input")

        # 3. Nhập giá trị khởi đầu
        number_input.send_keys(INPUT_NUMBER_VALUE)

        # 4. Nhấn phím ARROW_UP để tăng giá trị lên 1 đơn vị
        number_input.send_keys(Keys.ARROW_UP)

        # 5. Đọc lại giá trị qua get_attribute('value')
        updated_value = number_input.get_attribute("value")

        # 6. Kiểm tra giá trị đã được tăng từ 50 lên 51
        self.assertEqual(
            updated_value,
            EXPECTED_INCREMENTED_VALUE,
            f"Giá trị sau khi bấm phím lên không đúng: kỳ vọng '{EXPECTED_INCREMENTED_VALUE}', thực tế '{updated_value}'"
        )

        # 7. Chụp ảnh minh chứng
        screenshot_path = os.path.join(OUTPUT_IMAGE_DIR, "tc05_inputs_arrow_up_increment.png")
        self.driver.save_screenshot(screenshot_path)

    def test_06_inputs_clear(self) -> None:
        """
        TC06: Kiểm tra xoá nội dung trong ô nhập bằng hàm clear().
        Sử dụng: get, find_element, send_keys, clear, get_attribute.
        """
        assert self.driver is not None
        # 1. Mở trang inputs
        self.driver.get(URL_INPUTS)

        # 2. Tìm ô input
        number_input = self.driver.find_element(By.CSS_SELECTOR, ".example input")

        # 3. Nhập dữ liệu ban đầu
        number_input.send_keys(INPUT_NUMBER_VALUE)
        self.assertEqual(number_input.get_attribute("value"), INPUT_NUMBER_VALUE)

        # 4. Sử dụng hàm clear để làm trống ô input
        number_input.clear()

        # 5. Kiểm tra giá trị đã trở về chuỗi rỗng
        cleared_value = number_input.get_attribute("value")
        self.assertEqual(
            cleared_value,
            EMPTY_STRING_VALUE,
            f"Ô input chưa được xoá sạch: thực tế vẫn còn '{cleared_value}'"
        )

        # 6. Chụp ảnh minh chứng
        screenshot_path = os.path.join(OUTPUT_IMAGE_DIR, "tc06_inputs_clear.png")
        self.driver.save_screenshot(screenshot_path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
