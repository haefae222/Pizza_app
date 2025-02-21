

**CSC1049**  
**3rd Year Project**  
**COMSCI**

**Faye Harlick		22712251**  
**Victoria Sinko		22346993**

**Blog**

**Saturday January 4th 2025**  
We decided to take a break from project work for the holidays to focus on recuperating after the winter exams. We began looking at Flutter tutorials, and going through the process of downloading it on our laptops and figuring out what libraries or tools we might have to download or install to have all the functionalities we need for our app.  
	In advance of coding, we spent a lot of time thinking about the page layout of our site, such as which links to include on which pages, which content to include on each page, basic UI design, etc. We sketched out ideas for a logo, and thought about the colour scheme we wanted for the app. We had a meeting with our supervisor to discuss our plan moving forward and if it seemed like we were on the right track.  
	As it was still relatively early in the physical development process, the outlook remained mostly experimental as we were only learning how to use Flutter and write Dart for the first time. We decided to start trying to build the basic pages of our app to see how Flutter worked for us, and check in after a bit and go from there.

**Friday January 17th 2025**  
After spending almost 2 weeks attempting to build our app on Flutter, it became very obvious to us that there were significant issues which were going to have a negative effect on our development process. The main issue was that learning how to use a new framework along with learning how to program in a new language was very time consuming, and we spent a lot of time figuring out how to fix basic syntax errors, trying to learn the layout and functionalities of the framework etc.  
	We felt like our time could’ve been put to better use, as we would’ve preferred to focus on developing our app functions and UI more rather than using up all our time learning how to work with the tools we decided to use.  
	Therefore, we made the decision to switch from developing with Flutter to developing with Django, which was a Python framework we already had a lot of experience using in the past. Instead of Dart, the frontend of the app was going to be made with HTML, CSS and JavaScript, which we also had a lot of experience with. Django also came with a lot of features that we felt worked well with our project, such as user authentication and database management.  
	Obviously, we did originally choose to use Flutter for a reason, as it’s a framework that’s designed specifically for developing mobile apps, and it excels in factors such as responsiveness. So, by steering away from Flutter we did possibly lose out on more advanced functionalities, but we felt that the benefits of working with a familiar framework and programming languages outweighed the losses here.  
	Our next priority was to remake the Flutter UI and pages we already had in Django, and essentially get our progress back up to speed.

**Wednesday January 29th 2025**  
After nearly two weeks, we had the base pages of the app developed to the point where we felt comfortable moving on to the more complex functionalities. A big aspect of our app we wanted to add was the location tracking feature. A Django framework exists which is intended to be used for location tracking in location-aware apps, called GeoDjango. We started to look into this and find out how to properly implement it in our app.  
	Another large aspect of the app we wanted to start working on was QR code generation. There are multiple APIs available online for QR code generation, so we had to do research to find out which one would work best with our app.  
	We also wanted to get more into advanced data storage and management, specifically with models such as user profiles, friends, previous meetups, etc.

**Monday February 10th 2025**  
At this point, backend development was mostly done on our app. We picked an API for QR code generation, called gogr.me, and managed to get it to correctly generate and display a QR code on our app which is then tied to each unique user, and logs a meetup when it is scanned.  
	Our location tracking feature was also implemented and moderately refined. Allowing the browser to access the user’s location data allowed it to obtain, store, and display the users’ latitude, longitude, and textual address. This was a major development as this, paired with the QR code implementation, meant that we were able to properly configure the ‘log meetup’ feature that our app’s main purpose is based on.  
	We had also refined our data storage, so now our SQLite database could efficiently store and retrieve data tied to specific users and locations.  
	Our next major concern was our UI, and hosting the app online. These went hand in hand, as they were both related to the mobile interface, which we had been neglecting until then. Meetups was intended to be used on a mobile device as it requires being mobile and needing a camera to be able to scan a QR code. Since we had been programming and testing exclusively on a desktop interface until now, we haven’t been able to see what the UI would actually look like on a phone. We needed to host the app online to be able to do this.

**Tuesday February 18th 2025**  
This past week was focused on getting the app hosted on a Redbrick server, updating the UI to look better on a mobile interface, and documentation. With some help from the Redbrick committee, any hosting issues were quickly resolved and we were able to make use of the online server as soon as it was available. We used this to access the app on our phones to be able to test and tweak the UI so that it would look better on a mobile device.  
	The documentation made up a large portion of the project, and we regretted not starting it earlier. Regardless, we had enough time to get everything written up and proofread, etc.  
	All that was left was to record our demonstration video, make any final changes we wanted, and upload everything to the Git Repo.

