program Maior3;
var
    num1, num2, num3, maior: Integer;
begin
    { Ler 3 números }
    writeln('Introduza o primeiro número: ');
    readln(num1);
    writeln('Introduza o segundo número: ');
    readln(num2);
    writeln('Introduza o terceiro número: ');
    readln(num3);
    { Calcular o maior }
    if (num1 > num2) then
        if (num1 > num3) then maior := num1;
        else maior := num3;
    else
        if (num2 > num3) then maior := num2;
        else maior := num3;
    { Escrever o resultado }
    writeLn('O maior é: ', maior);
end.