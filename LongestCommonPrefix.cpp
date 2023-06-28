class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        if (strs.size() == 0)
        {
            return "";
        }
        else if (strs.size() == 1)
        {
            return strs[0];
        }
        string prefix = "";
        int minLength = 200;
        for (int i = 0; i < strs.size(); i++)
        {
            int strLength = strs[i].length();
            minLength = min(minLength, strLength);
        }
        for (int i = 0; i < minLength; i++)
        {
            for (int j = 0; j < strs.size() - 1; j++)
            {
                if (strs[j][i] != strs[j + 1][i])
                {
                    return prefix;
                }
            }
            prefix += strs[0][i];
        }
        return prefix;
    }
};