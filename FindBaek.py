import requests
from bs4 import BeautifulSoup    #BeautifulSoup import

class FindBaekjoon :
    pi = [] 
    url = 'https://www.acmicpc.net/user/'
    nickName = ""
    getString = []
    htmlString =""
    response = ""


    def __init__(self,nickName):
        self.pi = []
        self.getString = []
        self.nickName = nickName
        print(self.getString)
        self.getString.append("<a href='/status?user_id=" + nickName + "&amp;result_id=4'>")
        self.getString.append("<td>")
        self.getString.append('<a href="/status?user_id=' + nickName + '&amp;result_id=6">')

        self.response = requests.get(self.url + self.nickName)
        self.htmlString = self.response.text

        for i in range(0,3) : 
            self.getPi(i)

    def getPi(self,idx) :
        c = 0
        pis = []
        for i in range(0, 300):
            pis.append(0)

        for i in range(1,len(self.getString[idx])):
            if self.getString[idx][c] == self.getString[idx][i] :
                c += 1
                pis[i] = c
            elif c != 0 :
                c = pis[c - 1]
                i -= 1

        self.pi.append(pis)


    def find(self,index):
        c  = 0
        idx = -1
        getlen = len(self.getString[index])
        htmllen = len(self.htmlString)
        ans = ""
        for i in range(0,htmllen) :
            if self.getString[index][c] == self.htmlString[i] :
                c += 1
                if c == getlen : 
                    c = self.pi[index][c]
                    idx = i
                    break

            elif c != 0:
                c = self.pi[index][c - 1]
                i -= 1

        if idx != -1 :
            for i in range(idx + 1,htmllen) :
                if self.htmlString[i] == '<' : break
                ans += self.htmlString[i]

        return ans 

    def Excute(self):
        ans = []
        for i in range(0,3) :
            ans.append(self.find(i))

        return ans
