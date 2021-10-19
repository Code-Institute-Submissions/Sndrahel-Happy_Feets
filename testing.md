## Testing

### Table of Contents

- [Test Strategy](#teststrategy)

- [Responsive Testing](#responsivetesting)

- [Functional/Features Testing](#functionaltesting)

- [Code Validation](#codevalidation)

- [Bugs / Issues](#bugsissues)


## Test Strategy

To test responsiveness of the site [Chrome DevTools](https://developer.chrome.com/docs/devtools/) will be used. This ensures the site is usable on a variety of different devices and screen sizes.

To ensure the site is fit for purpose all user stories and features documented in the main README.md file are to be tested. The test procedures
and results are documented below.

The code (HTML/CSS/JS/Python) must also satisfy the requirements of the online validation tools. These are:
* [W3C Markup Validation Service](https://validator.w3.org/). Check the markup of web documents.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/). Check Cascading Style Sheets
* [JS Hint](https://jshint.com/). Javascript code quality tool. 
* [PEP8 Online](http://pep8online.com/). Checks Python code for PEP8 compliance.

Google Lighthouse will be used to check the Performance, Accessibility, Best Practices and Search Engine Optimisation of the website.


## Responsive Testing

### Mobile & Tablet
The responsiveness of the site was tested using the Device Mode in [Chrome DevTools](https://developer.chrome.com/docs/devtools/). For mobile devices the minimum screen width the site was tested at was 320 pixels (iPhone SE). The following mobile and tablet options were tested in [Chrome DevTools](https://developer.chrome.com/docs/devtools/):

* iPhone 5/SE, iPhone 6/7/8, iPhone 6/7/8 Plus, iPhone X, iPad, iPad Pro, 


### Desktop
The responsiveness of the site on desktop devices was tested using Chrome browser. The site was tested using the following screen widths:

* 1024 pixels, 1280 pixels, 1440 pixels, 1600 pixels and 1920 pixels.

The site was consistently responsive across all devices and screen sizes with the layout responding as expected.


## Functional/Features Testing

### Test-001 : Navigation Bar
Test navigation bar links function correctly and that the correct links are displayed for admin and non admin users.

1. Open Chrome browser and navigate to: https://happy-feetss.herokuapp.com/ Logout of the site if logged in.
2. Check that the nav bar is fixed to the top of the browser window when scrolling down.
3. With the user logged out check that the following menu options appear in the My Account drop down menu:
    * Register & Login
4. Click each of the menu options listed above and confirm that you are taken to the correct page.
5. Click each of the menu options listed above and confirm that you are taken to the correct page. Clicking the Logout option should log you out of the website.
6. Login in using an administrator account and check that the following options appear in the nav bar:
    * Product Management, My Profile, My Wishlist, My Reviews & Logout
7. Click each of the menu options listed above and confirm that you are taken to the correct page. Clicking the Logout option should log you out of the website.
8. Confirm that all the navigation links under the menu drop down menu function correctly. On mobile devices these will collapse into a hamburger icon.
9. Confirm that the New In and On Sale links function correctly. On mobile devices these will collapse into a hamburger icon.
10. On mobile devices confirm that the Search, My Account and Shopping Bag icons are rendered at the top of the screen and function correctly.

#### Test Notes
All the navigation links function correctly for all users and link to the correct pages. For screen sizes <=992 pixels the correct navigation links
collapse into the hamburger menu and function correctly. The nav bar also remains fixed to the top of the page on both desktop and mobile devices. 
    
Tests performed using  Chrome desktop browser.

#### Test Results


### Test-002 : Footer
Test footer links function correctly and that it scrolls with the page contents.

1. Open Chrome browser and navigate to: https://happy-feetss.herokuapp.com/.
2. Check that the footer remains at the bottom of the screen even when very little content is present.
4. Click on the Contact Us link and conform that the Contact Us page is loaded.
5. Click on each social media link and verify it opens up the correct page in a new browser tab.


#### Test Notes
The footer is located at the bottom of the screen when little content is present and scrolls down when more content is added or when viewing a page with lots of content. The Contact Us option links to the correct page and all social media links are working and link to the correct pages, opening in a new tab.

Tests performed using  Chrome desktop browser.


#### Test Results


