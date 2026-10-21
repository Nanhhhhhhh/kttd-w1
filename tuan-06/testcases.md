# BÁO CÁO KIỂM THỬ TỰ ĐỘNG - TUẦN 06 (TEAM W1)

- **Chức năng:** Nhập liệu & phím đặc biệt (Inputs & Special Keys)
- **Đối tượng kiểm thử:**
  - Trang 1: `https://the-internet.herokuapp.com/key_presses`
  - Trang 2: `https://the-internet.herokuapp.com/inputs`
- **Thư viện sử dụng:** `selenium`, `unittest`, `pytest`, `pytest-html`

---

## 1. Danh sách Test Cases (Kịch bản kiểm thử)

| Mã TC | Tên ca kiểm thử | Trang kiểm thử | Các bước thực hiện | Dữ liệu đầu vào | Kết quả kỳ vọng | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC01** | Kiểm tra gõ phím ENTER | `/key_presses` | 1. Mở trang `/key_presses`<br>2. Định vị `#target`<br>3. Gửi phím `Keys.ENTER`<br>4. Lấy text từ `#result` | `Keys.ENTER` | Text hiển thị: `"You entered: ENTER"` | **PASSED** |
| **TC02** | Kiểm tra gõ phím TAB | `/key_presses` | 1. Mở trang `/key_presses`<br>2. Định vị `#target`<br>3. Gửi phím `Keys.TAB`<br>4. Lấy text từ `#result` | `Keys.TAB` | Text hiển thị: `"You entered: TAB"` | **PASSED** |
| **TC03** | Kiểm tra gõ phím ARROW_UP | `/key_presses` | 1. Mở trang `/key_presses`<br>2. Định vị `#target`<br>3. Gửi phím `Keys.ARROW_UP`<br>4. Lấy text từ `#result` | `Keys.ARROW_UP` | Text hiển thị: `"You entered: UP"` | **PASSED** |
| **TC04** | Kiểm tra nhập số & đọc giá trị | `/inputs` | 1. Mở trang `/inputs`<br>2. Định vị `input`<br>3. Kiểm tra `get_attribute("type")`<br>4. Gửi chuỗi số qua `send_keys`<br>5. Đọc `get_attribute("value")` | `"50"` | Type là `"number"`, value là `"50"` | **PASSED** |
| **TC05** | Kiểm tra tăng giá trị bằng phím lên | `/inputs` | 1. Mở trang `/inputs`<br>2. Nhập `"50"`<br>3. Gửi phím `Keys.ARROW_UP`<br>4. Đọc `get_attribute("value")` | `"50"` + `Keys.ARROW_UP` | Giá trị tăng thành `"51"` | **PASSED** |
| **TC06** | Kiểm tra xoá dữ liệu ô nhập | `/inputs` | 1. Mở trang `/inputs`<br>2. Nhập dữ liệu<br>3. Gọi hàm `clear()`<br>4. Đọc `get_attribute("value")` | `clear()` | Giá trị trở về rỗng `""` | **PASSED** |

---

## 2. Bảng đối chiếu các hàm bắt buộc theo yêu cầu phân công

| Hàm / Đối tượng bắt buộc | Vị trí áp dụng trong mã nguồn | Mục đích |
| :--- | :--- | :--- |
| `unittest.TestCase` | `class TestNhapLieuVaPhimDacBiet(unittest.TestCase)` | Kế thừa lớp kiểm thử chuẩn theo tài liệu Selenium (mục 2.3 & 2.4) |
| `setUp` | Phương thức `setUp(self)` | Chuẩn bị và kiểm tra trạng thái trước mỗi test |
| `tearDown` | Phương thức `tearDown(self)` | Dọn dẹp sau mỗi test |
| `get` | `self.driver.get(URL_KEY_PRESSES)`, `self.driver.get(URL_INPUTS)` | Điều hướng trình duyệt đến trang kiểm thử |
| `find_element` | `self.driver.find_element(By.ID, ...)` | Tìm kiếm phần tử trên cây DOM |
| `By.ID` | `By.ID, "target"`, `By.ID, "result"` | Định vị phần tử theo thuộc tính `id` |
| `send_keys` | `target_input.send_keys(...)`, `number_input.send_keys(...)` | Gửi chuỗi hoặc phím vào trường nhập liệu |
| `Keys.ENTER` | `target_input.send_keys(Keys.ENTER)` | Mô phỏng phím Enter |
| `Keys.TAB` | `target_input.send_keys(Keys.TAB)` | Mô phỏng phím Tab |
| `Keys.ARROW_UP` | `target_input.send_keys(Keys.ARROW_UP)` | Mô phỏng phím mũi tên lên |
| `clear` | `number_input.clear()` | Xoá toàn bộ nội dung trong ô nhập |
| `get_attribute` | `number_input.get_attribute("type")`, `get_attribute("value")` | Lấy giá trị các thuộc tính HTML của element |
| `text` | `result_element.text` | Lấy nội dung văn bản hiển thị của element |

---

## 3. Cách chạy và sinh báo cáo

1. **Chạy bằng unittest (chuẩn Python):**
   ```bash
   python3 -m unittest -v tuan-06/test_nhap_lieu_phim_dac_biet.py
   ```

2. **Chạy bằng pytest và sinh báo cáo HTML:**
   ```bash
   pytest -v tuan-06/test_nhap_lieu_phim_dac_biet.py --html=tuan-06/anh/report.html --self-contained-html
   ```

3. **Chạy chế độ hiển thị giao diện trình duyệt (không headless):**
   ```bash
   HEADLESS=false python3 -m unittest -v tuan-06/test_nhap_lieu_phim_dac_biet.py
   ```
