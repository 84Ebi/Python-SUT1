def main():
    try:
        
        
        
        lines = list()
        for i in range(6):
            a = input()
            lines.append(a)
        
        name1 ,name2 = lines[0].split(' ')
        name2 = name2.strip()
        health1 , health2 = lines[1].split(' ')
        health1 = int(health1)
        health2 = int(health2)
        damageA , damageB , damageC = lines[2].split(' ')
        cardsdamage = {'A':damageA,'B':damageB,'C':damageC}
        p1points = 0
        p2points = 0
        
        for i in range(3,6):
            tmpcardp1 ,tmpcardp2 = lines[i].split(' ')
            if int(cardsdamage[tmpcardp1[0]]) > int(cardsdamage[tmpcardp2[0]]):
                p1points += 1
            elif int(cardsdamage[tmpcardp2[0]]) > int(cardsdamage[tmpcardp1[0]]):
                p2points += 1
            health1 -= int(cardsdamage[tmpcardp2[0]])
            health2 -= int(cardsdamage[tmpcardp1[0]])
        print(name1 + " -> Score: "+str(p1points)+', Health: '+str(health1)+'\n'+name2 + " -> Score: "+str(p2points)+', Health: '+str(health2))
        #file1.write(name1 + " -> Score: "+str(p1points)+', Health: '+str(health1)+'\n'+name2 + " -> Score: "+str(p2points)+', Health: '+str(health2))
        
    except:
        print('Invalid Command.')
            
main()