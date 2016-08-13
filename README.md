# RunKeeper

This Sample django app has 2 ways to manage the RunSessions:
1- Restfull APIs (using TokenAuthenticatio)
2- Web Html forms.


APIs URLs:

1- http://localhost:8000/api-token-auth/
   Also add the following to the request body as json:{"username":"alaa","password":"alaa@123"}. (HTTP Method:POST)
   
   the result is:{"token":"2aff6490fd1c30ce46b3589e0b231f49e0c12ca7"}
   then we need to use this token with every API request to be authenticated, to do so we need to add the following header:
   "Authorization: Token 2aff6490fd1c30ce46b3589e0b231f49e0c12ca7"

2- http://localhost:8000/api/sessions/
    this will reterive all RunSessions. (HTTP Method:GET)
    
3- http://localhost:8000/api/sessions/29
    this will reterive RunSession by id. (HTTP Method:GET)
    
4- http://localhost:8000/api/sessions/29/speed
   Calculate the speed of this RunSession. (HTTP Method:GET)
   
5- http://localhost:8000/api/sessions/distance
   This will return the total distance for all RunSessions. (HTTP Method:GET)
   
6- http://localhost:8000/api/sessions/speed/average
   This is to calculate the average speed. (HTTP Method:GET)

7- http://localhost:8000/api/sessions/29/delete
   To delete a specific RunSession if exist. (HTTP Method:DELETE)

8- http://localhost:8000/api/sessions/create
   to create new RunSession by providing JSON object: {"distance": 1000,"duration": 1000}. (HTTP Method:POST)
   
9- http://localhost:8000/api/sessions/27/update
   To update specific RunSession if exist. (HTTP Method:PUT)



WEB FORM:
1- http://localhost:8000/sessions/
   This is the INDEX PAGE you can navigate to CREATE/VIEW/DELETE ..ETC.
   
   
ADMIN PAGE:
I've registered the RunSession so you can do whatever you want
http://localhost:8000/admin/
username:admin
password:admin@123
   


