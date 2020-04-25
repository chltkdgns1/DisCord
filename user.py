import json
class Users :
    baekjoonId = ""
    getReinforceCount = 0 # 남은 강화횟수
    solvedProblem = 0
    rank = 0
    wrong = 0

    def __init__(self,baekjoonId,getReinforceCount,solvedProblem,rank,wrong):
        self.baekjoonId = baekjoonId
        self.getReinforceCount = getReinforceCount
        self.solvedProblem = solvedProblem
        self.rank = rank
        self.wrong = wrong

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)