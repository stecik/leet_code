int MaximalSquare(char[][] matrix)
{
    int[][] matrix_int = new int[matrix.Length][];
    for (int i = 0; i < matrix.Length; i++)
    {
        int[] row_int = new int[matrix[i].Length];
        for (int j = 0; j < matrix[i].Length; j++)
        {
            row_int[j] = matrix[i][j] - '0';
        }
        matrix_int[i] = row_int;
    }
    int max_square = 0;
    foreach (int[] row in matrix_int)
    {
        foreach (int n in row)
        {
            if (n == 1)
            {
                max_square = 1;
                break;
            }
        }
    }
    for (int i = 1; i < matrix_int.Length; i++)
    {
        for (int j = 1; j < matrix_int[0].Length; j++)
        {
            if (matrix_int[i][j] == 1)
            {
                int val = Math.Min(Math.Min(matrix_int[i - 1][j], matrix_int[i][j - 1]), matrix_int[i - 1][j - 1]) + 1;
                matrix_int[i][j] = val;
                max_square = Math.Max(max_square, val);
            }
        }
    }
    return max_square * max_square;
}

char[][] matrix =
{
    ['1', '0', '1', '0', '0'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '0']
};

Console.WriteLine(MaximalSquare(matrix));

matrix =
[
    ['0', '1'],
    ['1', '0']
];


Console.WriteLine(MaximalSquare(matrix));