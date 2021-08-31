# Loadsheet Planner (WORK-IN-PROGRESS)

The Loadsheet planner application is designed for use by an airline dispatcher to quickly calculate the acceptable loads whilst preparing an aircraft for dispatch. <br>
It is designed to take a number of inputs from the user to narrow down the acceptable fuel, passenger and cargo loads available to them. In this scenario the fuel, passenger and cargo loads would have already been passed from the company and Flight Crew.

To try your hand planning a loadsheet please click [**here**](https://loadsheet-planner.herokuapp.com/).

![Image of the deployed application](assets/videos/app_load.gif)

# Contents

* [**User Experience UX**](<#user-experience-ux>)
    *  [User Stories](<#user-stories>)
    * [Owner Stories](<#owner-stories>)
    * [Definitions](<#definitions>)
    * [Instructions](<#instructions>)
* [**Data Model**](<#data-model>)
    * [Code flow charts](<#code-flow-charts>)
* [**Features**](<#features>)
    * [**Existing Features**](<#existing-features>)
    * [**Future Features**](<#future-features>)
* [**Technologies Used**](<#technologies-used>)
* [**Testing**](<#testing>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
*  [**Acknowledgements**](<#acknowledgements>)

# User Experience

## User Stories

* As a user I want to input data to creata a loadsheet.
* As a user I want to select which aircraft I am loading.
* As a user I want to input the fuel load.
* As a user I want to input the requested Passenger numbers.
* As a user I want to input the amount of cargo.
* As a user I want to know that my inputs are correct.

## Owner Stories

* As an owner I want to ensure the data entered is correct and valid.
* As an owner I want to ensure the loadsheet is useable by those detached from the input process.

[Back to top](<#contents>)
## Definitions
* Aircraft - 
    * Boeing 747-400 [![B747 image](assets/images/b747.jpg)](https://en.wikipedia.org/wiki/Boeing_747-400)
    * Embraer 190 [![E190 image](assets/images/e190.png)](https://en.wikipedia.org/wiki/Embraer_E-Jet_family)
    * Jetstream 41 [![J41 image](assets/images/j41.jpg)](https://en.wikipedia.org/wiki/British_Aerospace_Jetstream_41)

* Terminology - 
    * [**Loadsheet**](https://www.linkedin.com/pulse/aircraft-loadsheet-peter-irungu/) - Provides the crew with the various weights that are crutial for te flight. Compiled for information from the airline (passenger and cargo figures) and the crew themselves (fuel, aircraft specific weights).
    * [**Aircraft Dispatcher**](https://www.myworldofwork.co.uk/my-career-options/job-profiles/flight-dispatcher) - Provides the Pilots with the weight and balance information relevant to the flight. Also is the liason between the Pilots and the loading staff for both bags and passengers.
    * **Flight crew** - In this case Pilots, could include loadmaster and navigatior in other cases.
    * **Basic Weight** (eWeight in this app) - The weight of the aircraft without passengers, baggage or usable fuel.
    * **Traffic load** - For this app it is the mass of the passengers and bags. Often      cargo mass is also included in this definition.
    * **Zero Fuel weight (ZFW)** - The weight of the loaded aircraft without the fuel.
    * **Take off weight (TOW)** - The weight of the aircraft at take off. It is comprised off the Basic weight, traffic load and fuel. 
    * **Maximum take off weight (MTOW)** - The maximum weight the pilot is permitted to attempt to take off. Can be reduced for performance requirements (not functional in this app version).
    * **Underload** - The difference between the MTOW and the TOW.

[Back to top](<#contents>)
## Instructions

1. Select a, b or c to choose the aircraft you are going to load.
2. Input the fuel figure (in kg) that has been passed to you by the Flight crew.
3. Input the passenger numbers (adult/children) that has been passed to you by the Airline.
4. The Loadsheet Planner calculates the aircraft's underload.
5. If you have an underload, you can input the amount of cargo you require.
6. The loadsheet prints automatically on completion of the above steps. Currently it prints to the app interface.
7. The user is then given an option to load another flight or exit.

[Back to top](<#contents>)
# Data Model

## Code flow charts

![Code flow charts images](/assets/images/LSFlow.png)

[Back to top](<#contents>)
# Features

## Existing Features
* Welcome page
    * The page the Loadsheet Planner displays initially.
    ![Welcome page image](assets/images/opening-text.png)
* Fuel input
    * Initial fuel input page
    ![Fuel input image](assets/images/fuel-input.png)
    * Too much fuel - Fuel input is above the maximum allowed.
    ![High-fuel image](assets/images/high-fuel.png)
    * Not enough fuel - Fuel input is below the minimum required.
    ![Low fuel image](assets/images/low-fuel.png)
    * Incorrect input character - Input is not a number.
    ![Incorrect fuel input images](assets/images/nan-fuel.png)

* Passenger input
    * Initial passenger input.
    ![Passenger input image](assets/images/pax-input.png)
    * Too many passengers
    ![Too many pax image](assets/images/high-pax.png)
    * Incorrect input character
    ![Pax error image](assets/images/pax-error.png)

* No underload 
    * This feature prevent the loading of cargo as the aircraft is already too heavy. It directs the user to remove either some passengers, fuel or previously loaded cargo.
![Underload Image](assets/images/no-underload.png)

* Cargo input
    * Initial cargo input
    ![Cargo input image](assets/images/cargo-input.png)
    * Too much cargo
    ![Too much cargo image](assets/images/high-cargo.png)
    * Incorrect input character
    ![Incorrect cargo](assets/images/cargo-error.png)
* Print Loadsheet
    * Prints the compiled loadsheet to the application interface and gives the user the option to load another flight or exit.
    ![Printed loadsheet](assets/images/printing-loadsheet.png)
## Future Features
* The loadsheet displaying on the browser screen. Within the confines of the CI template this feature isn't possible. For this release the loadsheet is stored as a pdf in the workspace after it is printed to the screen. [Loadsheet](loadsheet.pdf)

[Back to top](<#contents>)
# Technologies Used
* Python
* GitHub
* Lucid Charts


[Back to top](<#contents>)
# Testing

[Back to top](<#contents>)
# Deployment

[Back to top](<#contents>)
# Credits



[Back to top](<#contents>)
# Acknowledgements

[Back to top](<#contents>)

