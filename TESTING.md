# Testing

Testing in development was done using the terminal in the IDE, Visual Studio Code. When developing the VinVentory app, I referenced the flowcharts I had created, and used the 'print' function to track the flow of data throughout each process. I would manually test each function or menu option with correct and incorrect inputs multiple times once I though the function to be complete. Once I was confident a function was operating correctly, I removed the print statements used to track variables, inputs and outputs.

The site was deployed to Heroku after the main bulk of development was complete and due to the Heroku terminal width limits i had to remove some information, to better display tables in screen. Once I had made the necessary changes for Heroku deployment, I tested all functions with correct, incorrect and edge case values.

![VinVentory Responsive Image](/media/images/screenshots/responsive.png)

- The deployed site can be found at - [VinVentory Heroku App](https://vinventory-5fcb36a00949.herokuapp.com/)
- The repository can be found at - [VinVentory Repo](https://github.com/KyleMardell/vinventory)

- - -

## Contents

- - -

## Validator

In order to validate the python code to pep8 standards, I used the Code Institute Python Linter. I ran each module through the CI Python Linter and made the necessary changes to produce no errors or warnings. These were usually trailing whitespace or lines too long, which were both easily rectifiable by removing trailing spaces and splitting long lines into multiple shorter lines.

- [Code Institute Python Linter](https://pep8ci.herokuapp.com/#) 

## Unit Tests

## Testing GIFs

I have included some short GIFs of my input validation testing. As many functions are re-used I did not include GIFs for all functions, but tried to include at least one occurrence of each bit of validation.

- Find ID
    - [GIF](/media/gifs/tests/find-id-valid.gif)
- Search stock
    - [GIF](/media/gifs/tests/search-stock-valid.gif)
- Add car
    - [GIF 1](/media/gifs/tests/new-car-valid1.gif)
    - [GIF 2](/media/gifs/tests/new-car-valid2.gif)
    - [GIF 3](/media/gifs/tests/new-car-valid3.gif)
    - [GIF 4](/media/gifs/tests/new-car-valid4.gif)
- Edit car
    - [GIF 1](/media/gifs/tests/edit-valid1.gif)
    - [GIF 2](/media/gifs/tests/edit-valid2.gif)
    - [GIF 3](/media/gifs/tests/edit-valid3.gif)
    - [GIF 4](/media/gifs/tests/edit-valid4.gif)
    - [GIF 5](/media/gifs/tests/edit-valid5.gif)
- Sell car
    - [GIF](/media/gifs/tests/sell-car-valid1.gif)
- Sales report
    - [GIF](/media/gifs/tests/sales-report-valid.gif)
- Delivery request
    - [GIF](/media/gifs/tests/delivery-request-valid.gif)

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
| 'Menu' option | Error message displayed | Entered no input | Error displayed - 'Not a valid input. Please try again' | Pass |
| --- |
| Stock Menu |
| 'View List of All Stock' option | Table of all stock is displayed | Enter '1' as input| All stock displayed | Pass |
| 'View Car Information' option | View car info option displayed, user asked to enter ID number | Enter '2' as input | Option displayed, user asked to enter ID number | Pass |
| 'Search Stock by Key Words' option | Search stock displayed, user asked to enter terms | Enter '3' as input | Search stock displayed, user asked to enter terms | Pass |
| 'Return to Main Menu' option | Main menu displayed | Enter '0' as input | Main menu displayed | Pass |
| 'Menu' option | Error message displayed | Entered '4' as input | Error displayed - 'Not a valid input. Please try again' | Pass |
| 'Menu' option | Error message displayed | Entered '-1' as input | Error displayed - 'Error: Must be a positive number' | Pass |
| 'Menu' option | Error message displayed | Entered 'hello' as input | Error displayed - 'Not a valid input. Please try again' | Pass |
| 'Menu' option | Error message displayed | Entered no input | Error displayed - 'Not a valid input. Please try again' | Pass |
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
| 'Return to main menu or quit' | Error message displayed | Entered a word as input (hello) | Error displayed - 'Not a valid input. Please try again' | Pass |
| 'Return to main menu or quit' | Error message displayed | Entered '1' as input | Error displayed - 'Not a valid input. Please try again' | Pass |
| 'Return to main menu or quit' | Error message displayed | Entered no input | Error displayed - 'Not a valid input. Please try again' | Pass |
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
| 'Return to main menu or quit' | Error message displayed | Entered no input | Error displayed - 'Not a valid input. Please try again' | Pass |
| --- |
| Add/Edit Menu |
| 'Add a new car to the stock sheet' menu option | Add car option displayed, user asked for input | Entered '1' as input | Add car option and input message displayed | Pass |
| 'Edit a car currently in stock' menu option | Edit car option displayed, user asked for car ID input | Entered '2' as input | Edit car option and ID input displayed | Pass |
| 'Mark a car as sold' menu option | Sell car option displayed, user asked for car ID input | Entered '3' as input | Sell car option and ID input displayed | Pass |
| 'Create delivery request' menu option | Delivery request option displayed, user asked for car ID input | Entered '4' as input | Delivery request option and ID input displayed | Pass |
| 'Delete a car from the stock sheet' menu option | Delete car option displayed, user asked for car ID input | Entered '5' as input | Delete car option and ID input displayed | Pass |
| 'Return to Main Menu' option | Main menu displayed | Entered '0' as input | Main menu displayed | Pass |
| 'Menu' option | Error message displayed | Entered '6' as input | Error displayed - 'Not a valid input. Please try again' | Pass |
| 'Menu' option | Error message displayed | Entered '-1' as input | Error displayed - 'Error: Must be a positive number' | Pass |
| 'Menu' option | Error message displayed | Entered 'hello' as input | Error displayed - 'Not a valid input. Please try again' | Pass |
| 'Menu' option | Error message displayed | Entered no input | Error displayed - 'Not a valid input. Please try again' | Pass |
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
| Confirm uncommon colour value | input cancelled | Entered 'n' as input | Input cancelled, colour input re-displayed | Pass |
| Confirm uncommon colour value | input cancelled | Entered 'N' as input | Input cancelled, colour input re-displayed | Pass |
| Confirm uncommon colour value | Error message displayed | Entered '0' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm uncommon colour value | Error message displayed | Entered 'hello' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm uncommon colour value | Error message displayed | Entered no input | Error displayed - 'Not a valid entry, please try again.' | Pass |
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
| Confirm price value | Input cancelled | Entered 'n' as input | Input cancelled, price input re-displayed | Pass |
| Confirm price value | Input cancelled | Entered 'N' as input | Input cancelled, price input re-displayed | Pass |
| Confirm price value | Error message displayed | Entered '0' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm price value | Error message displayed | Entered 'hello' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm price value | Error message displayed | Entered no input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Enter car 'price' input | Error message displayed | Entered price value (<= cost + repairs) as input | Error displayed - 'Error: Price must be larger than total cost including repairs.' | Pass |
| Enter car 'price' input | Error message displayed | Entered '-5' as input | Error displayed - 'Error: Must be a positive number.' | Pass |
| Enter car 'price' input | Error message displayed | Entered 'hello' as input | Error displayed - 'Error: Not a valid number.' | Pass |
| Enter car 'price' input | Error message displayed | Entered no input | Error displayed - 'Error: Not a valid number.' | Pass |
| ID automatically generated | Unique ID created, confirmation displayed | Entered all car details | Unique ID automatically created, car confirmation displayed | Pass |
| Confirm new car details | Input Confirmed, save sar to stock sheet | Entered 'y' as input | Car saved to stock sheet | Pass |
| Confirm new car details | Input Confirmed, save sar to stock sheet | Entered 'Y' as input | Car saved to stock sheet | Pass |
| Confirm new car details | Input cancelled | Entered 'n' as input | Input cancelled, enter make input displayed | Pass |
| Confirm new car details | Input cancelled | Entered 'N' as input | Input cancelled, enter make input displayed | Pass |
| Confirm new car details | Error message displayed | Entered '0' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm new car details | Error message displayed | Entered 'hello' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm new car details | Error message displayed | Entered no input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Edit Car In Stock |
| Edit car details (Find car by ID) | Car information and edit confirmation displayed | Entered a valid ID number | Car information and confirmation displayed | Pass |
| Edit car details (Find car by ID) | Error message displayed | Entered an invalid ID number (from a sold car) | Error displayed - 'Car ID: # not found.' | Pass |
| Edit car details (Find car by ID) | Error message displayed | Entered a negative number | Error displayed - 'Error: Must be a positive number' | Pass |
| Edit car details (Find car by ID) | Error message displayed | Entered a word | Error displayed - 'Error: Not a valid number.' | Pass |
| Edit car details (Find car by ID) | Error message displayed | Entered no input | Error displayed - 'Error: Not a valid number.' | Pass |
| Edit car details (Find car by ID) | Error message displayed | Entered numbers and letters | Error displayed - 'Car ID: # not found.' | Pass |
| Confirm edit car details | Input Confirmed | Entered 'y' as input | Value entered, edit information displayed | Pass |
| Confirm edit car details | Input Confirmed | Entered 'Y' as input | Value entered, edit information displayed | Pass |
| Confirm edit car details | Input cancelled | Entered 'n' as input | Input cancelled, ID input re-displayed | Pass |
| Confirm edit car details | Input cancelled | Entered 'N' as input | Input cancelled, ID input re-displayed | Pass |
| Confirm edit car details | Error message displayed | Entered '0' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm edit car details | Error message displayed | Entered 'hello' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm edit car details | Error message displayed | Entered no input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Edit car details | Edit make (manufacturer) value | Entered 'make' as input | Asked to enter new value | Pass |
| Make (manufacturer) input, testing is the same as when adding a car, see above. |
| Edit car details | Edit model value | Entered 'model' as input | Asked to enter new value | Pass |
| Model input, testing is the same as when adding a car, see above. |
| Edit car details | Edit year value | Entered 'year' as input | Asked to enter new value | Pass |
| Year input, testing is the same as when adding a car, see above. |
| Edit car details | Edit colour value | Entered 'colour' as input | Asked to enter new value | Pass |
| Colour input, testing is the same as when adding a car, see above. |
| Edit car details | Edit status value | Entered 'status' as input | Asked to enter new value | Pass |
| Status input, testing is the same as when adding a car, see above. |
| Edit car details | Edit cost value | Entered 'cost' as input | Asked to enter new value | Pass |
| Cost input, testing is the same as when adding a car, see above. |
| Edit car details | Edit repairs value | Entered 'repairs' as input| Asked to enter new value | Pass |
| Repairs input, testing is the same as when adding a car, see above. |
| Edit car details | Edit price value | Entered 'price' as input | Asked to enter new value | Pass |
| Price input, testing is the same as when adding a car, see above. |
| Edit car details | Error message displayed | Entered '1' as input | Error displayed - 'Invalid input, please try again.' | Pass |
| Edit car details | Error message displayed | Entered 'hello' as input | Error displayed - 'Invalid input, please try again.' | Pass |
| Edit car details | Error message displayed | Entered 'maake' (misspelling) as input | Error displayed - 'Invalid input, please try again.' | Pass |
| Edit car details | Error message displayed | Entered no input | Error displayed - 'Invalid input, please try again.' | Pass |
| Edit car details | Car information and save details confirmation displayed | Entered '0' as input | Car information and confirmation displayed | Pass |
| Confirm save car details | Input Confirmed | Entered 'y' as input | Car saved to stock sheet, feedback displayed | Pass |
| Confirm save car details | Input Confirmed | Entered 'Y' as input | Car saved to stock sheet, feedback displayed | Pass |
| Confirm save car details | Input cancelled | Entered 'n' as input | Input cancelled, edit car confirmation re-displayed | Pass |
| Confirm save car details | Input cancelled | Entered 'N' as input | Input cancelled, edit car confirmation re-displayed | Pass |
| Confirm save car details | Error message displayed | Entered '0' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm save car details | Error message displayed | Entered 'hello' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm save car details | Error message displayed | Entered no input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Sell a car |
| Sell car (Find car by ID) | Car information and sale confirmation displayed | Entered a valid ID number | Car information and confirmation displayed | Pass |
| Sell car (Find car by ID) | Error message displayed | Entered an invalid ID number (from a sold car) | Error displayed - 'Car ID: # not found.' | Pass |
| Sell car (Find car by ID) | Error message displayed | Entered a negative number | Error displayed - 'Error: Must be a positive number' | Pass |
| Sell car (Find car by ID) | Error message displayed | Entered a word | Error displayed - 'Error: Not a valid number.' | Pass |
| Sell car (Find car by ID) | Error message displayed | Entered no input | Error displayed - 'Error: Not a valid number.' | Pass |
| Sell car (Find car by ID) | Error message displayed | Entered numbers and letters | Error displayed - 'Car ID: # not found.' | Pass |
| Confirm sell car details | Input Confirmed | Entered 'y' as input | Value entered, price input displayed | Pass |
| Confirm sell car details | Input Confirmed | Entered 'Y' as input | Value entered, price input displayed | Pass |
| Confirm sell car details | Input cancelled | Entered 'n' as input | Input cancelled, menu option displayed | Pass |
| Confirm sell car details | Input cancelled | Entered 'N' as input | Input cancelled, menu option displayed | Pass |
| Confirm sell car details | Error message displayed | Entered '0' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm sell car details | Error message displayed | Entered 'hello' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm sell car details | Error message displayed | Entered no input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Enter car 'sale amount' input | Value entered, sale confirmation displayed | Entered *sale price value* (e.g. 20000) as input | Value entered, confirmation displayed | Pass |
| Confirm sell car | Input Confirmed, car saved to sale sheet, removed from stock | Entered 'y' as input | Car saved to sale sheet, removed from stock | Pass |
| Confirm sell car | Input Confirmed, car saved to sale sheet, removed from stock | Entered 'Y' as input | Car saved to sale sheet, removed from stock | Pass |
| Confirm sell car | Input cancelled | Entered 'n' as input | Input cancelled, price input displayed | Pass |
| Confirm sell car | Input cancelled | Entered 'N' as input | Input cancelled, price input displayed | Pass |
| Confirm sell car | Input cancelled | Entered '0' as input | Input cancelled, menu option displayed | Pass |
| Confirm sell car | Error message displayed | Entered '1' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm sell car | Error message displayed | Entered 'hello' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm sell car | Error message displayed | Entered no input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Request Delivery |
| Request delivery (Find car by ID) | Car information and delivery request displayed | Entered a valid ID number | Car information and delivery request displayed | Pass |
| Request delivery (Find car by ID) | Error message displayed | Entered an invalid ID number (from a sold car) | Error displayed - 'Car ID: # not found.' | Pass |
| Request delivery (Find car by ID) | Error message displayed | Entered a negative number | Error displayed - 'Error: Must be a positive number' | Pass |
| Request delivery (Find car by ID) | Error message displayed | Entered a word | Error displayed - 'Error: Not a valid number.' | Pass |
| Request delivery (Find car by ID) | Error message displayed | Entered no input | Error displayed - 'Error: Not a valid number.' | Pass |
| Request delivery (Find car by ID) | Error message displayed | Entered numbers and letters | Error displayed - 'Car ID: # not found.' | Pass |
| Confirm delivery request car details | Input Confirmed | Entered 'y' as input | Value entered, site input displayed | Pass |
| Confirm delivery request car details | Input Confirmed | Entered 'Y' as input | Value entered, site input displayed | Pass |
| Confirm delivery request car details | Input cancelled | Entered 'n' as input | Input cancelled, ID input displayed | Pass |
| Confirm delivery request car details | Input cancelled | Entered 'N' as input | Input cancelled, ID input displayed | Pass |
| Confirm delivery request car details | Error message displayed | Entered '0' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm delivery request car details | Error message displayed | Entered 'hello' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm delivery request car details | Error message displayed | Entered no input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Request Delivery (location input) | Delivery requested, added to deliveries sheet | Entered valid location | Delivery request confirmed, added to deliveries sheet | Pass |
| Request delivery (location input) | Error message displayed | Entered '0' as input | Error displayed - 'Site not found: please enter a valid site name.' | Pass |
| Request delivery (location input) | Error message displayed | Entered 'hello' as input | Error displayed - 'Site not found: please enter a valid site name.' | Pass |
| Request delivery (location input) | Error message displayed | Entered *current site* as input | Error displayed - 'Error: *current site* is the current site. Please enter a different site.' | Pass |
| Request delivery (location input) | Error message displayed | Entered no input | Error displayed - 'Error: is the current site. Please enter a different site.' | Pass |
| Delete car from stock |
| Delete car (Find car by ID) | Car information and delete confirmation displayed | Entered a valid ID number | Car information and confirmation displayed | Pass |
| Delete car (Find car by ID) | Error message displayed | Entered an invalid ID number (from a sold car) | Error displayed - 'Car ID: # not found.' | Pass |
| Delete car (Find car by ID) | Error message displayed | Entered a negative number | Error displayed - 'Error: Must be a positive number' | Pass |
| Delete car (Find car by ID) | Error message displayed | Entered a word | Error displayed - 'Error: Not a valid number.' | Pass |
| Delete car (Find car by ID) | Error message displayed | Entered no input | Error displayed - 'Error: Not a valid number.' | Pass |
| Delete car (Find car by ID) | Error message displayed | Entered numbers and letters | Error displayed - 'Car ID: # not found.' | Pass |
| Confirm delete car from stock | Car deleted from stock sheet | Entered 'y' as input | Car deleted, feedback displayed | Pass |
| Confirm delete car from stock | Car deleted from stock sheet | Entered 'Y' as input | Car deleted, feedback displayed | Pass |
| Confirm delete car from stock | Input cancelled | Entered 'n' as input | Input cancelled, 'return to menu or quit' displayed | Pass |
| Confirm delete car from stock | Input cancelled | Entered 'N' as input | Input cancelled, 'return to menu or quit' displayed | Pass |
| Confirm delete car from stock | Error message displayed | Entered '0' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm delete car from stock | Error message displayed | Entered 'hello' as input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| Confirm delete car from stock | Error message displayed | Entered no input | Error displayed - 'Not a valid entry, please try again.' | Pass |
| --- |
| Sales Reports Menu |
| 'Current Month: Sales List' menu option | Current sales list displayed | Entered '1' as input | Current sales list displayed | Pass |
| 'Current Month: Sales Report' menu option | Current sales report displayed | Entered '2' as input | Current sales report displayed | Pass |
| 'Sales History: Sales Lists' menu option | Past sales list, year input displayed | Entered '3' as input | Year input displayed | Pass |
| 'Sales History: Sales Reports' menu option | Past sales report, year input displayed | Entered '4' as input | Year input displayed | Pass |
| 'Return to Main Menu' option | Main menu displayed | Entered '0' as input | Main menu displayed | Pass |
| 'Menu' option | Error message displayed | Entered '5' as input | Error displayed - 'Not a valid input. Please try again' | Pass |
| 'Menu' option | Error message displayed | Entered '-1' as input | Error displayed - 'Error: Must be a positive number' | Pass |
| 'Menu' option | Error message displayed | Entered 'hello' as input | Error displayed - 'Not a valid input. Please try again' | Pass |
| 'Menu' option | Error message displayed | Entered no input | Error displayed - 'Not a valid input. Please try again' | Pass |
| Sales History: Sales Lists | Year entered, month input displayed | Entered '2024' as input | Month input displayed | Pass |
| Sales History: Sales Lists | Error message displayed | Entered '1909' input | Error displayed - 'Invalid year.' | Pass |
| Sales History: Sales Lists | Error message displayed | Entered '2025' input | Error displayed - 'Invalid year.' | Pass |
| Sales History: Sales Lists | Error message displayed | Entered 'hello' input | Error displayed - 'Error: Not a valid number.' | Pass |
| Sales History: Sales Lists | Error message displayed | Entered no input | Error displayed - 'Error: Not a valid number.' | Pass |
| Sales History: Sales Lists | Sales list displayed | Entered '4' as input (valid month) | Sales list displayed | Pass |
| Sales History: Sales Lists | Error message displayed | Entered '9' input (checking for missing sheet) | Error displayed - 'Error, sheet not found.' | Pass |
| Sales History: Sales Lists | Error message displayed | Entered '0' input | Error displayed - 'Invalid month.' | Pass |
| Sales History: Sales Lists | Error message displayed | Entered '20' input | Error displayed - 'Invalid month.' | Pass |
| Sales History: Sales Lists | Error message displayed | Entered 'hello' input | Error displayed - 'Error: Not a valid number.' | Pass |
| Sales History: Sales Lists | Error message displayed | Entered no input | Error displayed - 'Error: Not a valid number.' | Pass |
| Sales History: Sales Reports | Year entered, month input displayed | Entered '2024' as input | Month input displayed | Pass |
| Sales History: Sales Reports | Error message displayed | Entered '1909' input | Error displayed - 'Invalid year.' | Pass |
| Sales History: Sales Reports | Error message displayed | Entered '2025' input | Error displayed - 'Invalid year.' | Pass |
| Sales History: Sales Reports | Error message displayed | Entered 'hello' input | Error displayed - 'Error: Not a valid number.' | Pass |
| Sales History: Sales Reports | Error message displayed | Entered no input | Error displayed - 'Error: Not a valid number.' | Pass |
| Sales History: Sales Reports | Sales list displayed | Entered '4' as input (valid month) | Sales report displayed | Pass |
| Sales History: Sales Reports | Error message displayed | Entered '9' input (checking for missing sheet) | Error displayed - 'Error, sheet not found.' | Pass |
| Sales History: Sales Reports | Error message displayed | Entered '0' input | Error displayed - 'Invalid month.' | Pass |
| Sales History: Sales Reports | Error message displayed | Entered '20' input | Error displayed - 'Invalid month.' | Pass |
| Sales History: Sales Reports | Error message displayed | Entered 'hello' input | Error displayed - 'Error: Not a valid number.' | Pass |
| Sales History: Sales Reports | Error message displayed | Entered no input | Error displayed - 'Error: Not a valid number.' | Pass |
| --- |
| Delivery Reports Menu |
| 'Full Delivery Report' menu option | Full delivery report displayed | Entered '1' as input | Full delivery report displayed | Pass |
| 'Requested Deliveries' menu option | Requested deliveries report displayed | Entered '2' as input | Requested deliveries report displayed | Pass |
| 'Scheduled Deliveries' menu option | Scheduled deliveries report displayed | Entered '3' as input | Scheduled deliveries report displayed | Pass |
| 'Completed Deliveries' menu option | Completed deliveries report displayed | Entered '4' as input | Completed deliveries report displayed | Pass |
| 'Create Delivery Request' menu option | Delivery request displayed | Entered '5' as input | Delivery Request displayed | Pass |
| Delivery request testing same as above in add/edit menu |
| 'Return to Main Menu' option | Main menu displayed | Entered '0' as input | Main menu displayed | Pass |
| 'Menu' option | Error message displayed | Entered '6' as input | Error displayed - 'Not a valid input. Please try again' | Pass |
| 'Menu' option | Error message displayed | Entered 'hello' as input | Error displayed - 'Not a valid input. Please try again' | Pass |
| 'Menu' option | Error message displayed | Entered '-1' as input | Error displayed - 'Error: Must be a positive number' | Pass |
| 'Menu' option | Error message displayed | Entered no input | Error displayed - 'Not a valid input. Please try again' | Pass |
| Help Menu |
| Help is displayed as a single text file that is separated by section and can be scrolled through to find the help required. A 'return to menu or quit' option is displayed and testing is the same as above. |