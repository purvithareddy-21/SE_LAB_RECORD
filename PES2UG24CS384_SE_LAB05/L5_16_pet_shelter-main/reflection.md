\# Lab 5: Reflection



\### 1. What did you learn from static code analysis?



I learned that static analysis tools can identify coding-style problems, potential bugs, and security risks without executing the code. Pylint checks code quality, Flake8 checks style and common errors, and Bandit checks for security issues.



\### 2. Which issue was the most important, and why?



SQL injection was an important security risk because unsafe SQL queries can allow user input to change a database command. Parameterized queries help prevent this problem.



\### 3. What changes did you make to improve the code?



I used parameterized SQL queries, avoided mutable default arguments, used the `secrets` module for adoption codes, followed Python naming conventions, and handled empty database query results safely.



\### 4. What did you learn from rerunning the analysis tools?



Rerunning the tools helped me check whether the reported issues had been resolved. The final code received a Pylint score of 10/10, Bandit reported no security issues, and Flake8 produced an empty report. These results indicate improved code quality, although functional testing is also necessary.



