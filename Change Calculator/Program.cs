using static System.Convert;
using static System.Console;

// Constants:
const int TWO_DOLLARS = 200;
const int ONE_DOLLAR = 100;
const int FIFTY_CENTS = 50;
const int TWENTY_CENTS = 20;
const int TEN_CENTS = 10;
const int FIVE_CENTS = 5;

// Variables:
int costOfItem;
int amountPaid;
int changeValue;
int toGive;
string line;

//Steps:
WriteLine("The Change Calculator!");
WriteLine();

// Get the details from the user.

    // Get the cost (store in costOfItem)
    Write("What is the cost of the Item ? (In cents):  ");
    line = ReadLine();
    costOfItem = ToInt32(line);
    WriteLine();

    // Get the amount paid (store in amountPaid)
    Write("Please enter the amount paid ? (In cents):  ");
    line = ReadLine();
    amountPaid = ToInt32(line);
    WriteLine();

    // Calculate the amount of change to provide
        // Give change
        changeValue = amountPaid - costOfItem;
               
        WriteLine("Dispensing your change..... Please Wait....");
        WriteLine();
            // Give $2 coins
            // Calculate the number of $2 coins to give
            // Update the amount of change remaining to give
            // Output the number of $2 coins to give - using Write
                toGive = changeValue / TWO_DOLLARS;
                changeValue = changeValue - toGive * TWO_DOLLARS;
                Write($"{toGive} x $2, ");

        //Give $1 coins (as with $2 above but with ONE_DOLLAR)
            // Calculate the number of $1 coins to give
            // Update the amount of change remaining to give
            // Output the number of $1 coins to give - using Write
                toGive = changeValue / ONE_DOLLAR;
                changeValue = changeValue - toGive * ONE_DOLLAR;
                Write($"{toGive} x $1, ");

       // Give 50c coins (...)
            // Calculate the number of 50c coins to give
            // Update the amount of change remaining to give
            // Output the number of 50c coins to give - using Write
                toGive = changeValue / FIFTY_CENTS;
                changeValue = changeValue - toGive * FIFTY_CENTS;            
                Write($"{toGive} x 50c, ");

       // Give 20c coins
            // Calculate the number of 20c coins to give
            // Update the amount of change remaining to give
            // Output the number of 20c coins to give - using Write
                toGive = changeValue / TWENTY_CENTS;            
                changeValue = changeValue - toGive * TWENTY_CENTS;
                Write($"{toGive} x 20c, ");

        // Give 10c coins
            // Calculate the number of 10c coins to give
            // Update the amount of change remaining to give
            // Output the number of 10c coins to give - using Write
                toGive = changeValue / TEN_CENTS;
                changeValue = changeValue - toGive * TEN_CENTS;
                Write($"{toGive} x 10c, ");

        // Give 5c coins
            // Calculate the number of 5c coins to give
            // Update the amount of change remaining to give
            // Output the number of 5c coins to give - using Write
                toGive = changeValue / FIVE_CENTS;
                changeValue = changeValue - toGive * FIVE_CENTS;
                Write($"{toGive} x 5c, ");
                WriteLine();
                WriteLine();

        WriteLine("Thank you, Please come again !");
        WriteLine();
