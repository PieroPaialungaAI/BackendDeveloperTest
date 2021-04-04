# BackendDeveloperTest
Description of the codes that I've been used for the Backend Developer test. 
The file __app.py__  creates the server, and by using the http://localhost:8080/ address you can perform one of these function:
I've launched app.py by using the terminal in a folder containing __templates__ that has been used for the score input function. app.py does not require any input to work, so the terminal input is simple:

```python
python app.py
```

## Login:

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

## Score setting:

The login session will create a dictionary on  user_id.txt that will look like this:
```
{"1": "OOUYHDF"},{"2": "GGAZGQW"},{"3": "VVBXTCE"},{"4": "RRXMFJP"},{"5": "WWWZMME"},{"6": "RRNKFFH"},{"7": "NNZLOEA"},{"8": "FFYXOOU"},{"9": "GGYDDII"},{"10": "GGXDWOP"},{"11": "BBSAZNU"},{"12": "JJACNGJ"},{"13": "UUIWPZI"},{"14": "RRAKLPC"},{"15": "LLXHTFF"},{"16": "WWQSDOT"},{"17": "VVZWUMV"},{"18": "XXLJDQZ"},{"19": "UUPGZYY"},{"20": "SSNGRPL"},
```

Then, by setting a level_id and a specific sessionkey it is possible to save, for that specific user, a specific score. This is done in two steps.

The first one is to use, for example:
```
http://localhost:8080/level_id=1/sessionkey=OOUYHDF
```
That means: select the first level and the user n.1 (that has sessionkey = OOUYHDF).

Once this is done, the second step is to insert an integer value in the specific space that will appear after the previous step is made.



