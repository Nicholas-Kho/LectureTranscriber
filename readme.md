# Respotify - Spotify Statistics 
### Fullstack development of a website. 
### Backend:  Django
### Frontend: React & Nodejs
 All data is taken from the Spotify WebAPI which requires the user to login

## Production Link
https://respotify-test-gsmlc.ondigitalocean.app

## Environment Variables (Production will require these)

To run this project, you will need to add the following environment variables to your .env file

`CLIENT_ID` - Client ID from the Spotify Application

`CLIENT_SECRET` - Client Secret from the Spotify Application

`SPOTIPY_REDIRECT_URI` - Redirect URI

## Deployment

To deploy this project:
- Install all libraries from `requirements.txt`
- Install `node.js` and `django`

Build the static files by running:
```bash
  npm run build
```

```bash
  python manage.py collectstatic
```
Run the application by running:
```bash
  python manage.py runserver
```

## Spotify API
The Spotify API is used to fetch user's song informations. You must create your own Spotify Developer account if you wish to deploy this project.  When the user authenticates, they will be redirected back to a callback URI with their authentication token given back to the server.

## Redirect URI

The redirect URI is the link that the user will get redirected to after successfully authenticating their Spotify account. It must be redirected to the /callback link so that the website is able to read and store the information given from Spotify. `http://127.0.0.1:8000/callback/` may be used as a development callback URI.

