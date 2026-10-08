- python 題目
    1. 總分
        
        ```python
        for student_grade in students_grade:
            total = 0
            for key, value in student_grade.items():
                # print(key, value)
                if key == "name": # 相加分數時，忽略這個 key
                    continue
                total += value
            print(f"{student_grade['name']:8} 總分: {total:3} 分")
        
        ```
        
    2. 平均
        
        ```python
        for student_grade in students_grade:
            total = 0
            cnt = 0
            for key, value in student_grade.items():
                # print(key, value)
                if key == "name": # 相加分數時，忽略這個 key
                    continue
                cnt += 1
                total += value
            print(f"{student_grade['name']:8} 總分: {total/cnt:3.2f} 分")
        
        ```
        
    3. 最高分
        
        ```python
        result = ""
        highest_score = 0
        for student_grade in students_grade:
            if student_grade["數學"] > highest_score:
                # 紀錄目前的最高分和學生姓名
                highest_score = student_grade["數學"] 
                result = student_grade["name"]
        
        print(result)
        ```
        
    4. 國文平均
        
        ```python
        total = 0
        for student_grade in students_grade:
            print(student_grade["國文"])
            total += student_grade["國文"]
        print(f"{total/len(students_grade):.2f}")
        ```
        
    5. 不及格
        
        ```python
        result = set()
        for student_grade in students_grade:
            for key, value in student_grade.items():
                if key == "name":
                    continue
                if value < 60:
                    # print(student_grade["name"])
                    result.add(student_grade["name"])
        
        print(list(result))
        ```
        
    6. 新增總分
        
        ```python
        for student_grade in students_grade:
            total = 0
            for key, value in student_grade.items():
                # print(key, value)
                if key == "name": # 相加分數時，忽略這個 key
                    continue
                total += value
            # print(f"{student_grade['name']:8} 總分: {total:3} 分")
            student_grade["總分"] = total
        
        print(students_grade)
        ```
        
    7. 三科大於80
        
        ```python
        for student_grade in students_grade:
            cnt = 0
            for key, value in student_grade.items():
                if key == "name" or key == "總分":
                    continue
                
                if value > 80:
                    cnt += 1
                
                if cnt >= 3:
                    print(student_grade["name"])
        ```
        
    8. 整理
        
        ```python
        result = {}
        for student_grade in students_grade:
            result[student_grade["name"]] = {}
            for key, value in student_grade.items():
                if key == "name":
                    continue
                result[student_grade["name"]][key] = value
        
        print(result)
        ```
        
        ```python
        result = {}
        for student_grade in students_grade:
            copy_student_grade = student_grade.copy() # 複製一份資料出來
            copy_student_grade.pop("name") # 移除 name 的資料 只保留成績
            result[student_grade["name"]] = copy_student_grade
        
        print(result)
        ```