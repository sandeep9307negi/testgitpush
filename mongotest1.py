import pymongo
client = pymongo.MongoClient("mongodb+srv://sandeep:Mech0422@cluster0.pstrh.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    'name': 'sandeep' , 'emailid': 'negis9778' , 'surname': 'negi'
}d = {
    'name': 'sandeep' , 'emailid': 'negis9778' , 'surname': 'negi'
}d = {
    'name': 'sandeep' , 'emailid': 'negis9778' , 'surname': 'negi'
}d = {
    'name': 'sandeep' , 'emailid': 'negis9778' , 'surname': 'negi'
}d = {
    'name': 'sandeep' , 'emailid': 'negis9778' , 'surname': 'negi'
}d = {
    'name': 'sandeep' , 'emailid': 'negis9778' , 'surname': 'negi'
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )