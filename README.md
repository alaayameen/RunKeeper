# RunKeeper

This Sample django app has 2 ways to manage the RunSessions:
1- Restfull APIs (using TokenAuthenticatio)
2- Web Html forms.


APIs URLs:

1- http://localhost:8000/api-token-auth/
   Also add the following to the request body as json:{"username":"alaa","password":"alaa@123"}
   
   the result is:{"token":"2aff6490fd1c30ce46b3589e0b231f49e0c12ca7"}
   then we need to use this token with every API request to be authenticated, to do so we need to add the following header:
   "Authorization: Token 2aff6490fd1c30ce46b3589e0b231f49e0c12ca7"

2- http://localhost:8000/api/sessions/
    this will reterive all RunSessions
    
3- http://localhost:8000/api/sessions/29
    this will reterive RunSession by id.
    
   


