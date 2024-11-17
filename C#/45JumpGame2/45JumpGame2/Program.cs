int Jump(int[] nums)
{
    int i = 0;
    int jumps = 0;
    while (i < nums.Length - 1)
    {
        int k = 0;
        int maxReach = -1;
        for (int j = 1; j < Math.Min(nums[i] + 1, nums.Length - i); j++)
        {
            if (i + j == nums.Length - 1)
                return jumps + 1;
            if (nums[i + j] + i + j >= maxReach)
            {
                maxReach = nums[i + j] + i + j;
                k = i + j;
            }
        }
        i = k;
        jumps++;
    }
    return jumps;
}

int[] nums = [2, 3, 1, 1, 4];
Console.WriteLine(Jump(nums));
nums = [2, 1];
Console.WriteLine(Jump(nums));
nums = [1, 2, 3];
Console.WriteLine(Jump(nums));
nums = [3, 2, 1];
Console.WriteLine(Jump(nums));
nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0];
Console.WriteLine(Jump(nums));
nums = [10, 10, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0];
Console.WriteLine(Jump(nums));
nums = [2, 3, 1];
Console.WriteLine(Jump(nums));



