n = int(input())
students = [] # 학생 정보를 담을 리스트

# 모든 학생 정보를 입력받기
for _ in range(n):
    students.append(input().split())

'''
1) 두 번째 원소를 기준으로 내림차순 정렬
2) 두 번재 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
3) 세 번재 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
4) 네 번재 원소가 같은 경우, 첫 번재 원소를 기준으로 오름차순 정렬
'''
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬되 학생 정보에서 이름만 출력
for student in students:
    print(student[0])

'''
12
JunKyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
'''