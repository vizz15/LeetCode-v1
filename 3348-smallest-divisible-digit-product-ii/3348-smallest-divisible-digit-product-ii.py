class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        def get_factors(t):
            c2 = c3 = c5 = c7 = 0
            while t % 2 == 0: c2 += 1; t //= 2
            while t % 3 == 0: c3 += 1; t //= 3
            while t % 5 == 0: c5 += 1; t //= 5
            while t % 7 == 0: c7 += 1; t //= 7
            
            # If there are residual primes other than 2, 3, 5, 7, it's impossible to form with digits 1-9
            if t > 1: return None
            return c2, c3, c5, c7

        factors = get_factors(t)
        if not factors: return "-1"
        t2, t3, t5, t7 = factors

        # Pre-assigning mapping for components of factor bases from digit 0-9
        f2 = [0, 0, 1, 0, 2, 0, 1, 0, 3, 0]
        f3 = [0, 0, 0, 1, 0, 0, 1, 0, 0, 2]
        f5 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        f7 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

        def min_len(r2, r3, r5, r7):
            r2, r3, r5, r7 = max(0, r2), max(0, r3), max(0, r5), max(0, r7)
            # Baseline minimum space calculating digits 8 and 9 usage
            ans = (r2 + 2) // 3 + (r3 + 1) // 2
            # Compare if one occurrence usage of digit 6 resolves edge cases to shrink slots
            if r2 > 0 and r3 > 0:
                ans = min(ans, 1 + (r2 - 1 + 2) // 3 + (r3 - 1 + 1) // 2)
            return ans + r5 + r7
        
        N = len(num)
        
        # Check if num inherently passes the conditions right away 
        if '0' not in num:
            c2 = c3 = c5 = c7 = 0
            for char in num:
                d = int(char)
                c2 += f2[d]
                c3 += f3[d]
                c5 += f5[d]
                c7 += f7[d]
            if c2 >= t2 and c3 >= t3 and c5 >= t5 and c7 >= t7:
                return num
        
        # Lock our checking index ceiling bounding any zero placements breaking limits
        z = num.find('0')
        if z == -1: z = N
        
        # Building rolling prefix factor arrays tracking for dynamically fast lookups avoiding loops later
        pref_2, pref_3, pref_5, pref_7 = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)
        for i in range(N):
            d = int(num[i])
            pref_2[i+1] = pref_2[i] + f2[d]
            pref_3[i+1] = pref_3[i] + f3[d]
            pref_5[i+1] = pref_5[i] + f5[d]
            pref_7[i+1] = pref_7[i] + f7[d]
            
        def build_suffix(length, r2, r3, r5, r7):
            res = []
            for pos in range(length):
                for d in range(1, 10):
                    nr2 = max(0, r2 - f2[d])
                    nr3 = max(0, r3 - f3[d])
                    nr5 = max(0, r5 - f5[d])
                    nr7 = max(0, r7 - f7[d])
                    
                    if min_len(nr2, nr3, nr5, nr7) <= length - 1 - pos:
                        res.append(str(d))
                        r2, r3, r5, r7 = nr2, nr3, nr5, nr7
                        break
            return "".join(res)

        # Tracing from largest depth right to left (allowing smallest Lexicographically changed increments)
        for i in range(min(N - 1, z), -1, -1):
            req2 = max(0, t2 - pref_2[i])
            req3 = max(0, t3 - pref_3[i])
            req5 = max(0, t5 - pref_5[i])
            req7 = max(0, t7 - pref_7[i])
            
            for d in range(int(num[i]) + 1, 10):
                nr2 = max(0, req2 - f2[d])
                nr3 = max(0, req3 - f3[d])
                nr5 = max(0, req5 - f5[d])
                nr7 = max(0, req7 - f7[d])
                
                # Validation checking if requirements can be satisfied by remainder spaces limits bounds
                if min_len(nr2, nr3, nr5, nr7) <= N - 1 - i:
                    suffix = build_suffix(N - 1 - i, nr2, nr3, nr5, nr7)
                    return num[:i] + str(d) + suffix
                    
        # Failsafe if string requires extending length beyond N due to extreme bounds
        req2, req3, req5, req7 = t2, t3, t5, t7
        ml = min_len(req2, req3, req5, req7)
        L = max(N + 1, ml)
        return build_suffix(L, req2, req3, req5, req7)