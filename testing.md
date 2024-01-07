
# Testing

Once the Application was operating I set for testing it for errors and to ensure that any possible errors can be made were caught.

The deployed project live link is [HERE](/README.mdhttps://task-bliss-bb2bc46bd6cf.herokuapp.com/) - ***Use Ctrl (Cmd) and click to open in a new window.*** 

Here are some sample tests you can perform:

| **Functionality Verification** | **User Interaction and Menu Options** | **Infinite Loop and Quitting** | **Error Handling**|**Edge Cases and Boundary Conditions**|**User Interface and Readability**|
|--------------|----------------|----------------| -------------|-------------------------|---------------|
|Ensure that tasks were added successfully through the add_task() function |
| Verify that the list_tasks() function displays the tasks with their corresponding indices when listing | Confirm that the user is presented with a menu displaying options to add, list, delete tasks, or quit the application| Verify that the application runs in an infinite loop until the user chooses to quit (option 4)| Check that the program handles invalid inputs gracefully, providing clear error messages and allowing the user to continue interacting with the application| Test the application with various scenarios, including an empty task list, deleting tasks from an empty list, and entering non-numeric values for choices | Assess the clarity and readability of the command-line interface, ensuring that prompts and messages are user-friendly|if the user enters unexpected behavior for choice the result is an error so you just click on the run program button to go back to the option display| Tt did not work as expected
|it's Confirmed that the delete_task() function removes a selected task and displays a success message |  Ensure that the program reacts appropriately to the user's choice, calling the corresponding functions| Confirms that selecting option 4 displays the "Good Luck" message and exits the application |  Worked as expected |
|Check that the program correctly handles invalid input by catching ValueError and prompting the user to enter a valid choice | worked as expected | Worked as expected|
|Worked as expected | 

## Testing Browsers
The app was tested in the following browsers (based on my own testing and those of people who tested the app):

- Chrome
- Edge
- Firefox
- Oprea
- Safari

It worked without issues in the above browsers.

## Error page
The error page was not created but if the user does anything unexpected you just need click on the (run programm button) (I couldn't upload the run program button image, i refer to the diplay image)
![run programm](/assets/images/Display.png)

## Future Updates

As a result of testing requests for future functionality include:

It is incorrect without having to start again, when the choice entered is anything else like "space" "letter" besides the choice given the result shouldn#t be error  

Task Details:

Extend the task structure to include additional details (e.g., description, notes). Modify the add_task() and list_tasks() functions to handle and display these details.

Task Completion and Progress Tracking:

Implement a feature to mark tasks as complete. Enhance the list_tasks() function to display completed tasks separately, and add a progress indicator to track overall task completion.
 

### [BACK TO README](https://github.com/Graciekan21/Task-bliss/main/README.md)
