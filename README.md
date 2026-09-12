# AIAE Class

AI 應用工程師養成班的集中式學習紀錄。

這個 repository 用來同步家裡與學校兩台電腦上的課程檔案。Python、HTML/CSS、JavaScript、MySQL、課堂筆記、考試與跨科專案都集中在同一個 Git repository 中。

## 資料夾

- `01_Python/`：Python 課程與練習，保留原本的 Module 結構
- `02_HTML_CSS/`：HTML 與 CSS 課程
- `03_JavaScript/`：JavaScript 課程，保留原本的模組結構
- `04_MySQL/`：MySQL 課程與 SQL 檔案
- `05_Other_Courses/`：其他課程
- `Projects/`：跨科整合專案
- `Exams/`：測驗、考前練習與訂正
- `Notes/`：自己的跨科筆記與重點整理

> Git 不會保存真正的空資料夾，因此尚未放入課程內容的資料夾會先保留 `.gitkeep`。

## 雙機同步流程

### 每次開始寫程式前

```bash
git pull
```

### 完成當次課程或練習後

```bash
git status
git add .
git commit -m "YYYY-MM-DD 科目：本次內容"
git push
```

例如：

```bash
git commit -m "2026-09-12 JavaScript：陣列與函式練習"
```

### 回到另一台電腦

```bash
git pull
```

## 最重要的規則

1. 開始工作前先 `git pull`。
2. 結束工作後再 `git add`、`git commit`、`git push`。
3. 不要讓家裡與學校兩台電腦同時修改同一個檔案。
4. 執行 `git status` 確認狀態後再離開。
5. 不上傳密碼、API Key、資料庫密碼、`.env` 或虛擬環境。

## 首次下載

```bash
git clone https://github.com/jazzwind1973-byte/AIAE-Class.git
cd AIAE-Class
```

舊的 `python` 與 `Javascript-class` repositories 暫時保留作為原始備份。
