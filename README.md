# Cathay API Testing Framework

基於 Python 的 API 自動化測試框架，使用 Postman Collections 執行 API 測試並生成詳細報告。

## 專案概述

本專案提供三個主要模組的 API 測試：
- **Product (產品)** - 產品相關 API 測試
- **Category (分類)** - 分類相關 API 測試  
- **Brand (品牌)** - 品牌相關 API 測試

## 環境需求

- Python 3.8+
- Node.js (用於安裝 Newman)
- npm

## 安裝與設置

### 1. 克隆專案
```bash
git clone <repository-url>
cd cathay
```

### 2. 創建虛擬環境
```bash
# 創建虛擬環境
python -m venv venv

# 激活虛擬環境
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 3. 安裝 Python 依賴
```bash
pip install -r requirements.txt
```

### 4. 安裝 Newman CLI
```bash
npm install -g newman newman-reporter-htmlextra
```

### 5. 準備測試文件

將 Postman Collection 文件放入對應目錄：
```
api_test/
├── product/
│   └── cathay_product.postman_collection.json
├── category/
│   └── cathay_category.postman_collection.json
└── brand/
    └── cathay_brand.postman_collection.json
```

## 使用方式

### 執行所有測試
```bash
# 確保虛擬環境已激活
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows

# 執行測試
python api_and_integration_test.py
```

### 測試執行流程
1. 併發執行所有模組測試 (product, category, brand)
2. 生成 HTML 和 JSON 報告
3. 轉換 JSON 報告為 Word 文檔
4. 如有失敗測試，記錄至 `failed_tests.txt`

## 輸出文件

測試完成後會在以下目錄生成報告：
- `html/` - HTML 格式測試報告
- `json/` - JSON 格式測試報告
- `docx/` - Word 文檔格式報告

## 專案結構

```
cathay/
├── api_and_integration_test.py    # 主要測試執行引擎
├── configs.py                     # 測試模組配置
├── convert_word.py                # Word 報告生成工具
├── requirements.txt               # Python 依賴套件
├── CLAUDE.md                      # Claude Code 指引
├── README.md                      # 專案說明文件
├── venv/                         # Python 虛擬環境 (自動生成)
├── api_test/                     # Postman Collection 文件目錄
│   ├── product/
│   ├── category/
│   └── brand/
├── html/                         # HTML 報告 (執行時生成)
├── json/                         # JSON 報告 (執行時生成)
└── docx/                         # Word 報告 (執行時生成)
```

## 配置說明

### 測試模組配置 (configs.py)
- `MODULE`: 併發執行的測試模組
- 每個測試使用獨立的環境變數檔案避免衝突

### 環境隔離
- 每個測試執行時會產生獨立的環境檔案
- 包含獨立的 API 金鑰與 Session Token
- 測試完成後自動清理環境檔案

## 故障排除

### 常見問題
1. **Newman 未安裝**
   ```bash
   npm install -g newman newman-reporter-htmlextra
   ```

2. **Python 依賴缺失**
   ```bash
   pip install -r requirements.txt
   ```

3. **虛擬環境未激活**
   ```bash
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

4. **Postman Collection 文件缺失**
   - 確認文件已放置在正確的目錄路徑
   - 檢查檔案名稱是否與 `configs.py` 中定義的一致

### 停用虛擬環境
```bash
deactivate
```

## 開發說明

如需添加新的測試模組：
1. 在 `api_test/` 下建立新目錄
2. 添加對應的 Postman Collection 文件
3. 更新 `configs.py` 中的模組定義
4. 選擇適當的執行模式 (併發或順序執行)

## 授權

[在此添加授權資訊]