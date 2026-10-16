# 연습문제 4-2: 공백 제외 글자 수, 단어 수, 라인 수
from pathlib import Path

def main():
    while True:
        filename = input("읽을 파일명 (Quit! 종료): ").strip()
        if filename == 'Quit!':
            return
        try:
            text = Path(filename).read_text(encoding='utf-8')
        except FileNotFoundError:
            print("파일이 없습니다. 다른 파일명을 입력하세요.")
            continue
        except (OSError, UnicodeError) as error:
            print("파일을 읽을 수 없습니다:", error)
            continue
        characters = sum(not char.isspace() for char in text)
        words = len(text.split())
        # 마지막 개행은 새 빈 줄로 세지 않는다. 빈 파일은 0줄이다.
        lines = text.count('\n') + (1 if text and not text.endswith('\n') else 0)
        print(f"characters : {characters}")
        print(f"words      : {words}")
        print(f"lines      : {lines}")
        return

if __name__ == '__main__':
    main()
