# 🗃️ Module 4：資料結構 Data Structures

> 深入學習 Python 中各種資料結構的操作與應用

---

## 🎯 學習目標

完成本模組後，你將能夠：
- ✅ 熟練操作字串的各種方法
- ✅ 掌握列表的增刪改查操作
- ✅ 理解元組的不可變特性
- ✅ 運用字典儲存與查詢鍵值對
- ✅ 使用集合進行去重與集合運算
- ✅ 精通切片操作

---

## 📂 檔案結構

| 檔案 | 內容 | 類型 |
|:---|:---|:---:|
| `4-0_note.ipynb` | 📋 資料結構比較表 | 筆記 |
| `4-1_string.ipynb` | 📝 字串方法 | 教學 |
| `4-1-1_format.ipynb` | 🔤 字串格式化 (% 與 format) | 教學 |
| `4-1-3_f-string.ipynb` | ✨ f-string 格式化 | 教學 |
| `4-2_list.ipynb` | 📋 列表操作 | 教學 |
| `4-3_tuple.ipynb` | 📦 元組操作 | 教學 |
| `4-4-1_dict.ipynb` | 📖 字典操作 | 教學 |
| `4-4-2_dict_for.ipynb` | 🔄 字典迭代 | 教學 |
| `4-5_set.ipynb` | 🎯 集合操作 | 教學 |
| `4-6_slicing.ipynb` | ✂️ 切片操作 | 教學 |

---

## 📊 資料結構比較表

| 型態 | 創建方式 | 可變性 | 有序性 | 重複元素 |
|:---:|:---|:---:|:---:|:---:|
| 📝 `str` | `"hello"` | ❌ 不可變 | ✅ 有序 | ✅ 可重複 |
| 📋 `list` | `[1, 2, 3]` | ✅ 可變 | ✅ 有序 | ✅ 可重複 |
| 📦 `tuple` | `(1, 2, 3)` | ❌ 不可變 | ✅ 有序 | ✅ 可重複 |
| 🎯 `set` | `{1, 2, 3}` | ✅ 可變 | ❌ 無序 | ❌ 不可重複 |
| 📖 `dict` | `{"a": 1}` | ✅ 可變 | ✅ 有序* | 鍵不可重複 |

> *Python 3.7+ 字典保持插入順序

---

## 📝 字串方法 String Methods

| 方法 | 功能 | 範例 |
|:---|:---|:---|
| `replace(old, new)` | 替換字串 | `"hello".replace("l", "L")` |
| `strip()` | 去除兩側空格 | `" hello ".strip()` |
| `upper()` | 轉大寫 | `"hello".upper()` |
| `lower()` | 轉小寫 | `"HELLO".lower()` |
| `split(sep)` | 分割字串 | `"a,b,c".split(",")` |
| `join(list)` | 合併字串 | `",".join(["a","b"])` |

---

## 📋 列表方法 List Methods

| 方法 | 功能 | 範例 |
|:---|:---|:---|
| `append(x)` | 新增元素至尾端 | `list.append(5)` |
| `insert(i, x)` | 在索引 i 插入元素 | `list.insert(0, 5)` |
| `remove(x)` | 移除第一個值為 x 的元素 | `list.remove(5)` |
| `pop(i)` | 移除並回傳索引 i 的元素 | `list.pop(0)` |
| `count(x)` | 計算 x 出現次數 | `list.count(5)` |
| `sort()` | 排序 | `list.sort()` |
| `reverse()` | 反轉 | `list.reverse()` |

---

## 🎯 List Comprehension 列表推導式

```python
# 語法
new_list = [expression for item in iterable if condition]

# 範例：產生 1-10 的偶數平方
squares = [x**2 for x in range(1, 11) if x % 2 == 0]
# 結果: [4, 16, 36, 64, 100]
```

---

## ✂️ 切片 Slicing

```python
# 語法: sequence[start:stop:step]

text = "Python"
text[0:3]    # "Pyt"  - 索引 0 到 2
text[::2]    # "Pto"  - 每隔一個字元
text[::-1]   # "nohtyP" - 反轉字串
```

---

## 📖 字典方法 Dict Methods

| 方法 | 功能 | 範例 |
|:---|:---|:---|
| `get(key, default)` | 取得值（安全） | `dict.get("a", 0)` |
| `keys()` | 取得所有鍵 | `dict.keys()` |
| `values()` | 取得所有值 | `dict.values()` |
| `items()` | 取得所有鍵值對 | `dict.items()` |
| `update(dict2)` | 更新/合併字典 | `dict.update({"b": 2})` |
| `pop(key)` | 移除並回傳值 | `dict.pop("a")` |

---

## 🎯 集合運算 Set Operations

| 運算 | 方法 | 運算子 | 說明 |
|:---|:---|:---:|:---|
| 聯集 | `union()` | `\|` | 所有元素 |
| 交集 | `intersection()` | `&` | 共同元素 |
| 差集 | `difference()` | `-` | 只在 A 不在 B |
| 對稱差集 | `symmetric_difference()` | `^` | 不重複的元素 |

---

[⬅️ 返回課程總覽](../README.md) | [上一章 Module3](../Module3/README.md) | [下一章 Module5 ➡️](../Module5/README.md)
