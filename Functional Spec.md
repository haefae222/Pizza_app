# CA326 COMSCI3

## 3rd Year Project
### Functional Specification Document
#### 2024/25

**Faye Harlick**  22712251  
**Victoria Sinko**  22346993

**Supervisor**: Stephen Blott

---

## Table of Contents

| **Section**                                      | **Page No.** |
| ------------------------------------------------ | ------------ |
| **Introduction**                                 | 2            |
| 1.1. Overview                                    | 2            |
| 1.2. Glossary                                    | 2            |
| **General Description**                          | 3            |
| 2.1. Product / System Functions                  | 3            |
| 2.2. User Characteristics and Objectives         | 3            |
| 2.3. Operational Scenarios                       | 4            |
| 2.4. Constraints                                 | 5            |
| **Functional Requirements**                      | 5            |
| 3.1. QR Code Implementation                      | 5            |
| 3.2. Adding Friends                              | 6            |
| 3.3. Login System                                | 6            |
| 3.4. Logging Meetings                            | 6            |
| 3.5. Ability to Download the App                 | 7            |
| 3.6. Post Creation and Interaction               | 7            |
| 3.7. Sending Messages                            | 8            |
| **System Architecture**                          | 9            |
| 4.1. System Architecture Diagram                 | 9            |
| **High-Level Design**                            | 9            |
| 5.1. Data Flow Diagram                           | 9            |
| **Preliminary Schedule**                         | 10           |
| 6.1. Gantt Chart                                 | 10           |

---

## 1. Introduction

### 1.1. Overview
The aim of our project is to implement, refine, and enhance the technologies available today that allow two or more people to prove that they were in the same location, at the same time.
Our main demonstration of this will be via a social app called MeetUps where users can only add other people when they are physically together at the same time. This idea came from the realisation that there is an extreme surplus of social media applications where the majority of a user’s connections are strangers.
We believe that people who appreciate and enjoy social interactions would find a lot of potential and use in our app, as connections with people that a user has only met in real life would be more meaningful and possibly more interesting than ones with strangers.
The features available in our app would similarly reflect modern social media apps, such as the option to post updates or content in some form (either text, image, or video-based), and the ability to privately message other users. The main unique functionality of our app is that a user can only add another user when they are both together in person at the same time.
The other features we would implement based on this are a calendar system for keeping track of past meetings and scheduling future ones, and specific information displayed on a user’s friends’ pages, such as where they met for the first time.


### 1.2. Glossary
**NFC** - This is the technology that allows two devices to ‘talk’ or communicate in short range. This is what allows bank cards to ‘tap’, for example. The farthest range of this is limited to about 20 centimeters, but typical NFC readers on most devices only function within 5-10 centimeters or so.

**GPS** - This is a tool most modern devices are equipped with, such as smartphones, smartwatches, cars, airplanes and most other vehicles. In simple terms, a GPS functions by transmitting a signal from a satellite which is then read by a GPS receiver in the device, allowing the location of the device to be accurately pinned on the globe. This is used in navigation, tracking and mapping.

**QR Code** - A QR Code is a two-dimensional barcode that, when scanned using a camera on a device or a special reader, performs a specific action on that device. For example, it could open a specific web page, or send a piece of information to a server. In a nutshell, QR Codes are used to store information. They can be used as an alternative to a link address.

---

## 2. General Description

### 2.1. Product / System Functions
Here are the main functions of our app/product:

- **Login and register an account** Straightforward; a user can make an account on the app using an email address, name, date of birth, and password. The app will be limited to 18+ only, as it is related to meeting people in person.
- **App download from app store**: The app will be available to freely download from the app store.
- **Creating posts**: A user will be able to create a post in the form of text, image, or video, which will then be visible to all of their added friends and on their profile page.
- **Adding friends**: A user will be able to add friends to the app, but only when they are together in person. This requirement will be verified via a combination of QR, GPS and NFC technology.
- **Messaging friends**:A user will be able to message their friends on the app. The chat interface will be similar to other social media or messaging apps, such as Instagram and Whatsapp.
- **Meetup calendar**: An interface resembling a calendar will be available on the app, where each user will be able to see their previous meetings and schedule future ones with their friends. Within this interface is where the options to log a meeting and schedule a future meeting will be.
- **Interacting with posts**: A user will be able to ‘like’, share, and leave comments on posts.
- **Unique friend information**: When a user views their list of friends, each one will contain unique information to them such as when and where they first met/added each other on MeetUps.

### 2.2. User Characteristics and Objectives
The app will be available on any mobile phone that can:
Connect to the internet
Scan a QR Code
Receive a GPS signal
Read and transmit an NFC signal
	Fortunately, most if not all modern mobile devices offer all of these features.
