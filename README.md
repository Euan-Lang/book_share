# book-share
### Now Live
  The site is now live at (https://euanlang28.pythonanywhere.com/bookShare/browse/)
### Setup

To see any style-related changes in the browser, such as adding classes, writing stylesheet declarations, you will need to setup a **Tailwind** compile process. Please see details below.
If you additionally want to enable live reload for any changes made to files in the `static` directory, please also follow the steps in the **Livereload** section below.

#### Tailwind

This project uses CSS framework [Tailwind](https://tailwindcss.com/). Rather than including a link/script tag, as in the case of Bootstrap, tailwind is a compiler that outputs a file CSS bundle file that can be included in the base.html template. Note that Tailwind only adds the styles that are actually used in the html files. So no more extraneous CSS classes crowding the scope as in the case of Bootstrap.

**Steps**

1. Navigate to the project root, open a terminal from there and run `cd static/css/tailwind`
2. Next, run `npm install` If you haven't npm installed on your device, please download and install nodejs on your device from [here](https://nodejs.org/en/download/)
3. Finally, `npm run build:css` This will start a Tailwind watch process that automatically outputs an updated CSS bundle file when you make any style-related changes.

#### Livereload

Livereload is a Python package that you will need to download first into your environment.

1. In a 2nd console tab run `pip install pip install django-livereload-server`
2. And then `python manage.py livereload`
3. In a 3rd console tab `python manage.py runserver`

So to have livereload enabled you should have 3 terminal tabs running simultaneously. Note how this is very easy to do with the integrated terminal in VSCode. ![image](https://user-images.githubusercontent.com/47913749/224489925-5ea9f44d-64e2-4df8-9c2c-1be4eee90f81.png)
Now when you open `127.0.0.1:8000` in the browser, whenever you make changes to any files in the static directory, the webpage should reload automatically with the new changes applied.
