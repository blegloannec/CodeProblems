program HeapSort;

{$ASSERTIONS ON}

const
   HeapMaxSize = 1000;  // /!\ not typed ~ macro

type
   Point = record
      x, y : Int32;
   end;
   HeapElem = ^Point;
   Heap	= record
      size : Int32;
      T    : Array[1..HeapMaxSize] of HeapElem;
   end;

// Comparison function e1 < e2 -- to adapt to the chosen HeapElem type
function HeapComp(var e1 : HeapElem; var e2 : HeapElem) : Boolean;
begin
   HeapComp := (e1^.x < e2^.x) or ((e1^.x = e2^.x) and (e1^.y < e2^.y));
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

procedure HeapPush(var H : Heap; constref e : HeapElem);  // constref = var+const
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

procedure Heapify(var T	: Array of HeapElem; l, r: Int32; var H	: Heap);
var
   i : Int32;
begin
   for i:=l to r do H.T[i-l+1] := T[i];
   H.size := r-l+1;
   for i:=H.size div 2 downto 1 do HeapAuxPercolateDown(H, i);
end;

// heap sort
procedure HeapSort(var T : Array of HeapElem; l, r : Int32);
var
   i : Int32;
   H : Heap;
begin
   Heapify(T, l, r, H);
   for i:=l to r do T[i] := HeapPop(H);
end;


// check
function HeapComp2(var e1 : HeapElem; var e2 : HeapElem) : Boolean;
begin
   HeapComp2 := (e1^.x < e2^.x) or ((e1^.x = e2^.x) and (e1^.y <= e2^.y));
end;

procedure Sorted(var T : Array of HeapElem; l, r : Int32);
var
   i : Int32;
begin
   for i:=l to r-1 do Assert(HeapComp2(T[i], T[i+1]), 'not sorted');
end;


// == MAIN ==
var
   i : Int32;
   T : Array[0..999] of ^Point;
begin
   Randomize();
   for i:=0 to 999 do begin
      new(T[i]);
      T[i]^.x := Random(100);
      T[i]^.y := Random(100);
   end;
   //for i:=0 to 9 do writeln(i, ' (', T[i]^.x, ',', T[i]^.y, ')');
   //writeln();
   HeapSort(T, 0, 999);
   Sorted(T, 0, 999);
   //for i:=0 to 9 do writeln(i, ' (', T[i]^.x, ',', T[i]^.y, ')');
end.
