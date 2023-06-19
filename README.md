# BeFitBackend

## Running app locally
Copy .env.template to .env

Starting containers
```shell
docker compose up backend # Runs db and backend container
```

Migrating database
```shell
docker compose run backend alembic upgrade head  # Creates all tables inside of database
```

Creating new migrations(Only required if you are updating db models)
```shell
docker compose run backend alembic revision --autogenerate -m "message"  # Creates migration file based on models
docker compose run backend alembic upgrade head  # Applies new migration to database
```

After running backend and migrations on address `http://127.0.0.1:8000/graphql` is playground for GraphQl

## Running linters
```shell
docker compose run --rm lint
```

## Running tests
```shell
docker compose run --rm test
```

## Authentication
For authentication we are using JWT

## Example queries

### Create user
```gql
mutation createUser {
  createUser(
    userObj: {username: "qwerty", avatarImg: "qwerty", isPublic: true, password: "qwerty", description: "qwerty"}
  ) {
    ... on User {
      id
      avatarImg
      description
      isActive
      isPublic
      username
    }
    ... on UserExists {
      __typename
      msg
    }
  }
}
```
response if user didn't exist
```json
{
  "data": {
    "createUser": {
      "id": 45,
      "avatarImg": "qwerty",
      "description": "qwerty",
      "isActive": true,
      "isPublic": true,
      "username": "qwerty1"
    }
  }
}
```
response if user exist
```json
{
  "data": {
    "createUser": {
      "__typename": "UserExists",
      "msg": "User with this name already exists"
    }
  }
}
```

### login
```gql
mutation login {
  login(password: "qwerty", username: "qwerty") {
    ... on LoginSuccess {
      __typename
      user {
        avatarImg
        description
        id
        isActive
        isPublic
        username
      }
      token {
        accessToken
        tokenType
      }
    }
    ... on LoginError {
      __typename
      message
    }
    ... on UserNotFound {
      __typename
      msg
    }
  }
}
```
Response if data are correct
```json
{
  "data": {
    "login": {
      "__typename": "LoginSuccess",
      "user": {
        "avatarImg": "qwerty",
        "description": "qwerty",
        "id": 44,
        "isActive": true,
        "isPublic": true,
        "username": "qwerty"
      },
      "token": {
        "accessToken": "Token",
        "tokenType": "Bearer"
      }
    }
  }
}
```
Response if user didn't exist
```json
{
  "data": {
    "login": {
      "__typename": "UserNotFound",
      "msg": "User with this name didn't exist"
    }
  }
}
```
Response if wrong password
```json
{
  "data": {
    "login": {
      "__typename": "LoginError",
      "message": "Wrong password"
    }
  }
}
```
### me
```gql
query current_user {
  current_user {
    ... on User {
      id
      description
      avatarImg
      isPublic
      isActive
      username
    }
    ... on MissingToken {
      __typename
      msg
    }
    ... on ExpiredToken {
      __typename
      msg
    }
  }
}
```
To run this query we need to add Authorization Header
```json
{
  "Authorization": "Bearer Token"
}
```
Response if everything is correct
```json
{
  "data": {
    "current_user": {
      "id": 44,
      "description": "qwerty",
      "avatarImg": "qwerty",
      "isPublic": true,
      "isActive": true,
      "username": "qwerty"
    }
  }
}
```
Response if no Header
```json
{
  "data": {
    "current_user": {
      "__typename": "MissingToken",
      "msg": "Token is missing, please login"
    }
  }
}
```
Response if Expired token
```json
{
  "data": {
    "current_user": {
      "__typename": "ExpiredToken",
      "msg": "Token is expired, please login again"
    }
  }
}
```
