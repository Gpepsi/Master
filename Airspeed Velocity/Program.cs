using static System.Console;
using static System.Convert;
using System.Threading;


// Declare constants:
 const double STROUHAL_LOW_EFFICIENCY = 0.4;
 const double STROUHAL_HIGH_EFFICIENCY = 0.2;

// Declare variables:
string birdName;
double freq;
double amp;
string line;

WriteLine("Welcome to the Airspeed Velocity Calculator");
WriteLine();

 //- birdName, line to store string data
Write("Please enter the name of the bird:  ");
birdName = ReadLine();

 // - freq, amp to store double data
Write("Please enter the frequency of the birds wing stroke in (bps): ");
line = ReadLine();
freq = ToDouble(line);

Write("Please enter the aplitude in meters (m):  ");
line = ReadLine();
amp = ToDouble(line);
WriteLine();
WriteLine();
Thread.Sleep(1000);

// Display program details
//Read in the name of the bird from the user
WriteLine($"The name of the bird you've entered is {birdName}");
//Read the frequency and amplitude - converting from string to double
WriteLine($"The frequency of the bird’s wing stroke is: {freq} bps, with an aplitude of {amp} meters");
WriteLine();
Thread.Sleep(5000);

// Declare variables:
double resultMax, resultMin;

// Calculate the airspeed, given the fixed Strouhal values
resultMax = freq * amp / STROUHAL_HIGH_EFFICIENCY;
resultMin = freq * amp / STROUHAL_LOW_EFFICIENCY;

// Output the bird's name, and its min and max airspeed
WriteLine($"The calculator has produced the following result for a {birdName}");
Thread.Sleep(3000);
WriteLine();
WriteLine($"With a the frequency of {freq} bps, and aplitude of {amp} meters;");
WriteLine($"The minimum airspeed is {resultMin}, with a maximum airspeed of {resultMax}");
WriteLine();
WriteLine();
Thread.Sleep(5000);
WriteLine("Thank you for using the Airspeed Calculator !");
WriteLine();