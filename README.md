# HAPPY FEETS

## Full Stack Frameworks with Django

![Responsive Mockup](media/mockup.png)  

---

## Project Summary

Happy Feets is....

This project is my final milstone project for Code Institute and is for educational purposes only.

View the live website: [Happy Feets](https://happy-feetss.herokuapp.com/) 

---
# Table of contents

- [UX](#ux)
    - [Strategy](#strategy)
    - [Scope](#scope)
        - [User stories](#user-stories)
    - [Structure of the website](#structure-of-the-website)
    - [Skeleton](#skeleton)
        - [Wireframes](#wireframes)
        - [Database Schema](#databese-schema)
    - [Surface](#surface)
- [Features](#features)
- [Technologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

---
# UX

## Strategy



## Scope

Based on the requirements of achieving user's and owner's goals and stories, below is the list of required pages with the features and functions:

- Simple design landing page that the purpose of the website is obvious to anybody and even first-time users know how to navigate the website. 
- Services page where users can view all the services the site provides.
- Blog page where user can read and comment on the latest post / news.
- About page where users can get information about the site and what it provides.
- Contact page where users can contact the admin of the site or to send a quotation,
- Checkout success page where users get confirmation of purchase
- Login / register page where users can log in or register.
- Logout function that users can safely log out the website and takes users back to the home page.
- Blog page management (admin only) where admin can add, edit, approve and delete content.


### User Stories

- Customers
    - User experience
        - As a customer, I would like to be able to navigate the website easily.
        - As a customer, I would like to see what the website is providing.
        - As a customer, I would like to see some information about the company.
        - As a customer, I would like to be able to contact the company.
    - User booking treatments / shopping
        - As a customer, I would like to search for all the packages/products the company sells.
        - As a customer, I would like to see the package/product price and description.
        - As a customer, I would like to be able to add products to my shopping cart.
        - As a customer, I would like to be able to edit my shopping cart.
        - As a customer, I would like to be able to checkout easily.
        - As a customer, I would like to receive confirmation of my order.
    - User account
        - As a customer, I would like to save my details to an account.
        - As a customer, I would like to see my previous order details.
        - As a customer, I would like to leave a review of the company.
- Website owner
    - Site management
        - As the business owner, I would like to be able to edit and add products easily.
        - As the business owner, I would like to be able to delete products.
        - As the business owner, I would like to have access to an admin section. 
        - As the business owner, I would like my customers to be able to shop on the site easily.
---

## Structures of the website

Website contains:
- Navigation bar is fixed and collapse to burger icon on mobile devices with essential links to navigate on the website.
- The home page first view will be simple in structure with a short text intro. 
- Below it will contain some information about services and a about snippet with a testimonial carousel. 
- The services page will contain information of what the services can be requested.
- The about page will contain information of what the site provides and some information about the site ethos.
- The contact page / request is a clean and simple contact.
- The footer will contains social media links.


## Skeleton

### Wireframes

I've created WireFrames using Balsamiq and have included the links to access them below, and they are the core pages of the website.

- [Desktop](readme_data/wireframes/wireframe-desktop.png)
- [Tablet](readme_data/wireframes/wireframe-tablet.png)
- [Mobile](readme_data/wireframes/wireframe-mobile.png)


### Database Schema

The database diagram shows a list of items in each object and relationships between each object. I've used Django default databases SQLite in gitpod environment and PostgreSQL database with Heroku as production enviroment.

- [Database Schema](readme_data/database/database-schema.png)


## Surface

### Colors
Colours used in a project:

### Fonts
As a main font I used...

### Images
Images used in this site are taken from:
- [Freepik](https://freepik.com/)
- [Pexels](https://www.pexels.com/)
- [Unsplash](https://unsplash.com/)


---
# Features:

## Existing Features:

### Base

![Landing Page]()

The landing page contains one fixed background image. User will see on landing page:
- Welcome Hero image
- Treatments information
- Shop information
- Testimonial snippet
- Classic footer with contact information

All links/snippets will contain a call to action button that redirect to selected subsite.

### Navbar

![Navbar]()

Navigation bar is located on the top of the website. It is responsive and transforms into a burger menu on smaller devices. Brand logo is located in the top left corner. It is a link and it always redirect user to the home page. Page links are in the center of the main header and underneath the search field. There are two different views of the navigation bar - one view to all users, and the other to those users who are logged in to the website.


### About Us

![About Us]()

This is where the users can read more detailed information about what the site is about and who the persons behind it are. 


### Treatments Selection

![Treatments]()

This is where the users can read more detailed information about treatments and packages. This page shows all available treatments.
From here user is encourage to buy a different packages.

For administrator here are an options to `Edit` or `Delete` packages.


### Shop

![Shop]()

This page offers products and has the same set up as Treatments. 


### Package/Product details

From this site user can select quantity, add selected package/product to the bag, view a bag or go back to treatments/shop site to view the whole asortment.


### Shopping Bag

![Shopping Bag]()

User can see all selected packages/products on the shopping bag page.
Update link is available to increase or decrease amount of packages/products.
Remove link will remove selected package/product.
Buttons below total amount to pay give an options to: go back and add more packages/products or go to secure checkout.


### Checkout

![Checkout]()

Secure checkout page allow user to add all nesesary ditails to place an order.
On right hand site of the screen there is order summary. A test purchase can be made with the following details:
- credit card: 4242 4242 4242 4242
- expiration date: 04 / 24
- CVC: 424
- ZIP: 42424

Complete order will submit a payment and redirect to order confirmation page.
Also user can go back to the bag to adjust shopping bag.


### Checkout success - Thank you

![Checkout Success]()

After purchase customer can see order summary and to buttons:
- Go back to home page - user will be redirected do home page
- Contact Us to book a space - user will be redirected to contact us page.


### Reigster

![Register]()

Simple registration form that allow user to register on the page.


### User Login

![Login]()

Login form that allow user to login on the page.


### My Profile

![Profile]()

If user is logged in then is able to view its profile. Options to update a profile or to browse order history are available.


### Contact Me

![Contact]()

This is just a mainly email link in the footer where user can contact the business owner to book a treatment, ask a question or make any other enquiry.


### Add Treatment / Product

This option is available to administrator only. Form allows to add name, description, image url or select an image from local storage.



## Features Left to Implement:

- Add blog/news site 
- 
- 
- 

----
# Technologies Used:

## Languages, framework libraries and programs:
- [HTML5](https://en.wikipedia.org/wiki/HTML) - For markup
- [CSS3](https://en.wikipedia.org/wiki/CSS) - For style
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - For interaction
- [Python3](https://www.python.org/) - As a backend programming language
- [Django](https://www.djangoproject.com/) - As the main framework of Python
- [SQLite](https://www.sqlite.org/index.html) - As a database in development mode
- [PostgreSQL](https://landing.aiven.io/en/aiven-for-postgresql/) - As a database in production mode
- [Getbootstrap](https://getbootstrap.com/) - For containers and layout
- [MDBootstrap](https://mdbootstrap.com/) - For card snippets
- [Google Fonts](https://fonts.google.com/) - For fonts
- [Font Awesome](https://fontawesome.com/) - For icons
- [Gitpod](https://www.gitpod.io/) - As Integrated Development Environment (IDE)
- [Git](https://git-scm.com/) - For local version control, keeping the files & documents
- [GitHub](https://github.com/) - For online version control and keeping the files & documents
- [Heroku](https://www.heroku.com/) - For deploying the website
- [Balsamiq](https://balsamiq.com/) - For wireframes
- [Am I responsive](http://ami.responsivedesign.is/) - For mockup

---  
# Testing:

## Validator Testing:
- [W3C Markup Validation Service](https://validator.w3.org/) - For testing HTML code
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - For testing CSS code
- [PEP8 Online](http://pep8online.com/) - For checking Python PEP8 requirements. 
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - For testing, style checking and debugging


### This project was tested with the following browsers: 
- Laptop MacOS Big Sur (ver 11.4): Google Chrome


### The following steps were taken:

- Manually testing via Devtools 
- Non-logged in user attempting to access content (refused)
- All buttons and links tested
- Users availing of the like button
- Image uploads tested - large, incorrect format etc. 
- Form tested with correct and incorrect detail 
- Clear user experience & navigation
- Picture loading speed
- Login/register/logout functionalities
- Edit, add, delete items & posts functionalities
- bugs or disabled links

### Issues / Unfixed Bugs:

- Like button not working properly with hovering as well as counting likes - not fixed 
- Testimonial carousell indicators doesnt float within the testimonial card on smaller devices - not fixed
- When running CSS validator there is alot of warnings depending on the full bootstrap theme choosen.
- I had issues with making the contact post - fixed.
- All through I had many issues to make it work as I planned for in the beginning. The main reason for that depends on that I choosed to go with a template instead of doing it all by my self from scratch. I discoverd during the way that it took me much more time to try to change the prewritten scripts then it would have done if I just started from scratch. Al though it has been a good experience with alot of lessons.


---
# Deployment

## Setting up
---
The website of this project requires back-end technologies such as server, application, and database so the website is deployed in [Heroku](https://www.heroku.com/), which is a cloud platform with a service supporting several programming languages, because GitHub can only host a static website. Heroku Postgres is used for the database, which is also a cloud-based platform, is used to store static files and images as Heroku has [no files system to store new files


## Setting up Heroku App
---
- Create an app in Heroku. Click *New*, put App name and select region.
- Add Heroku Postgres for the database.
- Install `gunicorn`, `dj_database_url` and `psycopg2-binary` to use Heroku Postgres, and run `pip3 freeze > requirements.txt` command to add them on requirments.txt.
- Update `settings.py` of the app. Import `dj_database_url`, comment out sqlite databases and add dj databases variable temporary while the database is transferred to Heroku Postgres.
- Run `python3 manage.py showmigrations` command to see the status of migrations (Currently not migrated). Run `python3 manage.py migrate` command to migrate.
- Create a super user with `python3 manage.py createsuperuser` command for product admin.
- Create a **Procfile** which specifies the commands that are executed by the app on startup.
- Temporary disable collectstatic by setting `heroku config:set DISABLE_COLLECTSTATIC = 1` and host name of Heroku to allowed hosts in `settings.py`.
- Generate a new secret key, set it up in Heroku and update `settings.py`. Change the setting of Debug mode that only True in Development mode.


## Deployment through Heroku
---
- Navigate to the "Deploy" section.
- Scroll down to "Deployment Method" and select "GitHub".
- Authorize the connection of Heroku to GitHub.
- Search for your GitHub repository name, and select the correct repository.
- For Deployment there are two options, Automatic Deployments or Manual.
- Automatic Deployment: This will prompt Heroku to re-build your app each time you push your code to GitHub.
- Manual Deployment: This will only prompt Heroku to build your app when you manually tell it to do so.
- Ensure the correct branch is selected "master/Main", and select a deployment method. For this project I chose Manual Deployment.


## How to Fork the respository
---
- Log into GitHub.
- In Github go to (https://github.com/Sndrahel/Handywoman.git).
- In the top right hand corner click "Fork".
- A copy of the repository will then be added to your repositories page.

## How to clone the repository
---
- Go to the GitHub repository.
- Locate the Code button which is to the left of the green gitpod button and click it.
- Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard.
- Open Git Bash.
- Change the current working directory to the one where you want the cloned directory.
- Type git clone and paste the URL from the clipboard.
- Press Enter to create your local clone.

 
---
# Credits

## Code:
- [Code Institute](https://codeinstitute.net/) - Inspiration of blog layout were taken from tutorial.
- [Youtube]() - Tutorial used for setting up sending email .  
- [Stack Overflow](https://stackoverflow.com/) - Was used to find solutions and debugging.
- [GitHub]() - Inspiration of structure for this README file were adapted from this site. 
- [GitHub]( - Inspiration of structure and contactforms were adapted from this site. 
- [GitHub]() - Inspiration of layout for main site were adapted from this site.
 

## Acknowledgments:

- Nishant Kumar: My Code Institute mentor who guided me through this process and shared a lot of valuable knowledge.


[Back to Table of contents](#table-of-contents)
