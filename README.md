### **General information**
A bot for monitoring community members will connect their Twitter accounts.\
A tool/API needs to be developed that will track the use of certain hashtags and handles associated with the community, retweets from community Twitter accounts, and participation in community Twitter spaces - all of which will be rewarded with "points" on the dashboard.

### **Communities must be tracked by the API**

* how many times someone likes a @project post
* how many times someone retweets a @project post
* how many times they comment on a @project post
* the number of times that @project retweets one of the community member posts
* the number of times that @project likes one of the community member posts
* the number of times that @project comments on the community member posts
* the time spent in twitter spaces of the @project, or number of spaces attended (we haven't found a solution yet)
* turning on notifications (we are still checking our solution)

### **Bot requirements**

* the bot will record the collected data in a data.json file, which will be stored on the server.
* bot will be configured through a web interface or API.
* the process needs to be automated so that the data is collected on the client platform automatically.

### **Used libs** 
* psycopg2-binary
* tweepy
* redis
* django
* celery

### **Project architecture**

![Project architecture](images/architecture.png "Title")
