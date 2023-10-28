class Solution:
    def countVowelPermutation(self, n: int) -> int:
        store = [1,1,1,1,1]
        MOD = 10**9 + 7
        A, E, I, O, U = 0, 1, 2, 3, 4
        for _ in range(1,n):
            a, e, i, o, u = store
            
            store[A] = (e + i + u) % MOD
            store[E] = (a + i) % MOD
            store[I] = (e + o) % MOD
            store[O] = (i)
            store[U] = (i + o) % MOD
            
        return sum(store) % MOD
