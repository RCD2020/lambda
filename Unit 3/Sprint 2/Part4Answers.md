# Answers for Unit 3 Sprint 2 Part 4

## In the Northwind database, what is the type of relationship between the Employee and Territory tables?

There is no direct relationship between the Employee and the Territory table. However there is a middle man. The Employee and EmployeeTerritory have a One to Many relationship, meaning that every record in Employee can have more than one entries in EmployeeTerritory that correlate. Territory is related to EmployeeTerritory with the same relationship, where Territory entries can relate to many EmployeeTerritory entries. By extension, this makes Employee indirectly related to Territory on a many to many basis.

## What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?

A document store like MongoDB is more appropriate when we are handling Big Data that is more complex, larger, and is more volatile. The reason for this is because a document database doesn't save it's data in multiple tables like a relational database, it's all one table, making it good for data that changes often, as you only need to change some values in one table instead of hunting down multiple values in several tables.

## What is "NewSQL", and what is it trying to achieve?

NewSQL is a new kind of relational databases that while still maintaining it's system of having multiple tables of associated table, attempt to make it as scalable and accessible as a document database.