# VinVentory
VinVentory is a used car management system. The VinVentory app is aimed at small used car businesses to hold information about their sales and cars in stock. Using the Google Sheets API as a database, VinVentory provides the ability for multiple sites to have an easy way to see what cars are in stock on other sites.

mockup screenshot here

- The deployed site can be found at - [VinVentory Heroku App]()
- The repository can be found at - [VinVentory Repo]()

- - - 

## Contents

- - - 

## User Experience

### First time visitor goals
First time visitors to the app are expected to be potential customers/clients of the VinVentory app. With this in mind, first time visitor goals are to provide a look at our solution to an existing problem, through a centralized vehicle stock, sales and delivery management system. First time visitor should be impressed by the usability and features of the VinVentory app, to help better manage vehicle stock and sales data.

### Returning visitor goals
Returning visitors to the app will usually be businesses with the VinVentory system deployed in their business. Therefore the returning visitor goals are to provide an easy to use and navigate vehicle management system. Data should be quickly accessible and easy to understand.

### App usage goals
The goals for the app usage is to provide a solution to a real world problem, through an effective online car management system. The app should provide an effective tool for small businesses with either a single or multiple sites, with the ability to track vehicle stock, mark cars as sold and see sales data, and request internal vehicle deliveries.

## Design

### Concept
The concept of the VinVentory vehicle management system is to provide a tool for small used car businesses to track stock and sales data, as well as request and track internal deliveries.
I wanted to create an app with a real world scenario in mind, and found this concept to be much larger in scope than initially expected, although keeping to a MVP, and not fully outfitting the app helped to rain in the scope.

### Worksheet / Database
I used Google Sheets API as a database to hold all the information about the car in stock, and all sales and delivery sheets. I had first designed the worksheets with columns for over 15 different vehicle details. Although once i had deployed to Heroku, i found the max character width was 80, and with this in mind i had to remove many columns of data to better display when deployed using Heroku. I had tried to include all information a potential customer may want to know, but had to reduce the scope due to the Heroku limitations. Even after removing many columns of information such as, milage and engine size, i feel that this MVP gives a good sense of what the VinVentory app could be once fully built, and these items would be easy enough to add in the future.

### Functionality
For the functionality of the app, i wanted to provide the user with information about what cars a business may currently have in stock, as well as current and past sales data. This means that the ability to add, edit and delete a car from the stock sheet needed to be included. 
The app also needed to be able to mark a car as sold, removing it from the stock sheet and adding it to the current months sales sheet, if the sales sheet exists, if not then one is automatically created.
The user can view a list of all car in stock, or alternatively search for a single car by using its internal ID number, or search for all cars with a matching input, such as all red cars, or all Citroen cars.
In order to add a car to the stock sheet, the user must enter all the required information when prompted and an internal ID will be automatically generated before the car is added to the stock sheet.
The user can also edit the details of a car currently in the stock sheet by entering is internal ID number. They can then choose which detail to edit and enter a new value.
When deleting a car from the stock sheet, the user must enter the internal ID of the car, and is shown a warning message before confirming and deleting the car.
A delivery request can be made for a car, adding its details to the delivery sheet and marking it status in the stock sheet with a "-D" to signal a delivery has been requested. I initially use the appendix "- Delivery Requested" but shortened it for better viewing on the Heroku deployment terminal.
There are multiple sales reports and tables that the user can view through each corresponding menu item. Sales tables show all car sold in a particular month, with added sales details such as sale price and date. Sales reports can be generated for the current month or any month since the VinVentory system has been implemented. A sales report shows data about how many cars hae been sold, total profits made, total costs etc.
Similarly delivery reports can be viewed in table format, with the option to filter deliveries by status.

### Menus
The menu system in the VinVentory app uses a simple number system, with the user inputting a number to navigate through the menus. There is a home menu welcoming the user to the app and displaying the sub-menu options. The sub menus are where the functionality of the app is contained. There are menus for stock, add/edit car details, sales reports, delivery reports and help. Within each of these menus there are the options to view data about cars in stock, sold cars per month, delivery requests etc. Each sub-menu function is explained in is corresponding readme section.

### Flowcharts

## Features

### Existing Features

#### Home Menu
The home menu serves as a way to welcome the user to the VinVentory app and navigate to another sub menu. The user is greeted with welcome message and an attractive ascii art image of a car to show the apps overall function. The user is shown a small menu of options to choose from and can enter a number to navigate to a sub menu or help section.
Entering 0 from the home menu will exit the program.

#### Stock Menu
The stock menu is where the user can view information about cars currently in stock. There are 3 options within the stock menu, view a list of all cars, view car information by ID, or search stock by keywords. The user can enter 0 to see an option to return to the main menu or exit the program. 

##### All Stock

##### Find By ID

##### Search by terms

#### Add/Edit/Sell/Delete Menu

##### Add Car To Stock

##### Edit Car In Stock

##### Sell Car

##### Request Delivery

##### Delete Car In Stock

#### Sales Reports Menu

##### Current Sales Table

##### Current Sales Report

##### Past Sales Table

##### Past Sales Month

#### Deliveries Menu

##### All Deliveries

##### Scheduled Deliveries

##### Requested Deliveries

##### Completed Deliveries

#### Help Menu

### FUture Features

## Deployment

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

## Testing

## Credits

### Ascii Art
To make the home screen more appealing, I wanted to incorporate the use of ascii art with the business details on the home screen.
I found an ascii art image of a car that I though fit the theme of the app from [ascii.co.uk/art/car](https://ascii.co.uk/art/car)
