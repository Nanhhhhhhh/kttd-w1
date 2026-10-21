---
marp: true
theme: uncover
class: invert
paginate: true
header: 'Học phần: Kiểm thử phần mềm – Thực hành kiểm thử tự động | Team W1'
footer: 'Tuần 6: Báo cáo Chuyên đề Tài liệu + Chức năng 1 (15 Phút)'
style: |
  section {
    font-family: 'SF Pro Display', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    background: #0f172a;
    color: #f8fafc;
    text-align: left;
    padding: 40px 60px;
    font-size: 24px;
  }
  h1 {
    color: #38bdf8;
    font-size: 42px;
    margin-bottom: 15px;
  }
  h2 {
    color: #38bdf8;
    font-size: 32px;
    border-bottom: 2px solid #334155;
    padding-bottom: 10px;
  }
  h3 {
    color: #93c5fd;
    font-size: 26px;
  }
  table {
    font-size: 19px;
    width: 100%;
    border-collapse: collapse;
    margin-top: 15px;
  }
  th {
    background-color: #1e293b;
    color: #38bdf8;
    padding: 10px;
    border: 1px solid #334155;
  }
  td {
    padding: 8px 12px;
    border: 1px solid #334155;
    background-color: #0f172a;
  }
  code {
    background: #1e293b;
    color: #f43f5e;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
  }
  pre {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 14px;
    font-size: 18px;
  }
  pre code {
    background: transparent;
    color: #e2e8f0;
    padding: 0;
  }
  .highlight {
    color: #fbbf24;
    font-weight: bold;
  }
  .tag {
    display: inline-block;
    padding: 2px 8px;
    background: #0284c7;
    color: white;
    border-radius: 4px;
    font-size: 14px;
    font-weight: 600;
  }
---

<!-- _class: invert lead -->
# KIỂM THỬ PHẦN MỀM TỰ ĐỘNG
## BÁO CÁO TUẦN 06: CHUYÊN ĐỀ TÀI LIỆU & CHỨC NĂNG 1

**Nhóm: W1 (Web Testing Team 1)**  
**Chủ đề:** Nhập liệu & Phím đặc biệt (*Inputs & Special Keys*)  
**Đối tượng kiểm thử:** `the-internet.herokuapp.com` (`/key_presses`, `/inputs`)  
**Thành viên thực hiện:** Đoàn Nam Anh (Trưởng nhóm & Kỹ sư kiểm thử)  
**Thời lượng báo cáo:** 15 phút

---

## 📋 NỘI DUNG BÁO CÁO (15 PHÚT)

1. **Phần 1: Quy trình làm việc nhóm trên GitHub (2 phút)**
   - Mô hình phân nhánh Git, Quản lý tiến độ bằng Issue & Pull Request.
2. **Phần 2: Tóm tắt chuyên đề tài liệu Selenium-Python (6 phút)**
   - Mục 2.1 – 2.4: Cấu trúc cơ bản & `unittest.TestCase`.
   - Mục 3.1 & 7.20: Tương tác với trang & đối tượng `WebElement`.
   - Mục 4.1 & 7.4: Bộ định vị `By.ID` & Phím đặc biệt (`Keys`).
3. **Phần 3: Thiết kế Test Cases & Triển khai Mã nguồn (4 phút)**
   - Kịch bản kiểm thử trên trang `/key_presses` và `/inputs`.
   - Áp dụng đầy đủ 13 hàm/phương thức bắt buộc theo phân công.
4. **Phần 4: Báo cáo kết quả chạy kiểm thử & Minh chứng (2 phút)**
   - Kết quả thực thi `pytest` (100% Passed), Báo cáo HTML & Ảnh chụp.
5. **Phần 5: Kết luận & Hỏi đáp (1 phút)**

---

## 🌳 QUY TRÌNH LÀM VIỆC NHÓM TRÊN GITHUB

Mô hình phân nhánh chuẩn mực tuân thủ hướng dẫn thực hành:

* **Nhánh `main`:** Lưu trữ bản phát hành ổn định, bảo vệ không push trực tiếp.
* **Nhánh `week-06`:** Nhánh tích hợp chung của tuần, tạo từ `main`.
* **Nhánh tính năng thành viên (`t06-*`):**
  - `t06-testcases`: Soạn kịch bản và tài liệu kiểm thử.
  - `t06-keypresses`: Phát triển mã kiểm thử trang `/key_presses`.
  - `t06-inputs`: Phát triển mã kiểm thử trang `/inputs`.
  - `t06-slide-report`: Chạy tổng hợp, chụp ảnh minh chứng và soạn slide.
* **Quản trị qua GitHub:**
  - Milestone: `Tuần 6 - Nhập liệu & phím đặc biệt`.
  - Quy trình PR: Mở PR vào `week-06` với cú pháp `Closes #<id>`, Reviewer duyệt trước khi Merge.
  - Kết tuần: Gộp `week-06` vào `main` qua Pull Request chính.

---

## 📚 TÀI LIỆU SELENIUM: CẤU TRÚC TEST VỚI UNITTEST (MỤC 2.1 – 2.4)

