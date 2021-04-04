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
