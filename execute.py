from handlers import log
log.info("Importing modules...")
try:
    import requests
except ModuleNotFoundError:
    log.error("Required module \'requests\' not found.\n\nPlease enter the following command to install the module: \'pip install requests\'\nRerun the program when this is complete.")
import sys
import os
from handlers import zip, config
log.success("Modules imported successfully!")

log.info("Loading config...")
config = config.getConfig()
log.success("Config loaded successfully!")

log.info("Getting user...")
usernameURL = "https://api.roblox.com/users/"+sys.argv[1]
usernameRequest = requests.get(url = usernameURL)
if usernameRequest.status_code == 404:
    log.error("User not found.  Please check your input and try again.")
    sys.exit(1)
usernameData = usernameRequest.json()

os.mkdir(usernameData['Username']+"/")
filepath = usernameData['Username']+"/"
log.success("User found!")

log.info("Getting groups...")
groupsURL = "https://api.roblox.com/users/"+sys.argv[1]+"/groups"
groupsRequest = requests.get(url = groupsURL)
groupsData = groupsRequest.json()
with open(filepath+usernameData['Username']+".txt","w") as file:
    file.write("Username: %s (%s)\n\n" % (usernameData['Username'], usernameData['Id']))
    file.write("Groups:\n")
    for k in groupsData:
        try:
            file.write("  - %s (%s) - %s (%s)\n" % (k['Name'], k['Id'], k['Role'], k['Rank']))
        except UnicodeEncodeError:
            try:
                file.write("  - [Error printing group name] (%s) - %s (%s)\n" % (k['Id'], k['Role'], k['Rank']))
            except UnicodeEncodeError:
                file.write("  - [Error printing group name] (%s) - [Error printing rank] (%s)\n" % (k['Id'], k['Rank']))
    file.close()
log.success("Groups found!")

log.info("Getting friends list...")
friendsURL = "https://friends.roblox.com/v1/users/"+sys.argv[1]+"/friends"
friendsRequest = requests.get(url = friendsURL)
friendsData = friendsRequest.json()
log.success("Friends list found!")
friendsCount = 0
processedFriendsCount = 0
for i in friendsData['data']:
    friendsCount += 1
for i in friendsData['data']:
    processedFriendsCount += 1
    log.info("Checking friend "+str(processedFriendsCount)+" of "+str(friendsCount))
    friendGroupsURL = "https://api.roblox.com/users/"+str(i['id'])+"/groups"
    friendGroupsRequest = requests.get(url = friendGroupsURL)
    friendGroupsData = friendGroupsRequest.json()
    with open(filepath+i['name']+".txt","w") as file:
        file.write("Username: %s (%s)\n\n" % (i['name'], i['id']))
        file.write("Groups:\n")
        for k in friendGroupsData:
            try:
                file.write("  - %s (%s) - %s (%s)\n" % (k['Name'], k['Id'], k['Role'], k['Rank']))
            except UnicodeEncodeError:
                    try:
                        file.write("  - [Error printing group name] (%s) - %s (%s)\n" % (k['Id'], k['Role'], k['Rank']))
                    except UnicodeEncodeError:
                        file.write("  - [Error printing group name] (%s) - [Error printing rank] (%s)\n" % (k['Id'], k['Rank']))
        file.close()
    log.success("Finished checking friend "+str(processedFriendsCount)+" of "+str(friendsCount))

zip.main(usernameData['Username'])
