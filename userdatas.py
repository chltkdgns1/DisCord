from firebases import Data
from FindBaek import FindBaekjoon
from user import Users
import random
import json

down = "큐윳 강화석 77 ㅓ억~"
up = "강화에 성공하였습니다!!!!!"

class UserData :

    def getBaejoonData(self,nick) :
        users = Data.child("Users").child(nick).get()
        if users == None : return None
        return users

    def getUserData(self,nick):
        return Data.child("Users").child(nick).get()

    def getItem(self,nick,item):
        return Data.child("Users").child(nick).child("아이템").get()

    def addUser(self,baekjoonId,nickName,getReinforceCount,rank,solvedProblem,wrong):
        ## 유저 중복되는지도 체크해줘야함
        joonUsers = Data.child("Baejoon").child(baekjoonId).get()

        if joonUsers != None :
             return -1

        users = Users(baekjoonId,getReinforceCount,solvedProblem,rank,wrong) # 마지막요소 디스코드랭킹인데 이건 따로 구해야함 ㅇㅋ?
    
        Data.child("Users").child(nickName).set(json.loads(users.toJSON()))
        Data.child("Users").child(nickName).child("아이템").child("롱소드").set(0)
        Data.child("Baejoon").child(baekjoonId).set(1)

        return 0
        # 파이어 베이스에 새로운 유저 데이터 업데이트

    def printReinforCount(self,nick):
        users = self.getUserData(nick)
        if users == None : return -1
        return users["getReinforceCount"]

    def userCheck(self,nick):
        users = self.getUserData(nick)
        if users == None : return -1
        return 0

    def nickCheck(self,nick):
        users = Data.child("Users").child(nick).get()

        if users == None : return 1
        return -1

    def itempCheck(self,nick,itemName):
        item = self.getItem(nick,itemName)
        if item == None : return -1
        return 0

    def printItemRein(self,nick,itemName):
        item = self.getItem(nick,itemName)
        if item == None : return -1
        return item[itemName]

    def reinforceItem(self,nickName,itemName,u):
        item = self.getItem(nickName,itemName)
        users = self.getUserData(nickName)
        if users == None : return -1
        if item == None : return -2

        if users["getReinforceCount"] == 0 :
            return -3

        r = users["getReinforceCount"]
        u = min(u,r)
        users["getReinforceCount"] -= u


        rein = item[itemName]

        a = 0
        b = 0
        c = 0
        while u != 0 :
            t = random.randrange(1,1001)
            if rein == 0 :
                if t <= 600 : 
                    rein += 1
                    a += 1
                else : 
                    if t <= 900 : 
                        rein -= 1
                        c += 1
                    b += 1
            elif rein == 1 :
                if t <= 500 : 
                    rein  += 1
                    a += 1
                else :  
                    if t <= 850 : 
                        rein -= 1
                        c += 1
                    b += 1
               
            elif rein == 2 :          
                if t <= 350 : 
                    rein  += 1
                    a += 1
                else :  
                    if t <= 800 : 
                        rein -= 1
                        c += 1
                    b += 1
            elif rein == 3 :
                if t <= 300 : 
                    rein  += 1
                    a += 1
                else :  
                    if t <= 700 : 
                        rein -= 1 
                        c += 1
                    b += 1         
            elif rein == 4 :
                if t <= 200 : 
                    rein  += 1
                    a += 1
                else :   
                    if t <= 500 : 
                        rein -= 1
                        c += 1
                    b += 1
         
            elif rein == 5 :
                if t <= 10 :  
                    rein  += 1
                    a += 1
                else :  
                    if t <= 400 : 
                        rein -= 1
                        c += 1
                    b += 1
                
            elif rein == 6 :
                if t <= 1 : 
                    rein  += 1
                    a += 1
                else :  
                    if t <= 300 : 
                        rein -= 1
                        c += 1
                    b += 1
            
            if rein < 0 : rein = 0
            u -= 1

        item[itemName] = rein 
        Data.child("Users").child(nickName).set(users)
        Data.child("Users").child(nickName).child("아이템").set(item)

        res = [] 
        res.append(a)
        res.append(b)
        res.append(c)
        return res

    def update(self,nick):
        users = Data.child("Users").child(nick).get()

        if users == None : return -1
        find = FindBaekjoon(users["baekjoonId"])
        ans = find.Excute()
        cnt =(int(ans[0]) - users["solvedProblem"]) * 5  
        users["getReinforceCount"] += cnt
        users["solvedProblem"] = int(ans[0])
        users["rank"] = int(ans[1])
        users["wrong"] = int(ans[2])
  
        Data.child("Users").child(nick).set(users)

userdata = UserData()