Mục 2.3 & 2.4 chỉ dẫn cách xây dựng bộ kiểm thử hướng đối tượng với thư viện chuẩn `unittest`:

```python
import unittest
from selenium import webdriver

class TestW1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Khởi tạo trình duyệt dùng chung tối ưu hiệu năng
        cls.driver = webdriver.Chrome(options=options)

    def setUp(self):
        # Hàm chạy trước mỗi ca kiểm thử (bắt buộc)
        self.assertIsNotNone(self.driver)

    def tearDown(self):
        # Hàm dọn dẹp sau mỗi ca kiểm thử (bắt buộc)
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
```

* **`setUp()` / `tearDown()`:** Đảm bảo tính độc lập và sạch sẽ giữa các bài kiểm thử.

---

## 🎯 TƯƠNG TÁC VỚI TRANG & WEBELEMENT (MỤC 3.1 & 7.20)

* **`get(url)`:** Điều hướng trình duyệt tới URL mục tiêu:
  ```python
  self.driver.get("https://the-internet.herokuapp.com/inputs")
  ```
* **`find_element(by, value)`:** Tìm kiếm phần tử đầu tiên trên cây DOM khớp điều kiện:
  ```python
  elem = self.driver.find_element(By.ID, "target")
  ```
* **Thuộc tính & phương thức cốt lõi của `WebElement`:**
  - `.send_keys(*value)`: Gửi chuỗi ký tự hoặc phím chức năng vào trường nhập.
  - `.clear()`: Xoá sạch toàn bộ nội dung hiện tại của ô nhập liệu (`<input>`).
  - `.get_attribute(name)`: Trích xuất thuộc tính HTML động (ví dụ `type`, `value`).
  - `.text`: Lấy chuỗi văn bản hiển thị (visible inner text) của phần tử.

---

## ⌨️ BỘ ĐỊNH VỊ BY ID & PHÍM ĐẶC BIỆT (MỤC 4.1 & 7.4)

* **Bộ định vị `By.ID`:**
  - Cách định vị nhanh nhất và đáng tin cậy nhất trong Selenium nhờ phương thức `document.getElementById` của trình duyệt.
  - Cú pháp: `driver.find_element(By.ID, "result")`.
* **Lớp `Keys` (Phím đặc biệt):**
  - Mô phỏng các phím không phải ký tự chữ thông thường trên bàn phím:
    * `Keys.ENTER`: Phím Enter / Return.
    * `Keys.TAB`: Phím chuyển tiêu điểm Tab.
    * `Keys.ARROW_UP`: Phím điều hướng mũi tên lên (dùng tăng giá trị số hoặc phím tắt).
  - Cú pháp kết hợp:
    ```python
    target_input.send_keys(Keys.ENTER)
    number_input.send_keys(Keys.ARROW_UP)
    ```

---

## 📝 BẢNG THIẾT KẾ KỊCH BẢN KIỂM THỬ (TEST CASES)

| Mã TC | Tên ca kiểm thử | Trang kiểm thử | Thao tác chính | Dữ liệu đầu vào | Kỳ vọng |
| :---: | :--- | :---: | :--- | :--- | :--- |
| **TC01** | Kiểm tra gõ phím ENTER | `/key_presses` | `send_keys(Keys.ENTER)` | `Keys.ENTER` | Text là `"You entered: ENTER"` |
| **TC02** | Kiểm tra gõ phím TAB | `/key_presses` | `send_keys(Keys.TAB)` | `Keys.TAB` | Text là `"You entered: TAB"` |
| **TC03** | Kiểm tra phím ARROW_UP | `/key_presses` | `send_keys(Keys.ARROW_UP)` | `Keys.ARROW_UP` | Text là `"You entered: UP"` |
| **TC04** | Kiểm tra nhập số & thuộc tính | `/inputs` | `send_keys("50")` + `get_attribute` | `"50"` | Type=`"number"`, Value=`"50"` |
| **TC05** | Kiểm tra tăng số bằng phím lên | `/inputs` | Nhập `"50"` + `Keys.ARROW_UP` | `Keys.ARROW_UP` | Value tăng thành `"51"` |
| **TC06** | Kiểm tra xoá dữ liệu ô nhập | `/inputs` | Gọi hàm `clear()` | `clear()` | Value trở về rỗng `""` |

---

## 💻 TRIỂN KHAI CODE: TRANG KEY PRESSES

```python
def test_01_key_presses_enter(self) -> None:
    # 1. Mở trang bằng get
    self.driver.get("https://the-internet.herokuapp.com/key_presses")
    
    # 2. Định vị phần tử theo By.ID
    target_input = self.driver.find_element(By.ID, "target")
    
    # Chặn reload form tự nhiên để kiểm tra kết quả tức thì
    self.driver.execute_script("document.querySelector('form').onsubmit = function(e){ e.preventDefault(); return false; };")
    
    # 3. Gửi phím ENTER bằng send_keys
    target_input.send_keys(Keys.ENTER)
    
    # 4. Kiểm tra nội dung text từ kết quả By.ID
    result = self.driver.find_element(By.ID, "result")
    self.assertEqual(result.text, "You entered: ENTER")
    self.driver.save_screenshot("tuan-06/anh/tc01_key_presses_enter.png")
```