The target audience for our MeetUps app specifically is adults (anyone over 18) that are passionate about meaningful social connections. However, it is important to note that the technology we will be using for the unique features of the app can be adjusted to fit numerous different contexts. For example, this could be used in a medical context, such as where a patient is required to prove that they have attended an appointment or picked up a prescription. Thus, it should be kept in mind that the target audience will vary depending on how these technologies are implemented.
	The app will function very similarly to existing social media and messaging apps, which most adults today already have experience with. Therefore, as long as we keep the layout of MeetUps typical and familiar, users shouldn’t have issues navigating the app. Our aim design-wise is for usage of the app to be as intuitive as possible.



### 2.3. Operational Scenarios
Here are some scenarios illustrating the functions of our app:

--**Creating an account**
The user must first have the app downloaded on their phone. When opening the app, they will be prompted to either log in to an existing account, or create a new one. In this case, the user will be creating a new account. They are brought to an interface for entering their account details, i.e. their email address, full name, date of birth and password. They will be blocked from creating an account for a set amount of time if they are under 18 years of age. Once their account is created, they are then brought to their profile page, where they have the option of adding extra details to their account such as a description of themselves and a profile picture. The user will automatically remain logged in on their device.

--**Adding a friend**
To add a friend on MeetUps, the user must first be logged in to their account. The user must also be physically together with the person they wish to add as a friend. This person must also be logged in to their account on the MeetUps app. The user will then select the option on the app for adding a new friend, which will promptly display their unique QR Code. When the potential friend scans the QR Code, both devices then ping a GPS signal to ensure that they are both in close proximity. Once this has been verified, both devices will then prompt their users to put their phones near each other. This is when they will communicate via NFC as a final level of verification, and the two users will be added as friends to each others’ account.

--**Logging a meeting**
After two users have been added as friends, there is no need to scan one of their QR Codes to log a meeting between them. One user just needs to go to their meeting calendar, select the ‘Log meeting’ option, and select which friend they would like to log a meeting with. Once they select the friend, both of their apps skip to pinging GPS signals, and then prompting the users to hold their phones close together so they can communicate via NFC. The date and location of the meeting is then saved to the calendar.

--**Messaging a friend**
A user is able to send messages to their friends. There will be a dedicated section of the app where all of a user’s conversations will be kept. When a user adds a new friend, their conversation is automatically added to the message section. The conversations will be sorted with the most recently updated one at the top, in descending order. The user will also have the option to pin conversations to the top of the list.

--**Making a post**
When the user is logged in to the app, they will have an option on the main page to make a post. When selected, they will be asked whether they want to make a text, image, or video post. Once the user has selected an option, they will then be able to enter the content of their post, and write a description for it if they wish. They can then submit the post, which will then appear on the main page where it will be visible to all the friends of the user.


### 2.4. Constraints
Our main constraints and challenges are as follows:

--**Lack of time**
The app must be functional by the 21st of February, which gives just over two months to complete the project.

--**Learning QR Code programming**
This is a new concept to the both of us, so we will have to dedicate a lot of time to learning how to automatically generate unique QR Codes, and have them function exactly as planned when they are scanned.

--**Learning how to obtain and use GPS data**
We need to be able to access and use the GPS data from the devices that use the app. We do not have experience programming mobile devices, so we will have to learn how to access this type of data.

--**Learning how to program NFC readers**
We want to be able to use NFC in our app, so we will have to learn how to program the app so that it is able to use the NFC reader in the devices.

--**Learning how to build a mobile app**
We have experience in making web apps, but neither of us have made a mobile app before. We will have to learn which programs to use to put a mobile app together.

--**Needing to learn new languages**
We may be required to learn some new programming languages for this project, such as Flask.

--**Managing compatibility across operating systems**
Victoria uses an iPhone, and Faye uses an Android, so we will have to take the compatibility of our operating systems into account when testing the functionality of the app.


---

## 3. Functional Requirements

### 3.1. QR Code Implementation

- **Description**:
When a user creates an account, a unique QR Code will be automatically generated that is connected to their account. When the user selects the option to add a new friend, their phone will display this QR Code so the other person can scan it using their phone camera. When this is done, it will kickstart the rest of the friend adding process which is outlined in section 2.3.

-**Criticality**:
Extremely critical. This is the most basic form of verification we should aim to achieve for proving two people are in the same place at the same time. We must implement this fully before moving on to more complicated functionalities.

-**Technical Issues**:
We need to ensure that every QR Code generated is unique and correctly tied to each account. We also need to make sure that both devices involved in the scanning process perform as intended after the scanning is complete.

-**Dependencies**:
The site/program we will use for generating the QR Codes. We may be limited to how many QR Codes we can freely generate, and there may possibly be limitations to the extent that we can program and customize the QR Codes. This is also dependent on the login system.


### 3.2. Adding Friends

-**Description**:
When a user is logged in to the app, they have the ability to add a new friend, given that they are physically together in person. Once added, the friend will be able to see the user’s posts, and they will be able to send messages to each other.

-**Criticality**:
Very critical. Building connections and adding friends on the app is the main demonstration of our project. It must be possible for a user to add a friend on the app after all of our verification methods have been satisfied.

