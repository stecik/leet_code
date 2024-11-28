IList<int> MajorityElement(int[] nums)
{
    int k = 3;
    Dictionary<int, int> candidates = [];
    foreach (int item in nums)
    {
        if (candidates.ContainsKey(item))
            candidates[item]++;
        else if (candidates.Keys.Count < k - 1)
            candidates[item] = 1;
        else
        {
            foreach (var kvp in candidates)
            {
                if (kvp.Value == 1)
                    candidates.Remove(kvp.Key);
                else
                    candidates[kvp.Key]--;
            }
        }
    }
    List<int> result = new List<int>();
    foreach (var kvp in candidates)
    {
        if (nums.Count(n => n == kvp.Key) > Math.Floor(nums.Length / (double)k))
            result.Add(kvp.Key);
    }
    return result;
}


int[] nums = [1, 1, 1, 1, 1, 12, 2, 2, 2, 2, 2, 2, 26, 9, 1];
foreach (int item in MajorityElement(nums))
{
    Console.Write(item);
    Console.Write(", ");
}
Console.WriteLine();

nums = [3, 2, 3];
foreach (int item in MajorityElement(nums))
{
    Console.Write(item);
    Console.Write(", ");
}