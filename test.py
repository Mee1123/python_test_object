"""
このファイルに解答コードを書いてください
"""




def read(path):#リストの読み出し
    dividen =1
    num_date = {}
    with open(path, 'r') as f:
        line = f.readline()
        while line is not "":
            print("1.最初に取得"+line)
            if ":" in line:
                print(":を確認"+line)
                single = date_entry(line)
                num_date[single[0]] = single[1].strip()
                print("num_dateを更新")
                print(num_date)
            else:
                print(line)
                dividen = int(line)
            line = f.readline()

    print("必要データ")
    print(num_date)
    print(dividen)


def date_entry(line):#データの辞書化
    word_list = "error"
    numer = -1
    try:
        char_list = list(line)
        is_number = True  # どこ:が出現するか
        numer = 0  # 整数i
        word_list: str = ""  # 文字列s
        for word in char_list:
            if word == ':':
                is_number = False
            if is_number:
                numer = int(word) + numer * 10
            else:
                word_list = word_list + str(word)
    except :
        print("エラー")
    return numer, word_list


def FizzBuzz(number):
    out_text = ("", "Fizz")[number % 5 == 0]
    out_text += ("", "Buzz")[number % 3 == 0]
    return out_text


def main():

    path = "sample1.txt"
    read(path)


if __name__ == '__main__':
    main()
