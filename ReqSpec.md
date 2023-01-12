# Documentation
## Contents:  
- [1.0 Overview](#10-overview)
  - [1.1 Purpose](#11-purpose)
  - [1.2 Scope](#12-scope)
  - [1.3 Definitions](#13-definitions)
  - [1.4 Breakdown](#14-breakdown)
  - [1.5 Timeline](#15-product-road-map)
- [2.0 Specification](#20-specification)
  - [2.1 Non-functional](#21-non-functional)
  - [2.2 Functional](#22-functional)
- [3.0 Requirements](#30-requirements)
  - [3.1 Non-functional](#31-non-functional)
  - [3.2 Functional](#32-functional)
- [4.0 Diagrams](#40-diagrams)
  - [4.1 User Stories](#41-user-stories-requirements)
    - [4.1.1 Manager](#411-manager)
    - [4.1.2 User (Everyone)](#412-user-everyone-voided-until-further-notice)
    - [4.1.3 Cyber Expert](#413-cyber-expert)
    - [4.1.4 Victim](#414-landlord)
    - [4.1.5 Reasons for using User Stories](#415-reasons-for-using-user-stories)
    - [4.1.6 Assumptions](#416-assumptions)
  - [4.2 Use Case Diagram](#42-use-case-diagram)
    - [4.2.1 Diagram (Requirements)](#421-diagram-requirements)
    - [4.2.2 Reasons for using a Use Case Diagram](#422-reasons-for-using-a-use-case-diagram)
    - [4.2.3 Assumptions](#423-assumptions)
  - [4.3 Sequence Diagram](#43-sequence-diagram)
    - [4.3.1 Diagram (Specification)](#431-diagram-specification)
    - [4.3.2 Reasons for using Sequence Diagram](#432-reasons-for-using-sequence-diagram)
    - [4.3.3 Assumptions](#433-assumptions)
  - [4.4 State Diagram](#44-state-diagram)
    - [4.4.1 Diagram (Specification)](#441-diagram-specification)
    - [4.4.2 Reasons for using a State Diagram](#442-reasons-for-using-a-state-diagram)
    - [4.4.3 Assumptions](#443-assumptions)
  - [4.5 Activity Diagram](#45-activity-diagram-specification)
    - [4.5.1 Diagram 1 (Specification)](#451-diagram-1)
    - [4.5.2 Diagram 2 (Specification)](#452-diagram-2)
    - [4.5.3 Reasons for using Context Diagram](#453-reasons-for-using-activity-diagram)
    - [4.5.4 Assumptions](#454-assumptions)
  - [4.6 Class Diagrams (Specification)](#46-class-diagram-specification)
    - [4.6.1 Diagram (Specification)](#461-diagram)
    - [4.6.2 Reasons for using a State Diagram](#462-reasons-for-using-class-diagram)
    - [4.6.3 Assumptions](#463-assumptions)
- [5.0 Concepts](#50-concepts)
- [6.0 Front-end Development](#60-front-end-development)
  - [6.1 Proof of Concept](#61-proof-of-concept)
- [7.0 Front-end Development](#70-back-end-development)
  - [7.1 Proof of Concept](#71-proof-of-concept)
- [8.0 Prototype 1](#80-prototype-1)
- [9.0 Prototype 2](#90-prototype-2)
- [10.0 Prototype 3](#100-prototype-3)
- [11.0 Prototype 4](#110-prototype-4)



# 1.0 Overview

## 1.1 Purpose
This document will give a detailed description for our program "<!-- Add app name here -->Visualising Cyber Threat Intelligence, A Decision-Making Tool for Cyber Security". This primary purpose of the document will be to give a high-level overview of the development cycle, from requirements and specifications to prototypes and the final program.


## 1.2 Scope
The program [<!-- Add app name here -->] will be used to visualize potential cyber security threats a business may face and provide suitable countermeasures with a list of details on aspects such as countermeasure type, price, ROI, etc. This application will use data from previous threats to predict all the previously mentioned details to the best possible accuracy. It will split the users into 3 different levels and give each a certain amount of control over the application, each user will be able to enter a certain set of data into the program for which it will reply with the optimal solutions using an [<!-- AI OR MATHS MODEL -->].

## 1.3 Definitions

* *ROI : Return of Investment*

* *Priority : Priority is the importance a certain requirment/specification is to the system, scaling from High(Highest priority) to Medium to Low(Lowest priority), with an additional "optional priority"*

## 1.4 Breakdown

We will create two systems that will work together to create this program:  
1. Visualization System:
    - Log in system
    - Registration system
    - Database for above with a log in system
    - General Home page
      - Graph
      - Recent attack breakdown
      - System status
    - Info Page
      - Threat information
    - Countermeasures - optimal choice
      - Safest
      - Optimal
      - Cheapest
2. Decision Making:
    - Log in database
    - Web scraper to get database of all the threats
    - Data aggregation -> filter threats, classify threats
    - Database for system status
    - Database for countermeasures
      - Tier list
      - Budget
      - Cost

## 1.5 Product Road Map

![Diagram](/Images/csa_product_roadmap.png "Product Road Map")

# 2.0 Specification
## 2.1 Non-functional

* **2.1.1** The System should take in data from a CSV and analyze and pre-process for use in the GUI
  * *Priority: High*

* **2.1.2** The system will use a database with hashed passwords to authenticate users of different access levels
  * *Priority: High*

* **2.1.3** The system will provide a status for 0 – 10 systems
  * *Priority: High*

* **2.1.4** The system should be able to generate three countermeasures from the dataset within 1 and 8 seconds 
  * *Priority: High*

* **2.1.5** The system results of the models will be authenticated with online resources to ensure accuracy 
  * *Priority: High*

* **2.1.6** The system should allow the user to toggle currency, changing all values based off an exchange rate 
  * *Priority: Medium*

## 2.2 Functional

* **2.2.1** The system should provide a login system that provides account creation, password change for 2 different user bases
  * *Priority: High*

* **2.2.2** The system should provide a live view of the systems for the company. Updated by an admin user
  * *Priority: Low*

* **2.2.3** The system should allow admin to add company services and alter the status of services 
  * *Priority: Low*

* **2.2.4** The system should take the dataset, pre-processes for threat type, distribution, frequency. Display the data in the form of a graph
  * *Priority: High*

* **2.2.5** The system should display 3 counter measures for a given threat the user is hovering over
  * *Priority: High*

* **2.2.6** The system will provide a model to calculate the Best, Optimal and Cheapest countermeasures for a given threat
  * *Priority: High*

* **2.2.7** The system will display technical details of varying complexity based on the type of user
  * *Priority: High*

* **2.2.8** The system should provide a search functionality to be able to return a countermeasure and a brief description
  * *Priority: Medium*

* **2.2.9** The system should provide a search functionality to allow the user to search for any given threat from the database and return relevant information
  * *Priority: Medium*

* **2.2.10** The system shall provide a page based on a given threat and visualize the cost and display relevant links to the threat
  * *Priority: High*

* **2.2.11** The system will display technical details of varying complexity based on the type of user
  * *Priority: High*

# 3.0 Requirements

## 3.1 Non-functional

* **3.1.1** Concise Datasets: Utilizing data aggregation to display the most amount of data possible in the most efficient format 
  * *Priority: Medium*

* **3.1.2** Fast Maths Models: We will be working with huge datasets, so the average computation time of an operation should be 1 second, with 8 seconds as a hard limit we need to be below 
  * *Priority: High*

* **3.1.3** Decision Maths Model: The model will be able to decide on the cheapest, optimal and safest investment strategies
  * *Priority: High*

* **3.1.4** Model Accuracy: Creating a maths model that is as accurate as possible given the supplied data sets 
  * *Priority: Medium*

* **3.1.5** Currency Conversion: Present all the data in US Dollars, but have the option to convert this amount to other currencies via a fixed exchange rate
  * *Priority: Medium*

* **3.1.6** Data Insertion: System admins should be able to upload their own companies' data given it being in the specified format
  * *Priority: Medium*

* **3.1.7** System Status Switching: A system admin should be able to change the data source in the future the suit companies need 
  * *Priority: Low*

## 3.2 Functional

* **3.2.1** User Login: The user needs to be able to login as a company manager or cyber engineer
  * *Priority: High*

* **3.2.2** Business Login: Home page will display information in terms of cost to the company, hiding more complex data
  * *Priority: Medium*

* **3.2.3** Expert Login: Home page will show a more comprehensive data set and allow for the user to manipulate these models and change data
  * *Priority: Medium*

* **3.2.4** View System Status: User needs to be able to see system status
  * *Priority: Optional/Low*

* **3.2.5** Threat Visualisation Tab: Recent cyber threats/attacks in a graph format 
  * *Priority: High*

* **3.2.6** Hovering over graphs: Hovering over graphs gives a list of the best countermeasures pulled from the countermeasures tab
  * *Priority: High*

* **3.2.7** Countermeasures Tab: User needs to be able to see a list of countermeasures based on a threat 
  * *Priority: High*

* **3.2.8** Countermeasures Search: User is able to search for information about a certain countermeasure by searching for it
  * *Priority: Medium*

* **3.2.9** Threat Search: User is able to search information about threats in a search bar 
  * *Priority: Medium*

* **3.2.10** Threat Viewer Page: User will be able to look at a page giving detailed information about a threat with an associated link to information about the threat.
  * *Priority: High*

* **3.2.11** Recommended Countermeasures Page: A list of our top 3 countermeasures: *Cheapest*; *Optimal*; *Safest*
  * *Priority: High*

# 4.0 Diagrams

## 4.1 User Stories (Requirements)

### 4.1.1 Manager

* **4.1.1.1** As a manager, I want to view the most effective method for securing our network in order to maximize our ROI

* **4.1.1.2** As a manager, I want to be able to view a simplified summary of threats to our network, to make a well-informed decision on how to act 

---
### 4.1.2 User (everyone) VOIDED UNTIL FURTHER NOTICE

<!--
* **4.1.2.1** As a user, I wish to be able to login to the software to view the potential threats to the company network

* **4.1.2.2** As a user, I wish to be able to see more information about a particular threat in order to understand its severity and how to combat it 

* **4.1.2.3** As a user, I wish to view an in-depth description of threats to better understand the effects of them on the company
-->
---
### 4.1.3 Cyber Expert

* **4.1.3.1** As a professional, I wish to be able to change the data set provided to make the models used up to date and as accurate as possible

* **4.1.3.2** As a professional, I wish to view the most recent cyber-attacks to see what areas of the company’s infrastructure are most vulnerable 

* **4.1.3.3** As a professional, I wish to see the system activity in order to see any new threats

* **4.1.3.4** As a professional, I wish to view in depth details on cyber attacks

---
### 4.1.4 Victim

* **4.1.4.1** As a cyber-attack victim, I wish to input information regarding recent attacks for the managers to make a well-informed decision. 

---
### 4.1.5 Reasons for using User Stories

We chose user stories because dealing with cyber threats at a business is often overlooked. User stories gives a first person perspective of different stakeholders, which helps in clarifying what the software should achieve from the clients' standpoint, and gives a rough idea of the priority certain requirements and what the system should be able to deal with.

### 4.1.6 Assumptions

* Cyber Professional has admin access to the system 

## 4.2 Use Case Diagram (Requirements)

### 4.2.1 Diagram

![Diagram](/Images/UseCaseDiagram.jpg "Use Case Diagram")

### 4.2.2 Reasons for using a Use Case Diagram

We used a use case diagram as it clearly outlines the different facets of each actor and what actions that may do on the app, additionally it signifies the level of access (User Access Level) of each actor and arranges them under the system correlating to that. It provides the framework for the actions that each actor can or may wish to complete. The Use Case diagram also clearly sets out both the functional and non-functional requirements of the user which is the foundation of the program

### 4.2.3 Assumptions

## 4.3 Sequence Diagram (Specification)

### 4.3.1 Diagram

![Diagram](/Images/SequenceDiagram.png "Sequence Diagram")

### 4.3.2 Reasons for using Sequence Diagram

We used a sequence diagram as it clearly defined what information would be shared between the users and the relevant system in a clear timeline. Additionally it abstracts the front and back end of the program to show us what each aspect of the program would be enacting

### 4.3.3 Assumptions


## 4.4 State Diagram (Specification)

### 4.4.1 Diagram

![Diagram](/Images/StateDiagram.png "State Diagram")

### 4.4.2 Reasons for using a State Diagram

The state diagram was chosen because, as the name implies, it displays all the states of the program can be in. It states the different abilities of each user, the red box outlining the feature set given to the experts and how they can tinker with the program. The state diagram made it easy to visualize exactly what each user should be capable of doing the the UAL they should have, by creating clear cut lines based on the users ability and knowledge of the given system.

### 4.4.3 Assumptions

## 4.5 Activity Diagram (Specification)

### 4.5.1 Diagram 1

![Diagram](/Images/ActivityDiagrams1.png "Activity Diagram")

### 4.5.2 Diagram 2

![Diagram](/Images/ActivityDiagrams2.png "Activity Diagram")

### 4.5.3 Reasons for using Activity Diagram

The activity diagram was chosen as it shows in a simple way how the users interact with the log in system. The log in system works as follows, the user enters their username and password; it then encounters local validation checks to ensure no illegal characters have been used and the fields have been filled in. This data is then hashed and a connection to the database is established, the login related data is retrieved. The result is then compared to the entries in the database and an appropriate result is sent back to the front end. This depicts a simple idea of how the log in system works and allows us whilst programming to make clean and efficient code as each step and been outlined, similarly with the threat search algorithm a identical comparison can be made. Furthermore, the activity diagram allows us to see how the backend communicates with the front end giving a layer of abstraction.

### 4.5.4 Assumptions

## 4.6 Class Diagram (Specification)

### 4.6.1 Diagram

![Diagram](/Images/ClassDiagram.png "Class Diagram")

### 4.6.2 Reasons for using Class Diagram

Class diagram allow us to show the entity relations between different aspects of the program and how they will interact/relate to one another. The top-level nodes are between the Cyber Security Expert, Businessman and the Maintainer, who has access to server logins and threat databases. These classes will make it easier to create code as we have separated the different *main* features of the program and as a result the diagram makes it easier to visualize the process of the program and ideas on how it would be implemented

### 4.6.3 Assumptions

# 5.0 Concepts

![Diagram](/Images/Prototype1.png "Concept 1")

# 6.0 Front-end Development

## 6.1 Proof of concept

# 7.0 Back-end Development

## 7.1 Proof of concept

# 8.0 Prototype 1

# 9.0 Prototype 2

# 10.0 Prototype 3

# 11.0 Prototype 4