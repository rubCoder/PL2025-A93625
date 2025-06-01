program TesteCase;
var
  x: integer;
begin
  x := 2;
  case x of
    1: writeln('Um');
    2: writeln('Dois ou três');
  else
    writeln('Outro número');
  end;
end.