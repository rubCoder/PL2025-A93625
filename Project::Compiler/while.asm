pushi 0              // const 0
storeg 0             // store a
L1:                  // while start
pushg 0              // var a
pushi 0              // const 0
inf                  // < comparison
jz L2                // exit loop
pushs "value of a: " // string "value of a: "
writes
pushg 0              // var a
writei
pushg 0              // var a
pushi 1              // const 1
add                  // + operation
storeg 0             // store a
jump L1
L2:                  // while end
stop                 // end of program