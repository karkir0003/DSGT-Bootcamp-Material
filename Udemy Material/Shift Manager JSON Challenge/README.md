Hi. I hope you are doing well. My team would like to develop a hospital shift manager application. We have some frontend designers (ie: UI/UX people), but we need your help as a
backend developer. To make our application work, we need you to help us work with our JSON data on the shifts. 


## Task 1: Hospital Pay
A worker is either a `medic` or `intern`. Per shift, a medic is paid $305 while an intern is paid $142. Build an endpoint that takes in a JSON file called `data.json` and produces a
file called `output.json` that is formatted as the following.

`{
  "workers": [
    {
      "id": 1,
      "price": 810
    },
    {
      "id": 2,
      "price": 810
    },
    {
      "id": 3,
      "price": 252
    },
    {
      "id": 4,
      "price": 540
    }
  ]
}`
