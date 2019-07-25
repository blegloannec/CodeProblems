// Two-pointer linear approach avoiding resorting to cubic-root
program Answer;
{$H+}
uses sysutils, classes;

// Helper to read a line and split tokens
procedure ParseIn(Inputs: TStrings) ;
var Line : string;
begin
    readln(Line);
    Inputs.Clear;
    Inputs.Delimiter := ' ';
    Inputs.DelimitedText := Line;
end;

function sum3(A,B : Int64) : Int64;
begin
    sum3 := A*A*A + B*B*B;
end;

function hooch(L,R,A1,B1 : Int64; var A2,B2 : Int64) : Boolean;
var V : Int64;
begin
    V := sum3(A1,B1);
    A2 := L-1; B2 := R;
    while (A2<=B2) and ((sum3(A2,B2) <> V) or (A2 = A1)) do begin
        Inc(A2);
        while sum3(A2,B2)>V do Dec(B2);
    end;
    hooch := (A2<=B2);
end;

var
    L,R,A,B : Int64;
    Inputs: TStringList;
begin
    Inputs := TStringList.Create;
    ParseIn(Inputs);
    L := StrToInt(Inputs[0]);
    R := StrToInt(Inputs[1]);
    ParseIn(Inputs);
    A := StrToInt(Inputs[0]);
    B := StrToInt(Inputs[1]);
    if hooch(L,R,A,B,A,B) then writeln(A, ' ', B)
    else writeln('VALID');
    flush(StdErr); flush(output); // DO NOT REMOVE
end.
