
mongodb = {'host': 'cluster0.1yisp.mongodb.net/Talett',
         'user': 'dbUser',
         'password': 'Summer00!'}

mongodbConfig = "mongodb+srv://{}:{}@{}?retryWrites=true&w=majority".format(mongodb['user'] ,mongodb['password'], mongodb['host'])

