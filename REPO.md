# SQA Course Project
TDCDJL-SQA2023-AUBURN

Lauren Lyons, Caleb Johnson, Dean Lee, & Jordyn Lewis

## Group Activities
Completed - Unpack the project KubeSec.zip.

Completed - Upload project as a GitHub repo on github.com. Format of the repo name is TEAMNAME-SQA2023-AUBURN.

Completed - In your project repo create README.md listing your team name and team members.

Completed - Report your activities and lessons learned. Put the report in your repo as REPO.md

## Deliverables

Report describing what activities your performed and what you have learned.
Logs/screenshots that show execution of forensics, fuzzing, and static analysis.

### Assigned to Lauren Lyons
4.a. Create a Git Hook that will run and report all security weaknesses in the project in a CSV file whenever a Python file is changed and committed.
This part of the project pulls in material learned in Workshop 6 and Workshop 4. 

- The use of git hooks and bandit are required to complete this. Bandit is a static analysis tool for python files. The pre-commit git hook is used so that the project file in our GitHub repo is scanned over every time a Python File is changed and committed. The security weaknesses are reported in the file SecurityChecks.csv.

- As learned from the website, https://www.atlassian.com/git/tutorials/git-hooks, Git Hooks are local to any given Git repository, and they are not copied over to the new repository when you run git clone. And, since hooks are local, .git/hooks directory isn’t cloned with the rest of your project, nor is it under version control. So, to combat this issue, I have copied the pre-commit file and pasted it in the main folder of the Git repo. To use it, simply copy and paste it into your local .git/hooks/ folder. Then once a commit is made, the git hook will run. The image below shows an example of it being run on my computer after the pre-commit file has been moved to the appropriate location.

### Assigned to Deal Lee
4.b. Create a fuzz.py file that will automatically fuzz 5 Python methods of your choice. Report any bugs you discovered by the fuzz.py file. fuzz.py will
be automatically executed from GitHub actions.
- Fuzzing will track the errors and potentially problematic data that goes through the 5 methods and causes errors and throws exceptions. Workshop 9.

### Assigned to Caleb Johnson and Jordyn Lewis
- 4.c. Integrate forensics by modifying 5 Python methods of your choice.

- Material pulled from Workshop 8.
- Caleb had to create a logger called simpleLogger.py and added logging to the functions in main.py and graphtaint.py.
- Jordyn...
