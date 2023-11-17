
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
|Load the webpage containing the navigation bar | Pass |
|Verify that the navigation bar is visible at the top of the page.| Pass|
|Cook with me" logo is present, correctly positioned, and functions as a navigation <br> link back to the home page|Pass|
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
|Identify the social media links for Facebook, YouTube, Google, and Instagram.    | Pass|
|Click on each social media link.|Pass|
|Verify that each link opens the corresponding social media page in a new tab.     |Pass|

#### Accessibility and Styling Test

- Objective: Validate the accessibility and styling of the footer. 

| Test |Result  |
|--|--|
|Load the webpage and navigate to the footer.|Pass|
|Verify that the social media icons are recognizable and visually appealing.|Pass|
|Inspect the footer's responsiveness on different screen sizes.|Pass|
|Confirm that the footer remains at the bottom of the page and does not overlap <br> with other content.|Pass|

#### Image Display Test

- Objective: Confirm that the images in the webpage are displayed correctly, with proper loading and rendering.

| Test |Result  |
|--|--|
|Load the webpage where images are expected to be displayed.|Pass|
|Inspect different sections of the webpage containing images.|Pass|
|Test the behavior on different devices and screen sizes to ensure responsive <br> image display.|Pass|

### Recipes

- Objective: Ensure the correct rendering and functionality of the recipes page template.

| Test |Result  |
|--|--|
|Verify that the page loads without any errors.|Pass|
|Check that the page displays a heading with the text "Recipes."|Pass|
|Resize the browser window to check the responsiveness of the grid layout.|Pass|
|Verify that the number of columns adjusts appropriately based on the screen size.|Pass|


#### Individual Recipe Cards

| Test                                                                                             | Status |
|--------------------------------------------------------------------------------------------------|--------|
| Ensure there is a card structure with a featured image and a title.                              | Pass   |
| Verify that the title is a clickable link that directs the user to the corresponding <br> recipe content page (recipe_content view).| Pass   |
                                            
#### Like Functionality

| Test                                                                                            | Status |
|-------------------------------------------------------------------------------------------------|--------|
| Check that each recipe card displays a heart icon representing the "like" functionality.        | Pass   |
| Verify that the heart icon changes based on whether the logged-in user has liked <br> the recipe: If the user has liked the recipe, the heart should be solid. If the user has not liked the recipe,<br> the heart should be regular. | Pass   |
| Check that each recipe card displays the correct count of likes.                                | Pass   |

## Recipe content

#### Image and Content Rendering

- Objective: Ensure the recipe image, title, ingredients, and method are correctly displayed on the Recipe Detail Page.

| Test                                                                                             | Status |
|--------------------------------------------------------------------------------------------------|--------|
| Open the web page displaying a recipe.                                                           | Pass   |
| Confirm that the recipe image is visible and correctly associated with the recipe title.         | Pass   |
| Verify that the ingredients and method sections are rendered accurately.                         | Pass   |

#### Comments Section

- Objective: Ensure comments are properly displayed with user information

| Test                                                                                             | Status |
|--------------------------------------------------------------------------------------------------|--------|
| Check if comments are visible on the page.                                                       | Pass   |
| Ensure there is a card structure with a featured image and a title.                              | Pass   |
| Verify that each comment includes the user's name, creation date, and comment body.              | Pass   |
| Confirm pagination works correctly if there are multiple comments.                               | Pass   |

#### Authenticated User Actions

- Objective: Validate actions for authenticated users in the Comments Section.

| Test                                                                                             | Status |
|--------------------------------------------------------------------------------------------------|--------|
| Ensure there is a card structure with a featured image and a title.                              | Pass   |
| Ensure there is a card structure with a featured image and a title.                              | Pass   |


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
|Load the webpage containing the navigation bar | Pass |
|Verify that the navigation bar is visible at the top of the page.| Pass|
|Cook with me" logo is present, correctly positioned, and functions as a navigation link back to the home page|Pass|
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

|Ensure there is a card structure with a featured image and a title.|Pass|
|Verify that the title is a clickable link that directs the user to the corresponding recipe content page (recipe_content view).|Pass|

#### Like Functionality
|Check that each recipe card displays a heart icon representing the "like" functionality.|Pass|
|Verify that the heart icon changes based on whether the logged-in user has liked the recipe: If the user has liked the recipe, the heart should be solid. If the user has not liked the recipe, the heart should be regular.|Pass|
|Check that each recipe card displays the correct count of likes.|Pass|

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