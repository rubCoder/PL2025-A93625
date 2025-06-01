pushs "Introduza um número inteiro positivo:" // string "Introduza um número inteiro positivo:"
writes
read
atoi
storeg 0             // store n
pushi 1              // const 1
storeg 2             // store fat
pushi 1              // const 1
storeg 1             // init i
L1:
pushg 1              // for i
pushg 0              // var n
supeq                // compare
jz L2                // exit loop
pushg 2              // var fat
pushg 1              // var i
mul                  // * operation
storeg 2             // store fat
pushg 1
pushi 1
add                  // step
storeg 1             // update i
jump L1
L2:
pushs "Fatorial de " // string "Fatorial de "
writes
pushg 0              // var n
writei
pushs ": "           // string ": "
writes
pushg 2              // var fat
writei
stop                 // end of program