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

`$ python detect_numbers_image.py  `

You will then be asked which is the name of the image to be processed, place the name based on images found in the images folder. Example: img1

It serves to detect the number of meters of web cam

`$ python detect_numbers_video.py `

As in the previous program you must enter the name of the video processing of the case, otherwise you should write camera to use the webcam.

A box where you will take the first picture (press 'c' to take photo) and analyze.
