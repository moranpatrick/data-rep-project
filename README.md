# Data Representation and Querying Project 2016
## This Repository Contains all the relevant code and information to run our web application.

## Contents

[Team Members](#team-members)  
[Project Overview](#overview)  
[Meetings](#meetings)  
[Integrated Development Environment](#ide)  
[Running the Application](#run-app)  
[Architecture](#architecture)  
[References](#References)  

## Team Members<a name = "team-members"></a>  
- Patrick Moran <g00179039@gmit.ie>  
- Gerard Naughton <g00209309@gmit.ie>


## Project Overview<a name = "overview"></a>  

One of our third year software projects is to develop a single-page web application (SPA) written in python. The module is called Data Representation and Querying and is taught to us in [GMIT](http://www.gmit.ie) Galway, Ireland.  

![alt text](screenshots/python.png) ![alt text](screenshots/flask.jpg)  


The following are the main instructions from the project specifications.  
>You are required to develop a single-page web application (SPA) written
in the programming language Python using the Flask framework.
You must devise an idea for a web application, write the software, write
documentation explaining how the application works, and write a short user
guide for it.  

Both Gerard and myself have a keen interest in football and the English Premier League. We therefore decided early on to try and make a single web application based on this fact.

After deciding on a fantasy football theme we took a look at some other web applications that already do something similar.

* Below are some of these examples  
http://www.fantasyfootballscout.co.uk/  
http://www.fiso.co.uk/forum/viewforum.php?f=18   

Given the timeframe for the project was only a few months our web application was naturally going to be smaller than some of the examples above.

#####  Here are the essentials we decided our web app must have.  
* Easy to use interface for the client. We want the user to have an easy flow through experience using our application.
* A forum where users can post comments relating to the subject and communicate with each other.  
* On our end, to make it an application, this data from the user must be manipulated. We decided to store the data in a database and have that data rendered on the web page.
* The ability to add a new fantasy football team on a weekly basis. Hard coding it at first but hopefully coming up with a better way.   

##### Advanced Features
* Admin Login and Team Updates

In the beginning we were unsure if these features would be added but we successfully managed to get them up and running in time.  
These features allow the admin, in this case Gerard and myself, to login and change our team selection, any time we want, from the website using the database to store our data. Instructions to do this and more will in the [Running the Application](#run-app) section.

## Meetings<a name = "meetings"></a>
Team meetings were held in either the Canteen or Library study rooms when they were available in the Galway Mayo Institute of Technology(GMIT), Dublin Road, County Galway.
During the course of the Project we had 6 meetings in total.

* Thursday 10th November 2016 13.00

We met in Study Room 5A and discussed on what we should do our Single page web-app on. Making sure it met the course projects requirements and was useful to the user.

* Thursday 17th November 10.00

We met in the Canteen and wrote out the html templates needed and what they should look like for our app. We also discussed the software requirements we would need to run the application and set out that we would have them installed and ready for the next meeting.

* Tuesday 22nd November 13.00

We met in Study Room 5B and we set up our git repository and published our first commit with the structure of our app. We then decided on what steps to work on next. Patrick would start on the routing system and form pages. Gerard would begin setting up the structure of our html pages and connecting up our pages to bootstrap.

* Thursday 24th November 10.00

We met up in Study Room 5A and began setting up our database. We initially decided to use couch.db. We hit a few problems with couch.db and found little documentation online to help. Patrick was going to continue on researching and if could not be solved we would look into using Sqlite3.

* Friday 25th November 10.00

We had a emergency meeting Friday over the phone about our database. We both decided to switch to Sqlite3 as there was more documentation online and we have experience of SQL from Second Year Computer Software and development. Patrick would work on importing Sqlite3 into the project and creating our sql.py. Gerard would work on taking in data from the form and putting it out to our database. We would meet up in Patricks house later to both work on html pages and css.

* Monday 28th November 12.00

We met up in Study Room 6A. After getting the main functionality of the app working we decided we had time to do the Advanced Features. Patrick worked on setting up login page and routing. Gerard worked on TeamEntry page, input of data to database and outputting it to the Home page. We then worked on tidying up the css and code. Patrick had previously made a template for the README.md file. We separated out what parts of the README.md we would carry out. Gerard would take on Team Members, Meetings and Running the Application. Patrick would work on Project Overview and Architecture. We would both work on References. This would be our last meeting.  

## Integrated Development Environment<a name = "ide"></a>
![alt text](screenshots/pycharm.png)  

The integrated development environment (IDE) we are using to manage our web application is [PyCharm](https://www.jetbrains.com/pycharm/specials/pycharm/pycharm.html?&gclid=CjwKEAiAjvrBBRDxm_nRusW3q1QSJAAzRI1tMeRbsl3nnPUUTJ5L67BdVe3Y8VA9VU3MoAYDhNFNLBoCmKfw_wcB&gclsrc=aw.ds.ds&dclid=CMTU-e7C0dACFY2D7QodmzYJxw). PyCharm was developed by [JetBrains](https://www.jetbrains.com/) and is the perfect environment for working with python.

Being students allowed us to get the professional edition of the IDE free of charge for as long as we are studying. If you are interested click [here](https://www.jetbrains.com/student/).

## Running The Application<a name = "run-app"></a>

## Architecture<a name = "architecture"></a>
#### In our project we have used:    

* **Languages**

Python | HTML | CSS
------ |  --- | ---
![alt text](screenshots/python.png) |  ![alt text](screenshots/html.png) | ![alt text](screenshots/css3.jpg)    
 https://www.python.org/ | https://www.w3.org/html/  | https://www.w3.org/Style/CSS/Overview.en.html   

 * **Frameworks**  
  Flask  
 http://flask.pocoo.org/  

* **Libraries**  

| Bootstrap | JQuery
| --------- | ------   
| ![alt text](screenshots/bt.png) |  ![alt text](screenshots/jquery.png)
| http://getbootstrap.com/ |  https://jquery.com/

* **Databases**  

| Sqlite  
| ------    
|  ![alt text](screenshots/sqlite.png)  
|  https://sqlite.org/     

###### Jinja 2  
Jinja2 is a modern and designer-friendly templating language for Python, modelled after Django’s templates. It is fast, widely used and secure with the optional sandboxed template execution environment. It comes installed and ready to use with the flask framework.  
 ![alt text](screenshots/jinja.png)   
http://jinja.pocoo.org/docs/dev/  
In order to have a clean, easier to read codebase we decided to make use of [Jinja Template Inheritence](http://flask.pocoo.org/docs/0.11/patterns/templateinheritance/). Its a  powerful feature of Jinja which allows the developer to build a base “skeleton” template that contains all the common elements of your site and defines blocks that child templates can override.  
We have one html base class which contains all the static code for our web application, for example the navbar and the footer are written just once in here. All other child templates extend from this base class.  
Below is an exert of what the base class would look like.

```
<!DOCTYPE html>
.
.
.

--- Navbar code here ---

{% block content %}

child template goes here

{% endblock %}

 <!-- errors -->
{% if error %}
    <p class="error"><strong>Error:</strong> {{ error }}</p>
{% endif %}

<!-- messages -->
{% for message in get_flashed_messages() %}
    {{ message }}
{% endfor %}
.
.
Footer Goes Here
```
And a child Template might look like
```
<!-- Child Template -->
{% extends "base.html" %}
{% block content %}

All code relevant to this html file goes in here

{% endblock %}
```


## References<a name = "References"></a>
* Online Video Tutorials  
https://www.youtube.com/playlist?list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM  
https://www.youtube.com/watch?v=Lv1fv-HmkQo&list=PLQVvvaa0QuDc_owjTbIY4rbgXOFkUYOUB  

* Login with message flashing - Advanced Feature  
http://flask.pocoo.org/docs/0.11/patterns/flashing/  

* Other References  
http://stackoverflow.com/questions/19759349/how-to-insert-variable-into-sqlite-database-in-python
http://getbootstrap.com/  
http://flask.pocoo.org/docs/0.11/    

* Images  
https://aptonic.com/blog/wp-content/uploads/2015/08/python-logo.png  
http://zewaren.net/site/sites/default/files/imagepicker/1/FlaskLogo.png  
http://jaydata.org/Media/Default/Provider/LeadImage/sqlite-1.png    
http://gel.ed.ac.uk/sites/default/files/styles/landscape_breakpoints_theme_uoe_mobile_1x/public/thumbnails/image/bootstrap250x250.png?itok=pRJ7rNAz    
http://webroad.pl/wp-content/uploads/2014/07/css3-logo-250x250.jpg    
http://tupleware.cs.brown.edu/wordpress/wp-content/uploads/2014/03/python.png      
https://davidwalsh.name/demo/html5250.png?preview    
http://jinja.pocoo.org/docs/dev/_static/jinja-small.png   
http://d3gnp09177mxuh.cloudfront.net/tech-page-images/jquery.png    
https://d3nmt5vlzunoa1.cloudfront.net/pycharm/files/2015/12/PyCharm_400x400_Twitter_logo_white.png  
