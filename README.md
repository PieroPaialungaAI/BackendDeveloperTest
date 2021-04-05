# BackendDeveloperTest
Description of the codes that I've been used for the Backend Developer test. 
The file __app.py__  creates the server, and by using the http://localhost:8080/ address you can perform one of these function.
I've launched app.py by using the terminal in a folder containing __templates__ that has been used for the score input function. app.py does not require any input to work, so the terminal input is simple:

```python
python app.py
```

## Login:

To perform a login of the _user_id_, it is required to label the user with an integer number. By using this number and the login path, a unique 6 digit string, that is its relative sessionkey will be given. 

Example:

Input:
```
http://localhost:8080/user_id=1/login
```
Output (displayed on the screen and stored on user_id.txt):
```
{"user": "OOUYHDF"}
```

## Score setting:

The login session will create a dictionary on  user_id.txt that will look like this:
```
{"1": "OOUYHDF"},{"2": "GGAZGQW"},{"3": "VVBXTCE"},{"4": "RRXMFJP"},{"5": "WWWZMME"},{"6": "RRNKFFH"},{"7": "NNZLOEA"},{"8": "FFYXOOU"},{"9": "GGYDDII"},{"10": "GGXDWOP"},{"11": "BBSAZNU"},{"12": "JJACNGJ"},{"13": "UUIWPZI"},{"14": "RRAKLPC"},{"15": "LLXHTFF"},{"16": "WWQSDOT"},{"17": "VVZWUMV"},{"18": "XXLJDQZ"},{"19": "UUPGZYY"},{"20": "SSNGRPL"},
```

Then, by setting a level_id and a specific sessionkey it is possible to save, for that specific user, a specific score. This is done in two steps.

The first one is to use, for example:
```
http://localhost:8080/level_id=1/sessionkey=OOUYHDF
```
That means: select the level n.1 and the user n.1 (that has sessionkey = OOUYHDF).

Once this is done, the second step is to insert an integer value in the specific space that will appear after the previous step is made.
This required a basic .html file that is found in the _templates_ folder.

When this process is done, let's say, for all the 20 users that have been selected, you will have a file named _levelID1summary.txt_
...(Obviously, if the level_id is 2 you will have _levelID2summary.txt_)...
It will look like this:


```
OOUYHDF,80/GGAZGQW,10/VVBXTCE,121/RRXMFJP,1000/WWWZMME,0/WWWZMME,1/RRNKFFH,4/NNZLOEA,88/FFYXOOU,97/GGYDDII,882/GGXDWOP,41/BBSAZNU,1900/JJACNGJ,1988/UUIWPZI,100/RRAKLPC,41/LLXHTFF,80000/WWQSDOT,7/VVZWUMV,5000/XXLJDQZ,16/UUPGZYY,20/SSNGRPL,48/
```
***
__NOTE: For example WWWZMME appears two times, but in the highscorelist it will appears only once, with its higher score.__
***

## Highscorelist:

Finally, by using the following input:

```
http://localhost:8080/level_id=1/highscorelist
```

You will have this output:

```
{"sessionkey": ["XXLJDQZ", "UUPGZYY", "GGXDWOP", "RRAKLPC", "SSNGRPL", "OOUYHDF", "NNZLOEA", "FFYXOOU", "UUIWPZI", "VVBXTCE", "GGYDDII", "RRXMFJP", "BBSAZNU", "JJACNGJ", "VVZWUMV"], "scores": [16, 20, 41, 41, 48, 80, 88, 97, 100, 121, 882, 1000, 1900, 1988, 5000]}
```

***
__NOTE: _templates_ is required to work, while _user_id.txt_ and _levelID1summary.txt_ are example output files that I've gotten by using the script. No external frameworks (e.g. numpy,pandas,...,) have been used.__ 
***
