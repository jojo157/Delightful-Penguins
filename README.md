# Leticias Art

## Introduction
Leticias Art is an ecommerce application for a sole artist to sell her work and interact in realtime with potential customers.  

View Live Website [here](https://leticiasart.herokuapp.com/)

![Leticias Art on different devices](media/readme/differentDevices.png)

Image created using [Am I responsive](http://ami.responsivedesign.is/)

## Table of Contents

- [UX](#ux)
  - [Strategy](#strategy)
    - [User Needs](#user-needs)
        - [As a site user](#as-a-site-user)
        - [As the business owner](#as-the-business-owner)
  - [Scope](#scope)
    - [Features](#features)
    - [Future Features](#future-features)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
    - [Wireframes](#wireframes)
    - [Database Design](#database-design)
  - [Surface](#surface)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
- [Testing](#testing)
    - [Code Validation](#code-validation)
        - [Html](#html)
          - []()
          - []()
          - []()
        - [CSS](#css)
        - [JavaScript](#javascript)
        - [Python](#python)
    - [Performance Testing](#performance-testing)
    - [User Stories Testing](#user-stories-testing)
      - [Site user](#site-user)
      - [Business owner](#business-owner)
    - [Functionality Testing](#functionality-testing)
    - [Validation Testing](#validation-testing)
    - [Access Testing](#access-testing) 
    - [CRUD Testing](#crud-testing)
    - [Compatibility Testing](#compatibility-testing)
        - [Different devices](#different-devices)
        - [Different Browsers](#different-browsers)
        - [Different Operating Systems](#different-operating-systems)
- [Technologies Used](#technologies-used)
    - [Frameworks and Libraries](#frameworks-and-libraries)
    - [Version Control](#version-control)
    - [Other Programs](#other-programs)
- [Deployment](#deployment)
  - [Run local](#run-local)
  - [Fork repository](#fork-repository)
- [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
    - [Acknowledgements](#acknowledgements)

## UX

The 5 planes of User Experience:

### Strategy
Leticias Art was created with the purpose of providing a platform for the Artist Leticia to advertise and sell her art pieces. 

#### User Needs

##### As a site user
- As a site user, I want to be able to browse the art that is available.
- As a site user, I want to be able to work out the total cost of a particular piece of art I am interested in. 
- As a site user, I want to be able to put through an order to buy the piece of art I like.
- As a site user, I want to be able to contact the artist with questions.
- As a site user, I want to save my order data for easy access. 

##### As the business owner
- As the business owner, I want to be able to advertise my current art pieces for sale.
- As the business owner, I want to be able to update my current art offering.
- As the business owner, I want to be able to add new art offerings.
- As the business owner, I want to be able to talk in real time with any potential customers that have entered the chat facility.
- As the business owner, I want to see a list of orders in date order.

### Scope

#### Features

The following features are in scope for this project.
- Register Functionality.
  - Validated form to allow user create a profile for accessing the application. 
- Login Functionality.
  - Validated form that checks the users stored details and logs user in only if a successful match. 
- Navigation Menu.
  - A navigation menu will be presented on all pages on application. 
- Responsive Design.
  - Application will be responsive on all device size and browsers.
- CRUD Functionality.
  - Application will enable the functionality to Create, Read, Update and Delete data.
- Database to store app data.
  - Postgres database will be used to store all application data.
- Realtime Chat facility
  - Contact chat facility on every page for realtime communication.
- Contact form
  - Contact form to enable user to send email to artist when artist offline. 
- Artist Add Art
  - Form to allow the artist to add a new piece of art to sell.
- Artist Edit Art
  - Form to amend an existing art piece.
- Turn on/off messaging functionality
 - A slider that changes functionality of chat window.
- My Orders
 - A page where logged in users will see their previous orders.
- Orders
 - A page for artist that will show all orders. 
- Detailed Art Page
 - A page that will show more data about an art piece.
- Cart
 - A user will be able to add an art piece to their cart.
- Checkout
 - A user will be able to checkout their order.
- Stripe payments
 - A user will be able to complete checkout with a card payments for their order total.
- 404 Error Page
  - A custom 404 error page if the user navigates to a resource that doesn't exist with a button to return home. 