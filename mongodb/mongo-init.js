// create application user and collection
var dbUser = getEnvVariable('APP_USER');
var dbPwd = getEnvVariable('APP_PWD');
var dbName = getEnvVariable('DB_NAME');
var dbCollectionName = getEnvVariable('DB_COLLECTION_NAME');
var rootUser = getEnvVariable ('MONGO_INITDB_ROOT_USERNAME');
var rootPass = getEnvVariable ('MONGO_INITDB_ROOT_PASSWORD'); 

db.auth(rootUser, rootPass)

db = db.getSiblingDB(dbName);

db.createUser(
    {
        user: dbUser,
        pwd: dbPwd,
        roles: ["readWrite"]
    }
);

db.createCollection(dbCollectionName);