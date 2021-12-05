Hi. I hope you are doing well. My team would like to develop a hospital shift manager application. We have some frontend designers (ie: UI/UX people), but we need your help as a backend developer. To make our application work, we need you to help us work with our JSON data on the shifts. NOTE that `data.json` and example `output.json` files are just examples for sake of formatting. Don't rely on these to "evaluate the correctness of your solution". It is your responsibility to test your implementation on some test cases. Your submission should clearly identify your code specific to `Task 1`, `Task 2`, `Task 3`, `Task 4`


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

## Task 2: Weekends
Saturdays and Sundays are weekend shifts. We want to reward our hardworking medics and interns for taking time to help out the patients in our hospital.
Medics and interns who have shifts on weekends are paid twice the normal fee. Adapt your code from Task 1 to work with this new constraint. Your `output.json` file should be formatted like the above example

## Task 3: Interims
Our hospital shift manager model is to price our service 5% of each shift. In addition to that we also help hospitals to fill in unassigned shifts with `interim` workers.
An interim is paid $543 per shift. We also take a fixed fee of $90 on each shift for which we provided an interim worker.

Adapt the price computation to take these new rules into account and to calculate our commission. Look in `data_interim.json` for example input. Expected output can be found in `output_interim.json`

## Task 4: Hardworkers
Our hospital coordinator would like to recognize the hardwork of each employee. They would like an automated way to identify the hardest working medic, intern, and interim. On the basis of "total pay received", construct a JSON file called `hardworkers.json` that is formatted as such:
```
{
   "medic": <first name of hard working medic>,
   "interim": <first name of hard working interim>,
   "intern": <first name of hard working intern>
}
```

