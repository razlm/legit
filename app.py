from flask import Flask, request
from keycloak import KeycloakAdmin
import time

app = Flask(__name__)
time.sleep(10)
# Keycloak settings
keycloak_admin = KeycloakAdmin(server_url="http://keycloak:8080/auth/",
                               username="admin",
                               password="admin",
                               realm_name="master",
                               verify=True)

# Endpoint to create a realm
@app.route('/create_realm', methods=['POST'])
def create_realm():
    realm_names = request.json['realm_names']

    # Check if realm names are valid subdomains
    for realm_name in realm_names:
        if not realm_name.isalnum():
            return f"Realm name '{realm_name}' is not a valid subdomain (dns).", 400

    # Check if realms with these names already exist
    realm_list = keycloak_admin.get_realms()
    existing_realms = []
    for realm in realm_list:
        if realm['realm'] in realm_names:
            existing_realms.append(realm['realm'])
    if existing_realms:
        return f"Realms '{', '.join(existing_realms)}' already exist.", 409

    # Create realms
    for realm_name in realm_names:
        realm_data = {
            "enabled": True,
            "id": realm_name,
            "realm": realm_name
        }
        keycloak_admin.create_realm(realm_data)

    return f"Realms '{', '.join(realm_names)}' created successfully.", 201


# Endpoint to enforce a new password policy for all existing realms
@app.route('/enforce_password_policy', methods=['POST'])
def enforce_password_policy():
    password_policy = request.json['password_policy']

    # Get all realms
    realm_list = keycloak_admin.get_realms()

    # Update password policy for all realms
    for realm in realm_list:
        realm_name = realm['realm']
        realm_id = realm['id']

        password_policy['id'] = realm_id

        keycloak_admin.update_realm(realm_name, password_policy)

    return "Password policy updated for all realms.", 200


if __name__ == '__main__':
    app.run(debug=True, port=5001)


