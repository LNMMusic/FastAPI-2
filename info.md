[Token]
- Use middleware on Routers to make a filter for Authentication and Validate the Token and its expiration

- If want to get metadata from the token for getting info about it, like user owner of the token, there are 2 options
    - Use Personalized Token Validation function or Token Metadata from [SERVICE-AUTH] [problem it overrides the middleware function]
    - Use Request objetc to reach to the header and 'authorization' [switable option because it doesn't run too much process]