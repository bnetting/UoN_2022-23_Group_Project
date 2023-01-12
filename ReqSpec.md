# Coursework 1  
## Contents:  
- [1.0 Overview](#10-overview)
  - [1.1 Purpose](#11-purpose)
  - [1.2 Scope](#12-scope)
  - [1.3 Definitions](#13-definitions)
- [2.0 Specification](#20-specification)
  - [2.1 Non-functional](#21-non-functional)
  - [2.2 Functional](#22-functional)
- [3.0 Requirements](#30-requirements)
  - [3.1 Non-functional](#31-non-functional)
  - [3.2 Functional](#32-functional)
- [4.0 Diagrams](#40-diagrams)
  - [4.1 User Stories](#41-user-stories)
    - [4.1.1 Occupant](#411-occupant)
    - [4.1.2 Viewer](#412-viewer)
    - [4.1.3 Letting Agency](#413-letting-agency)
    - [4.1.4 Landlord](#414-landlord)
    - [4.1.5 Quality Inspection Team](#415-quality-inspection-team)s
    - [4.1.6 Reasons for using User Stories](#416-reasons-for-using-user-stories)
  - [4.2 Use Case Diagram](#42-use-case-diagram)
    - [4.2.1 Diagram (Requirements)](#421-diagram-requirements)
    - [4.2.2 Reasons for using a Use Case Diagram](#422-reasons-for-using-a-use-case-diagram)
    - [4.2.3 Key notes for Use Case Diagram](#423-key-notes-for-use-case-diagram)
    - [4.2.4 Assumptions](#424-assumptions)
    - [4.2.5 Questions](#425-questions)
  - [4.3 Sequence Diagram](#43-sequence-diagram)
    - [4.3.1 Diagram 1 (Requirements)](#431-diagram-1-requirements)
    - [4.3.2 Diagram 2 (Specification)](#432-diagram-2-specification)
    - [4.3.3 Diagram 3 (Specification)](#433-diagram-3-specification)
    - [4.3.4 Reasons for using Sequence Diagram](#434-reasons-for-using-sequence-diagram)
    - [4.3.5 Key notes for Sequence Diagram](#435-key-notes-for-sequence-diagram)
    - [4.3.6 Assumptions](#436-assumptions)
    - [4.3.7 Questions](#437-questions)
  - [4.4 State Diagram](#44-state-diagram)
    - [4.4.1 Diagram (Specification)](#441-diagram-specification)
    - [4.4.2 Reasons for using a State Diagram](#442-reasons-for-using-a-state-diagram)
    - [4.4.3 Key notes for State Diagram](#443-key-notes-for-state-diagram)
    - [4.4.4 Assumptions](#444-assumptions)
    - [4.4.5 Questions](#445-questions)
  - [4.5 Context Diagram](#45-context-diagram)
    - [4.5.1 Diagram (Specification)](#451-diagram-specification)
    - [4.5.2 Reasons for using Context Diagram](#452-reasons-for-using-context-diagram)
    - [4.5.3 Key notes for Context Diagram](#453-key-notes-for-context-diagram)
- [5.0 Prototype](#50-prototype)
  - [5.1 Login page](#51-login-page)
  - [5.2 Property list view](#52-property-list-view)
  - [5.3 Specific property view](#53-specific-property-view)
  - [5.4 Landlord page](#54-landlord-page)
  - [5.5 Agency page](#55-agency-page)
  - [5.6 Assumptions](#56-assumptions)
# 1.0 Overview

## 1.1 Purpose
This document will give a detailed description for our program "<!-- Add app name here -->Visualising Cyber Threat Intelligence, A Decision-Making Tool for Cyber Security". This primary purpose of the document will be to give a high-level overview of the development cycle, from requirements and specifications to prototypes and the final program.


## 1.2 Scope
The program "<!-- Add app name here -->" will be used to visualize potential cyber security threats a business may face and provide suitable countermeasures with a list of details on aspects such as countermeasure type, price, ROI, etc. This application will use data from previous threats to predict all the previously mentioned details to the best possible accuracy. It will split the users into 3 different levels and give each a certain amount of control over the application, each user will be able to enter a certain set of data into the program for which it will reply with the optimal solutions using an [<!-- AI OR MATHS MODEL -->]

## 1.3 Definitions

* *ROI : Return of Investment*

* *Priority : Priority is the importance a certain requirment/specification is to the system, scaling from High(Highest priority) to Medium to Low(Lowest priority), with an additional "optional priority"*

# 2.0 Specification
## 2.1 Non-functional

* **2.1.1** Concise Datasets: Utilizing data aggregation to display the most amount of data possible in the most efficient format 
  * *Priority: Medium*

* **2.1.2** Fast Maths Models: We will be working with huge datasets, so the average computation time of an operation should be 1 second, with 8 seconds as a hard limit we need to be below 
  * *Priority: High*

* **2.1.3** Decision Maths Model: The model will be able to decide on the cheapest, optimal and safest investment strategies
  * *Priority: High*

* **2.1.4** Model Accuracy: Creating a maths model that is as accurate as possible given the supplied data sets 
  * *Priority: Medium*

* **2.1.5** Currency Conversion: Present all the data in US Dollars, but have the option to convert this amount to other currencies via a fixed exchange rate
  * *Priority: Medium*

* **2.1.6** Data Insertion: System admins should be able to upload their own companies' data given it being in the specified format
  * *Priority: Medium*

* **2.1.7** System Status Switching: A system admin should be able to change the data source in the future the suit companies need 
  * *Priority: Low*

## 2.2 Functional

* **2.2.1** User Login: The user needs to be able to login as a company manager or cyber engineer
  * *Priority: High*

* **2.2.2** Business Login: Home page will display information in terms of cost to the company, hiding more complex data
  * *Priority: Medium*

* **2.2.3** Expert Login: Home page will show a more comprehensive data set and allow for the user to manipulate these models and change data
  * *Priority: Medium*

* **2.2.4** View System Status: User needs to be able to see system status
  * *Priority: Optional/Low*

* **2.2.5** Threat Visualisation Tab: Recent cyber threats/attacks in a graph format 
  * *Priority: High*

* **2.2.6** Hovering over graphs: Hovering over graphs gives a list of the best countermeasures pulled from the countermeasures tab
  * *Priority: High*

* **2.2.7** Countermeasures Tab: User needs to be able to see a list of countermeasures based on a threat 
  * *Priority: High*

* **2.2.8** Countermeasures Search: User is able to search for information about a certain countermeasure by searching for it
  * *Priority: Medium*

* **2.2.9** Threat Search: User is able to search information about threats in a search bar 
  * *Priority: Medium*

* **2.2.10** Threat Viewer Page: User will be able to look at a page giving detailed information about a threat with an associated link to information about the threat.
  * *Priority: High*

* **2.2.11** Recommended Countermeasures Page: A list of our top 3 countermeasures: *Cheapest*; *Optimal*; *Safest*
  * *Priority: High*

# 3.0 Requirements

## 3.1 Non-functional


## 3.2 Functional



# 4.0 Diagrams

## 4.1 User Stories

### 4.1.1 Occupant
 
---
### 4.1.2 Viewer

### 4.1.3 Letting Agency

### 4.1.4 Landlord


### 4.1.5 Quality Inspection Team


### 4.1.6 Reasons for using User Stories

## 4.2 Use Case Diagram

### 4.2.1 Diagram (Requirements)


### 4.2.2 Reasons for using a Use Case Diagram
 
### 4.2.3 Key notes for Use Case Diagram

### 4.2.4 Assumptions

### 4.2.5 Questions

## 4.3 Sequence Diagram

### 4.3.1 Diagram 1 (Requirements)
 

### 4.3.2 Diagram 2 (Specification)


### 4.3.3 Diagram 3 (Specification)


### 4.3.4 Reasons for using Sequence Diagram


### 4.3.5 Key notes for Sequence Diagram


### 4.3.6 Assumptions


### 4.3.7 Questions

## 4.4 State Diagram

### 4.4.1 Diagram (Specification)


### 4.4.2 Reasons for using a State Diagram


### 4.4.3 Key notes for State Diagram 

### 4.4.4 Assumptions


### 4.4.5 Questions

## 4.5 Context Diagram

### 4.5.1 Diagram (Specification)

### 4.5.2 Reasons for using Context Diagram

### 4.5.3 Key notes for Context Diagram

# 5.0 Prototype

## 5.1 Login page

## 5.2 Property list view

## 5.3 Specific property view

## 5.4 Landlord page


## 5.5 Agency page


### 5.6 Assumptions
