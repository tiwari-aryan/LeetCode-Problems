class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int leftIndex = 0, rightIndex = height.size() - 1;
        int area, maxArea = 0;
        while (leftIndex != rightIndex)
        {
            area = min(height[leftIndex], height[rightIndex]) * (rightIndex - leftIndex);
            maxArea = max(area, maxArea);
            if (height[leftIndex] < height[rightIndex])
            {
                leftIndex += 1;
            }
            else
            {
                rightIndex -= 1;
            }
        }
        return maxArea;
    }
};