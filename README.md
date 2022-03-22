#### simpleNginxApp
simple nginx website, Mongodb to collect nginx access log
### How to use
**You can start entire application using below command**
```bash
docker-compose up -d
```

### Table of contents
- **Nginx**
- **Fluentd**
- **MongoDB**
- **Notification Application**

**Sensitive credntials are handled with either env variable or env-files.**


#### Nginx
- Nginx will serve a simple web page.
- Which is protected with HTTP basic auth.
- Location: `nginx`

#### Fluentd
- Fluentd will collect access log and `regex` plugin is used to parse the access log to filter out **agent**,**date** and **response code**.
- Fluentd container has access to nginx access log by mounting nginx access log location into it.
- `Tail` plugin read logs and which is given to `mongodb` output plugin, which is running as another contrainer.
- Location: `fluentd`

#### MongoDB 
- Mongodb container will create a database named 'fluentd' and a collection 'access` with help of `mongodb/mongo-init.js' script at the container startup.
- Location: `mongodb`
- You can view **mongodb collection** below;
```bash
> db.access.find()
{ "_id" : ObjectId("6234cb3be03324000ffdedd5"), "status" : "200", "agent" : "curl/7.58.0", "time" : ISODate("2022-03-19T09:10:36Z") }
{ "_id" : ObjectId("6234cb71e03324000ffdedd6"), "status" : "200", "agent" : "curl/7.58.0", "time" : ISODate("2022-03-19T09:11:30Z") }
{ "_id" : ObjectId("6234cb71e03324000ffdedd7"), "status" : "401", "agent" : "curl/7.58.0", "time" : ISODate("2022-03-19T09:11:34Z") }
{ "_id" : ObjectId("6234cd1ae03324001248bedf"), "status" : "403", "agent" : "curl/7.58.0", "time" : ISODate("2022-03-19T09:18:35Z") }
{ "_id" : ObjectId("6234cd1ae03324001248bee0"), "status" : "403", "agent" : "curl/7.58.0", "time" : ISODate("2022-03-19T09:18:53Z") }
```

#### Notification Application
- This will check for status code every 20 minutes and send email, if it exceedes more than 10 times.
- Location: `notifyApp`
