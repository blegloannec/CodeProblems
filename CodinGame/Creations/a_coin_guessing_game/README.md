Original inspiration: [Défi IdM](http://images.math.cnrs.fr/Fevrier-2017-2e-defi.html)

A few notes:
 * [Hall's theorem](https://en.wikipedia.org/wiki/Hall%27s_marriage_theorem) and [Tutte theorem](https://en.wikipedia.org/wiki/Tutte_theorem) give conditions for matchings to exist in bipartite, resp. general, graphs.
 * The symmetric difference between two perfect bipartite matchings always is a set of cycles. Hence if a bipartite graph having a perfect matching is a tree, then its matching is unique.
 * If the bipartite graph has a unique perfect matching, then the expected greedy approach (leaf-elimination) always work. Indeed, given a perfect matching, if all vertices have degree >=2 then all vertices are incident to 1 matched + >=1 non-matched edge, hence simply alternating between matched and non-matched edges we end up in an alternating cycle. As usual, it can be swapped to form another perfect matching, contradicting the uniqueness. Hence there always is a leaf in the graph, which is a forced matched, etc.
 * Another interesting way to represent this is to consider the oriented graph obtained by directing all edges from one component to another (arbitrarily, e.g. odd to even) and then merge the even-odd vertices pairs according to a given perfect matching. Then the matching is unique iff the resulting graph is a DAG (alternating cycles in the bipartite graph correspond exactly to oriented cycles in this graph whose vertices are the matched pairs).
 * Anyway the success of the expected approach is a necessary and sufficient condition for the problem to have a unique solution, hence that is what we use to generate the testcases.

A few interesting references:
 * Kozen-Vazirani-Vazirani, _NC Algorithms for Comparability Graphs, Interval Graphs, and Unique Perfect Matchings_, 1986
 * Rabin-Vazirani, _Maximum Matchings in General Graphs through Randomization_, 1989
