# nfa-dfa-conversion
Conversion from NFA to DFA

An NFA can have zero, one or more than one move from a given state on a given input symbol. An NFA can also have NULL moves (moves without input symbol). On the other hand, DFA has one and only one move from a given state on a given input symbol.

Conversion from NFA to DFA
Suppose there is an NFA N < Q, T, A, δ, F > which recognizes a language L. Then the DFA D < Q’, T, A, δ’, F’ > can be constructed for language L as:
Where Q is States, T is Transitions, A is state, 
Step 1: Initially Q’ = ɸ.

Step 2: Add A to Q’.

Step 3: For each state in Q’, find the possible set of states for each input symbol using transition function of NFA. If this set of states is not in Q’, add it to Q’.

Step 4: Final state of DFA will be all states with contain F (final states of NFA)


Following are the various parameters for NFA.
States = { A, B, C }
Transitions = ( 0, 1 )
End state = { C }
δ (Transition Function of NFA)

Step 1: Q’ = ɸ

Step 2: Q’ = {A}

Step 3: For each state in Q’, find the states for each input symbol.

Currently, state in Q’ is A, find moves from A on input symbol 0 and 1 using transition function of NFA and update the transition table of DFA.

δ’ (Transition Function of DFA)

Now { A, B } will be considered as a single state. As its entry is not in Q’, add it to Q’.
So Q’ = { A, { A, B } }
As there is no new state generated, we are done with the conversion. Final state of DFA will be state which has q2 as its component i.e., { A, C }

Now, moves from state { A, B } on different input symbols are not present in transition table of DFA, we will calculate it like:
δ’ ( { A, B }, 0 ) = δ ( A, 0 ) ∪ δ ( B, 0 ) = { A, B }
δ’ ( { A, B }, 1 ) = δ ( A, 1 ) ∪ δ ( B, 1 ) = { A, C }

Now { A, C } will be considered as a single state. As its entry is not in Q’, add it to Q’.
So Q’ = { A, { A, B }, { A, C } }

Now, moves from state {q0, q2} on different input symbols are not present in transition table of DFA, we will calculate it like:
δ’ ( { A, C }, 0 ) = δ ( A, 0 ) ∪ δ ( C, 0 ) = { A, B }
δ’ ( { A, C }, 1 ) = δ ( A, 1 ) ∪ δ ( C, 1) = { A }
Now we will update the transition table of DFA.

δ’ (Transition Function of DFA)
Now we will update the transition table of DFA.

As there is no new state generated, we are done with the conversion. Final state of DFA will be state which has q2 as its component i.e., { q0, q2 }

Following are the various parameters for DFA.
Q’ = { A, { A, B }, { A, C } }
T = ( 0, 1 )


# Implementation
Step 0 - User input for number of states and transitions

Step 1 - Create a dictionary with states as keys and paths as values 

Step 2- Create a nested dictionary for holding DFA. Newly created states would be appended to the states 

Step 3 - append the new states to new states list 

