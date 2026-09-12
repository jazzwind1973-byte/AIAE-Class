# 🏗️ Module 6：物件導向程式設計 OOP

> 學習類別與物件的概念，掌握物件導向程式設計的基礎

---

## 🎯 學習目標

完成本模組後，你將能夠：
- ✅ 理解類別與物件的概念
- ✅ 定義類別與建立物件實例
- ✅ 使用類別屬性與實例屬性
- ✅ 定義與呼叫方法
- ✅ 實作繼承與方法覆寫

---

## 📂 檔案結構

| 檔案 | 內容 | 類型 |
|:---|:---|:---:|
| `6-1.ipynb` | 🏗️ 類別與物件基礎 | 教學 |
| `6-2_class.ipynb` | 🔧 類別設計與繼承 | 教學 |

---

## 🏗️ 類別與物件基礎

### 📋 基本概念

| 術語 | 說明 | 比喻 |
|:---|:---|:---|
| **類別 (Class)** | 物件的藍圖/模板 | 汽車設計圖 |
| **物件 (Object)** | 類別的實例 | 實際的汽車 |
| **屬性 (Attribute)** | 物件的特徵/資料 | 汽車的顏色、品牌 |
| **方法 (Method)** | 物件的行為/功能 | 汽車的啟動、煞車 |

---

## 📝 類別定義語法

```python
class ClassName:
    """類別說明文件"""

    # 類別屬性（所有實例共享）
    class_attribute = "value"

    # 建構子（初始化方法）
    def __init__(self, param1, param2):
        # 實例屬性
        self.param1 = param1
        self.param2 = param2

    # 實例方法
    def method_name(self):
        return self.param1
```

---

## 📌 範例：定義 Dog 類別

```python
class Dog:
    """狗狗類別"""

    # 類別屬性
    species = "Canis familiaris"

    def __init__(self, name, age):
        # 實例屬性
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def description(self):
        return f"{self.name} is {self.age} years old"

# 建立物件
my_dog = Dog("Buddy", 3)
print(my_dog.bark())        # Buddy says Woof!
print(my_dog.description()) # Buddy is 3 years old
```

---

## 🔧 繼承 Inheritance

### 📋 概念
- 子類別可以繼承父類別的屬性和方法
- 子類別可以新增自己的屬性和方法
- 子類別可以覆寫（override）父類別的方法

```python
# 父類別
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

# 子類別
class Cat(Animal):
    def speak(self):  # 覆寫父類別方法
        return f"{self.name} says Meow!"

class Dog(Animal):
    def speak(self):  # 覆寫父類別方法
        return f"{self.name} says Woof!"

# 使用
cat = Cat("Whiskers")
dog = Dog("Buddy")
print(cat.speak())  # Whiskers says Meow!
print(dog.speak())  # Buddy says Woof!
```

---

## 📋 常用魔術方法 Magic Methods

| 方法 | 說明 | 使用時機 |
|:---|:---|:---|
| `__init__` | 建構子 | 初始化物件時 |
| `__str__` | 字串表示 | `print(obj)` 時 |
| `__repr__` | 開發者表示 | 偵錯時 |
| `__len__` | 長度 | `len(obj)` 時 |
| `__eq__` | 相等比較 | `obj1 == obj2` 時 |

---

## 🎮 練習題

### 練習 1：建立 Student 類別
- 屬性：name, student_id, grades (列表)
- 方法：
  - `add_grade(grade)` - 新增成績
  - `get_average()` - 計算平均成績

### 練習 2：繼承練習
- 建立 `Shape` 父類別
- 建立 `Rectangle` 和 `Circle` 子類別
- 實作 `area()` 方法計算面積

---

[⬅️ 返回課程總覽](../README.md) | [上一章 Module5](../Module5/README.md) | [下一章 Module7 ➡️](../Module7/README.md)
