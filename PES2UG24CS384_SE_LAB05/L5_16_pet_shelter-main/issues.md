\# Lab 5: Static Code Analysis 



\# Issues Found and Fixes



| No. | Issue in Original Code | Fix Applied |

|---|---|---|

| 1 | SQL query uses string formatting in `registerPet()`, creating an SQL injection risk. | Used parameterized SQL queries with `?` placeholders. |

| 2 | `tags=\[]` is a mutable default argument, so values can be shared between function calls. | Changed it to `tags=None` and created a new list inside the function. |

| 3 | `random.randint()` is used to generate adoption codes. | Replaced it with `secrets.randbelow()` for more secure random generation. |

| 4 | Function names such as `registerPet()`, `adoptionCode()`, `oldestAvailable()`, and `clearUnadopted()` do not follow Python's snake\_case naming convention. | Renamed them to `register\_pet()`, `adoption\_code()`, `oldest\_available()`, and `clear\_unadopted()`. |

| 5 | `oldestAvailable()` uses a bare `except`, which can hide unexpected errors. | Checked whether the query result is `None` before accessing the pet's name. |

| 6 | `clearUnadopted()` catches all exceptions and silently ignores them. | Removed the unnecessary exception handling so unexpected database errors are not hidden. |

| 7 | `shelterStatus()` uses a one-line `if` statement, reducing readability. | Used a standard multi-line `if` statement. |

| 8 | `adoption\_count` is modified using a global variable inside `adopt()`. | Passed the count as an argument and returned the updated count. |

| 9 | The original code has no module or function docstrings. | Added docstrings to describe the program and its functions. |



