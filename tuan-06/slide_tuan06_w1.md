---
marp: true
theme: uncover
class: invert
paginate: true
header: 'Học phần: Kiểm thử phần mềm tự động | Nhóm W1'
footer: 'Báo cáo Chuyên đề Selenium & Thực hành Kiểm thử Tuần 6'
style: |
  section {
    font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: #0b1329;
    color: #f8fafc;
    text-align: left;
    padding: 35px 55px;
    font-size: 20px;
  }
  h1 {
    color: #38bdf8;
    font-size: 38px;
    margin-bottom: 12px;
  }
  h2 {
    color: #38bdf8;
    font-size: 28px;
    border-bottom: 2px solid #334155;
    padding-bottom: 8px;
    margin-bottom: 15px;
  }
  h3 {
    color: #93c5fd;
    font-size: 22px;
    margin-bottom: 8px;
  }
  table {
    font-size: 16px;
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
  }
  th {
    background-color: #1e293b;
    color: #38bdf8;
    padding: 8px 10px;
    border: 1px solid #334155;
  }
  td {
    padding: 6px 10px;
    border: 1px solid #334155;
    background-color: #0b1329;
  }
  code {
    background: #1e293b;
    color: #34d399;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
    font-size: 16px;
  }
  pre {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 12px;
    font-size: 15px;
  }
  pre code {
    background: transparent;
    color: #34d399;
    padding: 0;
  }
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
  }
  .card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 16px;
  }
  .accent {
    color: #38bdf8;
    font-weight: bold;
  }
  .success {
    color: #34d399;
    font-weight: bold;
  }
  .warning {
    color: #fbbf24;
    font-weight: bold;
  }
---

<!-- _class: invert lead -->
# KIỂM THỬ PHẦN MỀM TỰ ĐỘNG
## BÁO CÁO CHUYÊN ĐỀ TÀI LIỆU SELENIUM & THỰC HÀNH KIỂM THỬ

