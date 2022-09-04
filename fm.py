import functools

best_chain = []
best_chain_length = 0
fm_matrix = []

def recur(chain, used_set):
    global best_chain, best_chain_length
    if len(chain) > best_chain_length:
        best_chain = chain.copy()
        best_chain_length = len(best_chain)
        print(f"Best chain ({best_chain_length}): {best_chain}")
    fm_list = fm_matrix[chain[-1]-1]
    for fm in fm_list:
        if fm not in used_set:
            chain.append(fm)
            used_set.add(fm)
            recur(chain, used_set)
            chain.pop()
            used_set.remove(fm)

def precompute_fm_matrix():
    
    for i in range(1, 101):
        fm_list = []
        for j in range(1, 101):
            if i == j:
                continue
            if i % j == 0 or j % i == 0:
                fm_list.append(j)
        fm_matrix.append(fm_list)

    #sort each list by fewest factors&multiples first
    #this tries factors and multiples of chain[-1] with the fewest remaining values first
    #this means in each chain, we try to use up the more 'difficult' numbers first -> leaves easier numbers later

    for i, n_fm_list in enumerate(fm_matrix):
        fm_matrix[i] = sorted(n_fm_list, key=lambda x: len(fm_matrix[x-1]))
        
    for x in fm_matrix:
        print(x)

def main():
    precompute_fm_matrix()
    for x in fm_matrix:
        print(x)
    for i in range(51,101):
        recur([i], {i})

main()
