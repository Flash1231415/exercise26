# 연습문제 4-1: 라인번호 출력 및 .sav 파일 저장
from pathlib import Path

def main():
    while True:
        filename = input("읽을 파일명 (Quit! 종료): ").strip()
        if filename == 'Quit!':
            return
        path = Path(filename)
        try:
            with path.open(encoding='utf-8') as source:
                lines = source.readlines()
        except FileNotFoundError:
            print("파일이 없습니다. 다른 파일명을 입력하세요.")
            continue
        except (OSError, UnicodeError) as error:
            print("파일을 읽을 수 없습니다:", error)
            continue
        numbered = ''.join(f"{i} {line.rstrip(chr(10)).rstrip(chr(13))}\n"
                           for i, line in enumerate(lines, 1))
        print(numbered, end='')
        output = path.with_suffix('.sav')
        if output == path:
            output = path.with_name(path.stem + '_numbered.sav')
        try:
            output.write_text(numbered, encoding='utf-8')
        except OSError as error:
            print("파일을 저장할 수 없습니다:", error)
            return
        print("저장 완료:", output)
        return

if __name__ == '__main__':
    main()
