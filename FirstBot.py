import discord
import json
from qureys import Qurey
from userdatas import userdata
from FindBaek import FindBaekjoon
cilent = discord.Client()

qurey = Qurey()

@cilent.event
async def on_read():
    game = discord.Game("알고리즘빡공중..")
    await client.change_presence(status=discord.Status.online, activity=game)

@cilent.event
async def on_message(message):

    nick = str(message.author)
    print(nick)
    s = nick.split('#')
    r = s[0] + s[1]
    nick = r

    if message.content.startswith("!명령어") :
        await message.channel.send("\
        \n\n오늘 새로한 업데이트 !!!!!!!\
        \n\n명령어 : !랭겜시작 \
        \n주어진 시간 동안 백준 문제를 풀어서 푼 사람의 순위를 알 수 있습니다.\
        \n--------------------------------\
        \n\n명령어 : !랭크보기 \
        \n랭겜시작하고 난 후의 순위를 볼 수 있습니다.\
        \n\n명령어 : !랭겜끝 \
        \n랭겜을 종료합니다.\
        \n--------------------------------\
        \n\n명령어 : !백준 \
        \n자신의 백준 랭킹, 풀은 문제, 틀린 문제를 알 수 있습니다.\
        \n--------------------------------\
        \n\n명령어 : !업데이트 \
        \n자신의 백준 랭킹, 풀은 문제, 틀린 문제를 디비와 연동합니다.\
        \n--------------------------------\
        \n\n명령어 : !등록 자신의 백준 ID\
        \n문제푼 횟수 * 5 로 강화석 지급\
        \n7강시 기프티콘 제공합니다\
        \n--------------------------------\
        \n\n명령어 : !강화 \
        \n추가된 명령어는 !강화 5\
        \n이런식으로 5번 연속강화 가능합니다.\
        \n10번 초과는 안되는 참고바랍니다.\
        \n초기버전이라 롱소드밖에 없습니다.\
        \n강화석을 모두 소진하면 더 이상 강화가 되지 않습니다.\
        \n--------------------------------\
        \n\n명령어 : !아이템 \
        \n자신의 강화한 아이템을 볼 수 있습니다.\
        \n초기버전이라 롱소드밖에 없습니다.\
        \n--------------------------------\
        \n\n명령어 : !추천 문제번호 + ' ' + 할말적어주면됩니다. \
        \n추천할 문제번호를 적고 내용을 간략하게 적어주세요\
        \n추천된 문제는 1주일 간격으로 초기화됩니다.\
        \n--------------------------------\
        \n\n명령어 : !문제 \
        \n추천된 문제를 출력합니다.\
        \n--------------------------------\
        \n\n명령어 : !클리어 \
        \n추천된 문제를 삭제합니다.\
        \n!클리어 + ' ' + 문제번호를 적으면\
        \n해당 문제만 삭제됩니다.\
        \n--------------------------------\
        \n\n명령어 : !강화석 \
        \n강화석의 남은 갯수를 볼 수 있습니다.\
        \n--------------------------------")

    elif message.content.startswith("!추천"):
        strs = message.content

        strArr = strs.split(' ')
        if len(strArr) < 2 :
            await message.channel.send("추천할 내용을 입력해주세요")
            return

        if strArr[1].isdigit() :
            if 1000 > int(strArr[1]) or int(strArr[1]) > 20000 :
                await message.channel.send("제대로된 문제번호를 입력해주세요")
                return
        else:
            await message.channel.send("올바른 형식이 아닙니다.")
            return

        sumStr = "| " + nick  + " | " + ' :  | ' + strArr[1] + ' | '  

        for i in range(2,len(strArr)) :
            sumStr += strArr[i] + ' '

        qurey.setProblem(strArr[1],sumStr)
        await message.channel.send("완료되었습니다.")
        
        return

    elif message.content.startswith("!랭겜끝") :
        ans = qurey.rankingEnd()

        if ans == -1 : 
            await message.channel.send("랭크게임이 시작중이지 않습니다.")
            return
       
        await message.channel.send(ans)
        return
 

    elif message.content.startswith("!랭겜시작") :
        ans = qurey.rankingStart()

        if ans == -1 :
            await message.channel.send("랭크게임 중이지 않습니다.")
            return
        elif ans == -2 :
            await message.channel.send("진행 중인 랭크게임이 존재합니다.")
            return

        await message.channel.send("지금부터 푼 문제수를 세서 랭킹을 출력합니다.")
        return

   
    elif message.content.startswith("!랭크보기") :
        ans = qurey.rankEx()    

        if ans == -1 :
            await message.channel.send("랭크게임이 시작하지 않았습니다.")
            return 

        await message.channel.send(ans)
        return


    elif message.content.startswith("!문제") :
        await message.channel.send(qurey.getProblem())
        return


    elif message.content.startswith("!클리어") :
        strs = message.content

        strArr = strs.split(' ')

        if len(strArr) == 1 :
            qurey.clearProblem("")
            await message.channel.send("추천문제가 삭제되었습니다.")
            return

        if strArr[1].isdigit() == False :
            await message.channel.send("입력 양식이 올바르지 않습니다.")
            return
  
        qurey.clearProblem(strArr[1])
        await message.channel.send("추천문제가 삭제되었습니다.")

        return    
        
    elif message.content.startswith("!백준") :
        ans = userdata.getBaejoonData(nick)
        if ans == None : 
            await message.channel.send("존재하지 않는 아이디입니다. 등록해주세요")
            return

    #  baekjoonId = ""
    #
    # solvedProblem = 0
    # rank = 0
    # wrong = 0
    #    print(  "백준 아이디 - "+ans["baekjoonId"] + "\
    #    \n랭킹       -  " + str(ans["rank"]) + "\
    #    \n풀은 문제  -  " + str(ans["solvedProblem"])+ "\
    #    \n틀린 횟수  -  " + str(ans["wrong"]) + "\n")

        await message.channel.send(  "백준 아이디 - "+ans["baekjoonId"] + "\
        \n랭킹              -  " + str(ans["rank"]) + "\
        \n풀은 문제     -  " + str(ans["solvedProblem"])+ "\
        \n틀린 횟수     -  " + str(ans["wrong"]) + "\n")
        return

    elif message.content.startswith("!강화석") :


        ans = userdata.printReinforCount(nick)

        if ans == -1 :
            await message.channel.send("존재하지 않는 아이디입니다. 등록해주세요")
            return

        await message.channel.send(nick + "님의 남은 강화석 수는 " + str(ans) + " 입니다.\
            \n알고리즘 문제를 풀어서 강화석을 얻어주세요 화이팅 ㅎ")

        return


    elif message.content.startswith("!아이템") :

        ans = userdata.printItemRein(nick,"롱소드")

        if ans == -1 :
            await message.channel.send("존재하지 않는 아이디입니다. 등록해주세요")
            return
        await message.channel.send(nick + "님의 롱소드는 " + str(ans) + " 강 입니다.")
        return
    elif message.content.startswith("!강화"):
        
        ch = userdata.userCheck(nick)
        if ch == -1 :
            await message.channel.send("존재하지 않는 아이디입니다. 등록해주세요")
            return

        strs = message.content

        splitStr = strs.split(" ")
        
        u = 1
        if len(splitStr) == 2 : 
            u = int(splitStr[1])

        elif len(splitStr) > 2 :
            await message.channel.send("잘못된 형식입니다. 다시 시도해주세요")
            return

        if u > 100 : u = 100
        ans = userdata.reinforceItem(nick,"롱소드",u)
        if ans == "-1" :
            await message.channel.send("존재하지 않는 아이디입니다. 등록해주세요")

        elif ans == "-2" :
            await message.channel.send("존재하지 않는 아이템입니다. 등록해주세요 (아직 등록란 없음 이거 출력되면 버그)")
            return

        elif ans == "-3" :
            await message.channel.send("강화석이 부족합니다.")
            return
        
        await message.channel.send(ans)
        cnt = userdata.printItemRein(nick,"롱소드")
        
        await message.channel.send(nick +" 님의 롱소드가 " + str(cnt) +" 강이 되었습니다.!!!!!")
        return

    elif message.content.startswith("!업데이트"):
        ans = userdata.update(nick)

        if ans == -1 : 
            await message.channel.send("존재하지 않는 아이디입니다. 등록해주세요")
            return 

        await message.channel.send("백준아이디와 디비를 동기화 완료했습니다")

        ans = userdata.getBaejoonData(nick)
        if ans == None : 
            await message.channel.send("존재하지 않는 아이디입니다. 등록해주세요")
            return

        await message.channel.send(  "백준 아이디 - "+ans["baekjoonId"] + "\
        \n랭킹              -  " + str(ans["rank"]) + "\
        \n풀은 문제     -  " + str(ans["solvedProblem"])+ "\
        \n틀린 횟수     -  " + str(ans["wrong"]) + "\n")
        return

    elif message.content.startswith("!등록"):
        strs = message.content

        ans = userdata.nickCheck(nick)
        if ans == -1 : 
            await message.channel.send("이미 등록된 닉네임입니다.")
            return

        arr = strs.split(" ")

        arrLen = len(arr)
        if arrLen > 2 or arrLen < 2:
            await message.channel.send("잘못된 형식입니다. 다시 시도해주세요")
            return

        await message.channel.send("사이트에서 데이터를 가져오는데 시간이 걸릴 수 있습니다.")

        #ch = userdata.checkSameBaekJoonID(arr[1])
        #if ch == -1 :
        #    await message.channel.send("이미 등록된 백준 아이디입니다. 다른 아이디를 이용해주세요")
        #    return 

        t = FindBaekjoon(arr[1])
        FindUsers = t
        ans = FindUsers.Excute()
        if ans[0] == "" : 
            await message.channel.send("아이디가 존재하지 않거나 문제를 한 문제도 풀지 않았습니다. 다시 시도해주세요")
            return

        await message.channel.send("등록하는중입니다. 기다려주세요...")


        res = userdata.addUser(arr[1],nick,int(ans[0]) * 5,int(ans[1]),int(ans[0]),int(ans[2]))

        #def addUser(self,baekjoonId,nickName,getReinforceCount,rank,solvedProblem,wrong):

        if res == -1 :
            await message.channel.send("계정은 하나만 사용 가능합니다")
            return

        await message.channel.send("성공적으로 등록하였습니다.")
        return

    elif message.content.startswith("안녕") :
        await message.channel.send("오늘도 힘찬 알고리즘 보낼까요? ㅎ")
        return
    elif message.content.startswith("ㅅㅂ") :
        await message.channel.send("^^ ㅣ 발 ㅈ같네 ㅎㅎ 봇이라 더 ㅈ같음 ㅎ")
        return
    elif message.content.startswith("하이") :
        await message.channel.send("오늘도 힘찬 알고리즘 보낼까요? ㅎ")
        return

cilent.run("x")