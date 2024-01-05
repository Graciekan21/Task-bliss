## To-Do List Bliss Application
![To-do lisk header](/assets/images/to-do-list.png/)

## Introduction
The To-Do List Bliss Application is a simple command-line tool designed to help users manage their tasks efficiently. Users can add, list, and delete tasks in an easy-to-use interface within the terminal. This application runs in an infinite loop, providing a seamless experience for managing your to-do list.

The deployed project live link is [HERE](https://task-bliss-bb2bc46bd6cf.herokuapp.com/) - ***Use Ctrl (Cmd) and click to open in a new window.*** 

## Contents

- [Introduction](#introduction)
- [Project](#project)
  - [User goals:](#user-goals)
  - [Site owner goals](#site-owner-goals)
- [Pre development](#pre-development)
- [Development](#development)
- [Features](#features)
  - [Add a New Task](#add-a-new-task)
  - [List Tasks](#list-tasksList-Tasks)
  - [Delete Task](#delete-a-taskdelete-Task)
  - [Quit](#quit)
  - [main Function](#main-function)
- [Additional Considerations](#dditional-Considerations)
- [Error Page](#error-page)
 - [Technologies Used](#technologies-used)
- [Resources](#resources)
- [Libraries](#libraries)
 - [Future Updates](#future-updates)  
- [Validation](#validation)
- [Deployment](#deployment)
- [Heroku](#heroku)
- [Branching the GitHub Repository using GitHub Desktop and Visual Studio Code](#branching-the-github-repository-using-github-desktop-and-visual-studio-code)
- [Bugs](#bugs)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

 
## Project 

Aims:
Efficiency Improvement:

- Aim to enhance users' productivity by providing a user-friendly and efficient task management system.
User Engagement:

- Encourage regular use and engagement with the application by offering features that make task management enjoyable and rewarding.
Cross-Platform Accessibility:

- Ensure the application is accessible across various devices and platforms, allowing users to manage their tasks seamlessly on desktop, mobile, and tablet devices.
Customization and Flexibility:

- Provide users with the ability to customize the application to suit their individual preferences and workflow.
Collaboration and Sharing:

- Enable collaboration by allowing users to share tasks and lists with others, fostering teamwork and shared responsibility.

### User goals:

- Task Management:

Users should be able to easily add, edit, and delete tasks.
Prioritize tasks to focus on what's most important.
Set due dates and reminders for tasks.
User-Friendly Interface:

Provide an intuitive and user-friendly interface for quick and efficient task management.
Cross-Platform Access:

Seamless synchronization across devices, enabling users to access their to-do lists wherever they are.
Customization:

User should have the ability to personalize the appearance and settings of the application to suit their preferences.
Collaboration:

Support collaborative features, such as task sharing and commenting, to enhance teamwork and project management.

### Site owner goals

- User Retention:

Aim to keep users engaged by providing regular updates, new features, and improvements to the application.
User Acquisition:

Attract new users through effective marketing strategies, partnerships, and positive user reviews.
Performance and Reliability:

Ensure the application is robust, with minimal downtime and optimal performance to build trust among users.
Data Security and Privacy:

Prioritize the security and privacy of user data, building trust in the application's handling of sensitive information.
Monetization (if applicable):

If the application is a commercial product, aim for a sustainable revenue model that benefits both the users and the business.

### Pre development
By the help of this great tool (Lucid.app) i able  create a flow chart and that what i followed step by step. it cllear of it performance.

![ flow chart](/assets/images/flow-chart.png)


 
### Development

Create a new Python project for the To-Do List App.
Set up the initial project structure, including any necessary folders or files.

I wrote the code following my Flow chart sturcture, section by section.
Setting Up the Project:

Implementing Core Functions:

Write functions for adding tasks, listing tasks, and deleting tasks.
Ensure these functions adhere to the logic outlined in the flowchart.


![ To-do list display](/assets/images/Display.png/)



## Features

### Add a New Task
list_tasks() Function:
Input: User selects to list tasks.
Output: Displays the list of tasks.
Functionality:
Checks if there are any tasks in the list.
If tasks exist, displays each task with its corresponding index.
If no tasks, displays a message indicating that there are no tasks.None specified in the flowchart.

![To-Do List Bliss](/assets/images/to-do-list.png/)

### List Tasks
list_tasks() Function:
Input: User selects to list tasks.
Output: Displays the list of tasks.
Functionality:
Checks if there are any tasks in the list.
If tasks exist, displays each task with its corresponding index.
If no tasks, displays a message indicating that there are no tasks.None specified in the flowchart.

![To-Do list list a task](/assets/images/cc-rm-name.png/)

### Delete a Task
Input: User selects to delete a task and provides the task number.
Output: Success message confirming the task deletion.
Functionality:
Calls list_tasks() to display the current tasks and their indices.
Takes user input for the task number to delete.
Deletes the specified task from the list.
Displays a success message indicating that the task has been deleted.
Error Handling:
Checks if the provided task number is within the valid range of indices.
Displays an error message if the task number is invalid.
None specified in the flowchart.

![To-Do list delete a task](/assets/images/cc-rm-profession-invalid.png)

### Quit
Option 4 allows users to exit the application, ending the to-do list management session.
The application will display a messaga Good Luck

![To-Do list Quit](/assets/images/cc-rm-profession-incorrect.png)

### main() Function:
Input: User selects options from the main menu.
Output: Executes the chosen functionality or quits the application.
Functionality:
Displays the main menu with options for adding, listing, and deleting tasks, and quitting.
Takes user input for their choice.
Calls the corresponding function based on the user's choice.
Loops until the user chooses to quit the application.

![ ](/assets/images/cc-rm-check-information-ok.png)

### Additional Considerations:
User Interface:
Ensure the user interface is clear and provides guidance for each step.
Looping:
Utilize loops to allow users to perform multiple actions without restarting the application.
Error Messages:
Provide informative error messages for better user understanding.


![](/assets/images/.png)

 ### Error Page

A 404 error page has been included. The html was run through the W3C html validator and errors removed. A css style file was created to support the display of the text on the page.


### Display options 
- Add a task
- List a tasks
- Delete a task
- Quit.
This is what Displays when the command is run and the the user can select option by number, it gives all the insturtions needed.

![Display options](assets/images/gsheet-rm-ccccp.png)


## Technologies Used

### Lucid.app
 I used Lucid to create the flow chart which helped mt develop the app.

[Lucid.app](https://lucid.app/)

### ChartGpt 
It was used correcting my Readme with spell checking 

### codebeautify
Was used for indentation, it was my saving grace.

[codebeautify](https://codebeautify.org/python-formatter-beautifier)

### Libraries
[pip3](hhttps://pypi.org/project/pip/a/)

## Validated

The app has been validated and it workes as it should [here-tesSting](https://githu/-p3/blob/main/va.md)


## Future Updates

### User Authentication:

Introduce user authentication to allow multiple users to have personalized to-do lists.
Each user could have a unique login, and their tasks would be stored securely.
Task Priority and Categories:

Implement a feature to prioritize tasks or categorize them (e.g., work, personal, urgent).
Allow users to assign due dates or set reminders for tasks.
Task Details and Notes:

Expand task entries to include additional details or notes.
Provide users with the ability to add descriptions, attachments, or links to tasks.

The ability for a manager to log into the system and confirm working dates and days for each contractor all in one place rather than via separate emails.

Relevant information is accessible by the umbrella company so that HR doesn't have to collate and forward this information.

 ## Validation

pEP8 - Python style guide checker imported - https://pep8ci.herokuapp.com//
 
The App performs well as it should but in the Pep8ci it show (all clear no errors found)
## Deployment

### Heroku

The Application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
2. Create a new app, add a unique app name ( for example Task-Bliss-p3) and then choose your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars add the private API key information using key 'CRED' and into the value area copy the API key information added to the .json file.  Also add a key 'PORT' and value '8000'.
6. Add required buildpacks (further dependencies). For this project, set it up so Python will be on top and Node.js on bottom
7. Go to "Deploy" and select "GitHub" in "Deployment method"
8. To connect Heroku app to your Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below.
9.  Choose the branch you want to build your app from
10. If preferred, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

### Branching the GitHub Repository using GitHub Desktop and Visual Studio Code
1. Go to the GitHub repository.
2. Click on the branch button in the left hand side under the repository name.
3. Give your branch a name.
4. Go to the CODE area on the right and select "Open with GitHub Desktop".
5. You will be asked if you want to clone the repository - say yes.
6. GitHub desktop will suggest what to do next - select Open code using Visual Studio Code.
   
The deployed project live link is [HERE]() - ***Use Ctrl (Cmd) and click to open in a new window.*** 

## Bugs solved

I faced alot of error indent and took me alot untill i used th tab key with the of stackoverflow, and slack

[Bugs solved](hhttps://pypi.org/project/pip/a/)

## Bug unsolved 
I couldn't solve the error though tried but it doesn't affect the code only when the code passes through pEp8ci then it show up. i will look it up how to solve that if i get accounter  with it next time
34: E722 do not use bare 'except'

[Bugs unsolved](hhttps://pypi.org/project/pip/a/)

### Acknowledgments
Special thanks to all contributors who offered invaluable assistance during the development of the To-Do List Application. Your support and insights were instrumental in overcoming challenges and ensuring the success of this project. Your dedication, expertise, and willingness to share knowledge made a significant impact, and I am truly grateful for your contributions. Together, we created a robust and user-friendly To-Do List App that reflects the collaborative spirit of the coding community. Thank you for being an essential part of this journey.

 - His channel helped me alot every time i was stack and understanding the project i wanted to do[@TSInfoTechnologies](​https://www.youtube.com/watch?v=n4YzgrfAIkI&t=140s&ab_channel=TSInfoTechnologies)

helped me in understanding how to delete a task function works[here](https://cppsecrets.com/users/1562979810410511510410110746116105119971141055153485564103109971051084699111109/Python-Delete-a-Task-Lis name - [-or-not/)


This was were i got the form of how to defining the function [here](https://www.javatpoint.com/simple-to-do-list-gui-application-in-python )


Using colorama import - [here](https://www.youtube.com/watch?v=u51Zjlnui4Y )


- His channle helped me alot i got most of the idea from here  [here](https://www.youtube.com/watch?v=TuM-7HjHdaA&ab_channel=Nazal)


I would like to express my heartfelt gratitude to Code Institute for providing an excellent learning environment and resources that enabled me to embark on and complete this coding project. A special thank you to the supportive community of fellow students on Slack, whose collaboration, insights, and encouragement were invaluable throughout this journey. Additionally, immense appreciation goes to my mentor, Jubril, for their guidance, expertise, and unwavering support. This project wouldn't have been possible without the collective efforts of the Code Institute community. Thank you all for being a crucial part of this learning experience.

