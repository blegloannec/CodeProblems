program Answer;
{$H+}
{ASSERTIONS ON}
uses sysutils, classes;

const
   HeapMaxSize = 5000;  // /!\ not typed ~ macro

type
   HeapElem = Int32;
   Heap	= record
      size : Int32;
      T    : Array[1..HeapMaxSize] of HeapElem;
   end;

// Comparison function e1 < e2 -- to adapt to the chosen HeapElem type
function HeapComp(var e1 : HeapElem; var e2 : HeapElem) : Boolean;
begin
   HeapComp := (e1 < e2);
end;

// Init -- can also be used to clear a heap
procedure HeapInit(var H : Heap);
begin
   H.size := 0;
end;

procedure HeapAuxSwap(var H : Heap; i, j : Int32);
var
   svg : HeapElem;
begin
   svg := H.T[i];
   H.T[i] := H.T[j];
   H.T[j] := svg;
end;

procedure HeapPush(var H : Heap; var e : HeapElem);
var
   i : Int32;
begin
   Assert(H.size < HeapMaxSize, 'heap max size exceeded');
   Inc(H.size);
   i := H.size;
   H.T[i] := e;
   // Upward percolation
   while (i>1) and HeapComp(H.T[i], H.T[i div 2]) do begin
      HeapAuxSwap(H, i div 2, i);
      i := i div 2;
   end;
end;

procedure HeapAuxPercolateDown(var H : Heap; i : Int32);
var
   l, r, j : Int32;
begin
   l := 2*i; r := l+1;
   while ((l <= H.size) and HeapComp(H.T[l], H.T[i])) or ((r <= H.size) and HeapComp(H.T[r], H.T[i])) do begin
      if (r <= H.size) and HeapComp(H.T[r], H.T[l]) then j := r
      else j := l;
      HeapAuxSwap(H, i, j);
      i := j; l := 2*i; r := l+1;
   end;
end;

function HeapTop(var H : Heap) : HeapElem;
begin
   Assert(H.size > 0, 'pop/top failed on empty heap');
   HeapTop := H.T[1];
end;

function HeapPop(var H : Heap) : HeapElem;
begin
   HeapPop := HeapTop(H);
   HeapAuxSwap(H, 1, H.size);
   Dec(H.size);
   HeapAuxPercolateDown(H, 1);
end;


// Helper to read a line and split tokens
procedure ParseIn(Inputs : TStrings);
var
   Line : string;
begin
   readln(Line);
   Inputs.Clear;
   Inputs.Delimiter := ' ';
   Inputs.DelimitedText := Line;
end;

var
   N, i, x, res : Int32;
   Inputs : TStringList;
   H : Heap;
begin
   Inputs := TStringList.Create;
   ParseIn(Inputs);
   N := StrToInt(Inputs[0]);
   ParseIn(Inputs);
   HeapInit(H);
   for i:=0 to N-1 do begin
      x := StrToInt(Inputs[i]);
      HeapPush(H, x);
   end;
   res := 0;
   while H.size > 1 do begin
      x := HeapPop(H) + HeapPop(H);
      HeapPush(H, x);
      res += x;
   end;
   writeln(res);
   flush(StdErr); flush(output); // DO NOT REMOVE
end.
