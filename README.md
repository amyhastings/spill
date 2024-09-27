# spill

### Purpose of the website
This Spill web application comprises my project for Module 3: Python of UCD's 24-03 Full-Stack Software Development Course. The objective of the project is as follows:

> The goal of this assignment is to build a web application. The web application should be built using Flask, incorporating modern HTML, CSS, and JavaScript to create an engaging and visually appealing web application. For example, you could create a portfolio website to showcase your projects, but the content of the web application is open to you. To host your web application, you will use https://render.com/.

I chose to prepare a web application for making anonymous confessions. The primary purpose of the website is to encourage users to unburden themselves of their secrets in an anonymous way, while facilitating a mechanism for likes and comments to allow users to show support and give feedback. The web application also provides a feed of confessions made allowing for the ancillary purpose of facilitating users who do not want to interact with the platform.

### Required features of the website
The text below outlines the principal requirements of the project for the website and how each requirement was satisfied.

- *Set up the Flask Environment.* I installed Flask, created a new directory for my Flask project, and intialised and activated the virtual environment.
- *Create Flask Application Files.* I created a Python file named app.py, imported the necessary Flask modules and set up the Flask application object and defined routes for different sections of the website.
- *Create HTML Files.* The project file includes nine HTML files. Each HTML file includes a basic structure, with the head and footer sections included in the base.html template.
- *Apply CSS Styling.* The CSS stylesheet, style.css, was included in the css subdirectory in the static directory of the project’s root directory. CSS styles were applied, as required to customize typography, colours, backgrounds, margins and padding. Responsiveness of this mobile-first website is addressed using CSS media queries.
- *Implement JavaScript Interactivity.* JavaScript files, script.js, comment.js and confession.js, were included in the js subdirectory in the static directory of the project’s root directory. JavaScript code was included in these files to add interactivity and dynamic behaviour to the website, including event listeners related to showing / hiding the navigation menu on smaller devices and indicating whether a post had been liked or unliked. The confession.js and comment.js files relate to form validation and providing appropriate feedback to users.
- *Integrate HTML, CSS, and JavaScript with Flask.* CSS and JavaScript files were integrated into the HTML files using the appropriate tags.
- *Define Flask Routes and Render HTML Files.* The Dublin History Quizzes website includes the following elements: a. Routes were defined for each section of the website in the app.py file; b. The render_template function from Flask was used to render the respective HTML files for each route; c. Lists were used to store and process data within the Flask application (this includes a list of pre-baked confession objects to populate the website to demonstrate usability); d. GET and POST methods were used in implementing Flask routes.
- *Test and Run the Flask Application.* The application was extensively tested on the localhost to ensure that all sections and pages were displayed and functioning correctly.
- *Hosting the Web App on Render.com.* The application was deployed to Render.com and the link is provided at the top of this document.

### Installation
A version of the website is deployed here: https://spill-p58o.onrender.com. To view this website off-line and/or make changes:
- clone the gitHub repository at https://github.com/amyhastings/spill;
- pip install -r requirements.txt;
- in the terminal, lauch the application python ./app.py.

### Licensing
This web application is the copyright of Amy Hastings. The font used in the logo and headers is Saphifen designed by Dhabee Studio.