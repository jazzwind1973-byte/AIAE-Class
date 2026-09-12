# ⚙️ Module 5：函式 Functions

> 學習如何定義和使用函式，讓程式碼更模組化、可重用

---

## 🎯 學習目標

完成本模組後，你將能夠：
- ✅ 定義和呼叫函式
- ✅ 使用參數和回傳值
- ✅ 理解變數作用域（區域 vs 全域）
- ✅ 使用 `global` 關鍵字
- ✅ 撰寫 Lambda 匿名函式

---

## 📂 檔案結構

| 檔案 | 內容 | 類型 |
|:---|:---|:---:|
| `5-1_function.ipynb` | ⚙️ 函式定義與呼叫 | 教學 |
| `5-2_global.ipynb` | 🌐 全域變數與 global | 教學 |
| `5-3_lambda.ipynb` | ✨ Lambda 匿名函式 | 教學 |

---

## ⚙️ 函式基礎

### 📋 定義函式

```python
def function_name(parameters):
    """函式說明文件"""
    # 函式內容
    return result
```

### 📌 範例

```python
# 定義函式
def greet(name):
    return f"Hello, {name}!"

# 呼叫函式
message = greet("Alice")
print(message)  # Hello, Alice!
```

---

## 📋 參數類型

| 類型 | 說明 | 範例 |
|:---|:---|:---|
| 位置參數 | 按順序傳入 | `def add(a, b)` |
| 預設參數 | 有預設值 | `def greet(name="Guest")` |
| 關鍵字參數 | 指定參數名稱 | `greet(name="Alice")` |
| *args | 可變位置參數 | `def sum(*nums)` |
| **kwargs | 可變關鍵字參數 | `def info(**data)` |

---

## 🌐 變數作用域 Scope

| 類型 | 說明 | 存取範圍 |
|:---:|:---|:---|
| 🏠 區域變數 | 函式內定義 | 只能在函式內存取 |
| 🌍 全域變數 | 函式外定義 | 整個程式都可存取 |

### ⚠️ 注意事項

```python
name = "Global"  # 全域變數

def change_name():
    global name  # 宣告使用全域變數
    name = "Changed"

change_name()
print(name)  # "Changed"
```

💡 **提示：** 盡量避免過度使用全域變數，會讓程式難以維護

---

## ✨ Lambda 匿名函式

### 📋 語法

```python
lambda arguments: expression
```

### 📌 範例

```python
# 一般函式
def add(a, b):
    return a + b

# Lambda 等效寫法
add = lambda a, b: a + b

# 使用
print(add(3, 5))  # 8
```

### 🔧 常見應用

```python
# 搭配 sort() 排序
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
students.sort(key=lambda x: x[1])  # 依分數排序

# 搭配 filter()
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6]

# 搭配 map()
doubled = list(map(lambda x: x * 2, numbers))
# [2, 4, 6, 8, 10, 12]
```

---

## 🎮 練習題

### 練習 1：改寫 Module2 Practice
將 Module2 的百貨公司折扣計算改寫成函式

### 練習 2：建立巢狀列表
建立一個 list，包含多個 `[1, 2, x]` 的子列表，其中 x 從 1 到 10

```python
# 預期結果
[[1, 2, 1], [1, 2, 2], [1, 2, 3], ..., [1, 2, 10]]
```

---

[⬅️ 返回課程總覽](../README.md) | [上一章 Module4](../Module4/README.md) | [下一章 Module6 ➡️](../Module6/README.md)
