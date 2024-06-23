# Testing

Testing in development was done using the terminal in the IDE, Visual Studio Code. When developing the VinVentory app, I referenced the flowcharts I had created, and used the 'print' function to track the flow of data throughout each process. I would manually test each function or menu option with correct and incorrect inputs multiple times once I though the function to be complete. Once I was confident a function was operating correctly, I removed the print statements used to track variables, inputs and outputs.

The site was deployed to Heroku after the main bulk of development was complete and due to the Heroku terminal width limits i had to remove some information, to better display tables in screen. Once I had made the necessary changes for Heroku deployment, I tested all functions with correct, incorrect and edge case values.

- - -

## Contents

- - -

## Validator

In order to validate the python code to pep8 standards, I used the Code Institute Python Linter. I ran each module through the CI Python Linter and made the necessary changes to produce no errors or warnings. These were usually trailing whitespace or lines too long, which were both easily rectifiable by removing trailing spaces and splitting long lines into multiple shorter lines.

- [Code Institute Python Linter](https://pep8ci.herokuapp.com/#) 

## Unit Tests

## Manual Testing

| Feature | Expected Outcome | Test Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Home Menu |
| 'Current Stock Info' menu option | Stock menu displayed | Enter '1' as input| Stock menu displayed | Pass |
| 'Add/Edit/Sell Car' menu option | Add/Edit menu displayed | Enter '2' as input | Add/Edit menu displayed | Pass |
| 'Sales Reports' menu option | Sales Reports menu displayed | Enter '3' as input | Sales Reports menu displayed | Pass |
| 'Delivery Reports/Requests' menu option | Delivery menu displayed | Enter '4' as input | Delivery menu displayed | Pass |
| 'Help' menu option | Help menu displayed | Enter '5' as input | Help menu displayed | Pass |
| 'Exit Program' option | Program is exited | Enter '0' as input | Program is exited | Pass |
| 'Menu' option | Error message displayed | Entered '6' as input | Error displayed - 'Not a valid input. Please try again' | Pass |
| 'Menu' option | Error message displayed | Entered '-1' as input | Error displayed - 'Error: Must be a positive number' | Pass |
| Stock Menu |
| 'View List of All Stock' option | Table of all stock is displayed | Enter '1' as input| All stock displayed | Pass |
| 'View Car Information' option | View car info option displayed, user asked to enter ID number | Enter '2' as input | Option displayed, user asked to enter ID number | Pass |
| 'Search Stock by Key Words' option | Search stock displayed, user asked to enter terms | Enter '3' as input | Search stock displayed, user asked to enter terms | Pass |
| 'Return to Main Menu' option | Main menu displayed | Enter '0' as input | Main menu displayed | Pass |
| 'Menu' option | Error message displayed | Entered '4' as input | Error displayed - 'Not a valid input. Please try again' | Pass |
| 'Menu' option | Error message displayed | Entered '-1' as input | Error displayed - 'Error: Must be a positive number' | Pass |
| View car information (ID required)|
| Find car by ID | A table of car information displayed | Entered a valid ID number | Table of car information displayed | Pass |
| Find car by ID | Error message displayed | Entered an invalid ID number (from a sold car) | Error displayed - 'Car ID: # not found.' | Pass |
| Find car by ID | Error message displayed | Entered a negative number | Error displayed - 'Error: Must be a positive number' | Pass |
| Find car by ID | Error message displayed | Entered a word | Error displayed - 'Error: Not a valid number.' | Pass |
| Find car by ID | Error message displayed | Entered no input | Error displayed - 'Error: Not a valid number.' | Pass |
| Find car by ID | Error message displayed | Entered numbers and letters | Error displayed - 'Car ID: # not found.' | Pass |
| 'Return to main menu or quit' | Main menu displayed | Entered 'm' as input | Main menu displayed | Pass |
| 'Return to main menu or quit' | Main menu displayed | Entered 'M' as input | Main menu displayed | Pass |
| 'Return to main menu or quit' | Program is exited | Entered '0' as input | Program is exited | Pass |
| 'Return to main menu or quit' | Error message displayed | Entered a word as input(hello) | Error displayed - 'Not a valid input. Please try again' | Pass |
| 'Return to main menu or quit' | Error message displayed | Entered a '1' | Error displayed - 'Not a valid input. Please try again' | Pass |
| Search Stock (ID required) |
| Search stock by terms | Table of cars displayed | Entered 'ReD' as input | Table of cars with colour 'red' displayed | Pass |
| Search stock by terms | Table of cars displayed | Entered '2017' as input | Table of cars with year '2017' displayed | Pass |
| Search stock by terms | Table of cars displayed | Entered 'red, Blue' as input | Table of cars with colour 'red' or 'blue' displayed | Pass |
| Search stock by terms | Table of cars displayed | Entered 'Ford, volvo' as input | Table of 'Volvo' and 'Ford displayed | Pass |
| Search stock by terms | Error message displayed | Entered 'red blue' as input | Error displayed - 'No Matches found for: ['red blue']' | Pass |
| Search stock by terms | Error message displayed | Entered no input | Error displayed - 'Error: No value entered' | Pass |
| Search stock by terms | Error message displayed | Entered '8gb-ef' as input (numbers, letters and symbols) | Error displayed - 'No Matches found for: ['8gb-ef']' | Pass |
| 'Return to main menu or quit' | Main menu displayed | Entered 'm' as input | Main menu displayed | Pass |
| 'Return to main menu or quit' | Main menu displayed | Entered 'M' as input | Main menu displayed | Pass |
| 'Return to main menu or quit' | Program is exited | Entered '0' as input | Program is exited | Pass |
| 'Return to main menu or quit' | Error message displayed | Entered a word as input (hello) | Error displayed - 'Not a valid input. Please try again' | Pass |
| 'Return to main menu or quit' | Error message displayed | Entered '1' as input | Error displayed - 'Not a valid input. Please try again' | Pass |
| 'Return to main menu or quit' | Error message displayed | Entered '-1' as input | Error displayed - 'Error: Must be a positive number' | Pass |
| Add/Edit Menu |
| 'Add a new car to the stock sheet' menu option | Add car option displayed, user asked for input | Entered '1' as input | Add car option and input message displayed | Pass |
| 'Edit a car currently in stock' menu option | Edit car option displayed, user asked for car ID input | Entered '2' as input | Edit car option and ID input displayed | Pass |
| 'Mark a car as sold' menu option | Sell car option displayed, user asked for car ID input | Entered '3' as input | Sell car option and ID input displayed | Pass |
| 'Create delivery request' menu option | Delivery request option displayed, user asked for car ID input | Entered '4' as input | Delivery request option and ID input displayed | Pass |
| 'Delete a car from the stock sheet' menu option | Delete car option displayed, user asked for car ID input | Entered '5' as input | Delete car option and ID input displayed | Pass |
| 'Return to Main Menu' option | Main menu displayed | Entered '0' as input | Main menu displayed | Pass |
| 'Menu' option | Error message displayed | Entered '5' as input | Error displayed - 'Not a valid input. Please try again' | Pass |
| 'Menu' option | Error message displayed | Entered '-1' as input | Error displayed - 'Error: Must be a positive number' | Pass |
| Add car to stock |
| Enter car 'make' (manufacturer) input | Value entered, next input displayed | Entered 'citroen' as input | Value entered, next input displayed | Pass |
| Enter car 'make' (manufacturer) input | Value entered, next input displayed | Entered 'Ford' as input | Value entered, next input displayed | Pass |
| Enter car 'make' (manufacturer) input | Error message displayed | Entered '867' as input | Error displayed - 'Input must not contain numbers, or special characters.' | Pass |
| Enter car 'make' (manufacturer) input | Error message displayed | Entered no input | Error displayed - 'Input must not contain numbers, or special characters.' | Pass |
| Enter car 'model' input | Value entered, next input displayed | Entered 'C1' as input | Value entered, next input displayed | Pass |
| Enter car 'model' input | Value entered, next input displayed | Entered 'Fiesta' as input | Value entered, next input displayed | Pass |
| Enter car 'model' | Error message displayed | Entered no input | Error displayed - 'Error: No value entered.' | Pass |
| Enter car 'year' input | Value entered, next input displayed | Entered '2018' as input | Value entered, next input displayed | Pass |
| Enter car 'year' input | Value entered, next input displayed | Entered '1988' as input | Value entered, next input displayed | Pass |
| Enter car 'year' input | Error message displayed | Entered '1909' as input | Error displayed - 'Error: Date is out of range.' | Pass |
| Enter car 'year' input | Error message displayed | Entered '2025' as input | Error displayed - 'Error: Date is out of range.' | Pass |
| Enter car 'year' input | Error message displayed | Entered 'hello' as input | Error displayed - 'Error: Not a valid number.' | Pass |
| Enter car 'year' | Error message displayed | Entered no input | Error displayed - 'Error: Not a valid number.' | Pass |
| Enter car 'colour' input | Value entered, next input displayed | Entered 'red' as input | Value entered, next input displayed | Pass |
| Enter car 'colour' input | Value entered, next input displayed | Entered 'Silver' as input | Value entered, next input displayed | Pass |
| Enter car 'colour' input | Confirmation message displayed ('*input* is not in our common colour list. Would you like to continue? (y/n)') | Entered 'hello' as input | Confirmation message displayed | Pass |
| Enter car 'colour' input | Confirmation message displayed ('*input* is not in our common colour list. Would you like to continue? (y/n)') | Entered no input | Confirmation message displayed | Pass |
| Confirm uncommon colour value | input confirmed | Entered 'y' as input | Value entered, next input displayed | Pass |
| Confirm uncommon colour value | input confirmed | Entered 'Y' as input | Value entered, next input displayed | Pass |
| Confirm uncommon colour value | input cancelled | Entered 'n' as input | Value input cancelled, colour input re-displayed | Pass |
| Confirm uncommon colour value | input cancelled | Entered 'N' as input | Value input cancelled, colour input re-displayed | Pass |
| Confirm uncommon colour value | Error message displayed | Entered '0' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm uncommon colour value | Error message displayed | Entered 'hello' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Enter car 'status' (location) input | Value entered, next input displayed | Entered 'Leeds' as input | Value entered, next input displayed | Pass |
| Enter car 'status' (location) input | Value entered, next input displayed | Entered 'Liverpool' as input | Value entered, next input displayed | Pass |
| Enter car 'status' (location) input | Value entered, next input displayed | Entered 'Manchester' as input | Value entered, next input displayed | Pass |
| Enter car 'status' (location) input | Value entered, next input displayed | Entered 'Preston' as input | Value entered, next input displayed | Pass |
| Enter car 'status' (location) input | Value entered, next input displayed | Entered 'Leeds' as input | Value entered, next input displayed | Pass |
| Enter car 'status' (location) input | Error message displayed | Entered 'London' as input | Error displayed - 'Error: Location is invalid.' | Pass |
| Enter car 'status' (location) input | Error message displayed | Entered 'hello' as input | Error displayed - 'Error: Location is invalid.' | Pass |
| Enter car 'status' (location) input | Error message displayed | Entered '1234' as input | Error displayed - 'Error: Location is invalid.' | Pass |
| Enter car 'status' (location) input | Error message displayed | Entered 'Liverpol' (misspelling) as input | Error displayed - 'Error: Location is invalid.' | Pass |
| Enter car 'status' (location) input | Error message displayed | Entered no input | Error displayed - 'Error: Location is invalid.' | Pass |
| Enter car 'cost' input | Value entered, next input displayed | Entered '10000' as input | Value entered, next input displayed | Pass |
| Enter car 'cost' input | Value entered, next input displayed | Entered '50' as input | Value entered, next input displayed | Pass |
| Enter car 'cost' input | Value entered, next input displayed | Entered '0' as input | Value entered, next input displayed | Pass |
| Enter car 'cost' input | Error message displayed | Entered '-5' as input | Error displayed - 'Error: Must be a positive number.' | Pass |
| Enter car 'cost' input | Error message displayed | Entered 'hello' as input | Error displayed - 'Error: Not a valid number.' | Pass |
| Enter car 'cost' input | Error message displayed | Entered no input | Error displayed - 'Error: Not a valid number.' | Pass |
| Enter car 'repairs' input | Value entered, next input displayed | Entered '10000' as input | Value entered, next input displayed | Pass |
| Enter car 'repairs' input | Value entered, next input displayed | Entered '50' as input | Value entered, next input displayed | Pass |
| Enter car 'repairs' input | Value entered, next input displayed | Entered '0' as input | Value entered, next input displayed | Pass |
| Enter car 'repairs' input | Error message displayed | Entered '-5' as input | Error displayed - 'Error: Must be a positive number.' | Pass |
| Enter car 'repairs' input | Error message displayed | Entered 'hello' as input | Error displayed - 'Error: Not a valid number.' | Pass |
| Enter car 'repairs' input | Error message displayed | Entered no input | Error displayed - 'Error: Not a valid number.' | Pass |
| Enter car 'price' input | Value entered, next input displayed | Entered '12500' as input | Value entered, next input displayed | Pass |
| Enter car 'price' input | Value entered, next input displayed | Entered '50' as input | Value entered, next input displayed | Pass |
| Enter car 'price' input | Value entered, next input displayed | Entered '0' as input | Value entered, next input displayed | Pass |
| Enter car 'price' input | Confirmation message displayed ('The price of *price* is less than 20% calculated profit. Is this correct?') | Entered price value (cost + repairs + 10) as input | Confirmation message displayed | Pass |
| Confirm price value | Input Confirmed | Entered 'y' as input | Value entered, next input displayed | Pass |
| Confirm price value | Input Confirmed | Entered 'Y' as input | Value entered, next input displayed | Pass |
| Confirm price value | Input cancelled | Entered 'n' as input | Value input cancelled, price input re-displayed | Pass |
| Confirm price value | Input cancelled | Entered 'N' as input | Value input cancelled, price input re-displayed | Pass |
| Confirm price value | Error message displayed | Entered '0' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm price value | Error message displayed | Entered 'hello' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Enter car 'price' input | Error message displayed | Entered price value (<= cost + repairs) as input | Error displayed - 'Error: Price must be larger than total cost including repairs.' | Pass |
| Enter car 'price' input | Error message displayed | Entered '-5' as input | Error displayed - 'Error: Must be a positive number.' | Pass |
| Enter car 'price' input | Error message displayed | Entered 'hello' as input | Error displayed - 'Error: Not a valid number.' | Pass |
| Enter car 'price' input | Error message displayed | Entered no input | Error displayed - 'Error: Not a valid number.' | Pass |
| Confirm new car details | Input Confirmed, save sar to stock sheet | Entered 'y' as input | Car saved to stock sheet | Pass |
| Confirm new car details | Input Confirmed, save sar to stock sheet | Entered 'Y' as input | Car saved to stock sheet | Pass |
| Confirm new car details | Input cancelled | Entered 'n' as input | Input cancelled, enter make input displayed | Pass |
| Confirm new car details | Input cancelled | Entered 'N' as input | Input cancelled, enter make input displayed | Pass |
| Confirm new car details | Error message displayed | Entered '0' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm new car details | Error message displayed | Entered 'hello' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |