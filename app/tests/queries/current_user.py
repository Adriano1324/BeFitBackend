CURRENT_USER_QUERY = """
query currentUser {
  currentUser {
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
"""
