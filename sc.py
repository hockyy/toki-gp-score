import json

totalScore = dict()
GPrank = [100, 75, 60, 50, 45, 40, 36, 32, 29, 26, 24, 22, 20, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
finalData = []
FIRSTGP = 16
LASTGP = 25

def main():
    for i in range(FIRSTGP, LASTGP + 1):
        try:
            contestID = f'TROC #{i}'
            with open(str(i) + '.json', 'r') as scoreData:
                score = json.loads(scoreData.read())
                rank = 0
                for details in score['indonesiaData']:
                    if(details['username'] not in totalScore.keys()):
                        totalScore[details['username']] = dict()
                    totalScore[details['username']][contestID] = GPrank[rank]
                    rank += 1
        except:
            break
    for contestant in totalScore.keys():
        peopleData = dict()
        peopleData['username'] = contestant
        finalScore = 0
        for i in range(FIRSTGP, LASTGP + 1):
            contestID = f'TROC #{i}'
            if(contestID in totalScore[contestant].keys()):
                peopleData[contestID] = totalScore[contestant][contestID]
                finalScore += totalScore[contestant][contestID]
            else:
                peopleData[contestID] = 0
        peopleData['Total Score'] = finalScore
        finalData.append(peopleData)
    print(json.dumps(sorted(finalData, key = lambda i: i['Total Score'], reverse = True)))

if __name__ == '__main__':
    main()