**Chuyên đề:** Nhập liệu & Phím đặc biệt (*Inputs & Special Keys*)  
**Đối tượng:** `the-internet.herokuapp.com` (`/key_presses`, `/inputs`)  
**Đơn vị:** Nhóm W1 (Web Testing Team 1)  
**Sinh viên thực hiện:** Đoàn Nam Anh (MSSV: A46489)  
**Kho mã nguồn:** [github.com/Nanhhhhhhh/kttd-w1](https://github.com/Nanhhhhhhh/kttd-w1)

---

## 📋 MỤC LỤC BÁO CÁO

<div class="grid-2">
<div class="card">

### PHẦN I: LÝ THUYẾT CHUYÊN ĐỀ
* **1. Kiến trúc WebDriver & Chuẩn W3C** (Mục 2.1)
* **2. Cơ chế điều hướng & Tải trang** (Mục 2.2)
* **3. Framework kiểm thử unittest** (Mục 2.3)
* **4. Vòng đời Test Fixture: setUp & tearDown** (Mục 2.4)
* **5. Bản chất WebElement & Tương tác DOM** (Mục 3.1, 7.20)
* **6. Bộ định vị By.ID & Lớp Keys** (Mục 4.1, 7.4)

</div>
<div class="card">

### PHẦN II: THỰC HÀNH & KẾT QUẢ
* **7. Phân tích đối tượng kiểm thử 2 trang**
* **8. Bảng thiết kế 6 Test Cases chi tiết**
* **9. Triển khai mã nguồn kiểm thử**
* **10. Báo cáo kết quả Pytest & Log chi tiết**
* **11. Hình ảnh minh chứng thực tế trên giao diện**
* **12. Bài học kinh nghiệm & Quy trình Git nhóm**

</div>
</div>

---

## 🏗️ 1. KIẾN TRÚC TỔNG THỂ SELENIUM WEBDRIVER (MỤC 2.1)

Selenium WebDriver vận hành theo **Mô hình kiến trúc 3 lớp (3-Tier Architecture)** tuân thủ tiêu chuẩn W3C WebDriver Specification:

<div class="grid-2">
<div class="card">

### 3 Lớp trong kiến trúc
1. **Client Language Bindings (Python SDK):** Cung cấp API hướng đối tượng cấp cao (`webdriver`, `By`, `Keys`, `WebElement`).
2. **Browser Driver (ChromeDriver):** Đóng vai trò máy chủ HTTP Server trung gian, nhận lệnh RESTful JSON qua cổng mạng nội bộ.
3. **Browser Engine (Google Chrome):** Trình duyệt thực thi trực tiếp thao tác DOM qua Chrome DevTools Protocol (CDP).

</div>
<div class="card">

### Chu trình bắt tay (Handshake)
```python
from selenium import webdriver

# 1. Client gửi POST /session
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')

# 2. Khởi tạo phiên kết nối
driver = webdriver.Chrome(options=options)
# -> Nhận lại: {"value": {"sessionId": "..."}}

# 3. Mọi thao tác sau đó gắn kèm SessionId
```

</div>
</div>

---

## 🌐 2. CƠ CHẾ ĐIỀU HƯỚNG & CHIẾN LƯỢC TẢI TRANG (MỤC 2.2)

Phương thức `driver.get(url)` là lời gọi đồng bộ (blocking call) gửi lệnh HTTP `POST /session/{id}/url`.

<div class="grid-2">
<div class="card">

### Bản chất & Kiểm tra tải trang
* WebDriver sẽ chờ đợi tín hiệu hoàn tất từ trình duyệt trước khi tiếp tục.
* Mục 2.2 chỉ dẫn cách xác minh trang đã tải thành công bằng thuộc tính `driver.title`:

```python
self.driver.get(URL_KEY_PRESSES)
self.assertIn("The Internet", self.driver.title)
```

</div>
<div class="card">

### 3 Chiến lược tải trang (Page Load)
* <span class="warning">normal (Mặc định):</span> Chờ sự kiện `window.onload`. Dễ bị nghẽn bởi script quảng cáo / tracking bên thứ ba.
* <span class="success">eager (Đã áp dụng):</span> Chờ sự kiện `DOMContentLoaded`. Trả quyền điều khiển ngay khi cây DOM sẵn sàng tương tác!
* <span class="accent">none:</span> Trả quyền điều khiển ngay sau khi gửi request URL.

</div>
</div>

---

## 🧪 3. FRAMEWORK KIỂM THỬ UNITTEST (MỤC 2.3)

Selenium Python tích hợp sâu với thư viện chuẩn `unittest`, triển khai theo kiến trúc xUnit:

<div class="grid-2">
<div class="card">

### 4 Trụ cột của xUnit
1. **Test Fixture:** Chuẩn bị môi trường trước khi test và thu dọn sau khi test.
2. **TestCase:** Đơn vị kiểm thử độc lập nhỏ nhất kiểm tra một chức năng cụ thể.
3. **TestSuite:** Tập hợp nhiều TestCase chạy cùng nhau.
4. **TestRunner:** Bộ điều phối thực thi và hiển thị kết quả (OK / FAILED).

</div>
<div class="card">

### Cấu trúc lớp kế thừa
```python
import unittest

class TestW1(unittest.TestCase):
    # TestRunner tự động quét mọi hàm
    # có tiền tố bắt đầu bằng 'test_'
    def test_01_enter(self):
        target = self.driver.find_element(...)
        target.send_keys(Keys.ENTER)
        
        # Khẳng định kiểm thử chuẩn:
        self.assertEqual(res.text, "...")
```

</div>
</div>

---

## 🔄 4. VÒNG ĐỜI TEST FIXTURE: SETUP & TEARDOWN (MỤC 2.4)

Chu trình sống của một bài kiểm thử tự động nhằm đảm bảo tính **Cách ly kiểm thử (Test Isolation)**:

<div class="grid-2">
<div class="card">

### Chu trình sống (Lifecycle)
* **`setUp()`:** Chạy tự động ngay trước mỗi hàm `test_*`. Đảm bảo WebDriver luôn sẵn sàng, xóa bỏ trạng thái cũ.
* **`tearDown()`:** Chạy tự động ngay sau mỗi hàm `test_*` (kể cả khi test ném Exception). Dọn dẹp session, đóng dialog.
* **Cách ly bài test:** Mỗi test method hoàn toàn độc lập, không bị ảnh hưởng bởi thất bại của test trước.

</div>
<div class="card">

### Tối ưu hóa hiệu năng thực tế
* **Per-Test Browser (Truyền thống):** Mở và đóng Chrome 6 lần $\rightarrow$ Mất ~30 giây.
* **Per-Class Browser (Áp dụng):**
  - Dùng `setUpClass()` mở 1 browser duy nhất.
  - Hàm `setUp()` kiểm tra trạng thái session.
  - Dùng `tearDownClass()` đóng browser.
  - $\rightarrow$ **Tốc độ chạy tăng gấp 6 lần (chỉ 5.01s)!**

</div>
</div>

---

## 🎯 5. BẢN CHẤT ĐỐI TƯỢNG WEBELEMENT (MỤC 3.1 & 7.20)

`WebElement` là một Proxy Object đại diện cho một node HTML cụ thể trên cây DOM của trình duyệt.

<div class="grid-2">
<div class="card">

### Các phương thức tương tác cốt lõi
* **`.send_keys(*values)`:** Gửi chuỗi ký tự hoặc phím chức năng. Phương thức này nối tiếp (append) vào dữ liệu đang có.
* **`.clear()`:** Xoá sạch toàn bộ nội dung trong ô `<input>` hoặc `<textarea>`. Kích hoạt focus, select-all và xóa.
* **Định danh UUID:** Mỗi phần tử có ID duy nhất do Driver gán (ví dụ `element-6066-11e4-...`).

</div>
<div class="card">

### Bẫy lỗi StaleElementReferenceException
* Xảy ra khi phần tử đã tìm thấy nhưng sau đó DOM bị reload hoặc re-render.
* **Tình huống gặp phải:** Khi gõ `Keys.ENTER` vào ô input trong thẻ `<form>`, trình duyệt submit form GET làm reload trang $\rightarrow$ WebElement bị stale!
* **Giải pháp:** Dùng `execute_script` inject `preventDefault()` ngăn reload form tự nhiên.

</div>
</div>

---

## ⚖️ 6. SO SÁNH .TEXT VÀ .GET_ATTRIBUTE() (MỤC 7.20)

| Tiêu chí | Thuộc tính `.text` | Phương thức `.get_attribute(name)` |
| :--- | :--- | :--- |
| **Bản chất** | Trả về thuộc tính `innerText` của phần tử theo chuẩn W3C | Đọc giá trị thuộc tính HTML động trong DOM |
| **Tầm nhìn (Visibility)** | Chỉ lấy văn bản **đang hiển thị** cho người dùng (ẩn các thẻ `display: none`) | Đọc được mọi thuộc tính kể cả khi phần tử bị ẩn |
| **Ứng dụng với thẻ `<input>`** | **KHÔNG** lấy được dữ liệu người dùng nhập (luôn trả về chuỗi rỗng `""`) | **LẤY CHÍNH XÁC** dữ liệu người dùng nhập thông qua `get_attribute("value")` |
| **Áp dụng trong bài test** | Lấy text thông báo: `result.text` $\rightarrow$ `"You entered: ENTER"` | Lấy type: `get_attribute("type")` $\rightarrow$ `"number"`, value $\rightarrow$ `"50"` |

---

## ⚡ 7. BỘ ĐỊNH VỊ BY.ID & TỐI ƯU HIỆU NĂNG (MỤC 4.1)

<div class="grid-2">
<div class="card">

### Bản chất cơ chế By.ID
* **Ánh xạ trực tiếp:** Gọi hàm native `document.getElementById()` của trình duyệt.
* **Độ phức tạp $O(1)$:** Trình duyệt lưu trữ ID theo bảng băm (Hash Map), truy xuất tức thì.
* **Tính duy nhất:** Chuẩn W3C HTML5 quy định `id` phải là duy nhất trên toàn bộ trang.
* **Cú pháp:**
  ```python
  target = driver.find_element(By.ID, "target")
  result = driver.find_element(By.ID, "result")
  ```

</div>
<div class="card">

### So sánh tốc độ các Locators
1. <span class="success">By.ID ($O(1)$):</span> Nhanh nhất, độ tin cậy cao nhất.
2. <span class="accent">By.NAME:</span> Rất nhanh, tối ưu cho form input.
3. <span class="accent">By.CSS_SELECTOR:</span> Nhanh, linh hoạt (`.example input`).
4. <span class="warning">By.XPATH ($O(N)$):</span> Chậm nhất vì phải quét duyệt cây DOM.
5. <span class="muted">Lưu ý:</span> Tránh các ID động tự sinh (như `btn_18492` trong React/Vue).

</div>
</div>

---

## ⌨️ 8. LỚP KEYS & MÔ PHỎNG PHÍM CHỨC NĂNG (MỤC 7.4)

Lớp `selenium.webdriver.common.keys.Keys` định nghĩa các phím đặc biệt dưới dạng hằng số Unicode nằm trong vùng **Private Use Area (PUA)** (từ `\ue000` đến `\ue03d`).

<div class="grid-2">
<div class="card">

### 3 Phím đặc biệt của đề tài
* **`Keys.ENTER` (`\ue007`):** Mô phỏng phím Enter / Return. Kích hoạt submit biểu mẫu.
* **`Keys.TAB` (`\ue004`):** Mô phỏng phím Tab. Chuyển focus giữa các trường điều khiển.
* **`Keys.ARROW_UP` (`\ue013`):** Mô phỏng phím mũi tên lên. Trên trang inputs số giúp tăng giá trị lên 1 đơn vị.

</div>
<div class="card">

### Chuỗi sự kiện bàn phím
```python
from selenium.webdriver.common.keys import Keys

# Trình duyệt phát chuỗi: keydown -> input -> keyup
target_input.send_keys(Keys.ENTER)
target_input.send_keys(Keys.TAB)
target_input.send_keys(Keys.ARROW_UP)

# Tăng giá trị số:
number_input.send_keys(Keys.ARROW_UP)
```

</div>
</div>

---

## 🔍 9. ĐỐI TƯỢNG KIỂM THỬ: PHÂN TÍCH 2 TRANG WEB

<div class="grid-2">
<div class="card">

### Trang 1: `/key_presses`
* **URL:** `the-internet.herokuapp.com/key_presses`
* **DOM:** `<input id='target'>` & `<p id='result'>`
* **JavaScript:** Lắng nghe sự kiện `$(document).keydown` và hiển thị mã phím tương ứng.
* **Thách thức:** Input nằm trong `<form>` không có `onsubmit="return false"`, khi nhấn Enter sẽ kích hoạt GET request reload trang.

</div>
<div class="card">

### Trang 2: `/inputs`
* **URL:** `the-internet.herokuapp.com/inputs`
* **DOM:** Thẻ `<input type="number">` nằm trong container `.example`.
* **Đặc tính native:** Trình duyệt chỉ chấp nhận số và tích hợp cơ chế step-up/step-down bằng phím mũi tên.
* **Mục tiêu:** Kiểm tra thuộc tính type, nhập chuỗi số, tăng số bằng ARROW_UP và xoá bằng clear().

</div>
</div>

---

## 📊 10. BẢNG THIẾT KẾ 6 KỊCH BẢN KIỂM THỬ

| Mã TC | Tên ca kiểm thử | Trang | Hàm sử dụng | Kết quả kỳ vọng | Trạng thái |
| :---: | :--- | :---: | :--- | :--- | :---: |
| **TC01** | Gõ phím ENTER | `/key_presses` | `get`, `By.ID`, `send_keys`, `Keys.ENTER`, `text` | Hiển thị: `"You entered: ENTER"` | <span class="success">PASSED</span> |
| **TC02** | Gõ phím TAB | `/key_presses` | `get`, `By.ID`, `send_keys`, `Keys.TAB`, `text` | Hiển thị: `"You entered: TAB"` | <span class="success">PASSED</span> |
| **TC03** | Gõ phím ARROW_UP | `/key_presses` | `get`, `By.ID`, `send_keys`, `Keys.ARROW_UP`, `text` | Hiển thị: `"You entered: UP"` | <span class="success">PASSED</span> |
| **TC04** | Nhập số & đọc giá trị | `/inputs` | `get`, `find_element`, `send_keys`, `get_attribute` | `type="number"`, `value="50"` | <span class="success">PASSED</span> |
| **TC05** | Tăng số bằng phím lên | `/inputs` | `send_keys`, `Keys.ARROW_UP`, `get_attribute` | `value` tăng từ `"50"` lên `"51"` | <span class="success">PASSED</span> |
| **TC06** | Xoá nội dung ô nhập | `/inputs` | `send_keys`, `clear`, `get_attribute` | `value` làm trống về rỗng `""` | <span class="success">PASSED</span> |

---

## 💻 11. TRIỂN KHAI CODE: TRANG KEY PRESSES (TC01 – TC03)

```python
def test_01_key_presses_enter(self) -> None:
    # 1. Điều hướng bằng hàm get
    self.driver.get(URL_KEY_PRESSES)
    
    # 2. Định vị phần tử bằng By.ID
    target = self.driver.find_element(By.ID, "target")
    
    # Chặn form tự động reload bằng JavaScript inject
    self.driver.execute_script(
        "document.querySelector('form').onsubmit = function(e){ e.preventDefault(); return false; };"
    )
    
    # 3. Gửi phím ENTER bằng send_keys kết hợp Keys.ENTER
    target.send_keys(Keys.ENTER)
    
    # 4. Trích xuất text thông báo bằng thuộc tính .text và kiểm tra
    result = self.driver.find_element(By.ID, "result")
    self.assertEqual(result.text, "You entered: ENTER")
    self.driver.save_screenshot("tuan-06/anh/tc01_key_presses_enter.png")
```

---

## 💻 12. TRIỂN KHAI CODE: TRANG INPUTS (TC04 – TC06)

```python
def test_04_inputs_send_keys_and_get_attribute(self) -> None:
    self.driver.get(URL_INPUTS)
    num_input = self.driver.find_element(By.CSS_SELECTOR, ".example input")
    
    # Kiểm tra thuộc tính type
    self.assertEqual(num_input.get_attribute("type"), "number")
    
    # Nhập giá trị số và kiểm tra giá trị bằng get_attribute("value")
    num_input.send_keys("50")
    self.assertEqual(num_input.get_attribute("value"), "50")

def test_06_inputs_clear(self) -> None:
    num_input = self.driver.find_element(By.CSS_SELECTOR, ".example input")
    num_input.send_keys("50")
    
    # Sử dụng hàm clear() làm rỗng trường nhập
    num_input.clear()
    self.assertEqual(num_input.get_attribute("value"), "")
```

---

## 📈 13. BÁO CÁO KẾT QUẢ THỰC THI KIỂM THỬ

<div class="grid-2">
<div class="card">

### Tổng hợp thông số
* **Tổng số bài test:** 6 / 6 Test Cases
* **Tỷ lệ thành công:** <span class="success">100% PASSED</span>
* **Thời gian thực thi:** <span class="accent">5.01 giây</span>
* **Môi trường:** Python 3.13.9, Selenium 4.51.0, Chrome 155 (Headless Eager)
* **Báo cáo HTML:** `tuan-06/anh/report.html`

</div>
<div class="card">

### Log Terminal Pytest
```text
tuan-06/test_nhap_lieu_phim_dac_biet.py::
  TestNhapLieuVaPhimDacBiet::
    test_01_key_presses_enter PASSED      [ 16%]
    test_02_key_presses_tab PASSED        [ 33%]
    test_03_key_presses_arrow_up PASSED   [ 50%]
    test_04_inputs_send_keys PASSED       [ 66%]
    test_05_inputs_arrow_up PASSED        [ 83%]
    test_06_inputs_clear PASSED           [100%]
================ 6 passed in 5.01s ===============
```

</div>
</div>

---

## 🖼️ 14. MINH CHỨNG THỰC TẾ TRÊN GIAO DIỆN

<div class="grid-2">
<div class="card">

### Trang /key_presses
* **ENTER:** Nhận phản hồi xanh lá `You entered: ENTER`.
* **TAB:** Nhận phản hồi xanh lá `You entered: TAB`.
* **ARROW_UP:** Nhận phản hồi xanh lá `You entered: UP`.
* Toàn bộ ảnh lưu tại `tuan-06/anh/tc01_*.png` đến `tc03_*.png`.

</div>
<div class="card">

### Trang /inputs
* **Nhập số:** Nhập chuỗi `"50"`, kiểm tra `value="50"`.
* **ARROW_UP:** Bấm phím lên, giá trị tự động tăng lên `"51"`.
* **clear():** Ô nhập được làm trống rỗng hoàn toàn `""`.
* Toàn bộ ảnh lưu tại `tuan-06/anh/tc04_*.png` đến `tc06_*.png`.

</div>
</div>

---

## 💡 15. BÀI HỌC KINH NGHIỆM KỸ THUẬT

1. **Hiểu sâu cơ chế sự kiện DOM của trình duyệt:**
   - Khi tương tác với các thẻ `<input>` nằm trong `<form>`, việc gõ phím `Keys.ENTER` sẽ phát sinh sự kiện submit mặc định. Cần chủ động kiểm soát vòng đời của trang bằng cách inject JavaScript `preventDefault()` để bảo toàn cây DOM.
2. **Chiến lược tải trang `eager` tối ưu thời gian:**
   - Trong môi trường thực tế, các trang web thường tải nhiều tài nguyên bên thứ ba (quảng cáo, script theo dõi). Cấu hình `page_load_strategy = 'eager'` giúp kiểm thử tập trung vào DOMContentLoaded mà không bị treo request.
3. **Quản lý phiên WebDriver hướng đối tượng:**
   - Kết hợp `setUpClass()` tái sử dụng một phiên trình duyệt cho toàn bộ test suite giúp tiết kiệm hơn 80% thời gian thực thi mà vẫn duy trì tính độc lập giữa các test case thông qua `setUp()` và `tearDown()`.

---

## 🌳 16. QUY TRÌNH LÀM VIỆC NHÓM TRÊN GITHUB

Tuân thủ nghiêm ngặt mô hình phân nhánh và quản trị chất lượng:

<div class="grid-2">
<div class="card">

### Quản trị qua Issues & Milestones
* **Milestone:** Tuần 6 – Nhập liệu & phím đặc biệt.
* **4 Issues độc lập:**
  - Issue #1: Kịch bản kiểm thử & tài liệu.
  - Issue #2: Code test trang `/key_presses`.
  - Issue #3: Code test trang `/inputs`.
  - Issue #4: Báo cáo, ảnh minh chứng & slide.

</div>
<div class="card">

### Mô hình nhánh & Pull Requests
* **Nhánh `week-06`:** Tích hợp chung của tuần, tạo từ `main`.
* **4 Nhánh tính năng:** `t06-testcases`, `t06-keypresses`, `t06-inputs`, `t06-slide-report`.
* **Pull Request:** Mở PR vào `week-06` với cú pháp `Closes #<id>`, review và merge.
* **Gộp vào `main`:** Cuối tuần nghiệm thu toàn bộ test và mở PR #9 vào `main`.

</div>
</div>

---

## 📌 17. TỔNG KẾT ĐÁNH GIÁ NHÓM W1

* **Độ bao phủ yêu cầu:** Đáp ứng **100%** toàn bộ 13 hàm và phương thức bắt buộc:
  - `get`, `find_element`, `By.ID`, `send_keys`, `Keys.ENTER`, `Keys.TAB`, `Keys.ARROW_UP`, `clear`, `get_attribute`, `text`, `unittest.TestCase`, `setUp`, `tearDown`.
* **Chất lượng mã nguồn:** Tuân thủ chuẩn PEP 8, có chú thích tiếng Việt giải thích từng bước, trích xuất hằng số rõ ràng, không có magic string / số lạ.
* **Bộ sản phẩm hoàn thiện:**
  - File mã nguồn kiểm thử: [`test_nhap_lieu_phim_dac_biet.py`](file:///Users/macos/kttd-w1/tuan-06/test_nhap_lieu_phim_dac_biet.py)
  - Tài liệu kịch bản: [`testcases.md`](file:///Users/macos/kttd-w1/tuan-06/testcases.md)
  - Slide trình chiếu: [`slide_tuan06_w1.pptx`](file:///Users/macos/kttd-w1/tuan-06/slide_tuan06_w1.pptx) & [`slide_tuan06_w1.html`](file:///Users/macos/kttd-w1/tuan-06/slide_tuan06_w1.html)
  - Thư mục ảnh và báo cáo: [`tuan-06/anh/`](file:///Users/macos/kttd-w1/tuan-06/anh)

---

<!-- _class: invert lead -->
# CẢM ƠN CÔ VÀ CÁC BẠN ĐÃ THEO DÕI!
## PHẦN HỎI & ĐÁP (Q & A)

**Nhóm W1 – Báo cáo Kiểm thử tự động Web The-Internet**  
Kho lưu trữ mã nguồn: [github.com/Nanhhhhhhh/kttd-w1](https://github.com/Nanhhhhhhh/kttd-w1)  
Pull Request nghiệm thu: [github.com/Nanhhhhhhh/kttd-w1/pull/9](https://github.com/Nanhhhhhhh/kttd-w1/pull/9)
