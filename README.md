# **_Issue Identification_**

The initial implementation of the Calendar program had issues that caused incorrect results, specifically regarding double bookings. To address these issues, a step-by-step debugging process was undertaken.

# Review the Provided Code

Upon reviewing the provided code, it was identified that the logic for checking and handling overlapping intervals in the Node class's insert method was not accurate. This discrepancy led to incorrect results when checking for double bookings in the Calendar class.

# Understanding the Problem

The Node class represents nodes in a binary search tree, where each node represents a time interval. The Calendar class is responsible for managing these intervals and checking for double bookings when attempting to schedule a new event.
The underlying issue was that the conditions for inserting a new node into the tree and checking for overlapping intervals were not correctly implemented.

# Correcting the Insertion Logic

To address the issues, the Node class's insert method was revised to properly handle the insertion of intervals. The corrected conditions now consider both left and right subtrees, ensuring accurate placement of intervals based on their start and end times.

# Refactoring and Testing

To improve the readability and maintainability of the code, a private _insert method was added to the Calendar class. This method takes care of the recursive insertion process, allowing for better organization of the code.
After making these corrections, the program was tested using the provided example inputs to ensure that it now produces the expected results.

# Documentation

This README.md file was created to provide clear documentation of the debugging process. It outlines the identified issues, the steps taken to address them, and the rationale behind each correction.
