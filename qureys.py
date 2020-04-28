from firebases import Data
from userdatas import userdata
import time

class Qurey:

    def setProblem(self,problem,name):
        Data.child("Problem").child(problem).set(name)
    
    def getProblem(self):
        problem = Data.child("Problem").get()

        if problem == None : return " 텅 ~ 비었습니다."
        if type(problem) == int : return " 텅 ~ 비었습니다."

        s = ""
        for a,b in problem.items():
            s += b + '\n'

        return s

    def clearProblem(self,problem):
        if problem == "" : 
            Data.child("Problem").delete()
            return

        Data.child("Problem").child(problem).delete()

    def rankingStart(self): #랭크게임 시작
        now = time.gmtime(time.time())

        users = Data.child("Users").get()
        data = Data.child("rank").get()

        if users == None : return -1
        if data != None : return -2
        if time != None : return -2

        t = str(now.tm_year) + "-" + str(now.tm_mon) + "-" + str(now.tm_mday) + " , " + str(now.tm_hour) + ":" + str(now.tm_min)
        Data.child("time").set(t)

        for a,b in users.items():
            userdata.update(a) 

        for a,b in users.items():
            Data.child("rank").child(a).set(b["solvedProblem"])

    def rankEx(self):   #랭크게임보기
        data = Data.child("rank").get()

        if data == None : return -1
        if time == None : return -2

        for a,b in data.items() :
            userdata.update(a) 

        users = Data.child("Users").get()

        x = []
        for a,b in users.items():
            temp = []
            temp.append(a)
            temp.append(b["solvedProblem"] - data[a])
            x.append(temp)
        
        x.sort(key = lambda x:x[1])

        ans = "시작 시간 : " + Data.child("time").get() + "\n"
        rk = 1
        for i in range(len(x) - 1,-1,-1):
            ans += str(rk) + "위 - " + x[i][0] + "님 푼 문제수 - " + str(x[i][1]) + '\n' 
            rk += 1

        return ans
    
    def rankingEnd(self): # 랭크게임끝내기
        data = Data.child("rank").get()

        if data == None : return -1

        now = time.gmtime(time.time())
        t = str(now.tm_year) + "-" + str(now.tm_mon) + "-" + str(now.tm_mday) + " , " + str(now.tm_hour) + ":" + str(now.tm_min)
        ans = "종료 시간 : " + t + "\n"
        ans += "최종순위 발표 : \n"
        ans += self.rankEx()
        Data.child("rank").delete()
        Data.child("time").delete()

        return ans