# HAPPY FEETS

## Full Stack Frameworks with Django

![Responsive Mockup](readme_data/mockup/mockup.png)  

---

## Project Summary

Happy Feets is a simple website that provides feet treatments as well as it is a shop. The site help customers to book and buy treatment packages or shop products of choice.

This project is my final milstone project for Code Institute and is for educational purposes only.

View the live website: [Happy Feets](https://happy-feetss.herokuapp.com/) 

---
# Table of contents

- [UX](#ux)
    - [Strategy](#strategy)
        - [Primary Goals](#primary-goals)
        - [Business Model](#business-model)
        - [Marketing](#marketing)
        - [Search Engine Optimisation](#search-engine-optimisation)
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
---

The purpose of this project is to build a simple website for a podiatrist where customers can buy treatments or products of choice. This website can be easily changed for different type of businesses. 

<br>

### Primary Goals

**The business owners primary goals are:**

- To be able to sell treatments and products online

- To have the ability to add, remove or edit products in the store

- To access a customers order, edit and/or remove it if necessary

- To access and keep track of customer information

- To own a website which is easy to use and navigate, for all types of users on all devices.

**A potential customers primary goals are:**

* To be able to view details of the available treatments and products from the online store, and purchase.

* To be able to register for an account

* To see an order history in their account

* To be able to edit their account details

* To easily navigate the whole website and keep track of all user interactions, for example the products in their cart

<br>

### Business Model

I have chosen a traditional B2C (Business to Customer without middle person) application, which has a straightforward and user friendly interface. This site offers feet treatments and products to shop for feets. 

The business flow is as follows:

- Happy Feets sells treatments that are performed at the clinic, and products from wholesale retailers or from the manifacturers themselvse.

- The website handles selling of products or treatments from Happy Feets to the end customer, the website user.

The intentions should be obvious and users should know as soon as they enter the site what it offers and how to use it's features.

<br>

### Marketing

This site has a Facebook Business page with a link on the page footer. It can be viewed [here](https://www.facebook.com/Happy-Feets-101835319100335)

Upon registering for an account, customers can check a box to receive news and offers through email via [Mailchimp](https://mailchimp.com/).

Upon registering, the user is redirected to a new page confirming their subscription. The site owner can now see the new subscriber on their audience dashboard, and new campaigns will be sent to them too.

### Search Engine Optimisation

I have generated a sitemap.xml and robots.txt file, and only included relevant links which helps Google map the pages of the site.

I have also done some research on highest searched words in podiatrist and feet treatments.

<br>

---
## Scope
---

Based on the requirements of achieving user's and owner's goals and stories, below is the list of required pages with the features and functions:

- Simple design landing page that the purpose of the website is obvious to anybody and even first-time users know how to navigate the website. 
- Treatments page where users can view and buy all the treatments.
- Shop page where user can view and buy all products.
- About page where users can get information about the siteowner and the company.
- Login / register (account) page where users can log in or register.

<br>

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
        - As a customer, I would like to be able to checkout easily and securely.
        - As a customer, I would like to receive confirmation of my order.
    - User account
        - As a customer, I would like to save my details to an account.
        - As a customer, I would like to see my previous order details.
        - As a customer, I would like to leave a review of the product.
- Website owner
    - Site management
        - As the business owner, I would like to be able to edit and add products easily.
        - As the business owner, I would like to be able to delete products.
        - As the business owner, I would like to have access to an admin section. 
        - As the business owner, I would like to be able to provide easy shopping experience for my customers.
<br>

---
## Structures of the website
---

Website contains:
- Navigation bar is fixed and collapse to burger icon on mobile devices with essential links to navigate on the website. 
- The home page will contain some information about treatment, shop and a testimonial carousel. 
- The treatments page will contain information of what kind of treatments can be requested.
- The shop page will contain information of what kind of products can be bought.
- The about page will contain information about the siteowner.
- The footer will contains social media links.

<br>

---
## Skeleton
---

### Wireframes

I've created WireFrames using [Balsamiq](https://balsamiq.com/) and have included the links to access them below, and they are the core pages of the website.

- [Desktop](readme_data/wireframes/wireframe-desktop.png)
- [Tablet](readme_data/wireframes/wireframe-tablet.png)
- [Mobile](readme_data/wireframes/wireframe-mobile.png)


### Database Schema

The database diagram shows a list of items in each object and relationships between each object. I've used Django default databases SQLite in gitpod environment and PostgreSQL database with Heroku as production enviroment.

- [Database Schema](readme_data/database/database-schema.png)

**Data Models**

The following models have been used to populate the database and for the site to function as it should:

- Order - a users successful purchase leads to an instance of the Order model being created, storing delivery and user data

- OrderLineItem - a model holding the product information for a single product, binding the product model together with the order

- Product/Treatment - the model for the product itself and its details

- Category - the category in which the product is placed

- User - the built in Django User model, facilitates the users basic information

- UserProfile - the model storing the users product and order information

- Review - a model for users to give the product a rating and a review

<br>

---
## Surface
---

### Frontend Design
The [Bootstrap](https://getbootstrap.com/) framework was used to implement the frontend of the website to give a responsive design that provides a good UX across all devices and screen sizes.

### Colors
A neutral colour scheme was chosen for the site as most of the colour on majority of pages is provided by the treatments and shop products. The main colors used are Black, White and Green.

### Icons
[Font Awesome](https://fontawesome.com/) has been used throughout this project to provide any icons that are required.

### Images
Images used in this site are taken from: [Freepik](https://freepik.com/)

<br>

# Features:

## Existing Features:
---

### Navbar

![Navbar](readme_data/mockup/navbar.png)

The navbar is fixed and will scroll with the page content.
The top row in navbar will include a link back to the home page, a search bar and links to My Accounts and the Shopping Cart.
The bottom section will include another navigation menu, which includes links to allow the user to browse the site.
On mobile the navigation links in the bottom row will collapse into a burger menu. The links to My Account and Shopping Cart will remain visible at the top of the screen for easy access.
The navigation links in the My Account dropdown will change when the user is registered and logged in.
A message bar will be positioned below the header to allow information to be presented to the user.

<br>

### Footer

![Footer](readme_data/mockup/footer.png)

The footer will be located at the bottom of each page. The footer contain contact information, a subscribe for newsletter and social media links.

<br>

### Home Page

![Home Page](readme_data/mockup/home.png)

The home page will contain some short information about: 
- treatments and a call to action button 
- shop and a call to action button 
- a testimonial carousel. 

<br>

### Shop / Treatments Page

![Shop/treatments](readme_data/mockup/shop.png)

The Shop / Treatments page will display all the products available on the site.
It also display a sort by bar that allows customer to sort existing products. The page will clearly display the product image, name, price and a description of the product. Clicking on the product image or the call to action button will open up a new page containing more details on the selected product.
If the user has administrator privileges and is logged in then there will be addition links on each item allow the user to edit/delete the product.

<br>

### Package/Product details

![Package/Product]()

This will display all data associated with a particular product. There will be buttons to allow the user to add the product to their shopping bag.
If the user has administrator privileges and is logged in then there will be addition links on each item allow the user to edit/delete the product.
If a user is logged in then they will be able to leave a product review/rating.

<br>

### Shopping Bag

![Shopping Bag]()

The shopping bag will display all items that that have been added by the user.
For each item it will show the unit price, quantity and total.
The user can change the quantity against each item and also remove it from their back if they no longer wish to purchase the product.
At the bottom of the page the basket total, delivery cost and order total will be displayed. 
A Keep Shopping and Checkout button will also be displayed at the bottom of the page.

<br>

### Checkout Page

![Checkout]()
The Checkout page will contain a brief summary of the order and a form for the delivery details.
If the user is logged in then the form will be populated with any address information the user has saved in their profile.
The form will be validated on submission and any errors/omissions will be reported back to the user.
The payment information system will be implemented by Stripe and it will allow the user to enter a card number, expiry date and CVC number.

 A test purchase can be made with the following details:
- credit card: 4242 4242 4242 4242
- expiration date: 04 / 24
- CVC: 424
- ZIP: 42424

Complete order will submit a payment and redirect to order confirmation page.
Also user can go back to the bag to adjust shopping bag.

<br>

### Profile Page

![Profile]()

Once a user is registered they will have access to their profile page. This allows the user to enter default delivery information, view previous orders and view/edit/delete any reviews they have written on the site.

<br>

### Product Management Page

![Product Management Page]()

Site administrators can use this page to add new products to the website and also edit existing products in the database.

<br>

---
## Features Left to Implement:
---

- Add a booking system so that customers can book treatments throuh a time table.
- Add blog/news site. 
- More styling, text and better pictures.

<br>

---
## Technologies Used:
---

### Languages 

- [HTML5](https://en.wikipedia.org/wiki/HTML) - For markup
- [CSS3](https://en.wikipedia.org/wiki/CSS) - For style
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - For interaction
- [Python3](https://www.python.org/) - As a backend programming language

### Framework & Libraries

- [Font Awesome](https://fontawesome.com/): provided all icons (social media icons etc.) used throughout the site.
- [Google Fonts](https://fonts.google.com/): provided the Lato font that is used throughout this website.
- [Bootstrap](https://getbootstrap.com/): a frontend framework for implementing responsive websites.
- [jQuery](https://jquery.com/): JavaScript library.
- [Django](https://www.djangoproject.com/): A Python based framework for developing secure and maintainable websites - the core of this project.
- [Amazon Web Services (AWS)](https://aws.amazon.com/): was used to host all static and media files using the [S3](https://aws.amazon.com/s3/) and [IAM](https://aws.amazon.com/iam/) services.
- [Stripe](https://stripe.com/gb): an API framework for processing secure payments.

### Database

- [Postgres](https://www.postgresql.org/) - Relational database, hosted and deployed via Heroku.

### Tools

- [Balsamiq](https://balsamiq.com/): was used to capture the initial wireframe models of the site.
- [GitPod](https://gitpod.io/): was used as the development environment.
- [GitHub](https://github.com/): was used to manage the configuration and control of the project.
- [Heroku](https://heroku.com): was used to deploy the project.
- [GMail](https://gmail.com): was used to provide the SMPT server allowing the app to send and receive emails.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/): a suite of tools used during the project development to debug problems and to test the website.
- [Am I Responsive](http://ami.responsivedesign.is/): was used to generate the website screen shots displayed at the top of this page.
- [Favicon](https://favicon.io/): was used to generate the favicon for the website.

<br>

---
## Testing:
---

See [testing.md](testing.md) for the testing documentation.

<br>

---
## Deployment
---

This project was developed using [GitPod](https://gitpod.io/) and the latest version of the code base can be found in the master branch of this
repository. No other branches were created during the development of this project.

### Cloning the Repository

To clone this [repository](https://github.com/Sndrahel/Happy_Feets.git) follow the instruction below:

1. Navigate to the [repository](https://github.com/Sndrahel/Happy_Feets.git).
2. Click on the **Code** button and copy the URL from the **Clone>>HTTPS** section.
3. Inside your development environment/IDE open a command terminal.
4. Create / navigate to the directory you would like the cloned copy to be made.
5. Type in the following command using the URL copied from step 2 and press Enter. This will create a cloned copy of the repository.
    * `git clone https://github.com/Sndrahel/Happy_Feets.git`

### Deploying to Heroku from Gitpod

1. Open [Heroku](https://heroku.com) in the browser and login creating a new account if required.
2. On the Heroku Dashboard click New->Create New App.
3. Give the app a new name and choose a region closest to you. Click the Create App button.
4. On the resource tab provision a new Postgres database selecting the free Hobby Dev plan.
5. To use Postgres in the application two packages are required - these are dj-database-url and psycopg2. To install these in Gitpod type the following commands:
    * `pip3 install dj_database_url`
    * `pip3 install psycopg2-binary`
6. Freeze the requirements in Gitpod by typing `pip3 freeze > requirements.txt`. Heroku will use the requirements.txt file to install these packages during deployment.
7. Open the settings.py file and import the dj_database_url package by adding `import dj_database_url` at the top of the file underneath `import os`.
8. In the database section comment out the default configuration and replace with the code below. The DATABASE_URL can be found under the settings tab in Heroku in the Config Vars section.

```
    DATABASES = {
        'default': dj_database_url.parse('DATABASE_URL')
    }
```
9. As a new database has been connected the migrations will need to run again to setup the database. Type in the following commands in Gitpod to run the migrations.
    * `python3 manage.py makemigrations`
    * `python3 manage.py migrate`
10. The database can be populated using the fixtures and JSON files. Run the following commands to load the data into the Postgres database:
    * `python3 manage.py loaddata genres`
    * `python3 manage.py loaddata artists`
    * `python3 manage.py loaddata record_labels`
    * `python3 manage.py loaddata products`
11. Create a superuser account for Django Administrator Panel using command `python3 manage.py createsuperuser`. When prompted enter a username, email address and password.
12. To ensure the database URL doesn't end up in version control replace the database configuration as setup in step 8 with the code below. When running on Heroku the DATABSE_URL will be defined in the Config Vars and the correct URL will be parsed by dj_database_url. Otherwise the sqlite database will be used when running in the Gitpod development environment.
```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
```
13. For the app to run the Gunicorn webserver package is required. To install this package run command `pip3 install gunicorn`.
14. Freeze the requirements by running command `pip3 freeze > requirements.txt`.
15. In the root directory of the project create a Procfile by running command `touch Procfile`. The Procfile is used to tell Heroku to create a web dyno to run gunicorn and serve our Django app.
16. Open the Procfile copy in the following text ensuring there is no blank line at the end of the file.
```
    web: gunicorn happy_feets.wsgi
```
17. Login to Heroku using the `heroku login -i` command.
18. As AWS will be used to host the static files we need to prevent Heroku from collecting static files during deployment. This can be done by setting DISABLE_COLLECTSTATIC to 1. Enter the following command to set DISABLE_COLLECTSTATIC:
    * `heroku config:set DISABLE_COLLECTSTATIC=1 --app app-name`
19. In the settings.py file add the Heroku app the list of allowed hosts. Also add in localhost to ensure the app still works in Gitpod.
    * `ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']`
20. Edit the .gitignore file (or create a new one if it doesn't exist) and add the following if required:
```
    core.Microsoft*
    core.mongo*
    core.python*
    env.py
    __pycache__/
    *.py[cod]
    node_modules/
    .github/
    *.sqlite3
    *.pyc
```
21. Commit the changes to the main Github repository using the following commands:
    * `git add .`
    * `git commit -m "Add commit message here"`
    * `git push`
22. Initialise the Heroku repository using command `heroku git:remote -a app-name`.
23. To deploy the app to Heroku push the changes to the remove Heroku repository using command `git push heroku main`. This will deploy the site without any static files.
24. To automatically deploy when any changes are committed to Github click in the Deploy tab in Heroku and set the Deployment method to Github.
25. In the Connect to GitHub section search for the repository and click connect when the correct one is found.
26. In the Automatic Deploys section click on the Automatic Deplots button. This ensures that every time we push any changes to Github the code will be automatically be deployed to heroku as well.
27. Create a new Django secret key using the [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) website.
28. In Heroku under the Settings tab create a new Config Var with a key name of SECRET_KEY with the value set to the key generated in the previous step.
29. To ensure the Heroku app picks up this key add the following to the settings.py file:
    * `SECRET_KEY = os.environ.get('SECRET_KEY', '')`
30. Commit the changes to Github. Heroku should pickup the changes from Github and deploy the site to app-name.herokuapp.com.


### AWS S3 Configuration

The AWS S3 service will be used to host all static files and images.

1. Open [AWS](https://aws.amazon.com) in the browser and login creating a new account if required.
2. Open the AWS Management Console and search for the S3 service using the search box if it isn't listed in your recently accessed services.
3. Click 'Create New Bucket' to create a new bucket. It is recommended to give the bucket the same name as your Heroku app.
4. Select the region closet to you.
5. Uncheck 'Block all public access' and using the tick box below to acknowledge that the bucket will be public. Click 'Create bucket'.
6. Select your bucket from the bucket list. In the properties tab turn on static website hosting and set the following default values then click save.
    * Index document: `index.html`
    * Error document: `error.html`
7. In the Permissions tab paste in the following CORS configuration then click save.
```
    [
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
    ]
```
8. In the Permissions tab go to the Bucket policy section and click the Edit button. Click the Policy Generator button to create a new security policy. Select/enter the following:
    * Policy Type: S3 Bucket Policy
    * Principal: *
    * Actions: GetObject
    * ARN: Copy the ARN from the Bucket Policy tab and paste here.
    * Click Add Statement then Generate Policy.
    * Copy the new policy and paste into the Bucket Policy editor.
    * To allow access to all resources add a "/*" onto the end of the Resource key value.
    * Save the new policy.
9. In the Permissions tab go to the Access Control section and click the Edit button. On the "Everyone (public access)" line check the List checkbox and click Save changes.
10. Go back to the services and select Identity and Access Management (IAM) to add a new user. Use the search bar if IAM isn't listed. IAM will be used to create new group, create an access policy giving the group access to the S3 bucket and to assign a user to the group so they can use the policy to access the files in the S3 bucket.
11. Under User Groups click the Create Group button. Enter a group name then scroll to the bottom and click Create group.
12. Under Policies click the Create Policy button. Follow the steps below:
    * Go to the JSON tab and select Import managed policy.
    * Search for the `AmazonS3FullAccess` policy and Import this.
    * From the S3 Bucket Policy page copy the ARN and paste this twice into the Resource key as shown below:
    ```
        "Resource": [
            "arn:aws:s3:::s3-bucket-name",
            "arn:aws:s3:::s3--bucket-name/*"
        ]
    ```
13. Click the Review Policy button giving the policy a name and description. Click the Create Policy button to save all changes.
14. Under User Groups select the group that was created above. On the Permissions tab select Attach Policies from the Add permissions dropdown menu. Search for the policy that was created above, select it and click the Add permissions button.
15. Under Users click the Add Users button and give the user a name. Check the Access Key - Programmatic access option and click next. On the next page add the user to the new group that was created above. Click through to the end then click Create User.
16. Download the CSV file - this contains the user access key and secret access key which will be used by the Django app for authentication. Save the file in a secure location as this cannot be downloaded again once the user has been created.
17. To connect Django to the new S3 Bucket two new packages are required: boto3 and django-storages. In Gitpod type the following commands to install the packages:
    * `pip3 install boto3`
    * `pip3 install django-storages`
18. Freeze the requirements by running command `pip3 freeze > requirements.txt`.
19. In the settings.py file add 'storages' to the INSTALLED_APPS list.
20. Add the following configuration to the settings.py file. As the S3 Bucket is only required when using Heroku an if statement is used to check if the variable USE_AWS exists. 
```
    if 'USE_AWS' in os.environ:
        # Bucket Config
        AWS_STORAGE_BUCKET_NAME = 'bucket-name'
        AWS_S3_REGION_NAME = 'eu-north-1'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
```
21. In Heroku at the following Config Vars to the app. The AWS keys can be found in the csv file that was downloaded when creating the S3 user. The DISABLE_COLLECTSTATIC can also be removed as Heroku will get the static files from AWS for any future deploys.
    * `AWS_ACCESS_KEY_ID : From the csv file`
    * `AWS_SECRET_ACCESS_KEY : From the csv file`
    * `USE_AWS : True`
    * Remove variable `DISABLE_COLLECTSTATIC`
22. In the settings.py file add the following inside the USE_AWS if statement to tell Django where the static files will be sourced from in production.
    * `AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'`
23. The next step is to configure Django to use S3 to store our static files whenever someone runs `collectstatic` and to also store any uploaded images in the S3 bucket.
24. In the root folder create a file by running `touch custom_storages.py`.
25. Copy the following configuration into the file and save:
```
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage


    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
```
26. In the settings.py file add the following inside the USE_AWS if statement to configure Django to use our custom storage class for static file storage and to override the static and media URLs in production.
```
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
27. In the settings.py add the following lines to the top of the USE_AWS if statement. These will configure the browser to cache static files for a long time as they don't change often.
```
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
```
28. At this point all the changes can be committed to Github triggering Heroku to deploy the app. Confirm all the static files have been uploaded to the S3 bucket.
29. To add the media files to the S3 bucket go to AWS S3, select the bucket and click on Create folder. Create a folder called media.
30. Inside the media folder click Upload to upload all the media files to the S3 bucket. Under Permissions set the Predefined ACL to Grant public-read access.
31. The superuser email address for the Postgres database needs to be confirmed to allow the user to login to the application. To do this login to the Django admin panel and confirm the email address for the superuser by checking the Verified box.


### Stripe Configuration
1. Login to Stripe and in the Developers section click on API Keys. In Heroku add the publishable and secret keys as the following config variables.
    * `STRIPE_PUBLIC_KEY`
    * `STRIPE_SECRET_KEY`
2. Click on the Webhooks link in the Developers section. Click on Add Endpoint configure as follows:
    * `EndPoint URL: https://app-name.herokuapp.com/checkout/wh/`
    * Click receive all events in the Events to send section and click Add Endpoint.
3. On the webhook screen reveal the Signing Secret and copy this into Heroku as a config variable named `STRIPE_WH_SECRET`.
4. To confirm the webhook is working send a test webhook from Stripe to ensure the listener is working.


### Email Configuration
The following process assumes that GMail will be used for sending and receiving emails.
1. Open [GMail](https://gmail.com) in the browser and login creating a new account if required.
2. Open the account settings, select Accounts and Import and then other Google account settings.
3. Click on the Security tab and turn on 2-Step Verification under Signing in to Google.
4. Click Get Started and enter your Gmail password and then follow the 2-Step Verification as instructed.
5. Once the 2-Step Verification has completed go back to the Security tab and select App passwords under Signing in to Google.
6. On the App passwords screen select Mail for the app and other for the device giving it the name Django. Click Generate to complete.
7. Copy the password and create a new config variable in Heroku called `EMAIL_HOST_PASS` pasting in the password as the value.
8. Also create another config variable in Heroku called `EMAIL_HOST_USER` and set this to the Gmail account.
9. In settings.py add the following:
```
    if 'DEVELOPMENT' in os.environ:
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        DEFAULT_FROM_EMAIL = 'app-name@example.com'
        EMAIL_SUBJECT_PREFIX = '[App-Name]'
    else:
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_USE_TLS = True
        EMAIL_PORT = 587
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
        EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
        DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
        EMAIL_SUBJECT_PREFIX = '[App-Name]'
```
10. Confirm the email is functioning correctly by registering a new user and checking that the email confimration is received.

<br>

---
## Credits
---

### Code:
- [Code Institute](https://codeinstitute.net/) - The majority of the code for this project comes from Code Institute Boutiqe Ado tutorial.
- [Youtube](https://www.youtube.com/watch?v=Y5vvGQyHtpM) - Tutorial used for adding rating and reviews to shop products.  
- [Stack Overflow](https://stackoverflow.com/) - Was used to find solutions and debugging.
- [GitHub](https://github.com/SteinOveHelset/saulgadgets/tree/master/apps/store) - Code for adding rating and reviews to shop products.
- [GitHub](https://aqua-nightingale-u38ms1hh.ws-eu17.gitpod.io/) - Inspiration of structure for this README file were adapted from this site. 
- [GitHub](https://github.com/johnvenkiah/CI_PP5_John_Venkiah) - Inspiration and code for reviews were adapted from this site. 
- [GitHub](https://github.com/ZahraSadiq/Milestone4-PosterBay) - Inspiration of style and layout were adapted from this site.

<br> 

### Acknowledgments:

- Nishant Kumar: My Code Institute mentor who guided me through this process and shared a lot of valuable knowledge.


[Back to Table of contents](#table-of-contents)
