# 📁 Module 8：檔案處理 File Handling

> 學習如何讀寫檔案、處理 JSON 資料，以及使用 OS 模組

---

## 🎯 學習目標

完成本模組後，你將能夠：
- ✅ 使用 `open()` 讀取和寫入檔案
- ✅ 處理 JSON 格式資料
- ✅ 使用 `os` 模組進行檔案系統操作

---

## 📂 檔案結構

| 檔案 | 內容 | 類型 |
|:---|:---|:---:|
| `8-1_open.ipynb` | 📖 檔案讀寫 open() | 教學 |
| `8-1-1_json.ipynb` | 📋 JSON 處理 | 教學 |
| `8-2_os.ipynb` | 💻 OS 模組 | 教學 |
| `8-3_practice.ipynb` | 🎮 綜合練習 | 練習 |
| `data.txt` | 📄 範例資料檔 | 資料 |

---

## 📖 open() 檔案操作

### 📋 檔案模式

| 模式 | 說明 | 檔案不存在時 |
|:---:|:---|:---|
| `"r"` | 🔍 讀取（預設） | 報錯 |
| `"w"` | ✏️ 寫入（覆蓋） | 創建新檔案 |
| `"a"` | ➕ 附加 | 創建新檔案 |
| `"x"` | 🆕 創建 | 創建，若存在則報錯 |
| `"t"` | 📝 文字模式（預設） | - |
| `"b"` | 💾 二進位模式 | - |

### 📌 讀取檔案

```python
# 方法 1：使用 with（推薦，自動關閉檔案）
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 方法 2：逐行讀取
with open("file.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

### 📌 寫入檔案

```python
# 覆蓋寫入
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!")

# 附加寫入
with open("file.txt", "a", encoding="utf-8") as f:
    f.write("\n這是新增的一行")
```

---

## 📋 JSON 處理

### 📋 常用方法

| 方法 | 說明 | 用途 |
|:---|:---|:---|
| `json.dump()` | 物件 → JSON 檔案 | 寫入檔案 |
| `json.dumps()` | 物件 → JSON 字串 | 轉換字串 |
| `json.load()` | JSON 檔案 → 物件 | 讀取檔案 |
| `json.loads()` | JSON 字串 → 物件 | 解析字串 |

### 📌 範例

```python
import json

# Python 物件轉 JSON
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data, ensure_ascii=False, indent=2)

# 寫入 JSON 檔案
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 讀取 JSON 檔案
with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
```

---

## 💻 OS 模組

### 📋 常用功能

| 方法 | 說明 |
|:---|:---|
| `os.path.exists(path)` | 檢查路徑是否存在 |
| `os.path.isfile(path)` | 檢查是否為檔案 |
| `os.path.isdir(path)` | 檢查是否為目錄 |
| `os.makedirs(path)` | 建立目錄（含子目錄） |
| `os.remove(path)` | 刪除檔案 |
| `os.listdir(path)` | 列出目錄內容 |
| `os.getcwd()` | 取得當前工作目錄 |

### 📌 範例

```python
import os

# 檢查檔案是否存在
if os.path.exists("data.txt"):
    print("檔案存在")
else:
    print("檔案不存在")

# 建立目錄
os.makedirs("output/data", exist_ok=True)

# 列出目錄內容
files = os.listdir(".")
for f in files:
    print(f)
```

---

## 🎮 練習題

### 練習 1：讀取並處理資料
讀取 `data.txt`，計算每行的字數

### 練習 2：JSON 資料處理
建立一個學生成績系統，將成績存入 JSON 檔案

### 練習 3：檔案管理
撰寫程式自動整理目錄中的檔案（按副檔名分類）

---

[⬅️ 返回課程總覽](../README.md) | [上一章 Module7](../Module7/README.md) | [下一章 Module9 ➡️](../Module9/README.md)
