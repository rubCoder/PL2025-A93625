pushs "Introduza o primeiro número: " // string "Introduza o primeiro número: "
writes
read
atoi
storeg 0             // store num1
pushs "Introduza o segundo número: " // string "Introduza o segundo número: "
writes
read
atoi
storeg 1             // store num2
pushs "Introduza o terceiro número: " // string "Introduza o terceiro número: "
writes
read
atoi
storeg 2             // store num3
pushg 0              // var num1
pushg 1              // var num2
sup                  // > comparison
jz L1                // if condition false, jump to else
pushg 0              // var num1
pushg 2              // var num3
sup                  // > comparison
jz L2                // if condition false, jump to else
pushg 0              // var num1
storeg 3             // store maior
L2:                  // end if
L1:                  // end if
pushs "O maior é: "  // string "O maior é: "
writes
pushg 3              // var maior
writei
stop                 // end of program