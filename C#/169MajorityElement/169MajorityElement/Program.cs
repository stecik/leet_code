int MajorityElement(int[] nums)
{
    int candidate = nums[0];
    int count = 1;
    foreach (int item in nums[1..])
    {
        if (count <= 0)
        {
            candidate = item;
            count = 1;
        }
        else if (candidate == item)
            count++;
        else
            count--;
    }
    return candidate;
}




int[] nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 61, 1, 1, 81, 1, 1, 1, 16];
Console.WriteLine(MajorityElement(nums));

nums = [3, 2, 3];
Console.WriteLine(MajorityElement(nums));

