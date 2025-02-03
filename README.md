# Mini-Project

# GUVI Web Application Automation 

## Description

This respository contains a Python pragram that performs GUVI Web Application Automation utilize Selenium WebDriver to automate various test cases.

## Project Description

This project automates testing of the GUVI web application using Python Selenium and Pytest. It covers both positive and negative test cases.

## Program Overview

The program navigates to a specific URL, to check the website is valid or not, the website title is valid or not, buttons are visible, clickable or not, Login and logout fucntions woking correctly or not and using invalid credentials to login in GUVI website.

## Program Descrition

* Functionality: Performs Automation testing on a website.
* Programmer: Naveen Kumar K
* Date: 15 Jan 2025
* Version: 1.0
* Code Library: Selenium
* Prerequisites: Python, Selenium, ChromeDriver

## Requirements

* Python 3.x
* Selenium
* ChromeDriver
* WebDriver Manager

## Installation

Install the required packages using pip:
1. Intal dependencies `pip install selenium webdriver-manager`.
2. Install dependencies: `pip install selenium pytest`.

## Run Tests
Execute the test cases using the following command:
`pytest -v -s Tests`.

## Test Reports
`pytest -v -s --capture=sys --html=Reports\Tests.html Tests`.
After execution, view the generated HTML report in the reports/ directory.
## Running Tests

 * Run all tests:
`pytest Tests`.

