program testeCase;
var
  x: Integer;
begin
  x := 2;
  case x of
    1: WriteLn('Um');
    2,3: WriteLn('dois e três');
  else
    WriteLn('Outro número');
  end;
end.
