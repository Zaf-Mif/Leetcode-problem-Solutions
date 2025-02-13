# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_paired = defaultdict(int)
        paired = []
        for i in range(len(cpdomains)):
            vis,rep =  cpdomains[i].split(" ")

            d1 = rep.split(".")
            for i in range(len(d1)):
                sub =".".join(d1[i:])
                count_paired[sub] += int(vis)

        ans = [f"{value} {key}" for key , value in count_paired.items() ] 
        
        return ans
