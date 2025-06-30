class Solution {
public:
    string robotWithString(string s) {
        
        std::vector<char> lowestCharAfterIdx(s.size());
        lowestCharAfterIdx.back() = 'z' + 1;
        for(int i = s.size() - 2; i >= 0; i--)
        {
            lowestCharAfterIdx[i] = std::min(lowestCharAfterIdx[i + 1], s[i + 1]);
        }

        std::stack<char> monoDecrStk;
        std::string returnVal = "";

        for(int i = 0; i < s.size(); i++)
        {
            monoDecrStk.emplace(s[i]);
            
            while(monoDecrStk.empty() == false && monoDecrStk.top() <= lowestCharAfterIdx[i])
            {
                returnVal.push_back(monoDecrStk.top());
                monoDecrStk.pop();
            }
        }

        return returnVal;
    }

};