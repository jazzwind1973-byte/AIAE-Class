# 🛡️ Module 7：例外處理 Exception Handling

> 學習如何優雅地處理程式執行時可能發生的錯誤

---

## 🎯 學習目標

完成本模組後，你將能夠：
- ✅ 使用 try-except 捕捉例外
- ✅ 處理多種不同類型的例外
- ✅ 使用 else 和 finally 子句
- ✅ 使用 raise 拋出自訂例外

---

## 📂 檔案結構

| 檔案 | 內容 | 類型 |
|:---|:---|:---:|
| `7-1_try_except.ipynb` | 🛡️ try-except 基礎 | 教學 |
| `7-2_raise.ipynb` | ⚡ raise 拋出例外 | 教學 |

---

## 🛡️ try-except 基本語法

```python
try:
    # 可能發生錯誤的程式碼
    result = 10 / 0
except ZeroDivisionError:
    # 處理特定錯誤
    print("不能除以零！")
except Exception as e:
    # 處理其他錯誤
    print(f"發生錯誤: {e}")
```

---

## 📋 完整語法結構

```python
try:
    # 嘗試執行的程式碼
    risky_operation()
except SpecificError:
    # 處理特定錯誤
    handle_specific_error()
except Exception as e:
    # 處理其他所有錯誤
    handle_general_error(e)
else:
    # 沒有錯誤時執行
    success_operation()
finally:
    # 無論如何都會執行
    cleanup_operation()
```

---

## 📊 常見例外類型

| 例外類型 | 說明 | 觸發情況 |
|:---|:---|:---|
| `ZeroDivisionError` | 除以零錯誤 | `10 / 0` |
| `TypeError` | 型別錯誤 | `"a" + 1` |
| `ValueError` | 值錯誤 | `int("abc")` |
| `IndexError` | 索引超出範圍 | `list[100]` |
| `KeyError` | 字典鍵不存在 | `dict["missing"]` |
| `FileNotFoundError` | 檔案不存在 | `open("missing.txt")` |
| `AttributeError` | 屬性不存在 | `obj.missing_attr` |
| `NameError` | 變數未定義 | 使用未宣告的變數 |

---

## ⚡ raise 拋出例外

### 📋 基本用法

```python
def divide(a, b):
    if b == 0:
        raise ValueError("除數不能為零！")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)  # 除數不能為零！
```

### 📋 自訂例外類別

```python
class CustomError(Exception):
    """自訂例外類別"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# 使用自訂例外
def validate_age(age):
    if age < 0:
        raise CustomError("年齡不能為負數！")
    if age > 150:
        raise CustomError("年齡不合理！")
    return age
```

---

## 💡 最佳實踐

| ✅ 建議做法 | ❌ 避免做法 |
|:---|:---|
| 捕捉特定例外 | 捕捉所有例外 `except:` |
| 提供有意義的錯誤訊息 | 忽略錯誤不處理 |
| 在適當的層級處理例外 | 過度使用 try-except |
| 使用 finally 清理資源 | 在 except 中隱藏錯誤 |

---

## 🎮 練習題

### 練習 1：安全的除法函式
撰寫一個 `safe_divide(a, b)` 函式，處理除以零的情況

### 練習 2：檔案讀取
撰寫程式讀取檔案，處理檔案不存在的情況

### 練習 3：使用者輸入驗證
撰寫程式要求使用者輸入年齡，並驗證輸入是否為有效數字

---

[⬅️ 返回課程總覽](../README.md) | [上一章 Module6](../Module6/README.md) | [下一章 Module8 ➡️](../Module8/README.md)
