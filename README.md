
# Website project with django appointment scheduling

A small website, allowing a coach to have an appointment system for his future clients. I did this project as part of an AI and data technician training at french [Simplon](https://simplon.co/) school. With the objective of integrating the next big promotion for the continuation of the training.

## Features

### Client features

- Registration system (Responsive w/ pure CSS)
- Connection system (Responsive w/ pure CSS)
- Appointment booking form
- View his appointment history

### Coach features

- View all patients in the appointment history
- Can write a note about an appointment (not visible to the patient)


## Deployment

This project was realized with PyCharm Professional. 
It is PyCharm that created my environment, normally everything should be working on your machine, if it is not the case you can always open an issue.

PyCharm uses the VirtualEnv environment, I advise you to choose this one or the one from Miniconda.

If you don't know how to create an environment, these links may help you:

- [Create a Venv environment](https://docs.python.org/fr/3/library/venv.html)
- [Create a Miniconda environment](https://calculs.univ-cotedazur.fr/?page_id=575&lang=en)


## Requirements

The [requirements.txt](https://github.com/neevaiti/Application_coach_Xu_Wenwu/blob/master/requirements.txt) contains all possible Python packages useful for the project.

You may need [Node-js](https://nodejs.org/en/) to run `npm` commands.

I used a JavaScript library to make a proper notification system.
Normally I have everything pushed from toastify-js, but it may not work for you. If this is the case, here is the github link of [Toastify-js](https://github.com/apvarun/toastify-js).


### Installation of Toastify-js

Run the below command to add toastify-js to your existing or new project.

```bash
  npm install --save toastify-js
```

or 

```bash
yarn add toastify-js -S
```


    
## Run the project Locally

Clone the project

```bash
  git clone https://github.com/neevaiti/Application_coach_Xu_Wenwu.git
```

I advice you to use **`SSH`** method.

```bash
git clone git@github.com:neevaiti/Application_coach_Xu_Wenwu.git
````

Go to the project directory :

```bash
  cd my-project
```

***⚠️ Don't forget to initialize your environment and to activate it ! Before making these commands :***

Do the database migrations :

```bash
python manage.py makemigrations
```

If no error :

```bash
python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```


## Useful Documentation

- [Django](https://www.djangoproject.com/) 
- [Python](https://docs.python.org/3/)


## Authors

- [@neevaiti](https://github.com/neevaiti)


## My opinion on this exercise
I started learning web development, HTML, CSS and JavaScript as a self-taught person. For me, Django is a good way to understand how the web works. Even if the project was done in a "primary" way, without the use of APIs. 
All this to say that I liked this project, because it is the web. And my goal later is to specialize in [React-js](https://reactjs.org/) and back-end in AI or data integration.

