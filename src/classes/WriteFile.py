# -*- coding: utf-8 -*-
import json
from distutils.log import error

class WriteFile:

    def setName(self, fileName):
        self.name = fileName

    def writeTweet(self, fileData):
        with open(self.name, "w", encoding="utf-8") as file:
            try:
                list_object_tweets = []

                for tweet in fileData:
                    list_object_tweets.append({
                        "id": tweet.id,
                        "text": tweet.text,
                        "likes": tweet.likes,
                        "created_at": tweet.created_at,
                        "source": tweet.source
                    })
                
                data = {
                    "tweets": list_object_tweets
                }
                json.dump(data, file, indent=4)
                print("Arquivo salvo")
            except Exception as ex:
                raise error("Erro ao salvar arquivo", ex)

        # with open(self.name, "w") as file:
        #     try:
        #         writer = csv.writer(file)
        #         writer.writerow(("id", "name", "text", "likes", "retweets", "created_at", "source"))
        #         for tweet in fileData:
        #             writer.writerow((
        #                 str(tweet.id), 
        #                 tweet.name, 
        #                 tweet.text, 
        #                 str(tweet.likes), 
        #                 str(tweet.retweets), 
        #                 tweet.created_at, 
        #                 tweet.source
        #             ))
        #         print("Arquivo salvo")
        #     except Exception as ex:
        #         raise error("Erro ao salvar arquivo", ex)



        # line = ""

        # header = "id; name; text; likes; retweets; created_at; source\n"
        # file.write(header)

        # for tweet in fileData:
        #     line += str(tweet.id) + "; "
        #     line += tweet.name + "; "
        #     line += tweet.text + "; "
        #     line += str(tweet.likes) + "; "
        #     line += str(tweet.retweets) + "; "
        #     line += tweet.created_at + "; "
        #     line += tweet.source + "\n"
        #     file.write(line)
        #     line = ""

        # file.close()

    def readFile(self):
        file = open(self.name, "r", encoding="utf-8")
        print(file.read())
        file.close()