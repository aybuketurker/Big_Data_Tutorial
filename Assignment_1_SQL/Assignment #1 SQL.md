# Assignment #1 SQL

---

![ryuji](http://nextshark.com/wp-content/uploads/2017/04/cute-dog-shiba-inu-ryuji-japan-17.jpg)

---

### Overview

To unzip the file, type unzip stencil.zip . Now you have all the files you will need for this assignment! You'll see three directories inside the unzipped directory;
problem1 , problem2 , and problem3 , which contain the stencils for your problems. Please use the stencils! (Note: additional files, as well as READMEs, are always welcome (and in the case of READMEs, expected) but traditionally READMEs aren't provided in the stencil.)

---

### Tools

### SQLite

SQLite is installed on all department machines. It can be accessed from the command line using sqlite3 : this will allow you to type your sql queries directly into the terminal. You can exit this environment by pushing ctrl+D or by typing .exit and pressing enter.
To load a pre-existing database, simply run:

` $ sqlite3 /course/cs1951a/pub/assignments/sql/data/[database_file].db`
As a more explicit example, to open a sql environment where you can query the social.db database, you can type:
 `$ sqlite3 /course/cs1951a/pub/assignments/sql/data/social.db`
To execute a SQL statement that you have saved in a file, you can run the following command:
`$ sqlite3 /course/cs1951a/pub/assignments/sql/data/[database_file].db < [query_file].sql `
For problem 1, use social.db . For problem 3, use ikea.db .

For more information on using SQLite from the command line, see http://www.sqlite.org/sqlite.html . Additionally, we have provided very helpful hints for most of the problems; you should be able to use these as a starting point if you get stuck before looking up additional information online.

---

### Problem 1: Social Network Analysis
#### 50 points
We provided a simple database for a social network, social.db . Here's the schema:

>Student(**ID** int, **name** text, **grade** int) <br/>
Friend(**ID1** int, **ID2** int)<br/>
Likes(**ID1** int, **ID2** int)<br/>

In the **Student** table, **ID** is a unique identifier for a particular student. **name** and **grade** correspond to the student's first name and grade.

In the **Friend** table, each (**ID1**, **ID2**) pair indicates that the student with **ID1** is friends with the student with **ID2** (and vice versa). The friendship is mutual, and if (**ID1**, **ID2**) is in the table, it is guaranteed that (**ID2**, **ID1**) exists in the table.

In the **Likes** table, each (**ID1**, **ID2**) pair indicates that the student with **ID1** likes the student with **ID2**. The (**ID1**, **ID2**) pair in the table does not guarantee that the (**ID2**, **ID1**) pair also exists in the table.

If you get stuck, there are many helpful resources on the web for SQL; [here](http://www.w3schools.com/sql/)'s one that many of us have found useful.

1. (2 points) Write a SQL statement that returns the names all students, ordered by name (A-Z). Save the query to **question1.sql**.
Hint: Remember to append all your answers with the ; symbol!
2. (2 points) Write a SQL statement that returns the names of students who are in grade 9. Results should be ordered by name (A-Z). Save the query to **question2.sql**.
Hint: Use the WHERE operation.
3. (4 points) Write a SQL statement that returns the names of students who are liked by at least one other student. Results should be ordered by name (A-Z). Save the query to **question3.sql**.
Careful! Some students are liked multiple times, but their name should only appear once. Take a look at the DISTINCT operator.
Hint: Think about what sort of join you want to use... The following website is quite useful: [link](http://blog.codinghorror.com/a-visual-explanation-of-sql-joins/). Be careful: RIGHT JOIN isn't availaible in sqlite, but you can just frame a RIGHT JOIN as a LEFT JOIN .
4. (6 points) Write a SQL statement that returns the names of students who aren't liked by any other students. Results should be ordered by name (A-Z). Save the query to **question4.sql**.
Hint: A certain type of join, which lets you know when there is nothing corresponding in the other table, is useful here.
5. (6 points) Write a SQL statement that returns the number of students in each grade. You should return the count and then the grade. Results should be ordered by grade (9-12). Save the query to **question5.sql**.
Hint: Use GROUP BY and COUNT .
6. (6 points) Write a SQL statement that returns the number of students not liked by anyone in each grade. Students should NOT be counted twice! You should return the count and then the grade. Results should be ordered by grade (9-12). Save the query to **question6.sql**.
Hint: Combine your previous answers!
7. (8 points) Write a SQL statement that returns the name and grade of all students who have more than 3 friends. Results should be ordered by name (A- Z), then grade (ascending). Save the query to **question7.sql**
Hint: You'll need to take a look at the HAVING function.
8. (8 points) Write a SQL statement that returns the name and grade of all students who are liked by any student who is in a grade below them. Results should be ordered by name (A-Z), then grade (ascending). Save the query to **question8.sql**
Hint: You can do this problem without using two SELECT statements, but doing so makes sure that all your answers are distinct. Also, future problems will require using two SELECT statements, so practicing here isn't a bad idea!
9. (8 points) Write a SQL statement to find pairs (A,B) such that student A likes student B, but A is not friends with B. The query should return 4 columns: ID1, name1, ID2, name2. Results should be ordered by ID1 (ascending), then ID2 (ascending). Save the query to **question9.sql**
Hint: Time to join stuff!
10. (Extra Credit) (3 points) For each pair (A,B) in the previous problem, find all the students C who can introduce them (C is friends with both A and B). The query should return 6 columns: ID1, name1, ID2, name2, ID3, name3. Results should be ordered by ID1 (ascending), ID2 (ascending), then ID3 (ascending). Save the query to **question10.sql**

### Problem 2: SQL Schema, the Sequel to SQL
#### 30 points
For this problem, you will be designing a star-inspired and a snowflake-inspired database schema based on IKEA Furniture. The following contains properties and types of Furniture which your schema must include. Your job is to figure out how to fit the following information into tables which go into your schema.

Your schema should be able to answer any question about the properties listed. Properties are in bold, like **this**.

The types contain properties (for example, Date contains the **year** property). The Furniture type additionally contains multiple sub-types, eg. Table, Bed, etc. These sub-types contain all the properties that Furniture contains, and may contain others; for example, Bed has the **Bed-Size** property, which Table does not have (but which Pull-out Bed Couch does!)

Your schema should also be able to answer any questions about types and sub- types.

Without any further ado, here's the information your schema has to encode:

 > Purchase Properties  <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Date  <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Customer <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Furniture <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Amount of Product**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Price per Product**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Address<br/>

---
> Date Properties<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Year**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Month**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Day**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Quarter**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Day-of-Week**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Hour**<br/>

---
> Customer Properties<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Birthday**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Address<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Loyalty Program Member**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Loyalty Program points** <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Loyalty Program start date**<br/>

---
> Address Properties<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Country**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**State**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**City**<br/>

---
> Furniture Properties<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Name**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Description**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Height**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Width**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Length**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Weight**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Material**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Assembly Box<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**height**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**width**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**length**<br/>

---
> Furniture Types<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bed<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bunk-Bed<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Bed Size**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Single-Bed<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Bed Size**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Double-Bed<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Bed Size**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Couch<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard Couch<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Legs**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pull-out Bed Couch<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Bed Size**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Legs**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Table<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Coffee Table<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Legs**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Kitchen Table<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Legs**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Drawers**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bed-side Table<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Legs**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Drawers**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dining-room Table<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Legs**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Chair<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Desk Chair<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Kitchen Chair<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dining Room Chair<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rocking Chair<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Shelves<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard Shelves<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Num Shelves**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Armoire<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Num Shelves**<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Standard Armoire<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Num Shelves**<br/>

---

Here are some example queries that your schema should be able to answer:

1. What is the average **Weight** of all Furniture?
2. How many **Drawers** do Tables with **Drawers** have on average?
3. What is the most common **Bed Size** among Furniture that contain b eds?
4. How many Tables were sold in 2015?
5. What percentage of Furniture was sold on Fridays in the US?

#### Here are some ideas to get you started:

1. A good start for creating a snow-flake schema is to create a new table for each specific type of item. Once you've done that, figure out where you can flatten out the schema without adding too much redundancy.
2. A good start for creating a star-schema is to try and group really similar items together. There are a couple of tricks you can use to accomplish this:
a. Not all Tables have **Drawers**, but you can always say that a table without any **Drawers** has 0 **Drawers**. Similarly, many countries don't have states, so you could create a special string which represents that there aren't any states.
b. Rather than enumerating lots of sub-types, like Kitchen Chair, Desk Chair, etc., you can create a property which labels each type. Similarly, the Date field in Purchase Properties could be a table or a lot of individual properties (like all the ones listed under Date Properties).
3. Remember to create unique identifiers to link your tables together! For example, a Purchase table almost certainly requires a **Customer ID** property and a **Product ID** property.

To show us your schema, you will hand in two pdfs: star.pdf and
snowflake.pdf , which detail your tables and their relationships. To create them, we
strongly recommend that you use UMLet: it is installed on the department machines and is avaible for download [here](http://www.umlet.com). To run it on a department machine, type umlet . Each schema will be worth 10 points; we will grade them on how credibly you create star and snowflake based schema, and on whether we can extract all the required information from them.

You also need to hand in a txt file, discussion.txt , which explains your choices in each schema, their relative tradeoffs, and which one you think IKEA would prefer to use. Your answers here will be worth 10 points.

---

### Problem 3: K-means 
#### 20 points
K-means clustering is an algorithm designed to sort data into groups based on similarity. To determine the groups, K-means repeatedly performs its update step, detailed by the following pseudocode:

```
For each data_point:
     Determine closest centroid
 For each centroid:
     Determine centroid location as average of data_points which are closest to that centroid
```

To determine the closest centroid, you will be using a variation on Euclidean distance: distance = $(x1 - x2)^2 + (y1 - y2)^2$ . To determine the centroids' new
locations, you average together the data points for which that was the closest centroid.

Your task is to implement one iteration of the update step in SQL.

The data you will be using is in the database ikea . It has the following schema:

>Furniture(**ID** int, **area** int, **cost** int) <br/>
Centroids(**ID** int, **area** int, **cost** int)<br/>

The values you will be comparing to each other are **area** and **cost**; i.e., in the above code x is **area** and y is **cost**. So, we are determining the similarity of different pieces of Furniture by seeing how similar (close in value) their (**area**, **cost**) tuples are when graphed in a Euclidean domain. The **IDs** are unique identifiers for the Furniture and the Centroids.

Hint: It is easiest to view this problem as two composite problems. First, you need associate each data point with a centroid, i.e., the first two lines of the pseudocode. Once each data point is associated with a centroid, you can then determine the new centroid locations (the final two lines of pseudocode). In doing this, you are implicitly creating a new table (perhaps with a SELECT statement?) and then querying the new table.

For more information about K-means, read [here](https://en.wikipedia.org/wiki/K-means_clustering). But don't worry; we will discuss the algorithm in more detail later in the course.

Your answer should return the centroids' **ID** s, **area** s, and **cost** s, in that order, ordered by **ID** (ascending). Save the query to **kmeans.sql**



