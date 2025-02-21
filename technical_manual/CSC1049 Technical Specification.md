

**CSC1049**  
**3rd Year Project**  
**COMSCI**

**Faye Harlick		22712251**  
**Victoria Sinko		22346993**

**Technical Specification**

**Table of Contents				p.0**

1. **Overview				p.1**

**1.1 Glossary**

2. **System Architecture			p.2**

	**2.1. Frontend**  
	**2.2. Backend**  
	**2.3. Database**  
	**2.4. Hosting**  
	**2.5. Static & Media Files**  
	**2.6. Third Party APIs**

3. **High-Level Design			p.3**  
   **3.1. System Models**  
   **3.2. DFD Diagram**  
   **3.3. Object-Oriented Design**  
   **3.4. API Implementation**  
4. **Requirements				p.5**  
   **4.1. Functional Requirements**  
   **4.2. Non-Functional Requirements**  
5. **Problems and Resolutions		p.6**

**5.1. Location**  
**5.2. Framework**  
**5.3. UI Design**  
**5.4. Store & Display User Data**  
**5.5. Hosting Online**  
**5.6. Git Troubles** 

6. **Installation Guide			p.8**

	**6.1. Prerequisites**  
	**6.2. Running Locally**  
	**6.3. Online App**

7. **Testing					p.9**

	**7.1. System Testing**  
	**7.2. User Testing**

8. **Future Enhancements			p.10**

**1\. Overview**  
Our system, called Meetups, is a social application focused around users being in the same location at the same time. The main idea is that a user can only add another user as a friend by logging a ‘meetup’, or an in-person meeting between the two people. It is then intended for users to continuously log their meetups whenever they see their friends in person. The users are verified to be in close proximity by confirming the GPS location of their devices.  
	Meetups is designed to be an alternative to modern social media where there are typically no barriers in place to prevent users from making contact and interacting with strangers on a regular basis. Therefore, the aim of Meetups is to encourage users to develop closer interpersonal relationships.  
	A typical use of the application would involve opening the app on a mobile browser, either registering or logging in to an account, then allowing the app to access the user’s location, and simply scanning the QR code on another user’s app to log their meetup. A user can also create posts which appear on a dashboard which can only be seen by them and their friends.

**1.1 Glossary**  
GPS:

- This stands for Global Positioning System. It is used by most modern smart devices, including smartphones, computers, cars, and so on. The device acts as a receiver for signals that GPS satellites emit while orbiting the earth. Through a process called trilateration, when the receiver is in range of 3 or more satellites then its exact location can be pinpointed on the map.

Django:

- A high-level Python web framework designed to help developers build secure, scalable, and maintainable web applications quickly. It follows the Model-View-Template architecture, providing built-in features like authentication, database management, and security protections to streamline development.

SQLite database:

- A lightweight, file-based database system that doesn’t require a separate server to operate. It stores data in a single file and is ideal for small to medium-sized applications.

Codebase:

- The complete collection of source code for an application, including all files, libraries, and resources used to build and maintain the software.

Authentication:

- The process of verifying the identity of a user, typically through credentials like a username/email and password, to allow access to the system.

Session management:

- A way of tracking user interaction with an application across multiple requests, ensuring that users stay logged in and can access their personal data securely.

Business Logic:

- The part of the application that defines how data is created, displayed, and modified according to the rules and objectives of the project.

Framework:

- A set of tools, libraries, and conventions that provide a foundation for building applications, reducing development time by offering reusable code and structures.

Hosting:

- Providing space on a server for an application or website so that it can be accessed by users over the internet.

Static files:

- Files such as images, CSS, and JavaScript that don’t change dynamically and are served directly to the user’s browser.

QR code:

- A type of barcode that can be scanned using a smartphone or other device to quickly share data, such as a web link or identifying information.

API (Application Programming Interface):

- A set of rules and tools that allows different software applications to communicate and share data or functionality with each other.

NFC (Near Field Communication):

- A short-range wireless technology that allows data to be exchanged between devices when they are placed close together, commonly used for contactless payments and data sharing.

