
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
| Log in with a user account.                                                                      | Pass   |
| Confirm the visibility of the "Add a Comment" section.                                           | Pass   |
| Submit a comment using the form.                                                                 | Pass   |
| Verify that the submitted comment appears in the comments section.                               | Pass   |

#### Anonymous User Actions

- Objective: Evaluate actions for anonymous users in the Comments Section.

| Test                                                                                             | Status |
|--------------------------------------------------------------------------------------------------|--------|
| Log out or open the page in an incognito/private browsing window.                                | Pass   |
| Verify that the "Add a Comment" section is not visible.                                          | Pass   |
| Verify that the system restricts the comment submission.                                         | Pass   |

#### CRUD 

- Objective: Validate CRUD Operations for User Comments
- Precondition: Log in with a user account that has access to the recipe detail page.

#### Create Comment

- Objective: Ensure users can create a new comment.

| Test                                                                                             | Status |
|--------------------------------------------------------------------------------------------------|--------|
| Open the web page displaying a recipe.                                                           | Pass   |
| Locate the "Add a Comment" section.                                                              | Pass   |
| Fill in the comment form with relevant information.                                              | Pass   |
| Click the "Publish" button.                                                                      | Pass   |
| Verify that the new comment appears in the comments section.                                     | Pass   |
| Confirm that the user's name, creation date, and comment body are correctly displayed.           | Pass   |

#### Read Comment

- Objective: Confirm the display of existing comments.

| Test                                                                                              | Status |
|-------------------------------------------------------------------------------------------------- |--------|
| Confirm that existing comments are visible, showing user names, creation dates, and comment bodies.| Pass   |
| Ensure that pagination works correctly if there are multiple comments.                            | Pass   |

#### Update Comment

- Objective: Ensure users can edit their own comments.

| Test                                                                                             | Status |
|--------------------------------------------------------------------------------------------------|--------|
| Click the "Edit" button.                                                                         | Pass   |
| Modify the comment text.                                                                         | Pass   |
| Click the "Publish" or "Save Changes" button.                                                    | Pass   |
| Verify that the edited comment appears in the comments section.                                  | Pass   |
| Confirm that the changes to the user's name, creation date, and comment body are reflected.      | Pass   |

#### Delete Comment

| Test                                                                                              | Status |
|-------------------------------------------------------------------------------------------------- |--------|
| Click the "Delete" button.                                                                        | Pass   |
| Confirm the deletion.                                                                             | Pass   |
| Verify that the comment is no longer visible in the comments section.                             | Pass   |

## Authentication

- Objective: Validate User Registration, Login, and Logout Functionality

#### User Registration

- Objective: Verify that users can successfully register with valid information.

| Test                                                                                             | Status |
|--------------------------------------------------------------------------------------------------|--------|
| Enter a unique username, an optional email, and a valid password.                                | Pass   |
| Click the "Sign Up" button.                                                                      | Pass   |
| Confirm redirection to the products page.                                                        | Pass   |
| Verify that the user can access content on the redirected page                                   | Pass   |

#### User Login

- Objective: Verify that users can successfully log in with correct credentials.

| Test                                                                                             | Status |
|--------------------------------------------------------------------------------------------------|--------|
| Enter the username used during registration and the corresponding password.                      | Pass   |
| Click the Sign In button.                                                                        | Pass   |
| Confirm redirection to the products page.                                                        | Pass   |
| Verify that the user can access content on the redirected page.                                  | Pass   |

#### User Logout

- Objective: Verify that users can successfully log out.

| Test                                                                                             | Status |
|--------------------------------------------------------------------------------------------------|--------|
| Locate and click the "Sign Out" link in the navbar.                                              | Pass   |
| On the Sign Out page, click the "Sign Out" button.                                               | Pass   |
| Confirm that the user is logged out.                                                             | Pass   |
| Verify redirection to the Home Page.                                                             | Pass   |


## Admim

| Test                                                                                             | Status |
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

| Test                                                                                             | Status |
|--------------------------------------------------------------------------------------------------|--------|
| Confirm that the home page is visually appealing on a desktop.                                   | Pass   |
| Validate the responsiveness on tablet devices.                                                   | Pass   |
| Ensure a user-friendly experience on mobile devices.                                             | Pass   |


## Browsers Compatibility

The website has undergone comprehensive testing across popular desktop browsers, including Google Chrome, Safari, Mozilla Firefox, Opera, and Microsoft Edge. Based on the testing results, no significant compatibility issues were identified, and the website functions as expected across these browsers.