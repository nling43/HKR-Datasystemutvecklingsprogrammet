Task description
When the covid-19 situation arose in early 2020 your small team of developers quickly found out how much questions you used to ask each other in person. Now that you all work from home most of the time you have resorted to using online chat instead. But this has resulted in that you all have to go back and read endless chat logs when you forget what you agreed on earlier.

To remedy this problem, you have decided to write a small script that reads a log file and then allow you to search for all messages sent by one user. To make the script a bit more versatile you have decided that the path to the log file shall be sent as a command line argument to the script. As everyone in the team is a bit sloppy when typing, the script needs to have error handling that clearly informs the user in case the specified path to the log file does not exist. The format of the error message can be seen in this example:

Error: The file ‘/Users/nna/messages.txt’ could not be found.

The script shall have a main function, a function for reading from the log file, and a function for formatting and displaying a message on the screen. There are some rules for how the file-reading function and the display function shall work:

read_file(filename)
Shall read the file specified by the parameter filename and create a list of tuples that is then returned. Each tuple shall consist of a name and a message. In the file each message takes up two rows, where the first row contains the senders name, and the second row contains the text of the message. Each log file can of course contain many messages sent by many different persons.

display_entry(name, message)
Shall use the two parameters to display a formatted output on the screen. The output shall follow this format:
[name] --> message

All other functionality needed in the script shall be added in the main function, this includes but is not limited to asking what name to search the log file for.
