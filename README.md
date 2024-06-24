# VinVentory
VinVentory is a used car management system. The VinVentory app is aimed at small used car businesses to hold information about their sales and cars in stock. Using the Google Sheets API as a database, VinVentory provides the ability for multiple sites to have an easy way to see what cars are in stock on other sites.

![VinVentory Responsive Image](/media/images/screenshots/responsive.png)

- The deployed site can be found at - [VinVentory Heroku App](https://vinventory-5fcb36a00949.herokuapp.com/)
- The repository can be found at - [VinVentory Repo](https://github.com/KyleMardell/vinventory)

- - - 

## Contents

- [User Experience](#user-experience)
    - [First Time Visitor Goals](#first-time-visitor-goals)
    - [Returning Visitor Goals](#returning-visitor-goals)
    - [App Use Goals](#app-use-goals)
- [Design](#design)
    - [Concept](#concept)
    - [Google Sheets](#worksheet--database)
    - [Functionality](#functionality)
    - [Menus](#menus)
    - [Flowcharts](#flowcharts)
- [Features](#features)
    - [Existing Features](#existing-features)
        - [Home Menu](#home-menu)
        - [Stock Menu](#stock-menu)
        - [Add/Edit Menu](#addeditselldelete-menu)
        - [Sales Reports Menu](#sales-reports-menu)
        - [Deliveries Menu](#deliveries-menu)
        - [Help Menu](#help-menu)
    - [Future Features](#future-features)
- [Deployment](#deployment)
    - [GitHub](#fork-repository)
    - [Google Sheets](#google-sheets)
    - [Heroku](#heroku)
- [Testing](#testing)
- [Credits](#credits)

- - - 

## User Experience

### First time visitor goals
First time visitors to the app are expected to be potential customers/clients of the VinVentory app. With this in mind, first time visitor goals are to provide a look at our solution to an existing problem, through a centralized vehicle stock, sales and delivery management system. First time visitors should be impressed by the usability and features of the VinVentory app, to help better manage vehicle stock and sales data.

### Returning visitor goals
Returning visitors to the app will usually be businesses with the VinVentory system deployed. Therefore the returning visitor goals are to provide an easy to use and navigate vehicle management system. Data should be quickly accessible and easy to understand, and the app should provide all the functionality a business requires.

### App use goals
The goals for app usage are to provide a solution to a real-world problem through an effective online car management system. The app should provide an effective tool for small businesses with either a single or multiple sites, with the ability to track vehicle stock, mark cars as sold, see sales data, and request internal vehicle deliveries. The app should be simple to use and a helpful tool to any small used car business.

## Design

### Concept
The concept of the VinVentory vehicle management system is to provide a tool for small used car businesses to track stock and sales data, as well as request and track internal deliveries. I wanted to create an app with a real-world scenario in mind and found this concept to be much larger in scope than initially expected. However, keeping to an MVP and not fully outfitting the app helped to rein in the scope.

### Worksheet / Database
I used Google Sheets API as a database to hold all the information about the cars in stock and all sales and delivery sheets. I had first designed the worksheets with columns for over 15 different vehicle details. However, once I deployed to Heroku, I found the max character width was 80, and with this in mind, I had to remove many columns of data to better display when deployed using Heroku. 

I had tried to include all information a potential customer may want to know but had to reduce the scope due to the Heroku limitations. Even after removing many columns of information such as mileage and engine size, I feel that this MVP(minimum viable product) gives a good sense of what the VinVentory app could be once fully built, and these items would be easy enough to add in the future.

#### Worksheet Screenshots
- [Stock Worksheet](/media/images/screenshots/stock-worksheet.png)
- [Sales Worksheet](/media/images/screenshots/sales-worksheet.png)
- [Delivery Worksheet](/media/images/screenshots/delivery-worksheet.png)

### Functionality
For the functionality of the app, I wanted to provide the user with information about what cars a business may currently have in stock, as well as current and past sales data. This means that the ability to add, edit, and delete a car from the stock sheet needed to be included.
The app also needed to be able to mark a car as sold, removing it from the stock sheet and adding it to the current month's sales sheet. If the sales sheet exists, if not, then one is automatically created.

The user can view a list of all cars in stock, or alternatively, search for a single car by using its internal ID number, or search for all cars with a matching input, such as all red cars, or all Citroen cars.
In order to add a car to the stock sheet, the user must enter all the required information when prompted, and an internal ID will be automatically generated before the car is added to the stock sheet.

The user can also edit the details of a car currently in the stock sheet by entering its internal ID number. They can then choose which detail to edit and enter a new value.
When deleting a car from the stock sheet, the user must enter the internal ID of the car and is shown a warning message before confirming and deleting the car.
A delivery request can be made for a car, adding its details to the delivery sheet and marking its status in the stock sheet with a "-D" to signal a delivery has been requested. I initially used the appendix "- Delivery Requested" but shortened it for better viewing on the Heroku deployment terminal.

There are multiple sales reports and tables that the user can view through each corresponding menu item. Sales tables show all cars sold in a particular month, with added sales details such as sale price and date. Sales reports can be generated for the current month or any month since the VinVentory system has been implemented. A sales report shows data about how many cars have been sold, total profits made, total costs, etc.

Similarly, delivery reports can be viewed in table format, with the option to filter deliveries by status.

### Menus
The menu system in the VinVentory app uses a simple number system, with the user inputting a number to navigate through the menus. There is a home menu welcoming the user to the app and displaying the sub-menu options. The sub-menus are where the functionality of the app is contained. 

There are menus for stock, add/edit car details, sales reports, delivery reports, and help. Within each of these menus, there are the options to view data about cars in stock, sold cars per month, delivery requests, etc. Each sub-menu function is explained in its corresponding readme section.

### Flowcharts
In order to visualize the menu flow and the flow of data, I created flowcharts before and during development. I used these when creating the menu options and as a guide for what functions I needed to build. 

Ultimately, I created more functions than I initially planned through flowcharts, to make the code easier to read or to separate larger functions.

![Menu Flowchart](/media/images/flowcharts/menu-flowchart.png)

#### Flowchart Screenshots
- [Stock Flowchart](/media/images/flowcharts/stock-flowchart.png)
- [Find By ID Flowchart](/media/images/flowcharts/find-id-flow-chart.png)
- [Search Flowchart](/media/images/flowcharts/search-flowchart.png)
- [Sell Car Flowchart](/media/images/flowcharts/sell-car-flowchart.png)
- [Add Car Flowchart](/media/images/flowcharts/add-car-flowchart.png)
- [Edit Car Flowchart](/media/images/flowcharts/edit-car-flowchart.png)
- [Delete Car Flowchart](/media/images/flowcharts/delete-car-flowchart.png)

## Features

### Existing Features

#### Home Menu
The home menu serves as a way to welcome the user to the VinVentory app and navigate to another sub-menu. The user is greeted with a welcome message and an attractive ASCII art image of a car to show the app's overall function. 

The user is shown a small menu of options to choose from and can enter a number to navigate to a sub-menu or help section. Entering 0 from the home menu will exit the program.

![Home Menu Screenshot](/media/images/screenshots/home-menu.png)

#### Stock Menu
The stock menu is where the user can view information about cars currently in stock. There are 3 options within the stock menu: view a list of all cars, view car information by ID, or search stock by keywords. 

The user can enter 0 to see an option to return to the main menu or exit the program.

![Stock Menu Screenshot](/media/images/screenshots/stock-menu.png)

##### All Stock
When selecting the all stock option, the user is shown a list of all cars in stock in an easy-to-read table format. When viewing all cars, vehicle repairs and cost are removed, showing only the price. This is with salespersons and customer interactions in mind, to limit the cost information when browsing cars in stock. As there may be many cars in stock at one time, the page will vertically overflow and can be viewed by scrolling up.

I originally included more car details such as mileage and engine size, but due to the size of the Heroku deployment mock terminal, I had to reduce the amount of information to better display the table of information on the screen. This meant I also had to adjust the Google Sheet worksheet by removing columns of information.

 Even with these changes, I feel that as an MVP (minimum viable product), the amount of information displayed fits the scope much better with columns removed.

- [All Stock Screenshot](/media/images/screenshots/all-stock.png)
- [All Stock GIF](/media/gifs/all-stock.gif)

##### Find By ID
The user can enter a car in stock ID number to view vehicle and repair costs as additional information. This gives the salesperson the option to calculate if they can give any discount on the listed car price.

This means if a customer has browsed the cars in stock and is considering purchasing a car, the salesperson can view purchase and repair costs if needed.
Validation when searching by ID includes checking for number input only, as well as if the entered ID number exists in the sheet.

- [Find By ID Screenshot](/media/images/screenshots/find-id.png)
- [Find By Id GIF](/media/gifs/find-by-id.gif)

##### Search by terms
The search by terms option lets the user enter a list of details to search for and all cars with matching data will be displayed in a table. This means the user can search for all Fords by entering 'Ford' and a table of all Ford cars will be displayed. The user can enter further terms separated by commas. 

For example, if the user wanted to see a table of all Fords and Citroens, they could enter 'Ford, Citroen', or 'Green, Blue, Ford' to see a table containing all Fords, blue, and green cars.
As validation, the user must enter either a single term or multiple terms separated by commas. 

If a term is not found, an error will be shown. The same error will be triggered if the user enters multiple terms separated by anything other than commas, e.g., a single space or dash.

- [Search Stock Screenshot](/media/images/screenshots/search-stock.png)
- [Search Stock GIF](/media/gifs/search-stock.gif)

#### Add/Edit/Sell/Delete Menu
The add/edit menu contains options focused on cars in stock. From here, the user can add a car to the stock sheet, edit or delete a car currently in stock, mark a car as sold, or request a delivery. 

These options were grouped as they all manipulate the stock sheet in some way and are the main way to interact with the car data other than simply viewing it.

![Add/Edit Menu](/media/images/screenshots/edit-menu.png)

##### Add Car To Stock
In order to add a car to stock, the user must enter all the required information, and an ID number will be automatically generated once all information has been entered. There are details for the car's make, model, year, color, status (current site), list price, purchase and repair costs. The user is ultimately responsible for the correct entry of the car details, although some validation exists for the inputs.

Validation includes checking car make only contains letters (no numbers or special characters), the current site is a valid location, and that only numbers are entered for price, purchase, and repair costs. For color validation, the entered value is checked against a list of common colors and if the value is not in the list, the user must confirm the entry. 

When entering a price, the value is checked against the entered repair and purchase costs. If the entered price is below the combined costs, the user is shown an error; if the price is less than 20% larger than the costs, the user is shown a warning message and can choose to confirm or re-enter a price.

- [Add Car GIF 1](/media/gifs/new-car1.gif)
- [Add Car GIF 2](/media/gifs/new-car2.gif)

##### Edit Car In Stock
When editing a car in stock, the user must enter the car's ID number. Once the correct car has been confirmed, they can enter which detail they wish to edit (e.g., make, model, color, etc.), and then enter the new value. 

This means the user can change any of the car's details other than the ID or location. The ID is fixed to each car, and the location can only be changed by requesting a delivery once a car is entered into the system.

For validation, the user-entered edit term is checked against a list of changeable details, with an error message displayed if the entered term does not exist. When entering a new value, the same validation as when adding a car applies.

- [Edit Car GIF1](/media/gifs/edit-car1.gif)
- [Edit Car GIF 2](/media/gifs/edit-car2.gif)
- [Edit Car GIF 3](/media/gifs/edit-car3.gif)

##### Sell Car
Users can mark a car as sold by using this option. The user must enter the car's sale amount, and then the car is removed from the stock sheet and added to the current sales sheet, with the additional sale price and current date of sale information included.

As a car could be sold for any price, the only validation included here is to check the entered value is a number. This means cars can be sold at a loss.

- [Sell Car GIF](/media/gifs/sell-car1.gif)

##### Request Delivery
An internal delivery of a car can be requested using this option. To request a delivery, the user must enter the ID number of the car they wish to request delivery for. They are then asked which site the delivery is to, with the current location removed as an option. 

Once all details have been entered, a scheduled date is automatically created, and all details are saved to the deliveries sheet. The status is updated with a '-D' on the stock sheet to indicate a delivery request.

The validation for the ID input is as per the 'find car by ID' function, and the input location is checked against a list of sites, with its current location removed.

- [Delivery Request GIF](/media/gifs/delivery-request.gif)

##### Delete Car In Stock
The user can delete a car in stock by entering the car's ID number. A warning will be shown, and the user will need to confirm the input before the car's details are deleted.

The car's ID is validated as per the 'find car by ID' function. A feedback message is shown when the car has been removed from the stock sheet.

- [Delete Car GIF](/media/gifs/delete-car.gif)

#### Sales Reports Menu
The sales reports menu is where the user can view current and past sales reports and tables. The options for past sales tables or reports require the year and month input of the report the user wishes to view.

![Sales Reports Menu](/media/images/screenshots/sales-menu.png)

##### Current Sales Table
This option displays a table of all sold cars in the current month. The sales data includes the sale price and total profit for each car. This gives the user a way to see if sales are on target and view the amount of profit made per car.

Validation for the current month includes checking if a worksheet already exists for that month by name; if not, then creating a new worksheet and giving the user feedback.

- [Current Sales Table GIF](/media/gifs/current-sales-table.gif)

##### Current Sales Report
The current month's sales report displays a sales report that includes data such as the total number of cars sold, total profit, average profit per car, etc. This is a quick way for the user to view a summary of the current month's sales.

Validation for the current month includes checking if a worksheet already exists for that month by name; if not, then creating a new worksheet and giving the user feedback.

- [Current Sales Report GIF](/media/gifs/current-sales-report.gif)

##### Past Sales Table
With this option, the user can view a table of any historic month's sales data by inputting the year and month they wish to view. An error message will be displayed if the entered month's sales sheet does not exist. For this version, I have included sales sheets for months back to 2/2024 (February 2024).

When the user enters the year and month to find a past sales sheet, the year and month are both validated, giving the user an error message for incorrect input or a missing sales sheet.

- [Past Sales Table GIF](/media/gifs/past-sales-table.gif)

##### Past Sales Report
Sales reports can be generated for each past sales month in the same format as a current month's sales sheet.
When the user enters the year and month to find a past sales sheet, the year and month are both validated, giving the user an error message for incorrect input or a missing sales sheet.

- [Past Sales Report GIF](/media/gifs/past-sales-report.gif)

#### Deliveries Menu
The deliveries menu gives the user the option to view the deliveries sheet data either in a full table or filtered by delivery status. 
There is also the option to request a delivery, as a user would expect to make a delivery request from here, even though it is included in a previous menu.

![Deliveries Menu](/media/images/screenshots/delivery-menu.png)

##### All Deliveries
This option displays a table of all entries in the deliveries worksheet. The user can then view all the requested, scheduled, and delivered car data in one place.

- [All Deliveries GIF](/media/gifs/delivery-report1.gif)

##### Scheduled Deliveries
The scheduled deliveries option displays a table of cars with the matching status 'scheduled'.

- [Scheduled Deliveries GIF](/media/gifs/delivery-report1.gif)

##### Requested Deliveries
The requested deliveries option displays a table of cars with the matching status 'requested'.

- [Requested Deliveries GIF](/media/gifs/delivery-report2.gif)

##### Completed Deliveries
The scheduled deliveries option displays a table of cars with the matching status 'delivered'.

- [Completed Deliveries GIF](/media/gifs/delivery-report2.gif)

#### Help Menu
The help menu provides the user with a single document help guide. The help guide is split into sections as per each menu option and details the use and function of each option.
This gives the user a better understanding of how the VinVentory app works and the features that are available.

![Help Menu](/media/images/screenshots/help-menu.png)

### Future Features
To expand on the VinVentory app in the future, I would like to create a standalone version of the app so it is not bound by the Heroku deployment limitations.
If this were the case, I would like to add the additional car information that I have removed to work within the limits of Heroku. This was information such as mileage and engine size, or buyer details for sold cars. I would also like to potentially include further details, providing customers and salespersons with a better view of a car's details.

I would like to add further functionality around the deliveries section, adding options to confirm delivery requests, edit scheduling, and mark cars as delivered.
In terms of the menus, I would like to add the ability to remain within a function once completing it, such as searching for two or more cars by ID without returning to the menu. Currently, when each function is finished, the user must return to the menu and re-enter that menu option to do it multiple times.

I would also like to add colour to the app's text in all areas. The use of colour can draw attention to different aspects of the app and indicate things such as warnings in red or confirmations in green. This would add a more appealing visual aspect to the app considering the app is text-based.

For sales reports, I would like to expand on the information shown by adding things such as location-specific data, giving the user the ability to see the performance of each site.
Finally, I would like to include a more detailed status for each car, displaying delivery information or deposit reservations.

Below I have included some screenshots of the tables before I removed additional data for Heroku deployment.
    - [Add car](/media/images/screenshots/features/add-car-screen1.png)
    - [All Stock](/media/images/screenshots/features/all-stock-screen.png)
    - [Find ID](/media/images/screenshots/features/find-id-screen.png)
    - [Sales Report](/media/images/screenshots/features/search-sales-table2.png)
    - [Delivery Report](/media/images/screenshots/features/requested-delivery-report.png)

## Deployment

When deploying locally there are multiple steps you need to take to ensure all elements are working correctly. To summarize, you must first clone the repo, create a Google Sheet and connect via the API, and finally create and deploy the app to Heroku. 
Each step is detailed below.

### Fork Repository

- To fork the repository
    - Login or Sign Up to GitHub
    - Navigate to the repository for this project [Quiz Crunch](https://github.com/KyleMardell/vinventory)
    - Click the "Fork" button on the top right of the page

### Clone Repository

- To clone the repository
    - Login or Sign Up to GitHub
    - Navigate to the repository for this project [Quiz Crunch](https://github.com/KyleMardell/vinventory)
    - Click on the "Code" button
    - Select how you would like to clone (HTTPS, SSH, or GitHub CLI)
    - Copy your chosen link
    - Open the terminal of your code editor or IDE
    - Change the current working directory to the location you want to use for the cloned directory
    - Type "git clone" into the terminal followed by the copied link and press enter.

### Google Sheets

- To set up the Google worksheet
    - Login or Sign up to your [Google](https://google.com) account
    - Navigate to Google Sheets
    - Click on the "Blank Spreadsheet" option to create a new spreadsheet
    - Name the spreadsheet (Note the name)
    - Enter headings as found in the [worksheets section](#worksheet--database)
    - Enter car data
- To activate the Google Sheets API
    - Navigate to Google Cloud
    - Click on the project drop down and create new project
    - Click on the menu dropdown and select "APIs & Services"
    - Search for "Google Sheets API" and enable to activate
    - Search for "Google Drive API" and enable to activate
    - Navigate to "Google Drive API" overview page
    - Click "Create Credentials"
    - Select "Google Drive API" for "Which API are you using?"
    - Select "Application Data" for "Which sata will you be accessing?"
    - Select "No, I'm not using them" for "... App engine or Cloud Functions?"
    - Click "Done"
    - Enter a "service account name" (I used "vinventory")
    - Click the "Grant this service account access to project" dropdown
    - Select "Editor" as the role
    - Click "Done"
    - Click on the account (vinventory) under "Service Accounts"
    - Navigate to the "keys" tab
    - Click the "Add key" dropdown, select "Create new key"
    - Select JSON, and click "Create"
    - API Credentials should be saved to "downloads" folder
    - Rename saved file to "creds.json"
- Link API to worksheet
    - Open "creds.json" file (add to project if deploying locally, ensure "creds.json" is added to gitignore file so not to add to repo)
    - Copy the email address from key "client_email"
    - Navigate to Google Sheets spreadsheet (vinventory)
    - Click the "Share" button
    - Paste in the "client_email" address
    - Select "Editor" from the dropdown option, un-tick "Notify people"
    - Click "Share"

## Heroku

- Deploy to Heroku
    - Login or sign up with your [Heroku[(https://heroku.com)] account
    - Navigate to the dashboard
    - Click "New" at the top right of the screen, select "Create new app"
    - Enter a unique name (I used vinventory)
    - Choose a region
    - Click "Create app"
    - Navigate to the "Settings" tab
    - Navigate to "Buildpacks"
    - Click "Add buildpack"
    - Add "Python" and "Node.js" as buildpacks
    - Click "Reveal Config Vars"
    - Add a new config var with key "PORT" and value "8000"
    - Add a new config var with key "CREDS" and add the contents of your creds.json file
    - Navigate to the "Deploy" tab
    - Select GitHub as deployment method
    - Authenticate with GitHub account
    - Search for repo name (vinventory), click "Connect"
    - Optionally enable "Automatic deploys"
    - Click "Deploy branch" under "Manual Deploy" ensuring main branch is selected

## Python Packages

In order to run the VinVentory app locally, you will need to make sure python is installed and install the following packages. This can usually be done using either "pip install 'package_name'" or "pip3 install 'package_name'" depending on which operating system you are using.

- Packages
    - "gspread google-auth"
    - "prettytable"
    - "pytest" (if running the test_input_validation.py file)

## Testing

Testing can be found at, [Testing](/TESTING.md)

## Credits

### Google Sheets API
I learned the use of the Google Sheets API through the [Code Institute](https://codeinstitute.net/) project "Love Sandwiches". I used the same API connection methods (creds, scope), expanding on the use of gspread to create the worksheet functions required for the VinVentory app. 

### Ascii Art
To make the home screen more appealing, I wanted to incorporate the use of ascii art with the business details on the home screen.
I found an ascii art image of a car that I though fit the theme of the app from [ascii.co.uk/art/car](https://ascii.co.uk/art/car)

### Python Unit testing
In order to learn about python unit testing, I followed a YouTube course on pytest by [Free Code Camp](https://www.youtube.com/watch?v=cHYq1MRoyI0&t=1787s) and referenced the [pytest documentation](https://docs.pytest.org/en/8.2.x/getting-started.html).

### Sheet data
Once i had created the headings or columns for my worksheets in Google sheets and committed to the designs, I used [Chat-GPT](https://chatgpt.com/) to generate the data for each car. I then copied the created table data into the stock worksheet. I then distributed that data over sales sheets both manually and when testing during development. I used a prompt such as "generate a table of random car data with 30 cars. There should be columns for the data id, make, model, year, colour, cost, repair cost and price".