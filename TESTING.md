## Manual Testing

In this testing process, you will be evaluating the functionality of project on both desktop and mobile platforms. Your thorough examination is crucial in ensuring that the application meets the highest standards of quality and performance.

The focus during manual testing should encompass all aspects of the application's functionality, including but not limited to:

Desktop Testing: Validate the application's behavior on various desktop browsers (e.g., Chrome, Firefox, Safari) to ensure a seamless experience for users accessing the platform from desktop devices.

Mobile Testing: Assess the application's responsiveness and functionality on mobile devices (e.g., smartphones, tablets) across different browsers and screen sizes.

If a test case passes, please flag it as "Pass" in your testing documentation. If any issues or anomalies are discovered, provide detailed information on the problem, including steps to reproduce, expected behavior, and actual observed behavior.

### User Navigation Tests

#### Navbar Presence Test

- Objective: Ensure the navigation bar is present and visible on the webpage.

| Test |Result  |
|--|--|
|Load the webpage containing the navigation bar. | Pass |
|Verify that the navigation bar is visible at the top of the page.| Pass|
|Cook with me" logo is present, correctly positioned, and functions as a navigation link back to the home page.|Pass|
|Check that the navigation links (Home, Recipes, Register/Login/Logout) are displayed.|Pass|

#### Navbar Toggle Test (Mobile Responsiveness)

- Objective: Verify the functionality of the navbar toggle button on smaller screens.

| Test |Result  |
|--|--|
|Access the webpage from a device with a small screen (e.g., smartphone or tablet). | Pass |
|Click on the navbar toggle button (hamburger icon).| Pass|
|Confirm that the navigation menu expands, displaying all navigation links.|Pass|
|Click the toggle button again to collapse the navigation menu.|Pass|

#### Social Media Links Test

- Objective: Confirm that the social media links in the footer direct users to the correct external pages.

| Test |Result  |
|--|--|
|Load the webpage containing the footer. | Pass |
|Identify the social media links for Facebook, YouTube, Google, and Instagram.| Pass|
|Click on each social media link.|Pass|
|Verify that each link opens the corresponding social media page in a new tab.|Pass|

#### Accessibility and Styling Test

- Objective: Validate the accessibility and styling of the footer. 

| Test |Result  |
|--|--|
|Load the webpage and navigate to the footer.|Pass|
|Verify that the social media icons are recognizable and visually appealing.|Pass|
|Inspect the footer's responsiveness on different screen sizes.|Pass|
|Confirm that the footer remains at the bottom of the page and does not overlap with other content.|Pass|

#### Image Display Test

- Objective: Confirm that the images in the webpage are displayed correctly, with proper loading and rendering.

| Test |Result  |
|--|--|
|Load the webpage where images are expected to be displayed.|Pass|
|Inspect different sections of the webpage containing images.|Pass|
|Test the behavior on different devices and screen sizes to ensure responsive image display.|Pass|

### Recipes

- Objective: Ensure the correct rendering and functionality of the recipes page template.

| Test |Result  |
|--|--|
|Verify that the page loads without any errors.|Pass|
|Check that the page displays a heading with the text "Recipes."|Pass|
|Resize the browser window to check the responsiveness of the grid layout.|Pass|
|Verify that the number of columns adjusts appropriately based on the screen size.|Pass|


#### Individual Recipe Cards

| Test                                                                                            | Result  |
|-------------------------------------------------------------------------------------------------|--------|
|Ensure there is a card structure with a featured image and a title.|Pass|
|Verify that the title is a clickable link that directs the user to the corresponding recipe content page (recipe_content view).|Pass|

#### Like Functionality

| Test                                                                                            | Result |
|-------------------------------------------------------------------------------------------------|--------|
| Check that each recipe card displays a heart icon representing the "like" functionality.        | Pass   |
| Verify that the heart icon changes based on whether the logged-in user has liked <br> the recipe: If the user has liked the recipe, the heart should be solid. If the user has not liked the recipe,<br> the heart should be regular. | Pass   |
| Check that each recipe card displays the correct count of likes.                                | Pass   |

## Recipe content

#### Image and Content Rendering

- Objective: Ensure the recipe image, title, ingredients, and method are correctly displayed on the Recipe Detail Page.

