from firebases import Data
from userdatas import userdata

class Qurey:

    def setProblem(self,problem,name):
        Data.child("Problem").child(problem).set(name)
    
    def getProblem(self):
        problem = Data.child("Problem").get()

        if problem == None : return " 텅 ~ 비었습니다."
        if type(problem) == int : return " 텅 ~ 비었습니다."

        s = "추천된 문제들 ^^ \n----------------------\n"
        for a,b in problem.items():
            s += b + '\n'

        s += "----------------------"
        return s

    def clearProblem(self,problem):
        if problem == "" : 
            Data.child("Problem").delete()
            return

        Data.child("Problem").child(problem).delete()

    def rankingStart(self): #랭크게임 시작
        users = Data.child("Users").get()
        data = Data.child("rank").get()

        if users == None : return -1
        if data != None : return -2

        for a,b in users.items():
            userdata.update(a) 

        for a,b in users.items():
            Data.child("rank").child(a).set(b["solvedProblem"])

    def rankEx(self):   #랭크게임보기
        data = Data.child("rank").get()

        if data == None : return -1

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

        ans = ""
        rk = 1
        for i in range(len(x) - 1,-1,-1):
            ans += str(rk) + "위 - " + x[i][0] + "님 푼 문제수 - " + str(x[i][1]) + '\n' 
            rk += 1

        return ans
    
    def rankingEnd(self): # 랭크게임끝내기
        data = Data.child("rank").get()

        if data == None : return -1

        ans = "최종순위 발표 : \n"
        ans += self.rankEx()
        Data.child("rank").delete()

        return ans