
# ENGLISH GROWS
![image](https://github.com/user-attachments/assets/c79dd927-349c-4739-8204-a0a7df15a9ae)


## Overview
This site is an e-commerce that sells services. The services provided are the following:
- Live online lessons for B2B and B2C customers:
  * Individual Lesson Packs
  * Reduced Groups

## Live Site
- You can view the deployed site on Heroku [here](https://english-grows-477471d17e50.herokuapp.com/)

## Repository
- You can check the Github repository [here](https://github.com/Ethra8/english-grows)

## Author
EDNA TORRES MUNILL


# TABLE OF CONTENTS
  
- [PROJECT OVERVIEW](#project-overview)  
    * [Live Site](#live-site)  
    * [Repository](#repository)  
    * [Author](#author)
- [UX](#ux)
    * [Target Audience](#target-audience)
    * [Project Goals](#project-goal)
    * [User Stories](#user-stories)
    * [User Profiles](#user-profiles)
 - [AGILE DEVELOPMENT](#agile-development)
 - [DESIGN CHOICES](#design-choices)
 - [FEATURES](#features)
    * [Navbar](#navbar)
    * [User Authentication](#user-authentication)
    * [Contact Form](#contact-form)
    * [Service Sorting](#service-sorting)
    * [Search Bar](#search-bar)
    * [Shopping Bag](#shopping-bag)
    * [Online Payments - Stripe API](#online-payments---stripe)
    * [404 Error Page](#404-error-page)
    * [SEO](#seo)
    * [Admin Console](#admin-console)
 - [TESTING](#testing)
   * [Defect Tracking](#defect-tracking)
     - [Github Issues](#github-issues)
     - [Defects of Note](#defects-of-note)
     - [Outstanding Defects](#outstanding-defects)
   * [Core Web Vitals](#core-web-vitals)
     - [Lighthouse Reports](#lighthouse-reports)
   * [Accessibility](#accessibility)
     - [Contrast Validation Reports](#contrast-validation-reports)
     - [General WCAG 2.1 Report](#general-wcag-2.1-report)
   * [Manual Testing](#manual-testing)
- [TECHNOLOGIES USED](#technologies-used)
   * [Languages](#languages)
   * [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
 -[CREDITS & ACKNOWEDGEMENTS](#credits-and-acknowledgements)



# UX
You will find in the points stated below a brief study aiming at providing the user with the best possible experience when visiting this site. 
## Target Audience
### B2B
Any company interested in improving their employees' level of English for one of the following reasons:
* Wants to compete in the international market
* Locally works with international customers

### B2C  
Any individual person wanting to improve their level of English tfor one of the following reasons:  
* Travel
* Careers
* University Students (e.g: Students must certify a B2 level of English to apply to the Erasmus program)
  
## Project Goal
  1. The site aims at providing B2B and B2C users with services they can buy: live online lessons in individual or reduced groups format.
  2. All users can register for an account.
  3. B2B users can send a contact form to receive customized offers on the type of service desired.
  4. B2C services available can be stored in a shopping bag and bought online through Stripe API.
  5. All users can subscribe to the monthly newsletter.
  6. Members of the monthly newsletter are informed of interesting cultural events, and social and historic facts related to the British culture, and English speaking countries around the world.

  
## USER STORIES
  
### As a first-time visitor 
#### B2C and B2B
1. [ ] MUST HAVE: I want to check the social media links to see the website profile, to look at photos from past events, and maybe follow.
2. [ ] COULD HAVE: I want to check a FAQS section to find relevant information on the services provided, benefits to creating an account (e.g.: free on-demmand material, newsletter), etc.
  
#### B2C
3. [X] MUST HAVE: I want to check all the services available.
4. [X] MUST HAVE: I want to sort the services by categories, or by price, and also be able to view only one specific category of services.
   
#### B2B
5. [X] MUST HAVE: I want to contact the site to receive a customized training plan and quote.
   
### As a Returning Visitor
6. [ ] COULD HAVE: I want to subscribe to the newsletter to be informed about special offers, new courses or features.
7. [X] I want to be able to easily register for an account, and receive an email confirmation after registering, so that I can verify that my account registration was successful.

### As an Authenticated User  
8. [X] I want to be able to easily login and logout, so that I can access my personal account information.
9. [X] I want to be able to easily recover my password in case I forget it, so that I can recover access to my ccount.
10. [ ] MUST HAVE: I want to be able to have a personalized user profile, so that I can view my personal order history and order confirmations.
11. [ ] MUST HAVE: I want to be able to update and save my billing information on my user profile.
  
#### Viewing and Navigation
* [ ] I want to view a list of services, so that I can easily choose what service suits me best.
* [ ] I want to be able to view specific type of service, so that I can quickly find services I'm interested in whitout having to go through all the services (e.g.: only ocmpany or individuals' services)
* [ ] I want to be able to view individual service details, so that I can identify the price and description.
* [ ] I want to be able to easily view the total of my purchase at any time, so that I can avoid spending too much.
    
#### Sorting and Searching
* [ ] I want to sort the list of available services, so that I can easily identify the best priced and sorted by types.
* [ ] I want to sort a specific type of service, so that I can find the best-priced services in a specific type.
* [ ] I want to sort multiple types of services simultaneously, so that I can find the best-priced services across broad types, such as 'individual' or 'reduced groups'.

  
### AGILE DEVELOPMENT
As part of the Agile development method, user stories have been created and implemented one at a time. Future features will be created following the *'Could Have'* and *'Won't Have/Wish'* labels on the [stories](#user).
[Kanba Project](https://github.com/users/Ethra8/projects/7)


# DESIGN CHOICES
The design of this site is thought to inspire professionality, trust, and the dark tones of blues provide foster a state of relaxation, of wellbeeing. Thi is the palette used, contrasting with white font:

![English Grows color palette](https://github.com/user-attachments/assets/e4736fe3-98b4-4a52-9692-04e88e3bf1f9)


# FEATURES

## Navbar
There are two navigation bars and both are responsive:
- The first, ***topnav*** has a dark blue ***#003366*** color, and is fixed on top of every single page of the site. It has three icons with links: logo(to home), user, bag.
- The second nav is on the individual services page, accessed through "For You" button on the home page. It has a search bar to search to seach whithin all the services for specific words.

https://github.com/user-attachments/assets/71ea8143-fb09-4948-8eb5-bf2eeeb86a10  

## User Authentication

 ![image](https://github.com/user-attachments/assets/90ed2427-bbf5-4117-bf76-0ca0f0859436)  

 ![image](https://github.com/user-attachments/assets/0324af75-5a15-4b25-bd67-de054fe30373)  

 ![image](https://github.com/user-attachments/assets/cbbcab9d-a5f5-4bdb-8c66-0e01795f29e5)  

 ![image](https://github.com/user-attachments/assets/19f04349-82f4-4bbe-b33e-f674599d5a9e)  

 ![image](https://github.com/user-attachments/assets/c654fa7b-8e72-4d86-9eef-f7ebfb2d6bdb)  

 ![image](https://github.com/user-attachments/assets/eafc5285-6a9e-45d7-975a-5d61768fa0a5)  

 ![image](https://github.com/user-attachments/assets/ed6abc95-9488-4eaa-958d-a5305101eefd)  

 ![image](https://github.com/user-attachments/assets/42bf8fa0-b1b4-479d-b47e-b05a3afac143)  

 https://github.com/user-attachments/assets/a05ad833-22d2-4918-af9c-399ab638847e

## Contact Form

https://github.com/user-attachments/assets/148b0e3d-b0d0-4f58-9eed-d86b26624faa  

## Product Sorting

https://github.com/user-attachments/assets/bafbf9ec-4e4d-4802-9856-65bd3ae02a98  

##Search Bar
The search bar is on the ***for you*** service page:


## Shopping Bag
Whithin the shopping bag, users can update quantity of service packs to buy, and eliminate any service from the bag as well. The subtototal is updated too depending on the quantity of each item. Then the user can check out, or return to services. Please refer to the follwoing videos and screen captures to see all these features in action.
https://github.com/user-attachments/assets/c5d745df-9c5d-490b-afe4-098bc30c4d05  

![image](https://github.com/user-attachments/assets/33e28d23-3d08-4886-b6e8-9658dde6d3b5)  

![image](https://github.com/user-attachments/assets/9c2d5574-e4e5-4a82-b32e-741e31c64035)  

https://github.com/user-attachments/assets/75625e41-44d3-4b62-b630-76f3f1d1a89a


## Online Payments - STRIPE API  
  ![image](https://github.com/user-attachments/assets/cc65c560-fec2-431c-8a76-39c68e2e3694)  

  ![image](https://github.com/user-attachments/assets/8697aa36-0ae5-4dd3-a9bd-18b5e21c3301)


## 404 Error Page
 ![image](https://github.com/user-attachments/assets/438748da-fb3f-4c70-8655-7fc0874ac368)

## SEO
The lighthouse web report (displayed in the ***Testing*** section below) passed the SEO at 100. I have included the following meta tags and info:  
```$python
<meta name="theme-color" content="teal">
<meta name="description" content="English Grows is a site that offers English teaching services online to B2B and B2C customers, offering     
   individual lesson packs and reduced group formats">
<meta name="keywords" content="English, teaching, learning, learn, lessons, tutor, teacher, education, private, groups, online groups, e-  
   learning, corporate, reduced, live">
<meta name="author" content="Edna Torres Munill">
```

## Admin Console
The admin console reflects most of the models present in this site, and features from django-allauth. The models are detailed in a section below, and the allauth are as follows:  
- ![image](https://github.com/user-attachments/assets/e291b79f-118a-4056-ae2d-e5ee263cc1b6)
- EMAILS
  * This is taken from django-allauth, and stores the emails of the registered users in the admin for future emailing campaigns, and to send the users the free monthly newsletter.
- AUTHENTICATION AND AUTHORIZATION
  * These also come from django-allauth, and is used to give certain permissions to users, to verify them manually, update information, or delete them.
 
# STRUCTURE & 
The site has been built using Django 5.1 in Python 3.12, and has the following structure:
- The site contains four ***django apps*** (bag, checkout, home, individual_services) with several models.
- You can check the code for further detail, and check the ***requirements.txt*** to know all the modules and their correspondent versions.

# TESTING  
## DEFECT TRACKING

### GITHUB ISSUES
All issues have been solved, and closed in Github by the creator of this site.
## DEFECTS OF NOTE
No defects of note have been detencted on this site.
## OUTSTANDING DEFECTS
No outstanding defects have been detected in this site.

## GENERAL PERFORMANCE
The following tests have been run for this project:  
## Lighthouse Report  
**To improve my first report, the following actions have been taken:**  
- Include a ***site.manifest***

### Tablet & Mobile Device

 ![image](https://github.com/user-attachments/assets/472387ec-a029-4864-9620-fb502980a630)  

### Laptop and Desktop
 
 ![image](https://github.com/user-attachments/assets/007e1868-8a11-42d0-9cdf-0ec96034c779)  

## CODE
## CSS
No critical errors were found whe passing the [W3C validator](https://jigsaw.w3.org/css-validator/)  
 
 ![image](https://github.com/user-attachments/assets/4b7cae97-029b-4268-8734-c5c9bb8dc913)  

## JS ES6
No critical errors were found whe passing the validator [JShint](http://www.jshint.com)  
- **checkout/static/checkout/js/stripe_elementss.js** :  
  ![image](https://github.com/user-attachments/assets/08cc8fd3-6fad-4f7c-993e-fa3ab76f9be9)

- **static/js/quantity_selector.js** :
  ![image](https://github.com/user-attachments/assets/f67fed89-1d45-4f2e-a343-4f05fb732e02)
  
  
   
## ACCESSIBILITY
This site has been tested to be ADA compliant, and has achieved **WCAG 2.1 validation**. Find below the contrast audits from ***Juicy Studio*** website and the general accessibility reports generated by ***EqualWeb Accessibility Checker*** Chrome extension, which have all achieved positive results. 

### CONTRAST VALIDATION REPORTS
Font and backgroud colors have passed at level AAA. The following reports have been generated by [Juicy Studio](https://juicystudio.com/services/luminositycontrastratio.php)

![image](https://github.com/user-attachments/assets/4d7ec2f4-1ef4-4814-b928-761bf5f6d374) ![image](https://github.com/user-attachments/assets/0502fbeb-d05e-4e57-843e-e883d2786fce)


### GENERAL WCAG 2.1 REPORT
This website is compliant with all international standards, as proved after ***EqualWeb Accessibility Checker*** scan of the site.  

 ![image](https://github.com/user-attachments/assets/64965aba-bc48-466c-9533-a345275bdc0c) ![image](https://github.com/user-attachments/assets/88ca69be-deb3-4f2d-9480-8416cf898756)


## MANUAL TESTING
### USER ACCOUNT
1. Registration process completed:
   * Form is posted to the databse reflected in the admin, as user is created.
   * User receives verification email  
     
     ![image](https://github.com/user-attachments/assets/e7016d88-602c-4bd8-91ff-a9abdabd497d)  

   * Verification url works as expected
    
     
  
   * Once user clicks on 'verify', he is redirected to home page, already logged in.
1. Password Reset / forgotten
   * After user clicks on 'forgotten password", user inputs the account email and confirmation message is displayed:
     
     ![image](https://github.com/user-attachments/assets/9ac13d2f-4dd1-4e00-abf6-a24ee0bd1445)
     
   * User receives an email with link to restore password.
     
     ![image](https://github.com/user-attachments/assets/cfdf883c-a180-4d89-8c4a-73d176b7dcc4)
     
     
# TECHNOLOGIES USED

## LANGUAGES
- **Python 3.12**
- **JS ES6**
- **CSS3**
- **HTML5**

## FRAMEWORKS, LIBRARIES AND PROGRAMS USED

- The following have been used:
  - **Django 5.1** - Whithin django framework, many libraries and modules have been used. For mode details on the libraies and modules, refer to *requirements.py* on the root directory.
  - Chrome Dev Tools - To inspect the elements, and be able to spot what element was having an unexpected behaviour, and correct it more efficiently. Also have used **_Lighthouse_** reports to check and improve core web vitals, including accessibility issues.
  - [Remove.bg](https://www.remove.bg/) to remove background from logo image.
  - [Favicon](https://favicon.io/) - To create the logo, and the icon on the title included in each page of this site
  - [Font Awesome](https://fontawesome.com/) - For the icons used
  - [Google Fonts](https://fonts.google.com/) - To select fonts and implement them in the site
  - [Github](https://github.com) - To deploy the site online, and Github desktop app to link _Visual Studio Code_ to Github.com
  - [Coolors](https://coolors.co) - To insert colors selected previously directly through visual studio code, but used this tool to display the palette beautifully, and insert it in this readme file.
  - [Amiresponsive](https://ui.dev/amiresponsive) - To display the site in all types of devices simultaneously.
  - [EqualWeb Accessibility Checker](https://chrome.google.com/webstore/detail/equalweb-accessibility-ch/imemciokfejbnonkkinhcdfigdilcllg/related?utm_source=chrome-ntp-icon) - Google Chrome extension to check general errors and contract errors for optimal accessibility.
  - [Juicy Studio](https://juicystudio.com/services/luminositycontrastratio.php) tool to generate accessibility reports related to contrast, following the **WCAG 2.0**'s luminosity contrast algorithm.
 
# CREDITS & ACKNOWEDGEMENTS
- All the images are free copyright, and have been taken from [Pexels.com].
- I have researched Stackoverflow, Youtube, W3School, Geeksforgeeks among other sites when encountering issues or knowledge blockers.
- I have found inspiration and revieved material from Code Institute Full Stack Web development course.


