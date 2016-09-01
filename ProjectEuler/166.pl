/* DISCLAIMER: The following approach is rather uninteresting
   and misses all symmetries (geometrical, but also 9-x on each cell)
   and other observations that could be made on the problem. For instance,
   let S be the sum on each line/column/diagonal, let X be the sum of the
   4 corner elements, C be the sum of the 4 central elements and E the
   sum of the 8 other (edges) elements. Then we have
   E = full square - both diagonals = 4S - 2S = 2S
   2C = 2 central lines + 2 central columns - E = 2S + 2S - 2S = 2S
   hence C = S !
   X = both diagonals - C = 2S - S = S too ! 

   So, tried this one in Prolog for fun, with very discussable success ;)
   used the following for increased heap size:
   $ GLOBALSZ=1048576 gprolog
   (also renamed to p166.pl, for instance, to have a valid name)
   which is sufficient to generate solutions for a given
   sum between 0 and 4*9 and count them (can't find a way
   to simply count them, hence findall+length).
   However due to prolog memory management, it seems
   impossible to count over all possible sums in a single
   call, so I had to do it on smaller sums intervals and
   gather the result manually...

   Also tried a handmade modified version of findall/3 to count
   without filling memory, which works but is way too slow
   due to the use of asserta/1 and retract/1.
*/

cagic(Grid,Sum) :-
	Grid = [C00,C01,C02,C03,C10,C11,C12,C13,C20,C21,C22,C23,C30,C31,C32,C33],
	fd_domain(Grid,0,9),
	Sum #= C00+C01+C02+C03,
	Sum #= C10+C11+C12+C13,
	Sum #= C20+C21+C22+C23,
	Sum #= C30+C31+C32+C33,
	Sum #= C00+C10+C20+C30,
	Sum #= C01+C11+C21+C31,
	Sum #= C02+C12+C22+C32,
	Sum #= C03+C13+C23+C33,
	Sum #= C00+C11+C22+C33,
	Sum #= C30+C21+C12+C03,
	fd_labeling(Grid).


% tricky twisted findall/3 to count
% unfortunately useless, too slow
countall(X,Goal,Count) :-
	resoudre(X,Goal),
	compter_solutions(Count).
	
resoudre(X,Goal) :-
	call(Goal),
	asserta(solution(X)),
	fail.
resoudre(_,_).

compter_solutions(Count) :-
	solution(X),
	retract(solution(X)),
	compter_solutions(C0),
	Count is C0+1,
	!.
compter_solutions(0).
% end of the tricky part


% bad way to count (memory expensive)
% but way faster than the "trick"
count(Sum,Count) :-
	findall(X,cagic(X,Sum),Sol),
	length(Sol,Count).

% tricky way of counting, but WAY TOO SLOW
count2(Sum,Count) :- countall(X,cagic(X,Sum),Count).


count_all(0,1) :- !.
count_all(Sum,Count) :-
	S0 is Sum-1,
	count_all(S0,C0),
	count(Sum,C1),
	Count is C0+C1.

main :- count_all(36,C), write(C), nl.

% commented as too expensive in memory
% had to change the limits 0 and 36 to smaller
% intervals manually
%:- initialization(main).
