

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

| ![][image1] |
| :---- |

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

[image1]: <data:image/png;base64,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>