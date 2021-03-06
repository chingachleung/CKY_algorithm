# binary grammar fixed with probabilty

grammar1 = {"S->NP VP":0.9,"S->VP": 0.1,"VP->N NP":0.5,"VP->V":0.1,"VP->V @VP_V":0.3, "VP->V PP": 0.1,
           "@VP_V->NP PP": 0.1, "NP->NP NP":0.1,"NP->NP NP": 0.2, "NP->N":0.7,"PP->P NP":1.0,
           "N->people":0.5,"N->fish":0.2,"N->tanks":0.2,"N->rods":0.1,"V->people":0.1,"V->fish":0.6,"V->tanks":0.1,
           "P->with":1} 
        
#transform the grammar into a list of tuple :

nonterms_list = []
for key in grammar1.keys():
    rule_split = key.split("->")
    if rule_split[0] not in nonterms_list:
        nonterms_list.append(rule_split[0]) 
nonterms_list

#Step one: assign catergory to each word 

sent = "fish people fish tanks".split()
n = len(sent)
table = [[{} for i in range(n+1)] for j in range(n+1)]

back = [[{} for i in range(n+1)] for j in range(n+1)]
print(table)


#handle first diagonal(assign classes, combine unary rules and look for the higest probabilities)

for i in range(len(sent)):
    for A in nonterms_list:
        temp_rule = "{}->{}".format(A,sent[i])
        if temp_rule in grammar1.keys():
            print(temp_rule + ":" + str(grammar1[temp_rule]))
            table[i][i+1][A] = grammar1[temp_rule]
            #handle unaries 
            for B in nonterms_list:
                temp_rule = "{}->{}".format(B,A)
                if temp_rule in grammar1.keys():
                    prob = grammar1[temp_rule] * table[i][i+1][A]
                    if B in table[i][i+1].keys():
                        if (prob>table[i][i+1][B]):
                            table[i][i+1][B] = prob # to replace existing non-terms rule with higher Prob
                            back[i][i+1][B] = A # to trace back to the root nodes 
                    else:
                        table[i][i+1][B] = prob
                    #handle unaries from non-terminal node: S    
                    for C in nonterms_list:
                        temp_rule = "{}->{}".format(C,B)
                        if temp_rule in grammar1.keys():
                            prob = grammar1[temp_rule] * table[i][i+1][B]
                            if C in table[i][i+1].keys():
                                if (prob>table[i][i+1][C]):
                                    table[i][i+1][C] = prob
                                    back[i][i+1][C] = B
                            else:
                                table[i][i+1][C] = prob

#handle the first diagonal into the second diagonal 

for i in range(len(sent)-1):
    begin = i
    split = i + 1
    end = i + 2
    for B in table[begin][split].keys():
        for C in table[split][end].keys():
            for A in nonterms_list:
                temp_rule = "{}->{} {}".format(A,B,C)
                if temp_rule in grammar1.keys():
                    prob = table[begin][split][B] * table[split][end][C] * grammar1[temp_rule]
                    if A in table[begin][end].keys():
                        if (prob>table[begin][end][A]):
                            table[begin][end][A] = prob
                            back[begin][end][A] = (split, B, C)
                    else:
                        table[begin][end][A] = prob
                    #handle uraries 
                    for D in nonterms_list:
                        temp_rule = "{}->{}".format(D,A)
                        if temp_rule in grammar1.keys():
                            prob = grammar1[temp_rule] * table[begin][end][A]
                            if D in table[begin][end].keys():
                                if (prob>table[begin][end][D]):
                                    table[begin][end][D] = prob
                                    back[begin][end][D] = A
                            else:
                                table[begin][end][D] = prob
                                
#handle the second diagonal into the third diagonal 

for i in range(len(sent)-2):
    begin = i
    split =[i+1,i+2]
    end = i + 3
    for split in split:
        for B in table[begin][split].keys():
            for C in table[split][end].keys():
                for A in nonterms_list:
                    temp_rule = "{}->{} {}".format(A,B,C)
                    if temp_rule in grammar1.keys():
                        prob = table[begin][split][B] * table[split][end][C] * grammar1[temp_rule]
                        if A in table[begin][end].keys():
                            if (prob>table[begin][end][A]):
                                table[begin][end][A] = prob
                                back[begin][end][A] = (split, B, C)
                        else:
                            table[begin][end][A] = prob
                        #handle uraries 
                        for D in nonterms_list:
                            temp_rule = "{}->{}".format(D,A)
                            if temp_rule in grammar1.keys():
                                prob = grammar1[temp_rule] * table[begin][end][A]
                                if D in table[begin][end].keys():
                                    if (prob>table[begin][end][D]):
                                        table[begin][end][D] = prob
                                        back[begin][end][D] = A
                            else:
                                table[begin][end][D] = prob

#handle the third diagonal into the final cell 

for i in range(len(sent)-3):
    begin = i
    split =[i+1,i+2,i+3]
    end = i + 4
    for split in split:
        for B in table[begin][split].keys():
            for C in table[split][end].keys():
                for A in nonterms_list:
                    temp_rule = "{}->{} {}".format(A,B,C)
                    if temp_rule in grammar1.keys():
                        prob = table[begin][split][B] * table[split][end][C] * grammar1[temp_rule]
                        if A in table[begin][end].keys():
                            if (prob>table[begin][end][A]):
                                table[begin][end][A] = prob
                                back[begin][end][A] = (split, B, C)
                        else:
                            table[begin][end][A] = prob
                        #handle uraries 
                        for D in nonterms_list:
                            temp_rule = "{}->{}".format(D,A)
                            if temp_rule in grammar1.keys():
                                prob = grammar1[temp_rule] * table[begin][end][A]
                                if D in table[begin][end].keys():
                                    if (prob>table[begin][end][D]):
                                        table[begin][end][D] = prob
                                        back[begin][end][D] = A
                            else:
                                table[begin][end][D] = prob  