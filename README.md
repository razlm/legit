# Application Name<br />
## Overview<br />
This application provides an HTTP service that allows users to create and manage Keycloak realms.
<br /><br />
## Prerequisites<br />
Before running the application, you must have the following installed on your system:<br /><br />

- Docker<br />
- Docker Compose<br /><br />
## Running the Application<br />
1. Clone the repository:<br />
`git clone https://github.com/razlm/legit.git`
<br /><br />
2. Change to the project directory:<br />
` cd legit `
<br /><br />
3. Build and run the containers using Docker Compose:<br />
` docker-compose up --build `

<br /><br />
## Using the Application<br />
### Creating a Realm<br />
To create a realm, send a POST request to the /create_realm endpoint with the following parameters:
<br />
- realm_name: The name of the realm to create.
<br />

## I've got some issues in the end, you need to exec -it to the flask docker and then run the command - docker ps - docker exec -it <ID> bash and then: <br />

For example:<br />

` curl -X POST   http://localhost:5001/create_realm   -H 'Content-Type: application/json'   -d '{"realm_names": ["myrealmexample"]}' `<br /><br />

### Creating Multiple Realms<br />

To create multiple realms, send a POST request to the /create_realms endpoint with the following parameters:
<br />
- realm_names: A list of realm names to create.<br />
For example:
<br />
` curl -X POST http://localhost:5001/create_realm -H 'Content-Type: application/json' -d '{ "realm_names": ["myrealm1", "myrealm2"]}' `<br /><br />
### Updating Password Creation Policy<br />
To update the password creation policy for all existing realms, send a POST request to the 
/update_password_policy endpoint with the following parameters:
<br /><br />
- min_length: The minimum length of passwords.
- min_lower: The minimum number of lowercase characters in passwords.
- min_upper: The minimum number of uppercase characters in passwords.
- min_digit: The minimum number of digit characters in passwords.
- min_special: The minimum number of special characters in passwords.
<br/ ><br />
For example:
## Not Working well!
<br />
`curl -X POST http://localhost:5001/update_password_policy -d '{"min_length": 8, "min_lower": 1, "min_upper": 
1, "min_digit": 1, "min_special": 1}'`
<br />

