# -*- coding: utf-8 -*-
from connections.Twitter import Twitter
from classes.WriteFile import WriteFile

def main():
    tt = Twitter()

    print("Escreva quais palavras você gostaria de pesquisar:")
    words = input()

    list_tweets = tt.searchTweets(str(words))
    print(list_tweets)

    print("Deseja escrever em um arquivo JSON? \n S - SIM \n N- - NÃO")
    isWriteFile = input()

    if(isWriteFile.upper() == "S"):
        print("Escreva o nome do arquivo:")
        fileName = input()
        file = WriteFile()
        file.setName(fileName + ".json")
        file.writeTweet(list_tweets)
        file.readFile()
    else:
        print("FIM!")


main()