---

## 💻 TRIỂN KHAI CODE: TRANG INPUTS

```python
def test_04_inputs_send_keys_and_get_attribute(self) -> None:
    self.driver.get("https://the-internet.herokuapp.com/inputs")
    number_input = self.driver.find_element(By.CSS_SELECTOR, ".example input")
    
    # Kiểm tra kiểu thuộc tính
    self.assertEqual(number_input.get_attribute("type"), "number")
    
    # Nhập số và đọc lại giá trị
    number_input.send_keys("50")
    self.assertEqual(number_input.get_attribute("value"), "50")

def test_06_inputs_clear(self) -> None:
    self.driver.get("https://the-internet.herokuapp.com/inputs")
    number_input = self.driver.find_element(By.CSS_SELECTOR, ".example input")
    number_input.send_keys("50")
    
    # Sử dụng hàm clear
    number_input.clear()
    self.assertEqual(number_input.get_attribute("value"), "")
```

---

## 📊 KẾT QUẢ THỰC THI KIỂM THỬ

* **Môi trường chạy:** Python 3.13, Selenium 4.51.0, Google Chrome 155 (Headless Eager).
* **Trình chạy kiểm thử:** `pytest 8.4.2` kết hợp plugin `pytest-html 4.2.0`.

```text
============================= test session starts ==============================
tuan-06/test_nhap_lieu_phim_dac_biet.py::TestNhapLieuVaPhimDacBiet::test_01_key_presses_enter PASSED [ 16%]
tuan-06/test_nhap_lieu_phim_dac_biet.py::TestNhapLieuVaPhimDacBiet::test_02_key_presses_tab PASSED [ 33%]
tuan-06/test_nhap_lieu_phim_dac_biet.py::TestNhapLieuVaPhimDacBiet::test_03_key_presses_arrow_up PASSED [ 50%]
tuan-06/test_nhap_lieu_phim_dac_biet.py::TestNhapLieuVaPhimDacBiet::test_04_inputs_send_keys_and_get_attribute PASSED [ 66%]
tuan-06/test_nhap_lieu_phim_dac_biet.py::TestNhapLieuVaPhimDacBiet::test_05_inputs_arrow_up_increment PASSED [ 83%]
tuan-06/test_nhap_lieu_phim_dac_biet.py::TestNhapLieuVaPhimDacBiet::test_06_inputs_clear PASSED [100%]

-- Generated html report: file:///Users/macos/kttd-w1/tuan-06/anh/report.html --
============================== 6 passed in 5.01s ===============================
```

Tỷ lệ thành công: **100% (6/6 Passed)**, thời gian chạy: **5.01 giây**.

---

## 📸 MINH CHỨNG THỰC TẾ TRÊN GIAO DIỆN

* **Key Presses:**
  - Nhấn `ENTER` -> Kết quả xanh lá: `You entered: ENTER`.
  - Nhấn `TAB` -> Kết quả xanh lá: `You entered: TAB`.
  - Nhấn `ARROW_UP` -> Kết quả xanh lá: `You entered: UP`.
* **Inputs:**
  - Nhập chuỗi `"50"` vào input number -> Giá trị hiển thị đúng `"50"`.
  - Nhấn `ARROW_UP` -> Giá trị tăng tự động lên `"51"`.
  - Gọi `clear()` -> Ô nhập trắng sạch rỗng hoàn toàn.
* Toàn bộ ảnh lưu tại: `tuan-06/anh/tc01_*.png` đến `tc06_*.png`.
* Báo cáo HTML tích hợp tại: `tuan-06/anh/report.html`.

---

## 🎯 BÀI HỌC KINH NGHIỆM & KẾT LUẬN

1. **Về xử lý kỹ thuật:**
   - Khi gõ phím `Keys.ENTER` trong thẻ `<form>` không có thuộc tính chặn, trang web sẽ tự động gửi request HTTP GET reload trang làm mất trạng thái element. Sử dụng JavaScript inject `preventDefault()` giúp kiểm tra chính xác phản hồi giao diện.
   - Sử dụng chiến lược `page_load_strategy = 'eager'` giúp kiểm thử trang web bên ngoài không bị nghẽn bởi các file script tracking chậm.
2. **Về quy trình nhóm:**
   - Phân chia công việc theo Issue rõ ràng giúp kiểm soát tiến độ từng bài test.
   - Thao tác qua nhánh riêng và Pull Request giúp tránh xung đột (merge conflicts) và đảm bảo chất lượng code trước khi gộp vào `main`.

---

<!-- _class: invert lead -->
# CẢM ƠN CÔ VÀ CÁC BẠN ĐÃ LẮNG NGHE!
## Q & A – HỎI VÀ ĐÁP
**Team W1 – Kiểm thử tự động Web the-internet**
