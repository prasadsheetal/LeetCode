class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                st.append(s[i])
            else:
                if st and((st[-1]=='(' and s[i]==')') or
                        (st[-1]=='{' and s[i]=='}') or
                        (st[-1]=='[' and s[i]==']')):
                    st.pop()
                else:
                    return False
        return not st
                
        