| Test                                                                                             | Result |
|--------------------------------------------------------------------------------------------------|--------|
| Open the web page displaying a recipe.                                                           | Pass   |
| Confirm that the recipe image is visible and correctly associated with the recipe title.         | Pass   |
| Verify that the ingredients and method sections are rendered accurately.                         | Pass   |

#### Comments Section

- Objective: Ensure comments are properly displayed with user information

| Test                                                                                             | Result |
|--------------------------------------------------------------------------------------------------|--------|
| Check if comments are visible on the page.                                                       | Pass   |
| Ensure there is a card structure with a featured image and a title.                              | Pass   |
| Verify that each comment includes the user's name, creation date, and comment body.              | Pass   |
| Confirm pagination works correctly if there are multiple comments.                               | Pass   |

#### Authenticated User Actions

- Objective: Validate actions for authenticated users in the Comments Section.

| Test                                                                                             | Result |
|--------------------------------------------------------------------------------------------------|--------|
| Log in with a user account.                                                                      | Pass   |
| Confirm the visibility of the "Add a Comment" section.                                           | Pass   |
| Submit a comment using the form.                                                                 | Pass   |
| Verify that the submitted comment appears in the comments section.                               | Pass   |

#### Anonymous User Actions

- Objective: Evaluate actions for anonymous users in the Comments Section.

| Test                                                                                             | Result |
|--------------------------------------------------------------------------------------------------|--------|
| Log out or open the page in an incognito/private browsing window.                                | Pass   |
| Verify that the "Add a Comment" section is not visible.                                          | Pass   |
| Verify that the system restricts the comment submission.                                         | Pass   |

#### CRUD 

- Objective: Validate CRUD Operations for User Comments
- Precondition: Log in with a user account that has access to the recipe detail page.

#### Create Comment

- Objective: Ensure users can create a new comment.

| Test                                                                                             | Result |
|--------------------------------------------------------------------------------------------------|--------|
| Open the web page displaying a recipe.                                                           | Pass   |
| Locate the "Add a Comment" section.                                                              | Pass   |
| Fill in the comment form with relevant information.                                              | Pass   |
| Click the "Publish" button.                                                                      | Pass   |
| Verify that the new comment appears in the comments section.                                     | Pass   |
| Confirm that the user's name, creation date, and comment body are correctly displayed.           | Pass   |

#### Read Comment

- Objective: Confirm the display of existing comments.

| Test                                                                                              | Result |
|-------------------------------------------------------------------------------------------------- |--------|
| Confirm that existing comments are visible, showing user names, creation dates, and comment bodies.| Pass  |
| Ensure that pagination works correctly if there are multiple comments.                            | Pass   |

#### Update Comment

- Objective: Ensure users can edit their own comments.

| Test                                                                                             | Result |
|--------------------------------------------------------------------------------------------------|--------|
| Click the "Edit" button.                                                                         | Pass   |
| Modify the comment text.                                                                         | Pass   |
| Click the "Update Comment" button.                                                               | Pass   |
| Verify that the edited comment appears in the comments section.                                  | Pass   |
| Confirm that the changes to the user's name, creation date, and comment body are reflected.      | Pass   |

#### Delete Comment

| Test                                                                                              | Result |
|-------------------------------------------------------------------------------------------------- |--------|
| Click the "Delete" button.                                                                        | Pass   |
| Confirm the deletion.                                                                             | Pass   |
| Verify that the comment is no longer visible in the comments section.                             | Pass   |

## Authentication

- Objective: Validate User Registration, Login, and Logout Functionality

#### User Registration

- Objective: Verify that users can successfully register with valid information.

| Test                                                                                             | Result |
|--------------------------------------------------------------------------------------------------|--------|
| Enter a unique username, an optional email, and a valid password.                                | Pass   |
| Click the "Sign Up" button.                                                                      | Pass   |
| Confirm redirection to the products page.                                                        | Pass   |
| Verify that the user can access content on the redirected page                                   | Pass   |

#### User Login

- Objective: Verify that users can successfully log in with correct credentials.

