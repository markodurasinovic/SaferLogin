# SaferLogin
A tool for generation, storage, and retreival of randomised username-password pairs to allow users to maintain safer online presence.

I was inspired to make this tool after reading the following article:
<https://www.seas.harvard.edu/news/2020/01/imperiled-information>

The idea behind this tool is for the user to generate a new username-password pair for each new website that they sign up for.
This will reduce the likelihood of their leaked data being easily associated through a commonly used username. The username and password are associated via a value provided by the user upon generation (i.e. "facebook") and stored on the user's computer. The user can later retrieve their username-password pair via this identifier.

Password generation and storage are optional. The user can also provide their own password, or simply omit a password altogether since the main purpose of the tool is storage and retreival of complex, randomised usernames for the user's various accounts.