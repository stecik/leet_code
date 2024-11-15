bool IsValid(string s)
{
    Stack<char> stack = new Stack<char>();
    Dictionary<char, char> map = new Dictionary<char, char>{
        {')', '('},
        {']', '['},
        {'}', '{'}
    };
    foreach (char c in s)
    {
        if (map.ContainsKey(c))
        {
            if (stack.Count == 0 || stack.Pop() != map[c])
            {
                return false;
            }
        }
        else
        {
            stack.Push(c);
        }
    }
    if (stack.Count == 0)
    {
        return true;
    }
    return false;
}


string s = "()";
Console.WriteLine(IsValid(s));
s = "()[]{}";
Console.WriteLine(IsValid(s));
s = "(]";
Console.WriteLine(IsValid(s));
s = "([)]";
Console.WriteLine(IsValid(s));
s = "{[]}";
Console.WriteLine(IsValid(s));