| Test                                                                                             | Result |
|--------------------------------------------------------------------------------------------------|--------|
| Enter the username used during registration and the corresponding password.                      | Pass   |
| Click the Sign In button.                                                                        | Pass   |
| Confirm redirection to the products page.                                                        | Pass   |
| Verify that the user can access content on the redirected page.                                  | Pass   |

#### User Logout

- Objective: Verify that users can successfully log out.

| Test                                                                                             | Result |
|--------------------------------------------------------------------------------------------------|--------|
| Locate and click the "Sign Out" link in the navbar.                                              | Pass   |
| On the Sign Out page, click the "Sign Out" button.                                               | Pass   |
| Confirm that the user is logged out.                                                             | Pass   |
| Verify redirection to the Home Page.                                                             | Pass   |


## Admim

| Test                                                                                             | Result |
|--------------------------------------------------------------------------------------------------|--------|
| Confirm that admin can post new recipes.                                                         | Pass   |
| Verify that admin can edit existing recipes.                                                     | Pass   |
| Confirm that admin can remove recipes.                                                           | Pass   |
| Confirm that administrators can approve comments.                                                | Pass   |
| Verify that administrators can delete comments.                                                  | Pass   |
| Confirm that administrators can delete user accounts.                                            | Pass   |

## Validate Responsiveness

#### Notes

- Document any instances where the layout or functionality breaks on different devices.
- Ensure that font sizes and images are appropriately scaled for different screens.
- Check for adherence to web accessibility standards, ensuring users with disabilities have a smooth experience.

| Test                                                                                             | Result |
|--------------------------------------------------------------------------------------------------|--------|
| Confirm that the home page is visually appealing on a desktop.                                   | Pass   |
| Validate the responsiveness on tablet devices.                                                   | Pass   |
| Ensure a user-friendly experience on mobile devices.                                             | Pass   |


## Browsers Compatibility

The website has undergone comprehensive testing across popular desktop browsers, including Google Chrome, Safari, Mozilla Firefox, Opera, and Microsoft Edge. Based on the testing results, no significant compatibility issues were identified, and the website functions as expected across these browsers.

# Unit Testing

## Overview

This document provides an overview of the unit tests implemented for various components in the Django project. The unit tests cover the admin, form, model, and views, ensuring robustness and reliability of the application.

## Test Statistics

- Total Tests: 27
- Test Coverage: 92%

## Test Results

### 1. Admin Tests

- [x] All admin tests pass successfully.
- [x] Admin panel customization functions as expected.

### 2. Form Tests

- [x] All form tests pass successfully.
- [x] Proper validation and submission handling are confirmed.

### 3. Model Tests

- [x] All model tests pass successfully.
- [x] Database integrity is maintained, and model methods work as intended.

### 4. Views Tests

- [x] All views tests pass successfully.
- [x] User authentication, form submissions, and template rendering are all validated.

## Test Coverage Analysis

The unit tests collectively provide a test coverage of 92%, ensuring that almost all aspects of the application are thoroughly tested.

<details>
<summary><strong>Unit Test</strong></summary>

![Unit test](/static/images/readme/unit-test.png)

</details>

## Validator test

I utilized the [W3C HTML Validator](https://validator.w3.org/)  Validator to thoroughly test all HTML code.

#### Home
- No errors were identified during testing.
<details>
<summary><strong>Home</strong></summary>

![home-validator](/static/images/readme/html-validator.jpg)

</details>

#### Recipes
- No errors were identified during testing.
<details>
<summary><strong>Recipes</strong></summary>

![recipes-validator](/static/images/readme/recipes-validator.jpg)

</details>

#### Recipe content

- CSS Property Error (font-optical-sizing): The 'font-optical-sizing' property was flagged as not being recognized or nonexistent. 
- Unicode Normalization Warning: A warning was raised about a text run not being in Unicode Normalization Form C.
- Obsolete Element Warning (Summernote)

These errors and warnings, while noted, do not compromise the overall performance or user experience of the application and have been intentionally excluded from further consideration.

<details>

![recipes-validator](/static/images/readme/recipes-content-error1.jpg)
![recipes-validator](/static/images/readme/recipe-content-error2.jpg)
![recipes-validator](/static/images/readme/recipe-content-erro3.jpg)
</details>
  
#### Register and Login

- As a result of these validations and corrections, the HTML code has been reviewed and confirmed to be in compliance with standards, and all identified errors have been resolved.

<details>

![login-validator](/static/images/readme/login-html-validator.jpg)
![signup-validator](/static/images/readme/signup-html-validator.jpg)

</details>

#### Logout

- No errors were identified during testing.

<details>

![logout-validator](/static/images/readme/logout-validator.jpg)

</details>

I utilized the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)  Validator to thoroughly test all CSS code.

