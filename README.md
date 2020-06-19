# Authenticate on Auth0 using username/password

If you are working on a web app that uses Auth0, and you are using their secure login widget to create a secure session, it is not always clear how you can create scripts that can authenticate in the same way.

In most scenarios you do not want programs to authenticate as users, you would rather build out APIs for automated access. Yet the authorised APIs might not always cover all of the same functions as the frontend API.

There are real use cases for trying to use a script to "pretend" to be a user on the front end:
- Unit testing that the frontend api is funcitoning as intended
- Simulating UI actions to test scale and throughput
- Simulating UI actions for the purposes of creating an "active" demo environment

There isn't a lot of documentation available in Auth0's website to help guide a dev through this process, but here is a sample wrapper class in python that will enable a user to simulate a front end user.

To use this class, you need to know the Client Secret for your Auth0 Application, so this is only useful in simulating behaviour on your own application. You cannot use this class to try to build automation for your own login on an application that you do not control.
