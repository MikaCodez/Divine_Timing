# Divine Timing
Divine Timing is an Eccommerce store that specialises in handcraft digital watches and traditional watches.

![responsive page](https://user-images.githubusercontent.com/65243328/184502312-b607df79-aee3-44f3-b988-e257eb320d37.JPG)

[Deployed site here](https://divinetiming.herokuapp.com/)


## UX
### Users
The user should be able to interact with the website freely and be able to visit the product pages of the site including, watches, glasses, watch straps etc. They will be able to also Sign up and login with an authenticated account that allows them to interact with their previous orders on their account etc.

### Admins
The Admins should be able to manage the accounts of the users registered to the site, and freely able to use product management to alter and delete products at will.

### Agile Methodology

Agile Methodology was used via Github Projects Kanban board in order to create user stories and execute them as issues in a sprint fashion.

### User Stories
| iD | Story | Resolution |
| --- | --- | --- |
| #1 | Account registration | Admin App |
| #2 | View a list of products | Web App |
| #3 | View individual product details | products Section |
| #4 | Able to identify different sectors of the site, Deals, clearance, offers etc. | Booking Section |
| #5 | Register for an account | Web App |
| #6 | Easy to login or logout | Web App |
| #7 | Enabled to password reset if lost account details  | Web App |
| #8 | Receive an email confirmation after registering  | Web App |
| #9 | Able to view purchases any time | Checkout App |
| #11 | Able to sort and search products  | Web App |
| #12 | Sort a specific category or product  | Web App |
| #13 | Search for a product by name or description  | Web App |
| #14 | View order history  | Checkout App |
| #15 | Remove or add items to cart/bag  | bag App |
| #16 | Easily able to enter Payment information  | Web App |
| #17 | Assured that payment information is safe and secure  | Web App |
| #19 | Receive an email confirmation after checking out  | Web App |
| #20 | Add a productt  | Admin App |
| #21 | Edit/update a product | Admin App |
| #22 | Delete a product  | Admin App |


### Purpose
The Application is designed as an eccomerce Watch and Jewelry store to attract users and purchase the products online via the store.
They will be sent the uxury items to their address once purchased.

  
### Colours


![coolors ghit]

#000002 Rich Black used Gradient for the main bulk of the site. To give the clean aesthetic.


#59CBCF Dark Turquoise for the Buttons on the site to help them stand alone.


#DED9D9 Gainsboro for the intermediary positions of the site to help create balance.


#D4CE91 Medium Champagne on the menu sections of the website to help the food and drinks stand out.


#446D03 Dark Olive Green on some of the vegetables of the website.


#25252F Raisin Black on the Gradient of the main bulk of the site.


#FCFBF8 Baby powder on the intermediary positions of the site to help create balance.



## Features
Home Page

The home page has an attractive layout to keep the user engaged and enticed for what's to come when they eventually visit the restaurant . The page has a Navigation bar that links to other sections of the site and buttons on the page that link straight to the booking. If the user is not a registered user and not logged in. The navbar has a login/register option and the button to take the user to the login page.

![ghit homepage 1](https://user-images.githubusercontent.com/65243328/173861087-271f5dea-b433-496e-af98-14ff760ebd47.JPG)
![ghit homepage 2](https://user-images.githubusercontent.com/65243328/173861110-80353367-fc31-4db5-a7bb-75092602b769.JPG)

Menu Page

The Menu Page has an eye-catching layout to keep the user engaged and enticed for what's to come when they eventually visit the restaurant displaying a variety of options for the user to choose from.


![ghit menu page](https://user-images.githubusercontent.com/65243328/173861128-5b934c14-537e-46d2-9702-c3a8d0fead54.JPG)
![ghit menu page 2](https://user-images.githubusercontent.com/65243328/173861118-ec841d7e-45ed-4255-9323-93df870a2980.JPG)

Booking Page

The Booking Page is where the user can input the date and time they want to visit the restaurant. There is also a form to leave their details for the Restaurant so the admin is aware of the user's requirements.

The Booking page also has a Google maps location of the Restaurant to help assist users in locating the restaurant for when they show up.

![ghit booking page 1](https://user-images.githubusercontent.com/65243328/173861149-75f4f125-76f1-4f06-92e5-1d80bb7cb37c.JPG)
![ghit booking page 2](https://user-images.githubusercontent.com/65243328/173861157-cde02af1-7dc9-43c1-8395-16844474867a.JPG)
![ghit booking page 3](https://user-images.githubusercontent.com/65243328/173861164-4330d63d-68f4-4a9f-9cb8-f80c16dc265d.JPG)


Login Page / Sign up Page

Allowing new users to sign up to the site to manage reservations and existing users to log in and manage their reservations also.
![usersignintesting](https://user-images.githubusercontent.com/65243328/176655079-8f78e6cf-bb15-471b-ae54-975e6edec918.JPG)
![userregistertesting](https://user-images.githubusercontent.com/65243328/176655117-3a53fdd5-ec12-49da-b927-e99bd7892f9b.JPG)


Manage Reservation page

Allowing existing users to View and Manage their reservations that have been approved by the Admin.

Edit a Reservation

Allowing existing users to make changes to their approved existing reservation.

Delete a Reservation

Allowing existing users to delete their approved existing reservation.

![update delete reservations](https://user-images.githubusercontent.com/65243328/176655229-030d667c-92d3-4155-9472-c826262efeaf.JPG)


## Future Features

Allowing Bookings to be set up so that it directly links to the reservation page rather than it being sent to GHIT staff mailbox.

Allowing users to be able to have a delivery future and order directly from the menu of the site.


## Testing
[Link to TESTING.MD here:](https://github.com/MikaCodez/GHITrestaurant/blob/main/Testing.md)


## Deployment
The site was deployed to Heroku. The below steps were carried out to deploy.

Deployment steps add the list of requirements by writing in the terminal "pip3 freeze > requirements.txt"

Git add and git commit the changes made

Log into Heroku or create a new account and log in

top right-hand corner click "New" and choose the option Create new app, if you are a new user, the "Create new app" button will appear in the middle of the screen

Write app name - it has to be unique, it cannot be the same as this app

Choose Region - Europe selected in this instance

Click "Create App"

The page of your project opens. 8. Choose "settings" from the menu on the top of page 9. Go to section "Config Vars" and click button "Reveal Config Vars"

Go to git pod and copy the content of "creds.json" file

In the field for "KEY" enter "CREDS" - all capital letters

Paste the content of "creds.json" and paste to field "VALUE" Click button "Add"

Add another key "PORT" and value "8000"

Go to section "Build packs" and click "Add build pack"

in this new window - click Python and "Save changes" click "Add build pack" again in this new window - click Node.js and "Save changes" take care to have those apps in this order: Python first, Node.js second, drag and drop if needed Next go to "Deploy" in the menu bar on the top

Go to section "deployment method", choose "GitHub"

New section will appear "Connect to GitHub" - Search for the repository to connect to

type the name of your repository and click "search"

once Heroku finds your repository - click "connect"

Scroll down to the section "Automatic Deploys"

Click "Enable automatic deploys" or choose "Deploy branch" and manually deploy

Click "Deploy branch"

Once the program runs: you should see the message "the app was successfully deployed" 23. Click the button "View"

Forking the GitHub repository By forking out of this repository you will be able to view and edit the code without affecting the original repository.

Locate the GitHub repository. Link can be found here: GHIT Restaurant Click the button in the top right-hand corner "Fork" This will take you to your own repository to a fork that is called the same as the original branch.

Making a local clone Locate the GitHub repository. Link can be found here. Next to the green Gitpod button you will see a button "code" with an arrow pointing down You are given the option to open with GitHub desktop or download zip You can also copy https full link, go to git bash and write git clone and paste the full link


## Technologies Used
Python All packages used can be found in the [requirements.txt](https://github.com/MikaCodez/GHITrestaurant/blob/main/requirements.txt) File.
HTML - Used for the template structures.
CSS - Used to style the markup.
Javascript - Custom use minimal, to set a timeout on bootstrap messages.
GitHub - to store the overall project repository.
GitPod - used as a workspace to do the coding.
Django - django frameworks to manage apps.
Figma - To design the wireframe of the complete project.
Google Fonts - to brandize 'Harmonic Poems' with google fonts. Used for logo and all the written content.
Fontawesome - fontawesome icons for social media links and as additional design.
Bootstrap - grid, layout, columns, cards and forms structure.
Heroku - for the deployment of the project.
Coolors - to choose the colour palette and colour shades.
PostgreSQL - database storage of the models.
Cloudinary - image and static files storage.
AmIResponsive - responsiveness of the site.
Lighthouse - used for testing site functionality.
PEP8 - used for Python files testing.
W3C Markup Validation Service - used for HTML testing.
W3C CSS Validation Service - used for CSS testing

## Resources
Code Institute's Slack Community.
Code Institute's Codestar Django Blog was used in the beginning stages of the development of this project. 
Django Documentation - Heavy Reliance on Django documentation to implement forms, models, views etc.
W3Schools documentation for CSS
Bootstrap Documentation - For implementing Bootstrap styles across project
Google
Stack overflow
Youtube - Also Heavy Reliance on youtube tutorials from Codemy.com and Pretty Printed especially when it came to views and models in py


## Credits

SCOPE code credits to Code Institute, Django Blog Walkthrough Project. HTML template credit to Lucian Tartea. I have amended the code to my Restaurant sites specification.

Credits also due to Code Institute staff for helping especially Tutor Support. Special Shout out to Rebecca, Scott and Alex. I relied on them heavily during Crunch time and they pulled through and managed to help me when I was at breaking points.

Also special shouts to Tom from Slack Community. Life Save and helped guide me when it came to implementing Static files for my project.

And a Major Shout out to my Wife CleliaMente! Best Life Partner that I could ask for that helped inspire this project and encouraged me to push through!!

