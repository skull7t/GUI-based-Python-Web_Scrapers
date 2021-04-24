PREREQUISITES

*python should be installed on user's system.

*users are required to create a  FREE account on following link to be able to receive price drop alert on their mail  https://www.mailjet.com/
and thus by  obtaining API key enter the api key in following files
1. amazon_Runcode.py : line 89,90  and also mention sender email at line:103
2. flipkart_runcode.py : line 89,90  and also mention sender email at line:96
3. yahoofin_Runcode.py : line 61,62  and also mention sender email at line:68
 

*users are required to install the following module into the path [C:\Users\Admin\AppData\Local\Programs\Python\Python37-32\Scripts] in 'cmd' window by changing path with 'cd' command followed by the above path or the path you have your python installed

*user's required to install following modules in this cmd window 
1. Beautifulsoup: 'pip install bs4'
2. Requests: 'pip install requests'
3. ToastNotifier: 'pip instal win10toast'
4. pyqt5: 'pip install pyqt'
5. validate_email: 'pip install validate_email'
6. validators: 'pip install validators'
7. mysql_connector: 'pip install mysql-connector' [optional] if you want to store the extracted data in your mysql database
NOTE : logs.py is purely database dependent file so to use it you nees to setup database

*users can connect their local database by making changes to the following files[ NOTE :  MAKE CHANGES ONLY IF YOU KNOW HOW TO SETUP DATABASE IN PYTHON ]	
1. amazon_Runcode.py :  from line 75 onwards.
2. flipkart_runcode.py :  from line 69 onwards.
	
CHANGES IN CODE : { OPTIONAL ONLY IF SOME PATH ERROR TAKES PLACE MAKE THE CHANGES }

FILE: amazon_main.py
CHANGES:
1.At line no.108 specify the path for a image to to be the icon of the Window. [NOTE : FILE TYPE SHOULD BE A .JPEG ]
2.At line no.116 specify the path for a image to to be the Logo of the Window. [NOTE : FILE TYPE SHOULD BE A .JPEG ] 

FILE: flipkart_main.py
CHANGES:
1.At line no.109 specify the path for a image to to be the icon of the Window. [NOTE : FILE TYPE SHOULD BE A .JPEG ]

2.At line no.243 specify the path for a image to to be the Logo of the Window. [NOTE : FILE TYPE SHOULD BE A .JPEG ]

FILE: yahoo_main.py
CHANGES:
1.At line no.168 specify the path for a image to to be the icon of the Window. [NOTE : FILE TYPE SHOULD BE A .JPEG ]

2.At line no.175 specify the path for a image to to be the Logo of the Window. [NOTE : FILE TYPE SHOULD BE A .JPEG ] 

FILE: content_main.py
CHANGES:
1.At line no.55 specify the path for a image to to be the icon of the Window. [NOTE : FILE TYPE SHOULD BE A .JPEG ]

FILE: email_main.py
CHANGES:
1.At line no.95 specify the path for a image to to be the icon of the Window. [NOTE : FILE TYPE SHOULD BE A .JPEG ]


FILE: MainScreen.py
CHANGES:
1.At line no.100 specify the path for a image to to be the icon of the Window. [NOTE : FILE TYPE SHOULD BE A .JPEG ]





















