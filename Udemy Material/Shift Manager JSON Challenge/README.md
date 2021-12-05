Hi. I hope you are doing well. My team would like to develop a hospital shift manager application. We have some frontend designers (ie: UI/UX people), but we need your help as a
backend developer. To make our application work, we need you to help us work with our JSON data on the shifts. 


## Task 1: Hospital Pay
A worker is either a `medic` or `intern`. Per shift, a medic is paid $305 while an intern is paid $142. Build an endpoint that takes in a JSON file called `data.json` and produces a
file called `output.json` that is formatted as the following.
```
{
  "workers": [
    {
      "id": 1,
      "pay": <worker1pay>
    },
    {
      "id": 2,
      "pay": <worker2pay>
    },
    {
      "id": 3,
      "pay": <worker3pay>
    },
    {
      "id": 4,
      "pay": <worker4pay>
    }
  ]
}
```

An example of `data.json` file is like:
```
{
  "workers": [
    { "id": 1, "first_name": "Julie", "status": "medic" },
    { "id": 2, "first_name": "Marc", "status": "medic" },
    { "id": 3, "first_name": "Antoine", "status": "intern" },
    { "id": 4, "first_name": "Emilie", "status": "medic" }
  ],
  "shifts": [
    { "id": 1, "planning_id": 1, "user_id": 1, "start_date": "2017-1-1" },
    { "id": 2, "planning_id": 1, "user_id": 2, "start_date": "2017-1-2" },
    { "id": 3, "planning_id": 1, "user_id": 3, "start_date": "2017-1-3" },
    { "id": 4, "planning_id": 1, "user_id": 4, "start_date": "2017-1-4" },
    { "id": 5, "planning_id": 1, "user_id": 1, "start_date": "2017-1-5" },
    { "id": 6, "planning_id": 1, "user_id": 2, "start_date": "2017-1-6" },
    { "id": 7, "planning_id": 1, "user_id": 3, "start_date": "2017-1-7" },
    { "id": 8, "planning_id": 1, "user_id": 4, "start_date": "2017-1-8" },
    { "id": 9, "planning_id": 1, "user_id": 1, "start_date": "2017-1-9" },
    { "id": 10, "planning_id": 1, "user_id": 2, "start_date": "2017-1-10" }
  ]
}
```
