
#Variables
occupied_carriers = 52
pilots_carriers = 4
data_carriers = 48
porteuses_donnees = open('porteuses.txt','wt')
porteuses_pilotes = open('pilotes.txt','wt')
space = 14 #Spacing betwwen pilots

carriers = list(range(int(-occupied_carriers/2),0))+list(range(1,int(occupied_carriers/2+1)))

p = [ ((2*i+1)-pilots_carriers)*int(space/2) for i in list(range(int(pilots_carriers)))]
[carriers.remove(i) for i in p]

porteuses_pilotes.write(str((p,)))
porteuses_donnees.write(str((carriers,))) 
porteuses_pilotes.close()
porteuses_donnees.close()
