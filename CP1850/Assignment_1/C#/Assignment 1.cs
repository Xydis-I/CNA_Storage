LetterGradeConverter();
TipCalculator();
ChangeCalculator();
ShippingCalculator();
TableOfPowers();
return;

//Problem 1
static void LetterGradeConverter()
{
    Console.WriteLine("Letter Grade Converter");
    while (true)
    {
        Console.Write("\nEnter numerical grade: ");
        var input = Console.ReadLine();

        if (string.IsNullOrWhiteSpace(input) || !int.TryParse(input, out var num))
            continue;

        var letterGrade = num switch
        {
            >= 88 and <= 100 => "A",
            >= 80 and <= 87 => "B",
            >= 67 and <= 79 => "C",
            >= 60 and <= 66 => "D",
            _ => "F"
        };

        Console.WriteLine("Letter Grade: {0}", letterGrade);

        Console.Write("\nContinue? (y/n): ");
        input = Console.ReadLine();
        if (string.IsNullOrWhiteSpace(input) || input.ToLower() != "y")
            break;
    }
    Console.WriteLine("\nBye!");
}

//Problem 2
static void TipCalculator()
{
    while (true)
    {
        Console.Write("Tip Calculator\n\nCost of meal:\t$");
        if (!float.TryParse(Console.ReadLine(), out var input))
        {
            Console.Clear();
            continue;
        }

        Console.WriteLine("\n15%\nTip amount:\t{0:C}\nTotal amount:\t{1:C}\n\n"
                          + "20%\nTip amount:\t{2:C}\nTotal amount:\t{3:C}\n\n"
                          + "25%\nTip amount:\t{4:C}\nTotal amount:\t{5:C}\n\n",
                            input * 0.15, input * 1.15, input * 0.20, input * 1.20, input * 0.25, input * 1.25);
        break;
    }
}

//Problem 3
static void ChangeCalculator()
{
    Console.WriteLine("Change Calculator");
    while (true)
    {
        Console.Write("\nEnter number of cents (0-99): ");
        if (!decimal.TryParse(Console.ReadLine(), out var input))
        {
            Console.Clear();
            continue;
        }

        var quarters = Math.Floor(input / 25);
        input %= 25;
        var dimes = Math.Floor(input / 10);
        input %= 10;
        var nickels = Math.Floor(input / 5);
        input %= 5;

        Console.WriteLine("\nQuarters: {0}\nDimes:\t  {1}\nNickels:  {2}\nPennies:  {3}", quarters, dimes, nickels, input);

        Console.Write("\nContinue? (y/n): ");
        var cont = Console.ReadLine();
        if (string.IsNullOrWhiteSpace(cont) || cont.ToLower() != "y")
            break;
    }
    Console.WriteLine("\nBye!");
}

//Problem 4
static void ShippingCalculator()
{
    Console.WriteLine(string.Concat(Enumerable.Repeat("=", 63)) + "\nShipping Calculator\n" + string.Concat(Enumerable.Repeat("=", 63)));
    while (true)
    {
        Console.Write("Cost of items ordered:\t$");
        if (!float.TryParse(Console.ReadLine(), out var input))
        {
            Console.Clear();
            continue;
        }

        if (input < 0)
        {
            Console.WriteLine("You must enter a positive number. Please try again.");
            continue;
        }

        var shippingCost = input switch
        {
            < 30 => 5.95,
            >= 30 and <= 49.99f => 7.95,
            >= 50 and <= 74.99f => 9.95,
            _ => 0
        };

        Console.WriteLine("Shipping cost:\t\t{0:C}\nTotal cost:\t\t{1:C}", shippingCost, input + shippingCost);

        Console.Write("\nContinue? (y/n): ");
        var cont = Console.ReadLine();
        if (string.IsNullOrWhiteSpace(cont) || cont.ToLower() != "y")
            break;

        Console.WriteLine(string.Concat(Enumerable.Repeat("=", 63)));
    }
    Console.WriteLine(string.Concat(Enumerable.Repeat("=", 63)));
    Console.WriteLine("Bye!");
}

//Problem 5
static void TableOfPowers()
{
    Console.WriteLine("Table of Powers\n");

    while (true)
    {
        Console.Write("Start number: ");
        if (!int.TryParse(Console.ReadLine(), out var start))
        {
            Console.WriteLine("Please Enter Valid Numbers.");
            continue;
        }
        Console.Write("Stop number:  ");
        if (!int.TryParse(Console.ReadLine(), out var stop))
        {
            Console.WriteLine("Please Enter Valid Numbers.");
            continue;
        }

        if (start > stop)
        {
            Console.WriteLine("\nStart number must be less than Stop number\n");
            continue;
        }

        Console.WriteLine("Number\t  Squared      Cubed\n======\t  =======      =====");

        for (var num = start; num < stop + 1; num++)
            Console.WriteLine("{0}\t  {1}\t       {2}", num, Math.Pow(num, 2), Math.Pow(num, 3));
        break;
    }
}