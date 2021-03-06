# Cracking-the-coding-interview
A collection of my solutions to classic Computer Science problems

## Linked Lists

* **[List Cycle](https://github.com/dariack/Cracking-the-coding-interview/blob/master/ListCycle.py)**

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Try solving it using constant additional space.

Example :

Input : 

                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4

Return the node corresponding to node 3. 

* **[Remove Duplicates from Sorted List](https://github.com/dariack/Cracking-the-coding-interview/blob/master/RemoveDuplicatesFromSortedList.py)**

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given `1->1->2`, return `1->2`.
Given `1->1->2->3->3`, return `1->2->3`.

* **[Remove Nth Node from List End](https://github.com/dariack/Cracking-the-coding-interview/blob/master/RemoveNthNodeFromListEnd.py)**

Given a linked list, remove the nth node from the end of list and return its head.

For example,
Given linked list: `1->2->3->4->5`, and `n = 2`.
After removing the second node from the end, the linked list becomes `1->2->3->5`.

Note:
If `n` is greater than the size of the list, remove the first node of the list.
Try doing it using constant additional space.

## Stacks And Queues

* **[Evaluate Expression In Reverse Polish Notation](https://github.com/dariack/Cracking-the-coding-interview/blob/master/EvaluateExpression.py)**

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are `+, -, *, /`. Each operand may be an integer or another expression.

For Example

```
Input 1:
    A =   ["2", "1", "+", "3", "*"]
Output 1:
    9
Explaination 1:
    starting from backside:
    *: ( )*( )
    3: ()*(3)
    +: ( () + () )*(3)
    1: ( () + (1) )*(3)
    2: ( (2) + (1) )*(3)
    ((2)+(1))*(3) = 9
    
Input 2:
    A = ["4", "13", "5", "/", "+"]
Output 2:
    6
Explaination 2:
    +: ()+()
    /: ()+(() / ())
    5: ()+(() / (5))
    1: ()+((13) / (5))
    4: (4)+((13) / (5))
    (4)+((13) / (5)) = 6
```
