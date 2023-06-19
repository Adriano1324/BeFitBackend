CREATE_USER_MUTATION = """
mutation createUser($avatarImg: String!,
                    $description: String!,
                    $isPublic: Boolean!,
                    $password: String!,
                    $username: String!) {
    createUser(
        userObj: {  username: $username,
                    isPublic: $isPublic,
                    password: $password,
                    description: $description,
                    avatarImg: $avatarImg}
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
"""
