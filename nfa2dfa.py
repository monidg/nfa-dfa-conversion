import pandas as pd

# User  Input                                
states = int(input("number of states : "))           
transitions = int(input("number of transitions : "))      

nfa = {} 

for i in range(states):  
    state = input("Enter state name : ")            
    nfa[state] = {}                          
    for j in range(transitions):
        path = input(" Enter path : ")              
        print("Enter end state from state {} travelling through path {} : ".format(state,path))
        end_state = [x for x in input().split()] 
        nfa[state][path] = end_state    

#Print NFA
print("\nNFA :- \n")
print(nfa)                                    
print("\nPrinting NFA table :- ")
nfa_table = pd.DataFrame(nfa)
print(nfa_table.transpose())

print("Enter final state of NFA : ")
nfa_final_state = [x for x in input().split()]  
    
new_states_list = []                        
dfa = {}                                     
keys_list = list(list(nfa.keys())[0])                 
path_list = list(nfa[keys_list[0]].keys())   




dfa[keys_list[0]] = {}                      
for y in range(transitions):
    var = "".join(nfa[keys_list[0]][path_list[y]])  
    dfa[keys_list[0]][path_list[y]] = var           
    if var not in keys_list:                        
        new_states_list.append(var)                 
        keys_list.append(var)                       
        
 
# DFA transition table

while len(new_states_list) != 0:                    
    dfa[new_states_list[0]] = {}                    
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)):
            temp = []                               
            for j in range(len(new_states_list[0])):
                temp += nfa[new_states_list[0][j]][path_list[i]] 
            s = ""
            s = s.join(temp)                        
            if s not in keys_list:                  
                new_states_list.append(s)            
                keys_list.append(s)                 
            dfa[new_states_list[0]][path_list[i]] = s  
        
    new_states_list.remove(new_states_list[0])    

#Print DFA  
print("\nDFA :- \n")    
print(dfa)                                         
print("\nPrinting DFA table :- ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())

dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break

 # DFA Final states     
print("\nFinal states of the DFA are : ",dfa_final_states) 

'''
# 0UTPUT

# states : 3
# transitions : 2
Enter state name : A
 Enter path : 0
Enter end state from state A travelling through path 0 : 
A B
 Enter path : 1
Enter end state from state A travelling through path 1 : 
A
Enter state name : B
 Enter path : 0
Enter end state from state B travelling through path 0 : 

 Enter path : 1
Enter end state from state B travelling through path 1 : 
C
Enter state name : C
 Enter path : 0
Enter end state from state C travelling through path 0 : 

 Enter path : 1
Enter end state from state C travelling through path 1 : 


NFA :- 

{'A': {'0': ['A', 'B'], '1': ['A']}, 'B': {'0': [], '1': ['C']}, 'C': {'0': [], '1': []}}

Printing NFA table :- 
        0    1
A  [A, B]  [A]
B      []  [C]
C      []   []
Enter final state of NFA : 
C

DFA :- 

{'A': {'0': 'AB', '1': 'A'}, 'AB': {'0': 'AB', '1': 'AC'}, 'AC': {'0': 'AB', '1': 'A'}}

Printing DFA table :- 
     0   1
A   AB   A
AB  AB  AC
AC  AB   A

Final states of the DFA are :  ['AC']
'''