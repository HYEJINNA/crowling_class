# -*- coding: utf-8 -*-
# fun_class/data 만들기 

def main():
    print("파일불러오기 시작")
    with open("data/news_article.txt",encoding="utf-8")as file:
        text= file.read()

    print("파일 불러오기 완료!")
    n = 0
    for word in text.split():
        if word in ['거리','한다']:
            n +=1
    print("단어갯수:", n)

if __name__ == "__main__":
    main()