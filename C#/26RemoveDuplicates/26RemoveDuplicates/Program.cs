int RemoveDuplicates(int[] nums)
{
    int k = 0;
    int i = 0;
    int j = 1;
    while (j < nums.Length)
    {
        if (nums[i] == nums[j])
        {
            j++;
        }
        else
        {
            nums[i + 1] = nums[j];
            j++;
            i++;
            k++;
        }
    }
    return k + 1;
}


int[] nums = { 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4 };
int k = RemoveDuplicates(nums);
Console.WriteLine(k);
Console.WriteLine(string.Join(", ", nums));