**2\. System Architecture**  
Meetups is a Django-based application that facilitates user’s meeting up and logging that they’ve met up. It is built using Django and hosted on the Redbrick servers at DCU. The system uses an SQLite database for storing user accounts and meetup data, and all components (backend, database, frontend) are integrated within the same codebase.  
When a user accesses the application through their browser, Django renders the necessary frontend pages and processes user input. Requests are sent to the Django backend, which handles authentication, session management, and business logic. The backend interacts with the SQLite database to retrieve or store data before returning the appropriate response to the user. Static and media files are served directly from the local server, ensuring quick access to necessary assets.

**2.1.** **Frontend (CSS and JavaScript)**  
The frontend consists of Django templates rendered by the Django framework. Users interact with the system via standard HTML, CSS and JavaScript served by Django views. No separate frontend frameworks are used.  
The system uses CSS for styling the web pages, and JavaScript for front-end interactions such as obtaining a user’s location, and making and deleting posts.

**2.2. Backend (Django Application)**  
The backend is developed using Django (Python) and manages all business logic, including user authentication, session management, and data processing. The system relies on Django’s built-in authentication framework with a custom user model to handle user accounts securely. Sessions are managed through Django’s session-based authentication, allowing users to log in and stay authenticated across multiple requests. All core functionalities such as meetup creation, user authentication, and data retrieval, are handled through Django views.  
Currently, Django views are handling all of the requests and responses made from the webpage; this can either be a HTML page or a JSON response.  
The models store and represent the data of the application and store this information in tables that we can see from the admin page. We also access these tables in the webpage to retrieve and show data, such as displaying how many friends a user has and showing posts, likes, and comments on the dashboard.  
Django templates generate dynamic HTML pages for the users to interact with. We have also included our own styling and logo to be consistent across the website.

**2.3. Database**  
Meetups uses SQLite (db.sqlite3) as its primary database. SQLite is lightweight and suitable for the scale of this app, making it a suitable choice for handling user accounts, meetups, and other relevant data. Since SQLite is embedded within the application, there is no need for an external database server, simplifying deployment and maintenance.

