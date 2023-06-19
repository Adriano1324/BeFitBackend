LOGIN = """
mutation login($password: String!, $username: String!) {
  login(password: $password, username: $username) {
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
      msg
    }
    ... on UserNotFound {
      __typename
      msg
    }
  }
}
"""
