#UTPL
###Professor:
- Rodrigo Barba [lrbarba@utpl.edu.ec](mailto:lrbarba@utpl.edu.ec)

###Student:
- Valeria Quinde [valeestefa15@gmail.com](https://plus.google.com/117826964296158384526/op/profilephoto)

#NUMBERS DETECTION
--------------------------
This work is done in order to put practical knowledge of machine vision using OpenCV and Pyhton, it can be edited and modified by anyone interested in improving it.
It was designed with the purpose of recognizing numbers light meters (eg meter in folder 'images')



System Requirements
-------------------
	•	An i3 or better processor. The faster the better, especially at high video resolutions.
	•	2 GB or more RAM.
	•	At least 100 MB Free Disk space 
	• Windows 7 or later, OS X 10.8 or later (has only been tested on 10.9), Linux 3.0+
	• Mobile device with 3.15 MP camera or more.

Installation
-------------
	1.	First, one should install the following libraries:
	◦	OpenCV version 2.4.10+
	◦	Python 2.7.9 (or any later Python 2.x) (See Installation on OS X if using a Mac)
	◦	Numpy 1.9.2+
	◦	Scipy 0.15.1+
	◦	Mahotas 1.3.0
	◦	Scikit_image 0.11.3
	◦	Scikit_learn 0.16.1
	2.	Now download and extract this repository with one of several options:
	◦	Clone the repository with $ git clone https://github.com/VAUTPL/Deteccion.git
	◦	Download the repository as a .zip or .tar.gz and then extract it.

Installation on OS X
--------------------
Apple uses a prior version of Python that does not support the latest Python libraries. One work around is to install Python with Homebrew:

`$ brew install python`

Replacing Apple's system Python with an unsupported version may break things. Therefore we linked Homebrew's Python into the system path without replacing the system Python:

`$ ln -s /usr/local/Cellar/python/2.x.y/bin/python /bin/hbpython`

Where 2.x.y is the version number of your Python.

Running
-------
From a command line in the folder of the repository:
You can detect with detect_numbers_image.py It serves to detect the number of meters of an image

`$ python detection_numbers_image.py  `

Next, You must write the name of picture, for example "img9"

Example: WRITE THE NAME OF THE PICTURE:img9

Now, We use the webcam device.

`$ python detection_numbers_video.py `

Previous program you must put the name of the video for the test, then you should write "camara" to use the webcam device or "video2" for load the video.

Example: PUT THE NAME 'video2'OR WRITE 'camara' FOR USE THE WEBCAM DEVICE:video2.

In the box red is the place where it take the picture, then press 'c' key. 

ADD NEW IMAGES
-------

If you add new pictures in the images folder, you have to do the following step:

Open the file "generating_samples.py", change the line 

`$ for cont in range(1,23,1):#change the new picture in the folder images `

if you add "2"  new pictures in the images folder, you change the number "23" for "25".

Next, Open the file "training.py", change the line 

`$for j in range(1,106,1):#change the new picture in the folder images`

In this examples, we add 2 new picture, for each one picture to create 5 images in samples folder, then 2 x 5 = 10 new images, this value should be update in the line code.

for example: 

`$for j in range(1,116,1):#change the new picture in the folder images`

In this line you change the number "106" for "116" for update the database of training.

Now, execute this file: "generating_samples.py"

`$ python generating_samples.py`

It is neccesary to execute the training file:

`$ python training.py`



