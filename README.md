# Scales & Tails

![Scales & Tails responsive screenshot]()

## Introduction

Scales & Tails is a information resource with social forum interactivity. Scales & Tails is my Code Institute Full-Stack Developer Bootcamp personal project - focusing on Django and Bootstrap frameworks, Database manipulation and CRUD functionality. It is for educational purposes only.

View live site here : [Scales & Tails]()  
  
For Admin access with relevant sign-in information: [Scales & Tails Admin]()

<hr>

## Table of Contents

- [Scales & Tails](#Scales & Tails)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
- [UX - User Experience](#ux---user-experience)
  - [Design Inspiration](#design-inspiration)
    - [Colour Scheme](#colour-scheme)
    - [Font](#font)
- [Project Planning](#project-planning)
  - [Strategy Plane](#strategy-plane)
    - [Site Goals](#site-goals)
  - [Agile Methodologies - Project Management](#agile-methodologies---project-management)
    - [MoSCoW Prioritization](#moscow-prioritization)
    - [Sprints](#sprints)
  - [User Stories](#user-stories)
    - [Visitor User Stories](#visitor-user-stories)
    - [Epic - User Profile](#epic---user-profile)
    - [Epic - Articles](#epic---articles)
    - [Epic - Booking](#epic---booking)
    - [Epic - Photo Gallery](#epic---photo-gallery)
    - [Epic - Visit Us/Reviews](#epic---visit-usreviews)
  - [Scope Plane](#scope-plane)
  - [Structural Plane](#structural-plane)
  - [Skeleton \& Surface Planes](#skeleton--surface-planes)
    - [Wireframes](#wireframes)
    - [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
    - [Security](#security)
- [Features](#features)
  - [User View - Registered/Unregistered](#user-view---registeredunregistered)
  - [CRUD Functionality](#crud-functionality)
  - [Feature Showcase](#feature-showcase)
  - [Future Features](#future-features)
- [Technologies \& Languages Used](#technologies--languages-used)
  - [Libraries \& Frameworks](#libraries--frameworks)
  - [Tools \& Programs](#tools--programs)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Connecting to GitHub](#connecting-to-github)
  - [Django Project Setup](#django-project-setup)
  - [Cloudinary API](#cloudinary-api)
  - [Elephant SQL](#elephant-sql)
  - [Heroku deployment](#heroku-deployment)
  - [Clone project](#clone-project)
  - [Fork Project](#fork-project)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
    - [Additional reading/tutorials/books/blogs](#additional-readingtutorialsbooksblogs)
  - [Acknowledgements](#acknowledgements)

## Overview

Scales and Tails is a site for users to look up care information for their pet snakes:

- Users that sign up can post questions they have or answer other users questions
- Create their own profiles
- Add pictures of their pets and their set ups
- View basic care sheets for multiple species of snake 

Scales & Tails is a fully responsive site, and is viewable across all platforms (mobile, tablet and desktop). This is a site for snake enthusiasts from beginners to experts to look up care information for their pets.
The site will be broken down into species sections where there will be basic care information and a forum section for users to ask questions, post replies or just upload images.


# UX - User Experience

## Design Inspiration



### Colour Scheme





### Font


  
# Project Planning  
 
## Strategy Plane



### Site Goals



## Agile Methodologies - Project Management



### MoSCoW Prioritization

I chose to follow the MoSCoW Prioritization method for Scales & Tails, identifying and labelling my:

- **Must Haves**: the 'required', critical components of the project. Completing my 'Must Haves' helped me to reach the MVP (Minimum Viable Product) for this project early, allowing me to develop the project further than originally planned.
  
- **Should Haves**: the components that are valuable to the project but not absolutely 'vital' at the MVP stage. The 'Must Haves' must receive priority over the 'Should Haves'.
- **Could Haves**: these are the features that are a 'bonus' to the project, it would be nice to have them in this phase, but only if the most important issues have been completed first and time allows.
- **Won't Haves**: the features or components that either no longer fit the project's brief or are of very low priority for this release. 

### Sprints



| Sprint No. | Sprint Content | Start/Finish Dates |
|------------|----------------|--------------------|
| #1 | Project Setup |  |
| #2 | All Auth Setup/Site Navigation |  |
| #3 | Profile/Articles Features |  |
| #4 | Booking/Gallery Features |  |
| #5 | Frontend Development |  |
| #6 | Testing/Documentation |  |


## User Stories

User stories and features recorded and managed on [GitHub Projects](<>)


### Visitor User Stories

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|


### Epic - User Profile

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|    


### Epic - Articles

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|


  
### Epic - Booking

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|


### Epic - Photo Gallery

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|

### Epic - Visit Us/Reviews

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|

    
    
## Scope Plane

As this would be a dual learning/building project using technologies that were new to me, such as Django, SQL, Bootstrap and Cloudinary, I was cautious to maintain consistent control over the scope of the project and not let my idea grow too big. With the sheer amount of files, I needed to lockdown my project features early on into manageable blocks so as not to lose track of the MVP. Following my learning of the Django MVT framework I was able to identify how to change the templated structure to produce different website features from my base HTML. This allowed me to build upon my original idea of 'Booking app' only, and to add a social experience around articles and shared images. Following Agile Planning Methodologies, I added my Developer Tasks, User Stories and Testing Tasks as issues on my [GitHub project board](), and set up Sprints to keep the flow of the project in check.

Essential features of my project were:

- A striking, accessible website that fulfils user needs
- Responsive website for users of mobile, tablet and desktop devices
- User Authentication
- User Profile creation and editing
- Article feature with full CRUD functionality
- Booking feature with full CRUD functionality
- Gallery wall with adding/deletion of images
- Business details to inform the user

Planning my project thoroughly from the start allowed me to identify areas of importance for MVP completion and satisfaction of assessment criteria, and to balance them with the feasibility of the features.


## Structural Plane

From initial concept to finished product, having icons as the navigation area was an idea that I stuck with. I wanted to understand how to implement icon-based UX successfully so that the user can easily understand its purpose. Bootstrap classes and components were used to help control the flexibility of the site alongside overriding some classes with my own CSS to style as much of the form inputs that I could. Site graphic components were created by myself in Figma and Procreate. Combining icons from Google's [Material Symbols & Icons]() pack, icons from [Flaticon](https://www.flaticon.com/) and my colour scheme, I created my navbar icons in Figma. Each icon was placed on a colour-themed rectangle with ```border-radius:30px;``` and exported as PNGs. I edited my Login/Logout icons with a pawprint in the center of lock to have them fit the dog theme better.  


![navbar icons]()  
*Navigation icons for *

  
Accessibility is very important to me and in case I missed the mark with my icon idea, I ensured that I created tooltips for both mobile and desktop views that reveal the icons purposes on hover with the mouse and hover/light touch on mobile.  

  
![desktop tooltips]()  
*Navigation bar tooltips demonstrated on Desktop*

 
Continuing with a similar shape of the icons, images and buttons on the Scales & Tails website are given a border-radius ranging from 20px - 30px to round off the corners and keep the styling consistent throughout the project.  
 
  
![image with rounded corners]()  
*Article card from the Articles section with rounded corner styling*

 
Headings were given thick, dashed, underline styling in the coordinating colour of their feature to mark the beginning of a section.

 
![header with underline]()  
*Sign Up page header with purple underline for Authentication related sections*  
  
  

I utilised webkits to change the appearance of my scrollbar to include rounded endpoints and a muted, purple/teal colour-gradient. This was especially so the smaller scrollbar within the profile dashboard would fit in with the projects design. The scrollbar change was successful in the Chrome browser but did not translate over to the Mozilla or Safari browsers. This will be looked at for the next deployment to hopefully continue the design over all browsers. 
  
  
![scrollbar]()  
*Modified Scrollbar*
  

To allow for ease of responsiveness, each section was designed keeping in mind the switch from 'row' to 'column' when moving from Desktop to Mobile/Tablet view. This approach allowed me to add more features to the project early on by reusing and repurposing sections of code.

## Skeleton & Surface Planes

### Wireframes

The wireframes for Scales & Tails were created in Figma and were high-spec from the beginning as I was sure of my design concept. [Figma](www.figma.com) is an easy and fast design system for web and software mockups that allows for great control and testing of ideas particularly within the specific frame sizes which represent different devices. As I was using Bootstrap, I was confident that I had created a modular structure for my feature elements that would suit a grid system and that would allow them to easily work across different devices and screen sizes.

**Mobile/Tablet view for:**  

- Home
- Sign Up
- Profile

Originally I had planned for the home page to be mostly icon based for quick and easy use. However, I felt that this format would suit a downloadable app version of Scales & Tails, instead of the web version, which regular users might avail of to give them quicker access to the booking page, especially if they are one-handed, walking the dog on the way to the park. This will be part of my future features for the project growth.

<details open>
    <summary>Mobile/Tablet Home Page Wireframe</summary>  
    <img src="">  
</details>
  
The hero image of the beagle and patterned background was created in Figma. The beagle was removed from it's photo background and placed over an SVG that I edited on [Pattern Monster](https://pattern.monster/memphis-1/). The corners were then rounded.

<details>
    <summary>Mobile/Tablet Sign Up Page Wireframe</summary>  
    <img src="">
</details>

<details>
    <summary>Mobile/Tablet Profile Page Wireframe</summary>  
    <img src="">
</details>

**Desktop view for:**

- Home
- Sign Up
- Profile
- Booking
- Gallery
- Find Us
- Contact Us

<details open>
    <summary>Desktop Home Page Wireframe</summary>  
    <img src="">  
</details>

<details>
    <summary>Desktop Home Page Footer Wireframe</summary>  
    <img src="">
</details>

<details>
    <summary>Desktop Sign Up Page Wireframe</summary>  
    <img src="">
</details>

<details>
    <summary>Desktop Profile Create Page Wireframe</summary>  
    <img src="">
</details>

<details>
    <summary>Desktop Profile View Page Wireframe</summary>  
    <img src=""> 
</details>


<details>
    <summary>Desktop Gallery Page Wireframe</summary>  
    <img src="">
</details>

<details>
    <summary>Desktop Gallery Add Photo Page Wireframe</summary>  
    <img src="">
</details>

<details>
    <summary>Desktop Contact Us Page Wireframe</summary>  
    <img src="d">  
</details>


### Database Schema - Entity Relationship Diagram

![ERD Image]()  
*Database Schema (ERD) for Scales & Tails displaying relationships between feature components saved within the database*

This Entity Relationship Diagram(ERD) demonstrates how each feature interacts with each other and the connected PostgreSQL Database. Using Django's User Model, and Django AllAuth to carry out all user authentication, a user_id is created when the user registers with their username and email. This allows the user to edit a blank profile, create new articles, add comments and photos which will display their username, and create and manage their bookings. For future development, a Feedback system will be included allowing users to leave a review of the park.

The Profile, Articles and Comments Models were inspired by the blog walkthrough by the Code Institute and the [] during my learning of Django. They helped me to get a good and secure grasp of the templating structure and connected Python files to push my features further, make them my own and then develop my Booking and Gallery Models.


Through the Admin Django Dashboard, the connected user_id to all data entered to the site means that the Admin can remove a User and their data completely through the additon of on_delete=models.CASCADE. At the moment, a user can remove any data they share with the site, but they cannot delete their account completely. This feature will come in the next version.

### Security


**AllAuth**  

Django AllAuth is an installable framework that takes care of the user registration and authentication process. Authentication was needed to determine when a user was registered or unregistered and it controlled what content was accessible on Scales & Tails. The setup of AllAuth included:

- installing it to my workspace dependencies
- adding it to my INSTALLED_APPS in my settings.py
- sourcing the AUTHENTICATION_BACKENDS from the AllAuth docs for my settings.py
- adding its URL to my projects 'urls.py'
- run database migrations to create the tables needed for AllAuth
- 
**Defensive Design**  

Scales & Tails was developed to ensure a smooth user experience, to the best of my current learning experience with Django. 

- Input validation and error messages provide feedback to the user to guide them towards the desired outcome. 
- Unregistered users are diverted to the Sign Up page from restricted access pages. 
- Authentication processes control edit/delete icons to reveal them to the content author only. 
- Deletion of data is confirmed through an additional modal, double-checking with the user.
- Error pages are displayed with 'Take me home' buttons to help users get back on track. 
- Testing and validation of features completes the process.

**CSRF Tokens** 

CSRF (Cross-Site Request Forgery) tokens are included in every form to help authenticate the request with the server when the form is submitted. Absence of these tokens can leave a site vulnerable to attackers who may steal a users data.
  

# Features

## User View - Registered/Unregistered

It was important to me from the beginning that Scales & Tails be accessible to an unregistered user, in some capacitites. I wanted the website to sell the product to a new user quickly by immediately inviting them into the community through the park's information, articles and gallery sections. The following is a breakdown of the site's accessibility for registered/unregistered users:

| Feature   | Unregistered User | Registered, Logged-In User |
|-----------|-------------------|-----------------|
| Home Page | Visable           | Visable         |
| Profile   | Not Visible - 'Profile' icon only appears for registered, logged-in users | Visable and full feature interaction available |



## CRUD Functionality

Users are able to Create, Read, Update and Delete their shared information on Scales & Tails. Some features make full CRUD functionality available, whilst others present the necessary options only. Here is my CRUD breakdown for Scales & Tails:

| Feature | Create | Read | Update | Delete |
|---------|--------|------|--------|--------|
| Profile | Created upon registration | Yes | Yes | Full Profile deletion is currently only available to Admin upon User Account deletion, the profile dashboard clears automatically if a user removes all of their articles or bookings |

| Gallery | Yes | Yes | No - this feature felt unneccessary as it's intention is a 'quick-sharing' of a photo, a minimal amount of information is required and users are able to delete the image if they wish | Yes |

## Feature Showcase 
  
**Header/Navigation & Footer**

*For features showcase, screenshots of the features in use were taken on Laptop/iPad Pro/iPhone 12 Pro*

<details open>
    <summary>Header & Navigation - All Users (Profile Icon only visible to Registered, Logged-In Users)</summary>  
    <img src="">  
</details>

![Profile Icon](documentation/final_views/profileicon_nav.png)  
*Registered, Logged In view with Profile Icon*  
  
As mentioned in the [Structural Plane](#structural-plane) section above, the icon navigation bar allows the user to make their way around the Scales & Tails site. The icons have a small amount of animation when hovered/clicked on and to reinforce the icon meaning, have tooltips on hover/touch (on mobile) that display their intention.
  


<details open>
    <summary>Footer - Visible to all Users</summary>  
    <img src="">  
</details>



**Home Page**

<details open>
    <summary>Home Page - Visible to all Users</summary>  
    <img src="">  
</details>

In the Home Page 'Hero' section, when a user is not registered they will see a 'Sign Up' button under the section text, which will bring them to the Sign Up page. When logged in, they will see 'Book Today!' which will bring them to the booking page.


**About Page**

<details>
    <summary>About Page - Visible to all Users</summary>  
    <img src="">  
</details>  


The 'About' section of the Home Page contains three sections of information for the user, 'About', 'Safety', 'Benefits'. These sections display paragraphs and bulleted lists of information about the park and its positive values and benefits. Within each paragraph is a colour-coded word which acts as a link to bring the user to an important section of the website.

![Paragraph link]()  
*'visit' provides a link to the Visit Us page as the user reads through the park's information*

<hr>

**Registration/SignUp**

<details open>
    <summary>Sign Up Page</summary>  
    <img src="">  
</details>
  
Users are required to add their Email, Username and Password twice, to ensure the correct one is saved. If any field is not filled in appropriately then a display message is used to inform the user with how to procede to complete the form. The Sign up and Sign in pages are created with default templates available with the AllAuth package. These templates are combined with the power of Bootstraps Crispy Forms pack to give extra control over the forms' appearance.

**Sign In**

<details open>
    <summary>Sign In Page</summary>  
    <img src="">  
</details>

On successful Sign In, the user is greeted with feedback through a message which confirms sign in. The 'open padlock' Log In icon now changes to a 'closed padlock' Log Out icon that the user can click to begin the Log Out process. A 'Forgot Password' page is also re-designed from the AllAuth templates but it's full functionality is not yet activated for this version.

![incorrect username/email warning]()  
*User is given feedback if they submit incorrect details where one item is correct and the other is incorrect*  


![fill out field warning]()  
*Django built in field warnings for incorrect/forgotten fields input*  


![Sign In message and Log In icon change]()  
*Sign In message and Log In icon change*


**Sign Out**

<details open>
    <summary>Sign Out Page</summary>  
    <img src="">  
</details>
  
A user may choose to return to the Home page and stay logged in or leave the site, logged out.

![sign out message]()  
*User is given feedback in message format to confirm sign out, Profile icon no longer visible in navigation bar - message disappears after 3 seconds or if user clicks 'x'*  

<hr>

**Profile**

<details open>
    <summary>Profile Page - Registered Users only</summary>  
    <img src="">  
</details>
  
The user profile is created upon registration and displays a placeholder image and 'Edit Profile' button to allow the user to personalise their view. With future releases this page will be accessible to other users and allow connection, currently it is only viewable to the user.
  
<details>
    <summary>Profile Page - Placeholder image for Profile</summary>  
    <img src="">  
</details>
  
  
**Profile Edit**

<details>
    <summary>Edit Profile Modal</summary>  
    <img src="">  
</details>

Modal appears over the Profile page and allows users to edit their Profile Picture, Display Name (Display Name will be required for the future features of leaving Feedback/Reviews, Adding Friends and Direct Messaging) and Bio. Using the RichTextField input field, user's have more control of the formatting of their text if they wish.

<hr>

**Articles**

<details open>
    <summary>Articles Page - Unregistered User View (mobile/tablet), Registered User View with 'Add Article' icon (desktop)</summary>  
    <img src="">  
</details>

<details>
    <summary>Read Article Page - Unregistered User View</summary>  
    <img src="">  
</details>  
  
Unregistered Users have access to all posts available on Scales & Tails. When registered and logged in, they may access the 'Add Post' button, 'Like/Unlike' icon and leave a comment for Admin approval. Articles created are displayed on individual 'cards' which display in rows for larger screens and columns for portrait, mobile view.

![site pagination arrow for moving page every 6 articles]()  
*Site pagination kicks in to display 6 articles per page. Arrows at the base of the article section allow users to move forward and back*  


Unregistered Users are free to read the articles and comments left on Scales & Tails but they cannot 'Like/Comment' them until they have signed up and logged in.

![like/comment count under article]()  
*A Likes and Comments counter is visible under every article. Logged-In Users can interact by clicking the heart outline to like. 'Heart outline' icon is replaced by filled Heart icon*  


![zero likes icon]()  
*Likes icon is represented by an outlined heart icon. When it receives a like from the logged-in user, it becomes a filled heart icon*  
  

<details open>
    <summary>Add a Comment - Registered User View</summary>  
    <img src="">  
</details>

A comment box is visible to logged-in users only. Their comment is submitted for review by the Admin, once approved, the comment appears on the website.

![comment awaiting approval message]()  
*Comment is awaiting approval message displayed after comment submit*
  

<details>
    <summary>Delete Comment - Registered User View for Comment Author only</summary>  
    <img src="">  
</details>

For the author of the comment, when logged in, a trash icon will appear to allow them to delete the comment if they wish. 


**Create Article**

<details open>
    <summary>Create Article Page - Registered, Logged In User View</summary>  
    <img src="">  
</details>  
  
The user may create an article and include their own image or allow a placeholder image. Feedback is given to the user to guide them if they do not fill out the required sections appropriately. The Submit button saves the article for Admin approval. Once approved, the article will appear on the main page.  
  

<details>
    <summary>Placeholder image for Articles - credit: Pattern Monster with Scales & Tails purple</summary>  
    <img src="">  
</details>


![feedback that article is awaiting spproval by Admin]()  
*Admin approval is required for articles to keep Scales & Tails on topic. Feedback is provided to the user by message that the article is awaiting approval*


**Edit Article**

<details open>
    <summary>Edit Article Page - Registered, Logged In User View - Article Author View - Edit/Delete Icon</summary>  
    <img src="">  
</details>

<details>
    <summary>Edit Article Page - Only accessible to the Article Author</summary>  
    <img src="">  
</details>
  
If a user spots a typo, error or wants to add new information to their article, then they may edit the article and submit for immediate reposting. A certain amount of trust exists between Admin and the Scales & Tails community to hope that no inappropriate or off-topic content will be shared, which will result in an immediate deletion of the user's account by the Admin. These issues will be locked down in the future development of Scales & Tails to allow certain content/words to be flagged and removed by the Admin or not allow the form to be submitted in the first place. Community guidelines will also be developed.

<details>
    <summary>Edit Article Message</summary>  
    <img src="">  
</details>


**Delete Article**

<details>
    <summary>Delete Article Page - Only accessible to the Article Author </summary>  
    <img src="">  
</details>

![delete article successful message]()  
*User is informed that their article has been deleted - message disappears after 3 seconds*


**Search Function**

<details open>
    <summary>Search Function - Visible on Article pages only</summary>  
    <img src="">  
</details>  
  
A user may search for something particular using the 'Search' field, which only appears on article related pages. If the search yields no results then the user is informed and provided with a link back to the articles.

<details>
    <summary>Search Function No Articles Found - Visible on Article pages only</summary>  
    <img src="">  
</details>

<hr>

**Bookings**

<details open>
    <summary>Bookings Page - Registered, logged-in Users only</summary>  
    <img src="">  
</details>
  
The booking system that has been created for Scales & Tails is a basic booking system that 'gets the job done' for the starting business. The user may create, edit and delete their bookings, they are informed if a date/time is unavailable and they see a display message if their booking is saved. For future development, the UI of this booking system will improve to make unavailable times shaded-out/hidden and the user will receive confirmation emails for all bookings saved. Only 4 bookings may be held for each user and currently this includes past bookings, which the user must delete themselves. This is to remind the user of all bookings incase they may have forgotten and not attended their booked time slot, making it unavailable for someone else. In the future booking feature, the user will receive an email informing them that they have missed a booking, the booking will be flagged with a red text message on the dashboard and the user will be reminded that repeated no-shows for bookings will have their access to bookings revoked for a period of time.

<details>
    <summary>Bookings Page - Max Bookings Reached</summary>  
    <img src="">  
</details>


**Booking Create**

<details open>
    <summary>Booking Create Page - Visible only to Logged-In Users</summary>  
    <img src="documentation/final_views/booking_c.png">  
</details>  
  
For creating a booking, the user is informed of the necessary fields to be filled in to secure the booking via feedback. The user may add a second dog if they wish, or leave this to another time. A dropdown selection of 'Breed Choices' is made available for quicker booking, with 'Other' included for mixed breeds. This information is important to the Scales & Tails staff member who maybe operating the gate for allowing entry. The dog's appearance will help them to identify and confirm the booking along with the human user information.
Date and time is selectable via a calendar widget for date and dropdown selection menu displaying the hour slots from 8am to 8pm. Scales & Tails is super kind and opens every single day of the year for it's community members.

![past booking warning]()  
*Warning shown to Users if they choose a date in the past, can only save a booking with a valid date/time*  
 
  
![unavaialable date/time]()  
*If a date/time combo is unavailable then the user is informed via warning message - future version of the booking system will have shaded out portions for the unavailable dates/times to make it easier on the user*  


![booking saved message]()  
*User feedback is delivered by message once a booking has been submitted through creation or edit- message disappears after 3 seconds*


**Edit Booking**

<details>
    <summary>Edit Booking Page - Visible for Logged-In Users who have made a previous Booking</summary>  
    <img src="">  
</details>

**Delete Booking**

<details>
    <summary>Delete Booking Page - Visible for Logged-In Users who have made a previous Booking</summary>  
    <img src="">  
</details>
  
A user may delete thier booking or return to the booking page incase they clicked the delete icon in error.

![deleted booking message]()  
*User feedback is delivered by message once a booking has been deleted - message dissappears after 3 seconds*

<hr>

**Gallery**

<details open>
    <summary>Gallery Page - Registered, Logged-In User View with 'Add Photo' icon, Unregistered User View without icon</summary>  
    <img src="">  
</details>
  
The Scales & Tails Gallery page allows the user and Admin to quickly upload snapshots from the park's activities to create a continuous flow of updated images. An overlay on hover/touch on mobile shows the user brief information about the photograph. The carousel of images at the top of the page shows some highlighted photos. For future development this carousel will display a collection of randomly selected images from the bulk of images availabale and stored in the Cloudinary database.    

<details>
    <summary>Gallery Page - Unregistered User view with photo info on hover(Desktop)/touch (on Mobile)</summary>  
    <img src="">  
</details>

**Add Photo**

<details open>
    <summary>Add Photo Page - Registered Users only</summary>  
    <img src="">  
</details>
  
All fields are required for the Upload Image form to be submitted and saved correctly. Feedback prompts the user if they have neglected a field.

**Delete Photo**

<details open>
    <summary>Photo Delete - Registered User View - delete icon only visible over the photos uploaded by that logged-in user. </summary>  
    <img src="">  
</details>

<details>
    <summary>Delete Photo Page</summary>  
    <img src="">  
</details>
  
If a user no longer wants their image to appear, or if they have made a mistake, thay may delete their image. Admin approval is not needed for images to be posted and future development will include community posting guidelines and a form of AI software to check the image for any unwanted content.  
   
![delete photo user message, successful deletion]()  
*User feedback is provided by message, informing user that the photo has been deleted successfully - message disappears after 3 seconds*

<hr>

**Visit Us**

<details>
    <summary>Visit Us Page</summary>  
    <img src="">  
</details>
  
This page offers the user business information including opening hours and address. An embedded interactive Google Map allows the user to see Scales & Tails's location without leaving the site. If they require driving directions to the park, they can click on the map's 'View larger map' link to go to Google Maps in a new browser tab.

For future development, this page will hold the 'Feedback' feature for registered users to leave a review of the park. 

<hr>

**403, 404, 500 Pages**

These templates were added to this project in order to give the user the functionality to return to the website by using the links in the navigation bar or the Back to Homepage button on the Error page.

![404 error page]()

- They are triggered when a user tries to access:
  - information that is not theirs - 403,
  - information that does not exist anymore - 404,
  - something has gone wrong with the server and cannot retrieve database - 500

**Admin Panel**

Through Django's built-in Administration Panel, the Admin has full access over the data submitted to the website by registered Users. To access the Admin panel the Admin user adds '/admin/' to the end of the URL to display [](). A username and password is requested. For Scales & Tails, Admin approval is needed for articles and comments to keep the site on topic and to prevent spamming. Registered, logged-in users' have instant access to make a booking and upload images.

![django admin panel view]()  
*Django Admin panel view for Scales & Tails Administrator - content selection menu on left hand side*  


Users articles and comments require approval by the Admin of Scales & Tails to keep the website content on topic. Admin can change the status of articles from 'Draft' to 'Published'.

<details>
    <summary>Dropdown menu allowing Admin to 'publish' a users article, 'Save' button must be clicked to confirm</summary>  
    <img src="">  
</details>  

  
<details>
    <summary>Dropdown menu allowing Admin to 'approve' a users comment, 'Go' must be clicked to confirm</summary>  
    <img src="">  
</details>
    

Admin can control users bookings via the Django Admin panel.  

<details>
    <summary>All bookings are made available to the Admin</summary>  
    <img src="">  
</details>


## Future Features

- 
# Technologies & Languages Used

- HTML
- CSS
- JavaScript
- Python
- [Github](https://www.github.com) used for online storage of codebase and Projects tool.
- [Figma](https://www.figma.com) for project design planning and wireframe creation.
- [Adobe Color](https://color.adobe.com) for colour theme creation and accessibility checkers.
- [Django](https://www.djangoproject.com/) was used as the Python framework for the site.
- [Cloudinary](https://cloudinary.com/) was used for cloud media storage of user uploaded images.
- [ElephantSQL](https://www.elephantsql.com/) was used to host the PostgreSQL database needed to collect and recall the users data.
- [Heroku](https://www.heroku.com) was used to host the Scales & Tails application.
- [WAVE](https://wave.webaim.org/) to evaluate the accessibility of the site.
- [Procreate](https://procreate.com/) for image creation and editing.

## Libraries & Frameworks

- Bootstrap v5.2.3
- Django v3.2.19
- Django AllAuth v0.54.0
- Django Crispy Forms v2.0
- Crispy Bootstrap5 v0.7
- Django Resized v1.0.2
- Django RichTextField v1.6.1
- Django Summernote v0.8.2
- Python Slugify v8.0.1
- Pillow v9.5
  
Further information is available in the [requirements.txt file]()

## Tools & Programs

- [EZGif](<https://ezgif.com/>) for gif conversion.
- [Convertio](https://convertio.co/) for file conversion to PNG, WEBP.
- [Tiny Png](https://tinypng.com/) for file size reduction.
- [Lucidchart](https://www.lucidchart.com/pages) for ERD (entity relationship diagram) creation.
- [Trello](https://www.trello.com) for intial project agile planning.
- [Perplexity AI](https://www.perplexity.ai/) for breaking down Python concepts and Django documentation into more understandable chunks.
- [Pattern Monster](https://pattern.monster/) for the hero image pattern SVG.
- [Favicon](https://favicon.io/) for converting an icon into favicon.
- [LogoAI](https://www.logoai.com/) for design inspiration using my font and colour choices.

# Testing

- For all testing, please refer to the [TESTING.md]() file.

# Deployment
  
## Connecting to GitHub  

To begin this project from scratch, you must first create a new GitHub repository using the [Code Institute's Template](https://github.com/Code-Institute-Org/ci-full-template). This template provides the relevant tools to get you started. To use this template:

1. Log in to [GitHub](https://github.com/) or create a new account.
2. Navigate to the above CI Full Template.
3. Click '**Use this template**' -> '**Create a new repository**'.
4. Choose a new repository name and click '**Create repository from template**'.
5. In your new repository space, click the purple CodeAnywhere (if this is your IDE of choice) button to generate a new workspace.

## Django Project Setup

1. Install Django and supporting libraries: 
   
- ```pip3 install 'django<4' gunicorn```
- ```pip3 install dj_database_url psycopg2```
- ```pip3 install dj3-cloudinary-storage```  
  
2. Once you have installed any relevant dependencies or libraries, such as the ones listed above, it is important to create a **requirements.txt** file and add all installed libraries to it with the ```pip3 freeze --local > requirements.txt``` command in the terminal.  
3. Create a new Django project in the terminal ```django-admin startproject Scales & Tails .```
4. Create a new app eg. ```python3 mangage.py startapp ```
5. Add this to list of **INSTALLED_APPS** in **settings.py** - '',
6. Create a superuser for the project to allow Admin access and enter credentials: ```python3 manage.py createsuperuser```
7. Migrate the changes with commands: ```python3 manage.py migrate```
8. An **env.py** file must be created to store all protected data such as the **DATABASE_URL** and **SECRET_KEY**. These may be called upon in your project's **settings.py** file along with your Database configurations. The **env.py** file must be added to your **gitignore** file so that your important, protected information is not pushed to public viewing on GitHub. For adding to **env.py**:

- ```import os```
- ```os.environ["DATABASE_URL"]="<copiedURLfromElephantSQL>"```
- ```os.environ["SECRET_KEY"]="my_super^secret@key"```
  
For adding to **settings.py**:

- ```import os```
- ```import dj_database_url```
- ```if os.path.exists("env.py"):```
- ```import env```
- ```SECRET_KEY = os.environ.get('SECRET_KEY')``` (actual key hidden within env.py)  

9. Replace **DATABASES** with:

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
```

10. Set up the templates directory in **settings.py**:
- Under ``BASE_DIR`` enter ``TEMPLATES_DIR = os.path.join(BASE_DIR, ‘templates’)``
- Update ``TEMPLATES = 'DIRS': [TEMPLATES_DIR]`` with:

```
os.path.join(BASE_DIR, 'templates'),
os.path.join(BASE_DIR, 'templates', 'allauth')
```

- Create the media, static and templates directories in top level of project file in IDE workspace.

11. A **Procfile** must be created within the project repo for Heroku deployment with the following placed within it: ```web: gunicorn *******.wsgi```
12. Make the necessary migrations again.

## Cloudinary API 

Cloudinary provides a cloud hosting solution for media storage. All users uploaded images in the FreeFid project are hosted here.

Set up a new account at [Cloudinary](https://cloudinary.com/) and add your Cloudinary API environment variable to your **env.py** and Heroku Config Vars.
In your project workspace: 

- Add Cloudinary libraries to INSTALLED_APPS in settings.py 
- In the order: 
```
   'cloudinary_storage',  
   'django.contrib.staticfiles',  
   'cloudinary',
```
- Add to **env.py** and link up with **settings.py**: ```os.environ["CLOUDINARY_URL"]="cloudinary://...."``` 
- Set Cloudinary as storage for media and static files in settings.py:
- ```STATIC_URL = '/static/'```
```
  STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'  
  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]  
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')‌  
  MEDIA_URL = '/media/'  
  DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

## Elephant SQL

A new database instance can be created on [Elephant SQL](https://www.elephantsql.com/) for your project. 

- Choose a name and select the **Tiny Turtle** plan, which is free.
- Select your Region and the nearest Data Center to you. 
- From your user dashboard, retrieve the important 'postgres://....' value. Place the value within your **DATABASE_URL**  in your **env.py** file and follow the below instructions to place it in your Heroku Config Vars.


## Heroku deployment

To start the deployment process , please follow the below steps:

1. Log in to [Heroku](https://id.heroku.com/login) or create an account if you are a new user.
2. Once logged in, in the Heroku Dashboard, navigate to the '**New**' button in the top, right corner, and select '**Create New App**'.
3. Enter an app name and choose your region. Click '**Create App**'. 
4. In the Deploy tab, click on the '**Settings**', reach the '**Config Vars**' section and click on '**Reveal Config Vars**'. Here you will enter KEY:VALUE pairs for the app to run successfully. The KEY:VALUE pairs that you will need are your: 
   
   - **CLOUDINARY_URL**: **cloudinary://....** 
   - **DATABASE_URL**:**postgres://...** 
   - **DISABLE_COLLECTSTATIC** of value '1' (N.B Remove this Config Var before deployment),
   -  **PORT**:**8000**
   -  **SECRET_KEY** and value  
  
5. Add the Heroku host name into **ALLOWED_HOSTS** in your projects **settings.py file** -> ```['herokuappname', ‘localhost’, ‘8000 port url’].```
6. Once you are sure that you have set up the required files including your requirements.txt and Procfile, you have ensured that **DEBUG=False**, save your project, add the files, commit for initial deployment and push the data to GitHub.
7. Go to the '**Deploy**' tab and choose GitHub as the Deployment method.
8. Search for the repository name, select the branch that you would like to build from, and connect it via the '**Connect**' button.
9.  Choose from '**Automatic**' or '**Manual**' deployment options, I chose the 'Manual' deployment method. Click '**Deploy Branch**'.
10. Once the waiting period for the app to build has finished, click the '**View**' link to bring you to your newly deployed site. If you receive any errors, Heroku will display a reason in the app build log for you to investigate. **DISABLE_COLLECTSTATIC**  may be removed from the Config Vars once you have saved and pushed an image within your project, as can **PORT:8000**.

## Clone project

A local clone of this repository can be made on GitHub. Please follow the below steps:

1. Navigate to GitHub and log in.
2. The [Scales & Tails Repository]() can be found at this location.
3. Above the repository file section, locate the '**Code**' button.
4. Click on this button and choose your clone method from HTTPS, SSH or GitHub CLI, copy the URL to your clipboard by clicking the '**Copy**' button.
5. Open your Git Bash Terminal.
6. Change the current working directory to the location you want the cloned directory to be made.
7. Type `git clone` and paste in the copied URL from step 4.
8. Press '**Enter**' for the local clone to be created.
9. Using the ``pip3 install -r requirements.txt`` command, the dependencies and libraries needed for Scales & Tails will be installed.
10. Set up your **env.py** file and from the above steps for Cloudinary and ElephantSQL, gather the Cloudinary API key and the Elephant SQL url for additon to your code.
11. Ensure that your **env.py** file is placed in your **.gitignore** file and follow the remaining steps in the above Django Project Setup section before pushing your code to GitHub.

## Fork Project

A copy of the original repository can be made through GitHub. Please follow the below steps to fork this repository:  

1. Navigate to GitHub and log in.  
2. Once logged in, navigate to this repository using this link [Scales & Tails Repository]().
3. Above the repository file section and to the top, right of the page is the '**Fork**' button, click on this to make a fork of this repository.
4. You should now have access to a forked copy of this repository in your Github account.
5. Follow the above Django Project Steps if you wish to work on the project.

# Credits

## Code

The following blogs/tutorials complemented my learning for this project, alongside the [Code Institute's](https://codeinstitute.net/ie/) Learning Content.

- [Django Docs](https://www.djangoproject.com/)
- [Bootstrap Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Code Institute's](https://github.com/Code-Institute-Org>) Blog/Boutique Ado walkthroughs
- [Django save method](https://docs.djangoproject.com/en/4.2/ref/models/instances/) in models.py  
- [Django UserCreationForm](https://www.javatpoint.com/django-usercreationform>) Creating New Users 
- [Advanced User Profile creation using allauth/signals](<https://dev.to/thepylot/create-advanced-user-sign-up-view-in-django-step-by-step-k9m)
- [Override Django's save method](https://www.sankalpjonna.com/learn-django/how-to-override-the-save-method-in-your-django-models)
- TypeError Datetime object issue for same day bookings - [#1](https://bobbyhadz.com/blog/python-check-if-variable-is-datetime-object)
                                                      - [#2](https://bobbyhadz.com/blog/python-typeerror-datetime-datetime-object-is-not-callable#:~:text=The%20Python%20%22TypeError%3A%20'datetime,and%20the%20built%2Din%20classes.)
- Find the [parent form element](https://www.geeksforgeeks.org/difference-between-dom-parentnode-and-parentelement-in-javascript/) of delete confirm button
- [Scrollbar styling](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_custom_scrollbar2)
- [Browser autofill styling overrule](https://stackoverflow.com/questions/2338102/override-browser-form-filling-and-input-highlighting-with-html-css)
- [Django Docs](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.readonly_fields) to make model item readonly for search function showing deleted articles
- [Django cleaned data how to](https://overiq.com/django-1-10/django-form-basics/?utm_content=cmp-true)

## Media

The following sites were used to gather the photographic media used in Scales & Tails:

- [Pexels](https://www.pexels.com/)
- [Unsplash](https://unsplash.com/)
 <details>
   <summary>Credit to the following photographers</summary>
   
   -Photo by Ivan Rojas: https://www.pexels.com/photo/boa-serpiente-28290883/

 </details>

 Additional photos were added by users or from my own pets.

### Additional reading/tutorials/books/blogs

- [Python Crash Course](https://www.oreilly.com/library/view/python-crash-course/9781492071266/), Author: Eric Matthes, Publisher: No Starch Press, Year: 2019 Edition.
- [Geeks for Geeks](https://www.geeksforgeeks.org/python-programming-language/?ref=ghm) for additional Python learning.

## Acknowledgements


  
 
  