<details>

![css-validator](/static/images/readme/css-validator.jpg)

</details>

## PEP8

All Python files within the 'cook_recipe' and 'cook_with_me' apps have undergone scrutiny using the Code Institute PEP8 Linter. Attached are images showcasing the identified errors and the subsequent resolution after addressing them.


<details>
<summary><strong>Admin</strong></summary>

![admin](/static/images/readme/admin-pep8-error.jpg)
![admin](/static/images/readme/admin-pep8.jpg)

</details>

<details>
<summary><strong>Forms</strong></summary>

![forms](/static/images/readme/forms-pep8-error.jpg)
![forms](/static/images/readme/forms-pep8.jpg)

</details>

<details>
<summary><strong>Model</strong></summary>

![Model](/static/images/readme/model-pep8-errors.jpg)
![Model](/static/images/readme/model-pep8.jpg)

</details>

<details>
<summary><strong>Urls</strong></summary>

![Urls](/static/images/readme/urls-pep8-error.jpg)
![Ulrs](/static/images/readme/urls-pep8.jpg)

</details>

<details>
<summary><strong>Views</strong></summary>

![Views](/static/images/readme/views-pep8-error.jpg)
![Views](/static/images/readme/views-pep8.jpg)

</details>

<details>
<summary><strong>Admin Test</strong></summary>

![admin test](/static/images/readme/admin-test-error.jpg)
![admin test](/static/images/readme/admin-test.jpg)

</details>

<details>
<summary><strong>Forms Test</strong></summary>

![forms test](/static/images/readme/forms-test-error.jpg)
![forms test](/static/images/readme/forms-test.jpg)

</details>

<details>
<summary><strong>Model</strong></summary>

![Model test](/static/images/readme/model-test-error.jpg)
![Model test](/static/images/readme/model-test.jpg)

</details>

<details>
<summary><strong>Views test</strong></summary>

![Views](/static/images/readme/views-test-error.jpg)
![Views](/static/images/readme/views-test.jpg)

</details>

## Accessibility

- Lighthouse was utilized to generate extensive reports on both performance and accessibility for the desktop and mobile versions of the site. The image below showcases the results for the Home page on desktop and mobile, respectively. Furthermore, sitewide results are detailed in the accompanying table.
All pages have successfully achieved a flawless accessibility score of 100.

- Bugs Fixed:
- Corrected the order of headings.
- Added descriptive messages for links.

### Lighthouse

<details>
<summary><strong>Home desktop</strong></summary>

![home-desktop](/static/images/readme/home-desktop-lighthouse.jpg)

</details>

<details>
<summary><strong>Home mobile</strong></summary>

![home-mobile](/static/images/readme/home-mobile-lighthouse.jpg)

</details>

<details>
<summary><strong>Recipes desktop</strong></summary>

![recipes-desktop](/static/images/readme/recipes-desktop-lighthouse.jpg)

</details>

<details>
<summary><strong>Recipes mobile</strong></summary>

![recipes-mobile](/static/images/readme/recipes-mobile-lighthouse.jpg)

</details>

#### Recipes content

- All recipe content has undergone thorough testing, achieving a perfect accessibility score of 100 according to Lighthouse testing.

<details>
<summary><strong>Recipes content desktop</strong></summary>

![recipes-content](/static/images/readme/recipes-content-desktop-lighthouse.jpg)

</details>
<details>
<summary><strong>Recipes content mobile</strong></summary>

![recipes-content](/static/images/readme/recipes-content-mobile-lighthouse.jpg)

</details>

<details>
<summary><strong>Sign up desktop</strong></summary>

![Sign up](/static/images/readme/signup-desktop-lighthouse.jpg)

</details>

<details>
<summary><strong>Sign up mobile</strong></summary>

