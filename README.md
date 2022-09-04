# fm_chains
Aims to optimise the [NRich factors and multiples chain problem](https://www.google.com) using a simple backtracking search. 

Uses a heuristic similar to MRV (Minimum Remaining Value) to provide a large speedup: at each recursion step, we select the next candidate in the chain by how many factors & multiples that candidate has. 

The fewer factors & multiples a candidate has, the earlier we attempt to pick it. This means that 'difficult' numbers with few multiples and factors e.g. 51 or 37, are picked early on. This is achieved by pre-computing the factors & multiples matrix, then applying a comparatorised sort:

    for i, n_fm_list in enumerate(fm_matrix):
        fm_matrix[i] = sorted(n_fm_list, key=lambda x: len(fm_matrix[x-1]))

