# 연습문제 2-2: 학생 명단 작성과 학번 조회
def main():
    students = {}
    while True:
        s = input("학번과 이름 입력 (Fin! 입력 종료, Quit! 프로그램 종료): ").strip()
        if s == 'Quit!':
            print("프로그램 종료")
            return
        if s == 'Fin!':
            break
        parts = s.split()
        if len(parts) != 2:
            print("학번과 이름을 공백으로 구분하여 입력하세요.")
            continue
        student_id, name = parts
        students[student_id] = name
    print("명단:", students)
    while True:
        student_id = input("조회할 학번 (Quit! 종료): ").strip()
        if student_id == 'Quit!':
            print("프로그램 종료")
            return
        print(students.get(student_id, 'not found!'))

if __name__ == '__main__':
    main()
