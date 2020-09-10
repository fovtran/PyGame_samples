// C# program to swap two
// nibbles in a byte
using System;

class GFG {

// Function for swapping
static int swapNibbles(int x)
{
    return ((x & 0x0F) << 4 |
            (x & 0xF0) >> 4);
}

// Driver code
public static void Main()
{ 
    int x = 100;
    Console.Write(swapNibbles(x));
}
}
