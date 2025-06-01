program Loop;

var
   a: integer;
begin
   a := 0;
   while a < 0 do
   begin
      writeln('value of a: ', a);
      a:=a+1;
   end;  
end.