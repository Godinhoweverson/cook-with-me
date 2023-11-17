# Cook with me

Welcome to Cook with Me, a delightful culinary journey where the art of cooking meets the joy of sharing. This website is dedicated to bringing the magic of recipes to your fingertips, allowing you to explore, create, and connect with fellow food enthusiasts. Whether you're a seasoned chef or a kitchen novice, there's something for everyone in our vibrant community.

![responsive](/static/images/readme/responsive.png)

## Table Of Contents

1. [UX Design](#ux-design)
2. [Project Strategy](#project-strategy)
3. [Project Sections](#project-sections)
4. [Scope](#scope)
5. [Features](#features)
7. [Testing](#testing)
8. [Technologies and Languages](#technologies-and-languages)
9. [Frameworks and Libraries](#frameworks-and-libraries)
10. [Project Dependencies](#project-dependencies)
11. [Deployment](#deployment)
12. [Credits & Acknowledgements](#credits--acknowledgements)

## UX Design 
Welcome to Cook with Me, a platform designed with a user-centric approach to enhance your culinary experience. Our UX design prioritizes simplicity, accessibility, and an immersive culinary journey for both seasoned chefs and cooking enthusiasts. Below, we'll delve into key aspects of our UX design.

### Intuitive Navigation
Cook with Me boasts an intuitive navigation system, ensuring that users can seamlessly explore recipes and features. The navigation bar, prominently positioned at the top, provides easy access to essential sections such as Home, Recipes, and User Authentication. Users can effortlessly find what they're looking for, making the overall experience smooth and enjoyable.

### User Authentication
The website offers a personalized experience through user authentication. By creating an account, users unlock additional features such as liking recipes, leaving comments. The authentication process is straightforward, encouraging users to become an integral part of the Cook with Me community.

### Responsive Design
Cook with Me is designed to be responsive, ensuring a consistent and visually appealing experience across various devices. Whether you're accessing the platform from a desktop, tablet, or smartphone, the layout adapts seamlessly to provide an optimal viewing and interaction experience.

### Engaging Visuals
Visual appeal is at the heart of Cook with Me. From stunning recipe images to an inviting layout, the platform leverages visuals to captivate users. The use of images in recipe cards and the home page carousel enhances the overall aesthetic, creating an enticing atmosphere for users to explore.

### Community Interaction
The UX design encourages community interaction through comments and engagement with other users. The comment section beneath recipes facilitates discussions, sharing experiences, and creating a sense of connection among users who share a passion for cooking.


## Project Strategy

### Overview
This project follows a structured strategy based on the MoSCoW prioritization framework. The project management and development progress are tracked using the GitHub Projects Kanban Board. This board serves as a visual representation of tasks and their current status, providing transparency and facilitating efficient collaboration.

## Project Sections

### Initial Setup

- Django Libraries, Project, and App Setup
- Ensure you have the necessary Django libraries installed
- Early Deployment on Heroku
- Bring Cook with Me to life by deploying an early version on Heroku. 

### Intuitive Web Navigation

- As a user, I want a clear and intuitive navigation system on the website, So that I can easily find the sections for recipes, login, register, and logout.
- As a user, I want to view a recipes option, So that I can easily find the recipe that I'm looking for.


### User Register, Login, and Logout

- As a user, I want to create a registration account, So that I can comment, edit, delete, and like recipes.
- As a user, I want to be able to log into the website, So that I can interact with the posts.


### CRUD Operations (Create, Update, Delete) and Likes

- As a user,I want to create comments, So that I can give feedback about recipes.
- As a user, I want to edit my comments, So that I can correct mistakes or change my opinion.
- As a user, I want to delete my comments, so that I can remove unwanted content.
- As a user, I want to give likes to the recipes, So that I can show my appreciation for the content.

### Admin Moderation

- As an admin, I want to post recipes, So that users can enjoy and engage with the content.
- As an admin, I want to manage and approve the comments, So that I can prevent unwanted content from being displayed.

## Scope

### Overview

As I embarked on the journey of creating this project, my primary focus was on the user experience. Envisioning the ideal recipe website from a user's perspective, I aimed for simplicity and clarity.

### Inspiration

To kickstart the project, I delved into various existing recipe websites. However, I noticed a common challenge—they often felt cluttered and overwhelming, bombarding users with an excess of information. Determined to offer a refreshing alternative, I conceived "Cook with Me" with a clear and distinct objective: to streamline the user's culinary exploration.

### Guiding Principles 

Simplicity: "Cook with Me" is designed with a commitment to simplicity. The interface is intentionally uncluttered, ensuring a seamless and enjoyable experience for users seeking culinary inspiration.

Focused Content: Our primary goal is to immerse users in the world of food. Unlike many recipe platforms, we concentrate solely on the essence of cooking. No distractions, no unnecessary information—just a straightforward path to finding the perfect recipe.

### Key Features
Intuitive Web Navigation: Users can effortlessly navigate through the website, locating sections for recipes, login, register, and logout with ease.

Recipe Focus: The heart of "Cook with Me" lies in its dedication to showcasing recipes. The platform is crafted to enable users to swiftly find the specific recipe they're searching for.

### Why "Cook with Me"?
In a digital landscape cluttered with culinary information, "Cook with Me" stands out as a beacon of simplicity. Here, the user's journey is centered on the joy of cooking. Say goodbye to chaotic interfaces—welcome to a space where food takes center stage.

## Goals

### Intuitive Web Navigation:

- Goal: Create a clear and intuitive navigation system.
- Strategy: Implement a straightforward navigation menu with dedicated sections for recipes, user authentication (login, register, logout), ensuring users can easily find what they need.

### User Registration, Login, and Logout:

- Goal: Enable users to interact with the platform by registering, logging in, and logging out.
- Strategy: Implement user authentication features, allowing users to create accounts, log in, and log out, enabling them to engage with the community and perform actions such as commenting, editing, deleting, and liking recipes.

### CRUD Operations (Create, Update, Delete) and Likes:

- Goal: Facilitate user interaction with recipes through comments and likes.
- Strategy: Implement CRUD operations for comments (create, edit, delete) and provide a like functionality for recipes, allowing users to express their opinions and appreciation.

### Admin Moderation:

- Goal: Empower administrators to manage content and ensure a positive user experience.
- Strategy: Implement admin features for posting recipes, as well as managing and approving comments to prevent unwanted or inappropriate content.

<details>
<summary><strong>Wireframes</strong></summary>

### DESKTOP

![Wireframes](/static/images/readme/home.png)
![Wireframes](/static/images/readme/recipes.png)
![Wireframes](/static/images/readme/recipe_content.png)
![Wireframes](/static/images/readme/login.png)
![Wireframes](/static/images/readme/signup.png)
![Wireframes](/static/images/readme/signout.png)

### MOBILE

![Wireframes](/static/images/readme/home-mobile.png)
![Wireframes](/static/images/readme/recipes-mobile.png)
![Wireframes](/static/images/readme/recipes-content-mobile.png)
![Wireframes](/static/images/readme/login-mobile.png)
![Wireframes](/static/images/readme/signup-mobile.png)
![Wireframes](/static/images/readme/signout-mobile.png)

</details>


<details>
<summary><strong>Flowchart logic</strong></summary>

![Wireframes](/static/images/readme/flowchart.png)

</details>

## Agile methodology

In the development of this project, I utilized the Agile methodology to ensure an iterative and flexible approach to software development. The project is structured around 10 key user stories, each contributing to four distinct milestones:

- Intuitive Web Navigation
- User Registration, Login, and Logout
- CRUD Operations (Create, Update, Delete)
- Likes and Admin Moderation

This classification helps prioritize features and functionalities, fostering a more streamlined and efficient development process. Each milestone addresses specific aspects, ensuring a comprehensive and organized implementation of the project's goals.

<details>
<summary><strong>Kanban Board</strong></summary>

![Kanban Board](/static/images/readme/strategyboard.png)

</details>


## Database Model

### Recipe Model

The Recipe model stands as the centerpiece of the application, gracefully capturing the essence of each culinary masterpiece:

- featured_image: The main image that brings your recipe to life, prominently displayed on the recipes page.
- recipe_image: An additional image for a more immersive recipe presentation, enhancing the visual experience on the recipes_content page.
- title: A unique title identifying each recipe.
- created_date: Automatically records the date and time when a recipe is added.
- content: A detailed description of the recipe, dynamically and user-friendly crafted with the help of Summernote. Responsible for the ingredients section on the recipes.
- content_method: Instructions and method content for preparing the recipe, with a default provided for convenience.
- status: A status indicator, allowing recipes to be in a "Draft" or "Published" state.
- likes: A dynamic relationship with the Django User model, facilitated by django-allauth, enabling users to express appreciation by liking recipes.

Additionally, the Recipe model includes methods such as <strong>__str__</strong> for a human-readable representation and <strong>number_of_likes</strong> to easily retrieve the count of likes for a recipe.

### Comment Model

The Comment model fosters user interaction and feedback:

- recipe: A ForeignKey establishing a link between comments and the respective recipe.
- user: ForeignKey to the Django User model, made possible by django-allauth, allowing registered users to leave comments.
- email: An optional field for providing an email address, enhancing engagement for anonymous users.
- content_body: The main content of the comment, dynamically and user-friendly composed with the help of Summernote.
- comment_approved: A boolean indicating whether the comment has been approved for public view.
- created_on: The timestamp capturing when the comment was added.

## Integrations

#### django-allauth
Seamlessly handles user authentication, signup, login, signout, and forms, ensuring a secure and user-friendly experience.

#### Summernote
Empowers content creation and editing with a WYSIWYG editor, making recipe descriptions and comments visually appealing and easy to compose. Enhance the engagement of your users with rich and dynamic content.

<details>
<summary><strong>Database Diagram</strong></summary>

![databasediagram](/static/images/readme/databasemodel.jpg)

</details>

## Fonts

In this project, I've employed the following fonts to enhance visual appeal:

- **Great Vibes (Cursive):** Applied to H1 elements on the home page.
- **Montserrat (Sans-serif):** Used for all other text, ensuring a clean and modern aesthetic throughout.


## Features

### Navbar

- Branding: The navbar features a prominent brand name, "Cook with me," serving as a clickable link to the home page.

- Responsive Design: Utilizes Bootstrap classes to ensure responsiveness on various screen sizes. The navigation bar collapses into a toggler on smaller screens for improved user experience.

- Navigation Links: Includes essential navigation links such as "Home" and "Recipes," ensuring easy access to key sections of the website.

- Authentication Handling: Dynamically displays "Logout" when the user is authenticated and "Register" and "Login" options when the user is not authenticated. This ensures a personalized experience based on user status.

<details>
<summary><strong>Navbar</strong></summary>

![Navbar](/static/images/readme/navbar.jpg)

</details>

### Footer

The following HTML code snippet represents the footer section of a website, specifically designed to include social media links and copyright information. The footer enhances user engagement and provides a way to connect with the website through various social platforms.

- Social Media Links: Includes buttons for popular social media platforms such as Facebook, YouTube, Google, and Instagram. Each button is styled as a link and opens in a new tab when clicked.

- Styling and Responsiveness: Utilizes Bootstrap classes to structure and style the footer. The design is responsive and adjusts gracefully to different screen sizes.

- Copyright Information: Displays a copyright notice along with the year, providing legal information about the content ownership.

<details>
<summary><strong>Footer</strong></summary>

![footer](/static/images/readme/footer.jpg)

</details>


## Home page

The homepage for the "Cook with Me" website, designed to immerse visitors in a culinary universe curated by Godinho. It beckons users to explore a delightful collection of recipes and embrace the joy of cooking and sharing meals.

### Sections

#### Title Section

- An engaging image capturing the essence of the culinary experience.
- A prominent title, "Cook with me," setting the tone for the website.
- Attribution to the creator, "By Godinho."

#### About Section
- A heartfelt description of the website's purpose and origin.
- An invitation for users to explore a personal culinary canvas filled with recipes crafted with passion.
- Emphasis on the joy of cooking and sharing meals as life's greatest pleasures.
- Encouragement for users to dive in, cook, and savor every bite.
- Includes a dynamic carousel display showcasing three images that complement the website's narrative.

<details>
<summary><strong>Home</strong></summary>

![home](/static/images/readme/homepage.jpg)

</details>

## Recipes

The recipes.html page is dedicated to showcasing a meticulously curated collection of delightful recipes on the "Cook with Me" website.

### Title Section

A descriptive title, setting the theme for the recipe section.

### Recipes Display
A list of recipes, each featuring:
- Recipe Title: Clearly indicating the name of the recipe.
- Recipe Image: An enticing image representing the visual appeal of the recipe.
- Likes Functionality: Users can express their appreciation for a recipe by clicking a heart icon, indicating a "like."
### Admin Page Integration

- Utilizes Django's admin page for seamless management of recipes.
- Admins can add, edit, or remove recipes effortlessly using the Recipe model.

### Usage
Incorporate the recipes.html file into your Django project to serve as the dedicated recipe page.
Utilize Django's admin page for efficient management of recipes via the Recipe model.
Customize the title, list of recipes, and images based on your culinary offerings.
Implement the likes functionality to enable users to express their appreciation for a recipe.

<details>
<summary><strong>Recipes</strong></summary>

![Recipes](/static/images/readme/recipepage.jpg)

</details>


## Recipes content

- The content block includes sections for displaying the recipe's title, image, ingredients, and method, with data coming from the Recipe model.
- A decorative SVG wave divider is included for visual appeal.
- The comments section displays existing comments, supports pagination, and allows authenticated users to create, edit, and delete comments.
- For non-authenticated users, a message encourages them to log in to post comments.
- Edit and delete functionalities are implemented for authenticated users to manage their comments. The user is redirected to the respective pages (edit_comment and delete_comment) for editing or confirming deletion.


<details>
<summary><strong>Recipes content</strong></summary>

![Recipes-content](/static/images/readme/recipe-content-title.jpg)
![content](/static/images/readme/recipe-content.jpg)
![comment](/static/images/readme/comment.jpg)
![edit](/static/images/readme/edit.jpg)
![delete](/static/images/readme/delete.jpg)

</details>

## User Authentication

The application incorporates Django Allauth for seamless user authentication. Three main forms are utilized. 

- Responsive design displays on the right side with an image on the left; on mobile, only the form is visible.

#### Sign Up:
- Users can register to engage with the site's features.
- Required fields: Username, optional email, and password (confirmation required).

#### Login:
- Registered users can log in.
- Required fields: Username and password.

#### Sign out:
-Allows users to log out securely.

<details>
<summary><strong>User Authentication</strong></summary>

![Signup](/static/images/readme/signup-feature-.jpg)
![Signin](/static/images/readme/signin-featurej.jpg)
![signout](/static/images/readme/signout-feature.jpg)


</details>

## Admin Panel Access

For administrative purposes, an admin panel is accessible through [this link](https://cook-with-me-0c33f788a701.herokuapp.com/admin/login/?next=/admin/). Access is restricted to authorized administrators or superusers. To log in, use your assigned username and password.

### Admin Capabilities:

#### Recipe Management:
Admins can post new recipes, manage existing ones, and keep the culinary content up-to-date.

#### Comment Administration:
Efficiently handle comments, including editing and deleting, to ensure a positive and engaging user experience.

#### User Management:
Manage user accounts, overseeing registrations, and ensuring a secure and enjoyable environment for all users.
This secure admin area ensures that the platform is well-maintained and content is curated effectively.

<details>
<summary><strong>Admin</strong></summary>

![admin](/static/images/readme/admin.jpg)

</details>

## Error Pages (403, 404, 500)

Custom error pages have been integrated to maintain the site's consistent look and feel in the following scenarios:

- When a user attempts to access a page that doesn't exist.
- When a user attempts to access a page for which they don't have the necessary permissions.
- In the event of a server error.

Each of these error pages includes a convenient link allowing users to easily return to the Home page. This ensures a seamless and user-friendly experience even when unexpected errors occur.

<details>
<summary><strong>403</strong></summary>

![admin](/static/images/readme/403-test.jpg)

</details>

<details>
<summary><strong>404</strong></summary>

![admin](/static/images/readme/404-test.jpg)

</details>

<details>
<summary><strong>500</strong></summary>

![admin](/static/images/readme/500-test.jpg)

</details>



## Future Features

While the current version of the project offers essential functionalities, I have exciting plans for future enhancements. Here are some features I'm considering:

**User Profiles:**
   - Implement user profiles to allow users to personalize their account.

**Advanced Search:**
   - Introduce a more robust search functionality, enabling users to find recipes based on various criteria.

**Recipe Ratings and Reviews:**
   - Enable users to rate and review recipes, fostering a sense of community and feedback.

**Social Media Sharing:**
   - Allow users to share their favorite recipes on social media platforms, increasing the project's visibility.

## Testing

The full testing documentation can be found in [TESTING.md](TESTING.md)


## Technologies and Languages

### Languages Used

#### HTML:
- Utilized for structuring the content and layout of web pages.

#### CSS:
- Applied to enhance the visual presentation and styling of the website.

#### JavaScript:
- Used for adding interactive and dynamic features to the user interface.

#### Python:
- The primary backend language, enabling server-side logic and data processing.

### Technologies

- [Code Anywhere](https://codeanywhere.com/) Used for coding and managing application files, facilitating seamless collaboration between the code editor and the repository.

- [GitHub](https://github.com/) Utilized for storing and version controlling the project, allowing for efficient collaboration, code sharing, and project management.

- [MockFlow](https://www.mockflow.com/) Used for creating database diagrams and flowcharts, aiding in the visual representation and planning of the project's structure.

- [Google Fonts](https://fonts.google.com/) Employed for styling text elements on the website, providing a diverse range of free and open-source fonts for enhanced typography.

- [Font Awesome](https://fontawesome.com/) Utilized for incorporating icons into the site, adding visually appealing and meaningful graphical elements.

- [Am I Responsive?](http://ami.responsivedesign.is/) Applied for creating responsive design images, allowing you to visualize how the website appears across various devices and screen sizes.

- [Chatgpt](https://openai.com/blog/chatgpt) Utilized to generate all written content, leveraging advanced natural language processing capabilities to create dynamic and interactive text throughout the application.

- [Vs code](https://code.visualstudio.com/) Utilized as the primary integrated development environment (IDE) for coding and managing project files, providing powerful features for efficient development.

- [Git](https://git-scm.com/) used for version control. (git add, git commit, git push)

- [Google Chrome Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) Used for website performance and SEO audits, providing insights into improving the overall quality and user experience of the site.

- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) Leveraged for debugging, profiling, and analyzing the performance of web applications during development.

- [W3C HTML Validator](https://validator.w3.org/) Applied for validating HTML code against W3C standards, ensuring adherence to best practices and promoting cross-browser compatibility.

- [W3C CSS Validator](https://css-validator.org/) Utilized for validating Cascading Style Sheets (CSS) code, ensuring compliance with W3C standards for consistent styling.

- [Wave Accessibility Tool](https://wave.webaim.org/) Employed for evaluating and enhancing website accessibility, providing insights and recommendations for creating a more inclusive web experience.

- [CI Python PEP8 Checker](https://pep8ci.herokuapp.com/) Implemented for continuous integration to check Python code against the PEP 8 style guide, promoting consistent and readable code.

- [Cloudinary](https://www.cloudimage.io/) Utilized for cloud-based image and video management, offering efficient storage, optimization, and delivery of media assets.

- [PostgreSQL](https://www.postgresql.org/) Chosen as the relational database management system (RDBMS) for storing and managing structured data within the application.

- [ElephantSQL](https://www.elephantsql.com/) Utilized as a hosted PostgreSQL service, simplifying database management and deployment.

- [Heroku](https://heroku.com) Deployed for hosting the web application, providing a cloud platform for easy application deployment, scaling, and management.

## Frameworks and Libraries

#### Bootstrap:
- Employed for responsive and mobile-first design, facilitating a consistent and appealing user experience across various devices.

#### Django:
- A high-level Python web framework utilized for building robust and scalable web applications.

## Project Dependencies
- To ensure the proper functioning of the "Cook with Me" web application, the project relies on various Python packages and libraries. Here's a list of dependencies along with their versions:

#### asgiref==3.7.2:
- ASGI (Asynchronous Server Gateway Interface) reference implementation.

#### cloudinary==1.36.0:
- Python SDK for interacting with the Cloudinary media management service.

#### dj-database-url==0.5.0:
- Utility to parse database URLs for Django applications.

#### dj3-cloudinary-storage==0.0.6:
- Django storage backend for Cloudinary.

#### Django==4.2.6:
- The core web framework for building the web application.

#### django-allauth==0.58.0:
- Authentication, registration, account management, and other user-related functionality for Django.

#### django-crispy-forms==1.14.0:
- A Django application to easily manage form rendering.

#### django-summernote==0.8.20.0:
- Integrates the Summernote WYSIWYG editor with Django.

#### django-widget-tweaks==1.5.0:
- A set of additional template filters for Django templates.

#### gunicorn==21.2.0:
- A production-ready WSGI server for running Django applications.

#### httplib2==0.20.2:
- A comprehensive HTTP client library.

#### oauthlib==3.2.0:
- A generic, reusable Python library for implementing OAuth1 and OAuth2 providers.

#### psycopg2-binary==2.9.9:
- PostgreSQL adapter for Python.

#### PyJWT==2.3.0:
- Python library for JSON Web Tokens.

#### python3-openid==3.2.0:
- Python OpenID library.

#### pytz==2023.3.post1:
- World timezone definitions for Python.

#### requests==2.31.0:
- A simple HTTP library for Python.

#### requests-oauthlib==1.3.1:
- OAuthlib authentication support for Requests.

#### sqlparse==0.4.4:
- A non-validating SQL parser for Python.


## Deployment

### Prerequisites
Before deploying the application, ensure the following prerequisites are met:

1. Requirements.txt
Keep the requirements.txt file updated with the latest Python module dependencies.

2. Procfile
Include a Procfile to configure Heroku deployment as a gunicorn web app.

3. Settings.py Configuration
Configure the ALLOWED_HOSTS list in settings.py (e.g., ['app_name.heroku.com', 'localhost']).
Verify that static files and directories are correctly configured.
4. Environment Variables
In the env.py file (gitignored), ensure the following hidden variables are configured correctly:

- SECRET_KEY
- DATABASE_URL
- CLOUDINARY_URL
- PORT

### Deployment on Heroku

#### Create a Heroku Account:

#### Sign up on Heroku.
- Optional: Sign Up with a Student Account:

#### Create a New App:
- Once logged in, create a new app on Heroku.

#### Configure App Details:
- Select an app name and region.

#### Connect to GitHub:
- Under "Deployment Method," select "Connect to GitHub."
- Connect to the desired repository (e.g., Coolcoders PP4).
- Enable automatic deploys and select the main branch.

#### Configure Environment Variables:
In the "Settings" tab, reveal config vars and input the required hidden variables.

#### Select Buildpacks:
- Choose Node.js and Python as the buildpack.

#### Deploy:
- Deploy the application.

### Fork the Repository
- Go to the GitHub Repository:

### Visit the GitHub repository.

#### Fork the Repository:
- Click on the "Fork" button in the upper right-hand corner.
- Edit the repository name and description if desired.
- Click the green "Create Fork" button.
- Clone the Repository

### Go to the GitHub Repository:
- Visit the GitHub repository.

### Clone the Repository:
- Locate the green "Code" button above the list of files and click it.
- Select the preferred cloning method (HTTPS, SSH, or GitHub CLI) and copy the URL.

### Open Git Bash:
- Change the current working directory to where you want the cloned directory.
- Type git clone and paste the URL from the clipboard (e.g., $ git clone https://github.com/Godinhoweverson/cook-with-me).
- Press Enter to create your local clone.
- Run the Repository Locally

#### Go to the GitHub Repository:
- Visit the GitHub repository.

#### Download Zip File:
- Locate the green "Code" button above the list of files and click it.
- From the dropdown menu, select "Download Zip."
- Download and open the zip file to run it in an editor.

#### Create env.py File:
- Create an env.py file and input the necessary environment variables.

#### Ensure PostgreSQL is Installed:
- Ensure PostgreSQL is installed on your computer, and ports are open.

#### Create a Virtual Environment:
Create a virtual environment for installing the Python modules listed in the pip file.

### Run Commands:

#### Run the following commands:
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver


## Credits & Acknowledgements

- Recipe Content and Images
All recipe content and images featured on this website are attributed to the culinary expertise of Gordon Ramsay. As a superfan and dedicated follower of his work, I am honored to showcase his exceptional recipes and delicious creations. Gordon Ramsay's influence on the culinary world has been a source of inspiration, and this project serves as a tribute to his remarkable contributions to the world of gastronomy.

I express my sincere gratitude to Gordon Ramsay for sharing his passion for food and cooking, making it possible for enthusiasts like me to enjoy and learn from his expertise.

Note: This project is created for educational and non-commercial purposes, and all credits for the recipes and images go to Gordon Ramsay.

- This website was built by following the walkthrough project Django Blog by Code Institute.
- Tips about Django and Python by the [Pythonando](https://www.youtube.com/@pythonando) channel on YouTube.
- Special thanks to [CFB Cursos](https://www.youtube.com/@cfbcursos) for valuable tips in Bootstrap
- I would like to express my gratitude to Narender Singh Mentor for providing valuable guidance and tips to improve my project.
- I extend my heartfelt thanks to my wife, Deborah, for her unwavering support and encouragement throughout the duration of this project.
