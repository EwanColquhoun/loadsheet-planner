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
* **Welcome page** <details><summary>Screenshots</summary>
    The page the Loadsheet Planner displays initially.<br>
    ![Welcome page image](assets/images/opening-text.png)</details>

* **Fuel input** <details><summary>Screenshots</summary>
    Initial fuel input page. <br>
    ![Fuel input image](assets/images/fuel-input.png)

    Too much fuel - Fuel input is above the maximum allowed. <br>
    ![High-fuel image](assets/images/high-fuel.png)

    Not enough fuel - Fuel input is below the minimum required. <br>
    ![Low fuel image](assets/images/low-fuel.png)

    Incorrect input character - Input is not a number. <br>
    ![Incorrect fuel input images](assets/images/nan-fuel.png)</details>

* **Passenger input** <details><summary>Screenshots</summary>
    Initial passenger input <br>
    ![Passenger input image](assets/images/pax-input.png)

    Too many passengers <br>
    ![Too many pax image](assets/images/high-pax.png)

    Incorrect input character <br>
    ![Pax error image](assets/images/pax-error.png)</details>

* **No underload** <details><summary>Screenshots</summary>
    This feature prevent the loading of cargo as the aircraft is already too heavy. It directs the user to remove either some passengers, fuel or previously loaded cargo. <br>
    ![Underload Image](assets/images/no-underload.png)</details>

* **Cargo input** <details><summary>Screenshots</summary>

    Initial cargo input <br>
    <img src="assets/images/cargo-input.png" alt="Cargo input image">

    Too much cargo <br>
    ![Too much cargo image](assets/images/high-cargo.png)

    Incorrect input character <br>
    ![Incorrect cargo](assets/images/cargo-error.png)</details>

* **Print Loadsheet** <details><summary>Screenshots</summary>
    Prints the compiled loadsheet to the application interface and gives the user the option to load another flight or exit. <br>
    ![Printed loadsheet](assets/images/printing-loadsheet.png)</details>


[Back to top](<#contents>)
## Future Features
* The loadsheet displaying on the browser screen. Within the confines of the CI template this feature isn't possible. For this release the loadsheet is stored as a pdf in the workspace after it is printed to the screen. [Loadsheet](loadsheet.pdf)

[Back to top](<#contents>)
# Technologies Used
* [Python](https://docs.python.org/3/contents.html) - primary language of the application.
* [GitHub](https://github.com/) - to host the repositories.
* [Gitpod](https://www.gitpod.io/) - as the IDE for the application.
* [Lucid Charts](https://www.lucidchart.com/) - to create the flow diagram.
* [OBS Studio](https://obsproject.com/) - to record the screen for the gif.
* [ezgif](https://ezgif.com/) - to create the gif for the top of the readme file.

[Back to top](<#contents>)
# Testing

[Back to top](<#contents>)
# Deployment

### **To deploy using [Heroku](https://www.heroku.com/):**

1. Ensure your requirements.txt file has the required dependencies. To do this you can use the following code in your IDE:
    > pip3 freeze > requirements.txt
    - Heroku will use this file to import the dependencies that are required.
3. Create or Login to your Heroku account.
4. Navigate to Dashboard. 
5. Click "New" and select "create new app" from the drop-down menu. This is found in the upper right portion of the window. 
6. Provide a name for your application, this needs to be unique, and select your region.
7. Click "Create App".

### Setting up Heroku

1. Navigate to "Settings" and scroll down to "build packs".
2. Click "build packs" and then click both "python" and "node.js"(node.js is needed for the Code Institute mock terminal.)
3. Ensure that the python buildpack is above the node.js buildpack, You can click and drag the packs to re-arrange them.
![Heroku Buildpack](assets/images/buildpacks.png)

### App Deployment

1. Navigate to the "Deploy" section.
2. Scroll down to "Deployment Method" and select "GitHub".
3. Authorize the connection of Heroku to GitHub.
4. Search for your GitHub repository name, and select the correct repository.
5. For Deployment there are two options, Automatic Deployments or Manual.
    - Automatic Deployment: This will prompt Heroku to re-build your app each time you push your code to GitHub.
    - Manual Deployment: This will only prompt Heroku to build your app when you manually tell it to do so. 
6. Ensure the correct branch is selected "master/Main", and select the deployment method that you desire. In this case, I will be using Automatic Deployment.
![Heroku deployment](assets/images/deploy.png)

### **To fork the repository on GitHub**
A copy of the GitHub Repository can be made by forking the repository. This copy can be viewed and changes can be made to the copy without affecting the original repository. Take the following steps to fork the repository;
1. Log in to **GitHub** and locate the [repository](https://github.com/EwanColquhoun/loadsheet-planner).
2. On the right hand side of the page inline with the repository name is a button called **'Fork'**, click on the button to create a copy of the original repository in your GitHub Account.
![GitHub forking process image](assets/images/forking.png)

### **To create a local clone of this project**
The method from cloning a project from GitHub is below:

1. Under the repository’s name, click on the **code** tab.
2. In the **Clone with HTTPS** section, click on the clipboard icon to copy the given URL.
![Cloning image](assets/images/clone.png)
3. In your IDE of choice, open **Git Bash**.
4. Change the current working directory to the location where you want the cloned directory to be made.
5. Type **git clone**, and then paste the URL copied from GitHub.
6. Press **enter** and the local clone will be created.

[Back to top](<#contents>)
# Credits
* Non-original code is credited in the [functions.py](functions.py) file. 
[Back to top](<#contents>)
# Acknowledgements

[Back to top](<#contents>)

