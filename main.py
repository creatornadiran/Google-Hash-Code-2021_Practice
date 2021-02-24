import random
import copy
f = open('input.txt','r+')
line= f.readline().split()
number_of_pizzas=int(line[0])
existing_groups={2:0,3:0,4:0}
existing_groups[2]=int(line[1])
existing_groups[3]=int(line[2])
existing_groups[4]=int(line[3])
pizzas={}
delivered_team=0
for i in range(number_of_pizzas):
    line= f.readline()
    pizzas[i]=line.split()[1:]
def comparison (lst,pizzas) :
    ingredient_list =[]
    for i in lst :
        for j in pizzas[i]:
            if j in ingredient_list :
                pass
            else :
                ingredient_list.append(j)
    return  len(ingredient_list)
max_point=0
for a in range(number_of_pizzas*10):
    delivered_team = 0
    copy_pizzas=copy.deepcopy(pizzas)
    copy_exist = copy.deepcopy(existing_groups)
    point=0
    choice_dict={2:[],3:[],4:[]}
    while(True):
        if len(copy_pizzas) == 0 | (copy_exist[2] == 0 & copy_exist[3] == 0 & copy_exist[4] == 0):
            break
        if len(copy_pizzas) == 1:
            break
        if len(copy_pizzas) < copy_exist[2]*2 & len(copy_pizzas) < copy_exist[3]*3 & len(copy_pizzas) < copy_exist[4]*4:
            break
        choice = random.randint(2,4)
        if copy_exist[2] == 0 & copy_exist[3] == 0  & copy_exist[4] ==0:
            break
        if copy_exist[choice] == 0:
            continue
        chsn_piz = []
        p=0
        while(True):
            if(p == choice):
                break
            if choice > len(copy_pizzas):
                break
            if len(list(copy_pizzas)) != 0:
                ra = random.choice(list(copy_pizzas.keys()))
            else:
                break
            if ra not in chsn_piz:
                chsn_piz.append(ra)
                p+=1
        old_point = point
        point += comparison(chsn_piz,copy_pizzas)**2
        if point > old_point:
            delivered_team += 1
            choice_dict[choice].append(chsn_piz)
        copy_exist[choice] -=1
        for i in chsn_piz:
            copy_pizzas.pop(i, None)
    if point > max_point:
        optimum = copy.deepcopy(choice_dict)
        optimum_delivered_team=delivered_team
        max_point=point
f = open("Submission file.txt","w")
f.writelines(f"{optimum_delivered_team}")
for i in sorted(optimum):
    for j in optimum[i]:
        f.write(f"\n{str(i)}")
        for k in j:
            f.write(f" {k}")

