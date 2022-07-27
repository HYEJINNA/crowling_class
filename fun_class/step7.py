# -*- coding: utf-8 -*-
import contextlib
import step6
import time 

@contextlib.contextmanager
def openReadOnly(fileName):


    read_file = open(fileName, mode='r', encoding="utf-8")

    yield read_file

    read_file.close()

def main(fileName):
    with openReadOnly(fileName) as file:
        text= file.read()
    
    n = 0
    for word in text.split():
        if word in ['카카오', '카카오모빌리티']:
            n +=1
    print("단어 갯수:", n)

if __name__ == "__main__":
    fileName = "data/news_article.txt"
    with step6.timer():
        main(fileName)
        time.sleep(0.25)