**2.4. Hosting**  
Meetups is hosted on Redbrick servers, which are managed by DCU’s Redbrick Society. The Django app and SQLite database are located in these servers which ensures accessibility through the university’s infrastructure.  
The system is available online at [https://urri-meetups.rb.dcu.ie/](https://urri-meetups.rb.dcu.ie/), which allows users to interact with it remotely.

**2.5. Static & Media Files**  
Static files, including CSS, JavaScript, and other frontend assets, are served through Django’s built-in static file handling system. Additionally, media files, such as user profile pictures or uploaded content, are stored locally in the MEDIA\_ROOT directory. The system does not use any cloud-based storage services, meaning all files are managed directly on the server.

**2.6. Third Party APIs**

- QR code generator ([https://gogr.me/api/](https://gogr.me/api/)), for generating QR codes that users must scan to log their meetups  
- Nomination ([https://nominatim.org/](https://nominatim.org/)), for converting the users’ location into a readable textual address  
- Mdn web docs ([https://developer.mozilla.org/en-US/docs/Web/API/Geolocation\_API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API)), to let users opt-in to letting the browser access their geolocation

In practice, these APIs are used to obtain the coordinate location of the user, generate a QR code that can be scanned to log a meetup, and display a readable address on the app.

**3\. High-Level Design**  
The high-level design of Meetups defines how the system components work together to provide core functionality. User accounts are managed using a custom Django authentication system, with profiles that track friendships and QR codes for meetup verification.  
The system follows a structured object-oriented design, where models represent users, meetups, posts, and comments, enabling seamless data management. The application also integrates third-party APIs for generating QR codes and retrieving user locations, ensuring accurate meetup verification and an interactive user experience.

**3.1. System Models**  
The system is designed using the Model-View-Template (MVT) architecture, which is Django’s implementation of the Model-View-Controller (MVC) pattern. The models represent the data structure and define how information is stored in the database. The views handle user requests, process data, and return responses, either in HTML or JSON format. The templates are responsible for dynamically rendering frontend pages based on the provided by the views.  
	The Meetups application structures data into key models representing users, relationships, interactions, and content. These models work together to facilitate a dynamic and interactive social experience, ensuring that all user data and interactions are efficiently stored and managed within the application’s database. Here are the main models:

- The User model is customized to use email-based authentication  
- The Profile model extends user functionality by adding a following system and a unique QR code for each user  
- Meetups between users are tracked using the Meetup model, which automatically establishes mutual connections upon scanning a QR code  
- The MeetupToDo model allows users to schedule planned meetings with others  
- The Post model enables users to create and share content, with a built-in like system  
- The Comment model allows for discussion and interaction on posts

**3.2. DFD Diagram**  
This Data Flow Diagram (DFD) illustrates how data moves between different parts of the system.

![Image of DFD diagram](Data_Flow_Diagram.drawio)

**3.3. Object-Oriented Design**  
The Meetups application is designed using object-oriented principles to ensure modularity and maintainability. The following object-oriented structures enable the system to efficiently manage user data, relationships, and social interactions while keeping the codebase scalable and reusable:

- The User model inherits from Django’s AbstractUser, allowing for a custom authentication system while reusing built-in functionality  
- The Profile model establishes a one-to-one relationship with User, extending its capabilities with additional attribute like a unique QR code and a following system  
- The Meetup model represents interaction between users, utilizing foreign key relationships to link two Profile instances while ensuring bidirectional friendships  
- The Post and Comment models follow a composition-based design, where a post can have multiple comments, and both models establish many-to-many relationships with users for likes and interactions.

Encapsulation is maintained by defining methods within models, such as like\_count() in Post, which prevents direct modification of related objects.

**3.4. Third Party API Implementation**  
Meetups integrates with multiple third-party APIs to enhance its functionality. The system interacts with these external services as follows:  
Geolocation API (MDN Web Docs)

- When a user attempts to log a meetup, their browser requests permission to access their GPS location. This data is then sent to the backend to verify proximity to another user.

Nominatim API

- Converts raw GPS coordinates into human-readable addresses, allowing users to see their location in a more understandable format

QR Code Generator (gogr.me)

- Generates QR codes dynamically for each user, which must be scanned to successfully log a meetup

These APIs work alongside Django’s backend to ensure smooth data collection, validation, and storage. The interaction between these components ensures that users can verify meetups, obtain accurate location data, and scan QR codes for logging.

**4\. Requirements Summary**  
The requirements of a system describe the specific actions or behaviours the system must perform, and define the system’s performance, usability, and other qualitative aspects.

**4.1. Functional Requirements**  
User Registration and Authentication:

- The system must allow users to register an account using an email address and password. Registered users should be able to log in and log out. The authentication should ensure secure login and user session management.

User Profile Management:

- Users must be able to view their profile. Each user’s profile should also track their friends and the meetups they’ve attended.

Meetup Logging:

- Users should be able to log a meetup by scanning another user’s QR code, confirming proximity via GPS location, and storing this information in the system. The system should automatically add the users as friends of each other once a meeting is logged.

Post Creation and Interaction:

- Users should be able to create posts on their dashboard, view posts from their friends, and interact with them by liking or commenting. Posts should include text and optional images.

Geolocation:

- The system must use the user’s device geolocation to confirm proximity when logging a meetup. Additionally, the system should display a user’s location in the form of a readable address.

**4.2. Non-Functional Requirements**  
Performance:

- The system should load pages and respond to user actions in less than 10 seconds under normal usage conditions. The server should handle multiple simultaneous users without significant degradation in performance.

Scalability:

- The application should be scalable to support a growing user base, meaning it should handle an increasing number of users, posts, meetups, and interactions without performance issues.

Security:

- The system must ensure the protection of user data including passwords, using encryption. It should follow best practices in securing the authentication process, and ensuring secure connections via HTTPS.

Availability:

- The system should be available most of the time with minimal downtime for maintenance. The server is redeployed every 6 hours.

Usability:

- The system should have an intuitive and easy-to-use interface, ensuring users can quickly understand how to register, log meetups, and interact with posts. The web app should be responsive, ensuring compatibility with mobile browsers.

Data Integrity:

- The system must ensure data consistency and correctness, including preventing duplicate meetups, posts, or interactions.

**5\. Problems and Resolution**  
Throughout the development of Meetups, we encountered a range of challenges, from selecting appropriate technologies to designing a responsive user interface and deploying the application on external servers. Many of these issues came from initial choices that ended up being impractical due to complexity or inexperience. By rethinking our approach, we focused on familiar tools and simplified some functionalities to optimize our development process.

**5.1. Location**  
One issue we faced was implementing the location tracking feature. At first we wanted to use GeoDjango, which is a Django framework for building location-aware web apps. It has functionalities such as spatial queries and distance calculations which would have been more convenient for handling GPS data.  
	However, there were significant issues during the installation and setup process. GeoDjango has complex dependencies like GDAL, GEOS, and PROJ, which all need to be properly configured. We also had limited control within the Redbrick server environment which made these libraries more difficult to install.  
GeoDjango also has a very steep learning curve, so we opted to use the browser’s Geolocation API together with Nominatim for retrieving users’ coordinates and translating them into readable addresses. This was more practical for the scope of the project because it allowed for quicker deployment, simpler maintenance, and ensured cross-platform compatibility.

**5.2. Framework**  
Another significant challenge we faced was choosing the right framework for developing the app. Originally we planned to use Flutter, which is a popular UI toolkit for building natively-compiled applications for mobile and web from a single codebase. It can create responsive and high-performance apps, and seemed to be an obvious choice but in practice we ended up running into a lot of issues.  
	To begin with, Dart was a completely new language to us (the main one used by Flutter), and learning it alongside Flutter’s architecture would have taken a significant amount of time. Flutter also had a complex setup process and debugging environment which slowed progress even more.  
	To solve this, we decided to switch to Django for the backend and use HTML, CSS and JavaScript for the frontend. This was a good choice because we had previous experience with Django, and it had built-in features that worked well with our project such as user authentication and database management. Since we were also familiar with Python, we saved time on learning a new language and were able to put more effort towards building the functionalities of our app.

**5.3. UI Design**  
A further challenge we encountered was designing a user interface (UI) that would be compatible with both desktop and mobile devices. Throughout most of the development process, we were coding and testing exclusively on laptops, meaning we could only see and interact with a desktop-based interface in real time. We weren’t able to deploy the app to the Redbrick server until roughly the final third of the project, which would have allowed us to access the app from our phones. When we did get it hosted, we realised that the desktop-based UI we had designed did not translate well to a mobile interface.  
	To resolve this, we made the decision to redesign the UI with a mobile-first approach. As the main functionalities of the app revolved around users meeting in person and scanning QR codes, it made much more sense to focus solely on mobile compatibility.  
While the ideal would have been creating an app that worked well on both desktop and mobile, Django doesn’t provide tools that implement responsive design for a dynamic app. Implementing this would have required additional frameworks or extensive CSS media queries, so we decided against it in favour of keeping within the project deadline, and instead focused solely on a mobile-friendly UI.

**5.4. Store & Display User Data**  
Another issue we faced was figuring out how to store and display user information from posts. We wanted an efficient way to associate posts with their creators, store related data such as likes and comments, and dynamically display this information on the dashboard.  
	We wanted the dashboard to display this information without running into performance issues caused by inefficient database calls, so we had to make sure we avoided making redundant queries which would have slowed down the app.  
	To support this, we designed the Post and Comment models with ForeignKey relationships linking them directly to the User model. This structure allowed Django’s Object-Relational Mapping (ORM) to efficiently fetch related user data (like email and profile details) whenever posts were displayed. We also included a ManyToManyField in the Post model to handle likes which made it easy to count and display them without additional queries. These model designs helped create a clean, responsive dashboard.

**5.5. Hosting Online**  
Another major challenge we encountered was figuring out how to host our application on the Redbrick server and learning how to create and configure build and Docker files. We had to be able to deploy our app so that it could be accessed remotely and tested on mobile devices, but since we didn’t have any prior experience with deploying on servers such as Redbrick, it made this process more difficult.  
	We had some experience with using Docker, but we struggled with understanding how to work with things like dependencies, Python environments, environment variables, static file handling, and configuring Docker files. This took a lot of research and help from more knowledgeable individuals to get everything working properly.

**5.6. Git Troubles**  
We also ran into issues with using GitLab and GitHub, as we were not fully familiar with using them for working on collaborative projects. We mainly worked off GitHub as we wanted to ensure we had a working backup set of files. The hosted server is also based on the code located on GitHub (which is then duplicated over to the main GitLab repository), as this was easier for the Redbrick society to access. Most of our problems revolved around merge conflicts, pulls and pushes getting rejected, etc. These were resolved with typical troubleshooting.

**6\. Installation Guide**  
The following are the instructions for setting up and deploying the Meetups Django application locally and on a hosting server:

**6.1. Prerequisites**  
Ensure the following tools and libraries are installed:

- Python (any modern version should work)  
- pip (Python package installer)  
- Docker (for creating and running containers)  
- Git (if cloning from a repository)

**6.2. Running Locally**

- Clone the Repository with ‘git clone \[repo url\]’  
- Enter the Meetups directory which has manage.py and requirements.txt in it  
- Run ‘pip install \-r requirements.txt’  
- Run ‘pip install Pillow’  
- Run ‘python manage.py runserver’  
- Access the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in the browser

**6.3. Online App**

- Access the hosted app on the Redbrick server at [https://urri-meetups.rb.dcu.ie](https://urri-meetups.rb.dcu.ie) 

**7\. Testing**  
Testing for the Meetups application was carried out through a combination of system testing and user testing, ensuring the system’s robustness, usability, and proper handling of edge cases.

**7.1. System Testing**  
System testing focused on verifying that all components of the application functioned as expected, both individually and as part of the integrated system. We primarily used Django’s built-in testing framework, which utilizes Python’s unittest library.  
Some other key aspects of our system testing included:  
Unit testing:

- We used test cases to check specific functions and methods in isolation, such as user authentication, post creation, and meetup logging. Each test case verified that a particular input produced the expected output.

Local server testing:

- Interacting with all components (such as buttons and forms) while logged in and logged out; Handling invalid inputs during registration and login; Checking UI consistency and functionality across multiple browsers and devices.

**7.2. User Testing**  
User testing involved both our own and external feedback from friends and family. This was for revealing usability issues, identifying potential bugs, and refining the user experience.  
The main aspects of this included:  
Self-testing:

- We thoroughly tested the application ourselves, interacting with all features and deliberately providing invalid inputs to observe error handling.

External feedback:

- We shared the hosted app link with friends and family and encouraged them to freely use the app and report back any bugs that were found or give suggestions for UI improvements. For example, we originally had the users’ location displayed as raw longitude and latitude, but we changed it to display a textual address based on feedback.

Cross-platform compatibility:

- We tested the UI on different browsers and devices. While initial designs were desktop-oriented due to development on laptops, feedback from mobile testing revealed inconsistencies. We had to redesign the interface to focus exclusively on a mobile-friendly experience, aligning with the app’s QR code scanning functionality.

Error handling:

- Whenever an error occurred during testing, we reviewed the console outputs and Django error messages to pinpoint and resolve the issues efficiently.

**8\. Future Enhancements**  
While the current version of Meetups successfully implements the core features and functions as intended, there are several areas for potential improvement and expansion. The following enhancements would improve the user experience, system performance, and security of the application:  
Responsive UI for Desktop and Mobile:

- The existing UI is optimized for mobile use. Future updates could involve redesigning the interface to ensure compatibility with both desktop and mobile platforms. This may require integrating additional frontend frameworks such as React or Bootstrap to create a dynamic, responsive design.

Refined and Modern UI Design:

- The interface could be further refined to offer a cleaner, more intuitive use experience that aligns with the design principles of modern social media platforms. Enhancements could include smoother animations, improved navigation, and a more visually appealing dashboard.

Self-Hosted Server & App Store Availability:

- Currently hosted on Redbrick servers, future versions could be hosted independently for greater control, scalability and reliability. Additionally, developing native mobile applications for iOS and Android platforms would make the app more accessible and user-friendly.

NFC Integration:

- Incorporating Near Field Communication (NFC) technology would allow users to log meetups even faster and more efficiently by tapping their devices together. This feature would streamline the meetup process and enhance user convenience.

Enhanced User Profile Information:

- To make user interactions more meaningful, additional details such as the location and date of a user’s first meetup could be displayed on friend’s profiles.

Age Restrictions:

- Given that the app is designed around in-person meetups, limiting access to users over 18 years old would help address ethical concerns related to safety and privacy, especially for younger users.

Improved Security Measures:

- As sensitive information like user locations is stored in the database, implementing advanced security measures is essential. Future updates could include more advanced data encryption and enhanced access control to safeguard user data against potential hacking attempts.

Automated Email Notifications:

- Incorporating an automatic email notification system would enhance user engagement. For example, users could receive emails when they log a new meetup, when friends make posts, or when significant updates occur within the app.

