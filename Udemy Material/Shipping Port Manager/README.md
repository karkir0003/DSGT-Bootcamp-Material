The COVID-19 Pandemic has severely impacted our supply chain. 
There have been reports of various ports in the United States at a backlog. This would greatly impact holiday shopping through things
like longer delivery times, higher prices, etc to compensate for supply chain issue. See this [link](https://www.cbsnews.com/news/60-minutes-supply-chain-crisis-2021-11-11/).


You have been hired to develop an automated shipping port manager. Let's suppose our fictional port is organized as follows:

1. We have a file called `port_capacity.json` which maps a aisle number to a maximum capacity (by total volume of containers). Example is shown below

```
{
   1: 10000,
   2: 2000,
   3: 500,
   4: 3000
}
```

2. You have a JSON file called `ships.json` which is structured as the following:

```
{
   "ship1": 
   containers: [
            {"name": "Amazon", "length": 2, "width": 3, "height": 5},
            {"name": "Awesome Steel", "length": 5, "width": 6, "height": 10},
            {"name": "Bob's Lumber", "length": 10, "width": 20, "height": 2}
   ],
   "ship2": 
   containers: [
            {"name": "Bob's Burgers", "length": 2, "width": 3, "height": 4},
            {"name": "Timber", "length": 3, "width": 6, "height": 9},
            {"name": "Coconuts", "length": 10, "width": 20, "height": 1}
   ]
   
}
```

## Task 1: 
Given 1 container (ie: a name, length, width, height), find which aisle to put the container in. You must satisfy the volume constraint. There can be multiple places to put the container, so it's up to you how you decide where to put the container. If you are unable to place the container anywhere, you can raise an error/warning. Such a container is "stuck on the ship". Your output file `dock.json` should be formatted as such (as an example to help you):

```
{
   1: [{"name": <insert name1 here>, "length": <insert length1 here>, "width": <insert width1 here>, "height": <insert height1 here>}, {"name": <insert name2 here>, "length": <insert length2 here>, "width": <insert width2 here>, "height": <insert height2 here>}]
   
   2: [{"name": <insert name3 here>, "length": <insert length3 here>, "width": <insert width3 here>, "height": <insert height3 here>}],
   3: []
}
```

## Task 2:
Now that we have an algorithm to determine where to place the containers in the dock, do Task 1, but with an input of `ships.json` instead of solely 1 container's specifications. We are trying to generalize Task 1 to work for any ship. Your output file `dock.json` should be formatted like the above. You should still be able to handle the case where we are unable to place the shipping container in our dock.

## Task 3:
Shipping containers can't just stay in the dock. Holiday shopper's items could be in those containers and these goodies must get to the recipients. We want to develop a way to determine if a certain container is on the dock for a truck to be able to load up. Given the name of a container, see if it exists. If so, return the information about the container (so the name, length, width, height). You should also update `dock.json` accordingly.


**Your code should clearly identify functionality relevant to each task (so identify task 1 functionality, task 2 functionality, task 3 functionality)**

## Tips/Advice:
This challenge could be tricky if you are new to JSON, so I have some tips to make this challenge not seem too daunting:

1. Approach the challenge part by part. The tasks should be done in order and each task builds. The purpose of this challenge is to help you guys build intuition about how you can problem-solve and develop a simple backend endpoint in a given application.
2. This challenge does not come provided with example JSON files. It is your responsibility to construct test files to ensure that your functionality works as intended
3. Please state any assumptions you make with regards to this challenge docstrings/comments in your code. 
4. This challenge is meant to be open ended on purpose to get you to problem solve. In the real world of software engineering, problems are very abstract and learning how to deal with challenging problems proves to be a rewarding learning experience 
5. Feel free to work with others on this challenge. Development is typically done in teams, so it helps to bounce ideas off of each other. Most importantly, make sure that the code for this challenge **is your own work**. We want to see **your understanding** of the material/challenge, not someone else's. 
6. Draw diagrams to help you brainstorm an approach for these problems. Analyzing a problem before coding is highly encouraged in practice.
