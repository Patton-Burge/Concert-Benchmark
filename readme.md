# PYTHON BENCHMARK
## WEDNESDAY 30 OCTOBER 2019
-------------------------

#### Goal
To create a terminal based application in python to buy tickets from "The Jefferson" music venue.

#### App Requirements
* The user should only be able to buy a maximum of four tickets to shows that are not sold out
* The shows.json file should update with the number of tickets sold after each transaction
* Each check-in is logged in the transactions.txt file following the same format as the existing logs
* No modifications to the _shape_ of the data file
* All inputs should have _reasonable_ validation

#### Passing & Completion Notes
A student passes the benchmark if.... 
* a user is able to buy a single ticket to a show that is not sold out, log the transaction, and save the show data
* the application is easy to use and understand
* the application is all dynamically loaded (i.e. no hard coding), has basic input validation, and the code is well organized
* runs without error

A student completes this benchmark if...
* all the conditions above are met
* the user is able to buy multiple tickets (no more than four) without exceeding the number of tickets left available
* the code is very well organized and extracted into purposeful functions
* implements some UX features to improve the design and make the information easier to understand
* the ticket.txt file is saved with the most recent ticket purchased (retaining the same formatting, hint: _''.center(40, ' ')_)

Clarification: 'tickets' in the data refers to the number of tickets remaining.

```
                                      /   )
                                     @| ?\
       ._-_.    _____________________@| ?\\
      +|\G/|+  | ____________________@| ?\\\
      +|\./|+  || O  o o o  =|=  |  =@| ?\\\\
      +|\./|+  || O  o o o   |  =|=  | -- ====
       `|H|'   ||______________________||\ \\\
        |a|    |________________________| \ \\\
        |H|    ||MM88MM<<<?<<<XHHHHMMMM||  \ \\\
        |a|    ||M88MM<<<?<<<XHHHMMMMMM||   \ \\\
        |H|    ||88MM<<<?<<<XHHHMMMMMMM||    \ \\\
        |a|    ||8MM<<<?<<<XHHHHMMMMMMM||     \ \\\
        |H|    ||MM<<<?<<<XHHHHMMMMMMMM||      \ \\\
        |H|    ||M<<<?<<<XHHHHMMMMMMMMM||       \ \\\
  _-_   |H|   _-_<<<?<<<XHHHHMMMMMMMMMM||        \ \\\
 /   \  |H|  /   \<?<<<XHHHHMMMMMMMMMMM||         \ \\\
 |    \_|a|_/    |?<<<XHHHHMMMMMMMMMMMM||          \ \\\
 \      |H|      /<<<XHHHHMMMMMMMMMMMMR||    =_     \ \\\   _
  \     |H|     /<<<XHHHHMMMMMMMMMMMRMM||   || |     \ \\\  ||\
   |    '"'    |<<<XHHHHMMMMMMMMMMMRMM8||   | | \   // \\\\ /  \
  /     ===     \<XHHHHMMMMMMMMMMMRMM8R||    | |  \-    \\\\   |
 /      ===   !  \HHHHMMMMMMMMMMMRMM8RM||     \ \       \\\\\\ \
|             | o |HMMMMMMMMMMMMMM988MM||        \\       \\\\  \
|      +---+ /  o |MMMMMMMMMMMMMM988MM<||          \\      \\\\   \
\       ___ /  o  /M/MMMMMRMMMRMM88MM<<||           \ \     \\\\     \
 \     |HHH|    l/MMMMMMMRMMMRMM88MM<<<||           | |     \\\\\\     \
  `-_   \_/   _-MMRMMMMMRMMMRMM88MM<<<?||           | |       \\\\   (O \
     """"""""' ~~~V~~""~~~~~~~~~~~~~~V~~~           \ \      <o=====o    |
                                                     \ \              (O |
                                                       \\                /
                                                         \\_            /
                                                            --_______--
```

##### Other Notes
If you see this posted before 12:30, wait until after lunch to start.\
Once you have completed the assignment you can work on your portfolio, codewars, or appropriate coding practice.