pushi 2              // const 2
storeg 0             // store x
pushg 0              // var x
dup
pushi 1              // const 1
equal
jz next_case_0       // check case 1
jump L2
next_case_0:
dup
pushi 2              // const 2
equal
jz next_case_1       // check case 2
jump L3
next_case_1:
dup
pushi 3              // const 3
equal
jz next_case_1       // check case 3
jump L3
next_case_1:
pop                  // no case matched
pushs "Outro número" // string "Outro número"
writes
jump L1
L2:                  // case branch 0
pop
pushs "Um"           // string "Um"
writes
jump L1
L3:                  // case branch 1
pop
pushs "dois e três"  // string "dois e três"
writes
jump L1
L1:                  // end case
stop                 // end of program