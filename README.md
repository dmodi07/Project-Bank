# Final Project Report

* Student Name: Dipen Modi
* Github Username: dmodi07
* Semester: Fall 2025
* Course: CS-5001



## Description 
General overview of the project, what you did, why you did it, etc. 

My project was inspired by my visit to the ATM when I looked at the screen. For my project, I really wanted to create something more, like a banking app, with multiple features such as an option to make a deposit, or withdraw money or check balance in account. I also wanted to include the option to have 3 bank accounts - chequing account, savings account and an investment account with options to invest money in fixed interest bonds, and other risky growth investments. 

## Key Features
Highlight some key features of this project that you want to show off/talk about/focus on. 

My project is based on the Bank of Evil, inspired from the movie Despicable Me, boasting some of the baddest villains of all time as loyal customers. Albeit, no matter how bad the villain is, he just cannot get past my (soon to be encrypted) user-authentication system. So each villain (oops, customer!) can only access their own account with their user id and password. If the user does not have an account with the Bank of Evil, the user can choose to either make an account or exit. Each new customer gets a unique account number representing their chequing account. Bank of Evil values their loyal customers and takes their data security extremely seriously. All data is securely stored in a secret JSON database (encryption coming soon!). Once logged in, our clients can check their balance, add more money or make a withdrawal.

## Guide
How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features. 

My project comprises of 4 files, namely -
1. main.py
2. jobs.py
3. bank_account.py
4. clients.json
Each file serves a purpose. `jobs.py` is a python file containing all my helper functions. `bank_account.py` contains a class of different banking transaction-actions, for making a deposit, making a withdrawal or checking account balance. `clients.json` is my database of clients, their user_ids, passwords, names, account numbers and account balance. Needless to say, `main.py` is my main file that ties it all together to make Bank of Evil operable and satisfy my fellow despicable clients, including the cute little minions.


## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.


## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 

### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.

I am very proud of everything to be honest. I never knew I could get this far already. One aspect that gave me a very difficult time was Classes and Objects. I spent a lot of time trying to understand how that works. In addition, navigating through with nested dictionary was both simple and very hard. I still feel like there is so much I am missing and so much more that I want to add to this. Oh and also, I had a lot of difficulty with trying to create a new account number for my new clients, since I have to find the most recent sequential id which is a string in a dictionary value, find it, split it, convert it to int() and then add +1, then convert it back to string and concatenate it with the starting part of the account number. For instance, if my last new customer got account number BE015, then the next new customer who makes an account would get BE016. This turned out to be harder than I had expected. My purpose for making this was to ensure each customer can have three account types - Chequing, Savings and Investment accounts, each with their unique identifier account number. But I must leave this portion for future due to limited time.


## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

Most of my documentation, trial and errors I did on Jupyter Notebooks. Only if it worked on ipynb did I put it on my main/jobs/bank_account files. I will include it with this project for your reference.

## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

Almost every code that I wrote, I tested it on jupyter notebook to ensure it was correct. Only once I was sure that it works did I include it in my project files.

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

There are far too many things I had to leave out due to limited time. This includes the things shared above such as an option to open three different accounts - chequing, savings and investment, an option to invest in different investment options, variable return stocks that are risky, fixed interest stock that is more stable, an option to take a loan at some interest rate. In addition, I wanted to include tools such as a simple calculator, mortgage calculator, credit score, and so on.

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.

I had an extraordinary time with this course. I think it really is designed to force everyone to win without them even realizing it. The amount of activities are perfectly balanced and scattered almost like Boom Beach, a strategy game by Supercell that I used to play back in the day. There is much to discover and each time I sit down with this course, each time I learn something new! That's the best part of it really. I love how some tips are shared in annoucements, some are shared through team activities, some through the homework assignments and some through the report and readme files. It's sooooo coooooool how professor has come up with this and put this all together. When I become a teacher, I will have big shoes to fill, and this project in a way gave me the right exposure to so much more than just python coding curriculum. I think I will be able to do a great job, all thanks to this course. 

### TO DO
---
[ ] Command line prompts \
[ ] Docstring \
[ ] Doctests \
[ ] Testing file \
[ ] Pycodestyle

