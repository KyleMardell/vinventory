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
| Select 'Current Stock Info' menu option | Stock menu displayed | Enter '1' as input| Stock menu displayed | Pass |
| Select 'Add/Edit/Sell Car' menu option | Add/Edit menu displayed | Enter '2' as input | Add/Edit menu displayed | Pass |
| Select 'Sales Reports' menu option | Sales Reports menu displayed | Enter '3' as input | Sales Reports menu displayed | Pass |
| Select 'Delivery Reports/Requests' menu option | Delivery menu displayed | Enter '4' as input | Delivery menu displayed | Pass |
| Select 'Help' menu option | Help menu displayed | Enter '5' as input | Help menu displayed | Pass |
| Select 'Exit Program' option | Program is exited | Enter '0' as input | Program is exited | Pass |
| Stock Menu |
| Select 'View List of All Stock' option | Table of all stock is displayed | Enter '1' as input| All stock displayed | Pass |
| Select 'View Car Information' option | View car info option displayed, user asked to enter ID number | Enter '2' as input | Option displayed, user asked to enter ID number | Pass |
| Select 'Search Stock by Key Words' option | Search stock displayed, user asked to enter terms | Enter '3' as input | Search stock displayed, user asked to enter terms | Pass |
| Select 'Return to Main Menu' option | Main menu displayed | Enter '0' as input | Main menu displayed | Pass |
| View car information (ID required)|
| Display car information | A table of car information displayed | Entered a valid ID number | Table of car information displayed | Pass |
| Display car information | Error message displayed | Entered an invalid ID number (from a sold car) | Error displayed - 'Car ID: # not found.' | Pass |
| Display car information | Error message displayed | Entered a negative number | Error displayed - 'Error: Must be a positive number' | Pass |
| Display car information | Error message displayed | Entered a word | Error displayed - 'Error: Not a valid number.' | Pass |
| Display car information | Error message displayed | Entered numbers and letters | Error displayed - 'Car ID: # not found.' | Pass |
| Search Stock (ID required) |
