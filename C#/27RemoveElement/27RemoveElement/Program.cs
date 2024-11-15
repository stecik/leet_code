int RemoveElement(int[] nums, int val)
{
    int i = 0;
    int j = 0;
    int k = 0;

    while (j < nums.Length)
    {
        if (nums[j] == val)
        {
            j++;
        }
        else
        {
            nums[i] = nums[j];
            i++;
            j++;
            k++;
        }
    }
    return k;
}


int[] nums = { 0, 3, 1, 0, 5, 0, 1, 0, 1, 2, 0, 3, 3, 0 };
int k = RemoveElement(nums, 0);
Console.WriteLine(k);
Console.WriteLine(string.Join(", ", nums));