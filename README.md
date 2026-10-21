# KTTD - Team W1: Kiểm thử tự động Web The-Internet

**Học phần:** Kiểm thử phần mềm – Thực hành kiểm thử tự động  
**Nhóm:** W1 (Web Testing Team 1)  
**Trang kiểm thử:** https://the-internet.herokuapp.com  
**Tài liệu tham khảo:** https://selenium-python.readthedocs.io  

---

## 👥 Thành viên nhóm & Phân công Tuần 6
- **Trưởng nhóm:** Đoàn Nam Anh (Quản trị repo, phân chia Issue, review PR và tổng hợp).
- **Chuyên đề Tuần 6:** Nhập liệu & phím đặc biệt (*Inputs & Special Keys*).
- **Mục tiêu:** Kiểm thử 2 trang `/key_presses` và `/inputs`, hoàn thành báo cáo chuyên đề và slide thuyết trình 15 phút.

---

## 🛠️ Cài đặt & Chuẩn bị môi trường

1. **Cài đặt thư viện phụ thuộc:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Chạy bộ kiểm thử tự động với Pytest (sinh báo cáo HTML):**
   ```bash
   pytest -v tuan-06/test_nhap_lieu_phim_dac_biet.py --html=tuan-06/anh/report.html --self-contained-html
   ```

3. **Chạy trực tiếp với Unittest:**
   ```bash
   python3 -m unittest -v tuan-06/test_nhap_lieu_phim_dac_biet.py
   ```

---

## 📁 Cấu trúc kho mã nguồn
```text
kttd-w1/
├── README.md
├── requirements.txt
├── .gitignore
├── .github/
│   └── pull_request_template.md
└── tuan-06/
    ├── test_nhap_lieu_phim_dac_biet.py
    ├── testcases.md
    ├── slide_tuan06_w1.md
    ├── slide_tuan06_w1.html
    ├── slide_tuan06_w1.pptx
    └── anh/
        ├── report.html
        ├── tc01_key_presses_enter.png
        ├── tc02_key_presses_tab.png
        ├── tc03_key_presses_arrow_up.png
        ├── tc04_inputs_send_keys.png
        ├── tc05_inputs_arrow_up_increment.png
        └── tc06_inputs_clear.png
```
