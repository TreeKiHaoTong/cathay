# Cathay API Testing Framework

API 自動化測試框架，測試 Product、Category、Brand、Message三個模組的 API。

## 需要的環境

- Python 3.8+
- Node.js
- npm

## 安裝(WSL環境)

```bash
# 1. 建立虛擬環境
python -m venv venv
source venv/bin/activate

# 2. 安裝套件
pip install -r requirements.txt
npm install -g newman newman-reporter-htmlextra
or
sudo npm install -g newman newman-reporter-htmlextra

# 3. 執行測試
python api_and_integration_test.py
```

## 測試結果

執行完會產生三種格式的報告：
- `html/` - 網頁版報告
- `json/` - JSON 格式 
- `docx/` - Word 文件

**維護測試模組**
1. 在 `api_test/` 加新資料夾
2. 放入 postman collection 檔案  
3. 修改 `configs.py`