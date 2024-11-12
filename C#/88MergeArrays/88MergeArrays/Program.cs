void Merge(int[] nums1, int m, int[] nums2, int n)
{
    int k = m + n - 1;
    while (n > 0)
    {
        if (m == 0 || nums1[m - 1] < nums2[n - 1])
        {
            nums1[k] = nums2[n - 1];
            n--;
        }
        else
        {
            nums1[k] = nums1[m - 1];
            nums1[m - 1] = 0;
            m--;
        }
        k--;
    }
}

int[] nums1 = { 1, 2, 3, 0, 0, 0 };
int m = 3;
int[] nums2 = { 2, 5, 6 };
int n = 3;
Merge(nums1, m, nums2, n);
Console.WriteLine(string.Join(", ", nums1));