![Sign up](/static/images/readme/signup-mobile-lighthouse.jpg)

</details>

<details>
<summary><strong>Login desktop</strong></summary>

![Login](/static/images/readme/login-desktop-lighthouse.jpg)

</details>
<details>
<summary><strong>Login mobile</strong></summary>

![Login](/static/images/readme/login-mobile-lighthouse.jpg)

</details>

<details>
<summary><strong>Signout desktop</strong></summary>

![Signout](/static/images/readme/signout-desktop-lighthouse.jpg)

</details>

<details>
<summary><strong>Signout mobile </strong></summary>

![Signout](/static/images/readme/signout-mobile-lighthouse.jpg)

</details>

## Wave

The WAVE web accessibility tool was employed to assess the accessibility of a web application, and it identified a total of 4 errors and 6 structural elements. These results are crucial for ensuring that the web content is inclusive and can be accessed by users with diverse abilities.

Errors (4):
The tool flagged 4 instances of "Empty Link" errors. Empty links can pose accessibility challenges, as users relying on screen readers or other assistive technologies may not receive meaningful information about the purpose or destination of the link. Addressing these errors is essential for providing a seamless and comprehensible experience for all users.

Structural Elements (6):
The evaluation also revealed the presence of 6 essential structural elements. These elements play a fundamental role in organizing and presenting content in a well-structured manner, contributing to a more accessible user experience. The structural elements identified include:

- Heading Level
- Unordered List
- Header
- Navigation
- Footer

Each of these elements serves a specific purpose in web page design, aiding in navigation, content hierarchy, and overall user comprehension.

Resolution
All identified errors and structural issues have been successfully addressed. The corrective actions taken ensure that the web application aligns with accessibility standards, providing an inclusive and user-friendly experience for individuals with diverse needs.

## Bugs

### Heroku Deployment 

#### Problem
During the deployment process on the Heroku platform, an issue surfaced and prompted a comprehensive investigation. Upon thorough analysis, it was identified that the python-apt==2.4.0+ubuntu1 package was causing complications in the deployment pipeline.

#### Problem Details
The presence of python-apt==2.4.0+ubuntu1 in the requirements.txt file was discovered to be irrelevant to the core functionality of the project. Despite its lack of relevance, its inclusion in the list of dependencies was leading to deployment challenges on Heroku, impeding the successful launch of the application.

#### Solution
To address this deployment issue and ensure a seamless deployment process on Heroku, the decision was made to eliminate the python-apt==2.4.0+ubuntu1 line from the requirements.txt file.

#### Implementation
The necessary modification has been applied to the requirements.txt file, removing the reference to python-apt==2.4.0+ubuntu1. This adjustment aims to streamline the deployment experience on Heroku and mitigate any challenges associated with the unnecessary package.

#### Result
By proactively removing the extraneous dependency python-apt==2.4.0+ubuntu1, I have successfully resolved the deployment issues, paving the way for smooth and successful deployments on Heroku. This update not only addresses the specific problem at hand but also contributes to the overall efficiency and reliability of the project, particularly during the testing and deployment phases.

### Issue: Images Not Displaying After Heroku Deployment
- Upon deploying the application on Heroku, images within forms failed to appear. The console reported the following error:

<strong>register.fdb3b090e8a2.jpeg:1
Failed to load resource: the server responded with a status of 404.</strong>

#### Resolution
- With the assistance of mentor Narender Singh, we identified and implemented the following solution:

#### CSS Adjustment
- The background image was removed from the style.css file to eliminate potential conflicts or loading issues.

#### HTML Modification
- Image tags (<img>) were added to the signup.html, signin.html, and signout.html files to explicitly include the images in the respective forms.

#### Result
- After these modifications, the images displayed properly on the web pages, resolving the issue encountered post-deployment.


## Conclusion

The extensive testing process, which encompassed manual testing, unit testing, validation, and accessibility checks, underlines my commitment to delivering a high-quality, accessible, and user-friendly web application. The resolution of identified issues ensures a smooth and reliable user experience across diverse devices and user scenarios. As a result, the application is well-prepared for deployment and use. My focus on quality assurance guarantees that users will encounter a seamless and enjoyable experience, reinforcing the reliability and inclusivity of the web application.