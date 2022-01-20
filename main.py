# -*- coding: utf-8 -*-
# @Time    : 2022/1/20 9:17
# @Author  : Leonard
# @Email   : leoleechn@hotmail.com
# @File    : main.py
# @software: PyCharm

import requests
from bs4 import BeautifulSoup
import pandas
import csv

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/97.0.4692.71 Safari/537.36"}


def allPage():
    urlList = []
    for i in range(10):
        url = "https://book.douban.com/top250?start=" + str(i * 25)
        urlList.append(url)
    return urlList


def pageResponse():
    for url in allPage():
        htmlResponse = requests.get(url, headers=header)
        htmlResponse.encoding = "utf-8"
        mainPage = BeautifulSoup(htmlResponse.text, "html.parser")
        nameMainInfoList = mainPage.find_all("div", class_="pl2")
        nameList = []
        for name in nameMainInfoList:
            bookName = name.find('a')["title"]
            nameList.append(bookName)

        authorMainInfoList = mainPage.find_all('p', class_="pl")
        authorList = []
        for author in authorMainInfoList:
            bookAuthor = author.get_text()
            authorList.append(bookAuthor)

        scoreMainInfoList = mainPage.find_all("span", class_="rating_nums")
        scoreList = []
        for score in scoreMainInfoList:
            bookScore = score.get_text()
            scoreList.append(bookScore)

        itemMainInfoList = mainPage.find_all("span", class_="inq")
        itemList = []
        for item in itemMainInfoList:
            bookItem = item.get_text()
            itemList.append(bookItem)

        # infoDict = {"书名": nameList, "信息": authorList, "评分": scoreList, "主旨": itemList}
        # file = open("data.csv", mode='a', encoding="utf-8")
        # writer = csv.writer(file)
        # writer.writerow(infoDict.values())
        # file.close()

        # dataFrame = pandas.DataFrame.from_dict({"书名": nameList, "信息": authorList, "评分": scoreList, "主旨": itemList},
        #                                        orient="index")
        # dataFrame.to_csv("data.csv", index=False, sep=',')

        # keyList = ["书名", "信息", "评分", "主旨"]
        # valueList = [nameList, authorList, scoreList, itemList]
        # infoList = zip(keyList, valueList)
        # infoDict = dict(infoList)

        # infoList = zip(nameList, authorList, scoreList, itemList)
        # file = open("data.csv", mode='a', encoding="utf-8")
        # writer = csv.writer(file, delimiter='\n')
        # writer.writerow(infoList)
        # file.close()

        keyList = ["书名", "信息", "评分", "主旨"]
        file = open("data.csv", mode='a', encoding="utf-8")
        writer = csv.writer(file)
        writer.writerow(keyList)
        for name, author, score, item in zip(nameList, authorList, scoreList, itemList):
            dataList = [name, author, score, item]
            writer.writerow(dataList)
        file.close()

    print("豆瓣TOP250书籍榜单信息获取完成!")


if __name__ == "__main__":
    pageResponse()
