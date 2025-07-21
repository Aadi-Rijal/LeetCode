class Solution:
    def makeFancyString(self, s: str) -> str:
        s_list= list(s)   
        j= 0   

        for i in range(len(s_list)):
            if j< 2 or s_list[j-2]!= s_list[i] or s_list[j-1]!= s_list[i]:
                s_list[j]= s_list[i]
                j+=1

        return "".join(s_list[:j])       