-**Technical Issues**:
Database configuration. Ensuring that our chosen database is able to manage a large volume of data with a lot of interconnected accounts.

-**Dependencies**:
This is dependent on the login system, and the methods we will use for verifying the proximity of the two users.


### 3.3. Login System

-**Description**:
When a user downloads the app, they must be required to register and log in to their account to be able to add other users as friends. This will require their email address, full name, date of birth, and a password.

-**Criticality**:
Very critical. A user should be logged in to access the functionalities of the app. This is not a difficult task to accomplish but it should be rigorously tested.

-**Technical Issues**:
Database configuration. Ensuring passwords and user data is secure and encrypted. If possible within the time constraint, we will attempt to implement an account recovery system.

-**Dependencies**:
Depends on the database to be able to manage a large volume of unique account data.

### 3.4. Logging Meetings

-**Description**:
When a user is logged in and in close proximity to one of their friends, they can log their meeting on the calendar interface on the app. They will not need to scan their QR Code, but they will need to use the NFC reader and GPS data on their mobile phones.

-**Criticality**:
Moderately critical. Logging physical meetings is a feature tied to the proof of proximity tools that we will implement in our system (QR Code, NFC and GPS), so it would benefit the demonstration for this to be fully implemented. However, it is not necessary for the general function of the system. 

-**Technical Issues**:
Similar to adding a new friend, managing this data on the database may be a challenge.

-**Dependencies**:
The login system, being able to add another user as a friend, and the methods for verifying proximity.


### 3.5. Ability to Download the App

-**Description**:
It should be possible to upload the app onto an app store so that it is accessible and downloadable by any mobile phone user.

-**Criticality**:
Somewhat critical. It is intended for the app to be free and available for download online. However, it is not 100% necessary for us to implement this in the context of this project

-**Technical Issues**:
Ensuring compatibility across operating systems. Following rules and requirements associated with releasing applications for downloading.

-**Dependencies**:
It costs money to host an app on an app store, and in some cases to also host a working database and server online. These might bar us from being able to release the app for download.


### 3.6. Post Creation and Interaction

-**Description**:
When a user is logged in, they will be able to make either a text, image, or video post which will then be visible on the main page to all of their friends. All users are able to interact with the posts, either via ‘liking’ them or by leaving a comment on them.

-**Criticality**:
Somewhat critical. This would be a good feature to implement but it is not necessary for the demonstration of the product.

-**Technical Issues**:
Database configuration. When a user uploads a post it needs to be stored on a database so that it can be accessed by the back end code of the app, so it can then be displayed on the main page. Images and videos take up a lot of memory, so we need to ensure that there are sufficient storage methods available for managing these.

-**Dependencies**:
This is dependent on both the login and friend adding system, as a user needs to be logged in to either create or interact with posts, and a user can only see the posts of other users they are friends with.

### 3.7. Sending Messages

-**Description**:
When a user is logged in, they will be able to send direct/personal messages to their friends. This interface will resemble other social media or messaging apps such as Instagram and Whatsapp.

-**Criticality**:
Somewhat critical. This would be a useful feature to implement to demonstrate communication between friends on the app, but it is not critical to the main functions or demonstration.

-**Technical Issues**:
This may require database configuration as well, if we decide to have text messages remain on the app indefinitely so that users can ‘scroll back’ to view older messages. This would require a lot of long-term storage. Other implementation methods to make this easier could include adding an automatic message deletion system, where texts are only stored on the database for a limited amount of time, such as a month.

-**Dependencies**:
This is dependent on both the login and friend adding system, as a user needs to be logged in to send messages and they can only send them to their friends.

---

## 4. System Architecture

### 4.1. System Architecture Diagram
The online database is where data such as users’ account details and post content will be stored and accessed.

The hosting server is the online server where the mobile app will be hosted and maintained.

The mobile app is the actual app and user interface that will be downloaded onto the mobile devices.

The mobile phones are required to communicate directly with each other in order to read their NFC signals.

The users are also required to communicate directly with each other because they need to meet physically in real life.

![Alt Text](https://gitlab.computing.dcu.ie/harlicf2/2025-csc1049-fharlick-locationapp/-/blob/main/system_architecture_diagram-1.png)


---

## 5. High-Level Design

### 5.1. Data Flow Diagram
A DFD diagram represents the flow of information between different points of the system. Our diagram shows how information flows between different components in our system, mainly what information is being provided by the user.

The user provides details (username, password and temporary location data) which is saved by the database.
The database then saves that information to verify each user
The database also saves content (posts, messages) and then retrieves it to display on the homepage of the application
Location data is only used and stored temporarily in the database when there’s a meeting or when a new friend is being added.
	


---

## 6. Preliminary Schedule

### 6.1. Gantt Chart
A Gantt chart detailing the project schedule will be included here, showing key milestones and deadlines.

---
