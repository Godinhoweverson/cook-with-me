# Cook with me

Welcome to Cook with Me, a delightful culinary journey where the art of cooking meets the joy of sharing. This website is dedicated to bringing the magic of recipes to your fingertips, allowing you to explore, create, and connect with fellow food enthusiasts. Whether you're a seasoned chef or a kitchen novice, there's something for everyone in our vibrant community.

![responsive](/static/images/readme/responsive.png)


  ***TABLE OF CONTENTS***


## UX Design 
Welcome to Cook with Me, a platform designed with a user-centric approach to enhance your culinary experience. Our UX design prioritizes simplicity, accessibility, and an immersive culinary journey for both seasoned chefs and cooking enthusiasts. Below, we'll delve into key aspects of our UX design.

### Intuitive Navigation
Cook with Me boasts an intuitive navigation system, ensuring that users can seamlessly explore recipes and features. The navigation bar, prominently positioned at the top, provides easy access to essential sections such as Home, Recipes, and User Authentication. Users can effortlessly find what they're looking for, making the overall experience smooth and enjoyable.

### User Authentication
The website offers a personalized experience through user authentication. By creating an account, users unlock additional features such as liking recipes, leaving comments, and saving favorite recipes. The authentication process is straightforward, encouraging users to become an integral part of the Cook with Me community.

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

### NavBar

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