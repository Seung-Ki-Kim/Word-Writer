## main.py
import random
import sys
import os

def answer_check_word(answer_words, words_en, random_index) :
    if (answer_words == words_en[random_index]) :
        return "Correct!"
    else :
        return words_en[random_index]

def answer_check_sentence(answer_sentences, sentences_en, random_index) :
    if (sentences_en[random_index] == answer_sentences) :
        return "Correct!"
    else :
        return sentences_en[random_index]

def resource_path(relative_path) :
    try :
        base_path = sys._MEIPASS
    except Exception :
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main() :
    while (True) :
        unit = "Unit " + input("Please enter the Unit number: ")

        try :
            words_en_path = resource_path("Resource/" + unit + "/Words_EN.txt")
            words_kor_path = resource_path("Resource/" + unit + "/Words_KOR.txt")
            sentences_en_path = resource_path("Resource/" + unit + "/Sentences_EN.txt")
            sentences_kor_path = resource_path("Resource/" + unit + "/Sentences_KOR.txt")

            with open(words_en_path, encoding = "UTF-8") as words :     ## 영단어
                words_en = words.readlines()

            with open(words_kor_path, encoding = "UTF-8") as words :    ## 한국어 단어
                words_kor = words.readlines()

            with open(sentences_en_path, encoding = "UTF-8") as sentences :    ## 영문장
                sentences_en = sentences.readlines()

            with open(sentences_kor_path, encoding = "UTF-8") as sentences :   ## 한국어 문장
                sentences_kor = sentences.readlines()

            break
        except FileNotFoundError :
            print("This unit isn't ready yet.")

    words_en = [i.strip() for i in words_en]
    words_kor = [i.strip() for i in words_kor]

    sentences_en = [i.strip() for i in sentences_en]
    sentences_kor = [i.strip() for i in sentences_kor]

    while (True) :
        random_index = random.randrange(0, len(words_en))

        question_words = words_kor[random_index]
        question_sentences = sentences_kor[random_index]

        print("- Please answer the question.")

        print("Q1: " + question_words)
        answer_words = input("A1: ")

        if (answer_words == "/exit") :
            break
        elif (answer_words == "/pass") :
            print(words_en[random_index])
            print()

            continue

        print("Q2: " + question_sentences)
        answer_sentences = input("A2: ")

        if (answer_sentences == "/exit") :
            break
        elif (answer_sentences == "/pass") :
            print(words_en[random_index])
            print(sentences_en[random_index])
            print()

            continue

        print("- Result")
        print(answer_check_word(answer_words, words_en, random_index))
        print(answer_check_sentence(answer_sentences, sentences_en, random_index))
        print()



if (__name__ == "__main__") :
    main()