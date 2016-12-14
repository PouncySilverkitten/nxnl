import json, os, operator, sys

botlings = []
rooms = {}
duplicates = {}
names = []

printRoom = False
printName = False
printDuplicates = False
printPaused = False

for filename in os.listdir(os.getcwd()):
    if "json" in filename:
        file = open(filename)
        botlings.append(json.loads(file.read()))

def printBotsInRoom(room):
    count = 0
    for bot in botlings:
        if bot['room'] == room:
            print(bot['nickname'])
            count += 1
    print("%i botlings in &%s:"%(count,room))

def printStatsForBot(bot):
    code = ""
    creator = ""
    room = []
    paused = []
    print("Stats for @%s:"%(bot))
    for bots in botlings:
        if bots['nickname'] == bot:
            code = bots['code']
            if creator is not "" and creator != bots['creator']:
                print("Multiple bots by that name by different makers.")
                return
            creator = bots['creator']
            room.append(bots['room'])
            if bots['paused']:
                paused.append("Paused")
            else:
                paused.append("Running")
            
    print("Code: %s\nCreator: %s\nRooms: %s\nStatus: %s"%(code,creator,str(room),str(paused)))

def printPausedInRoom(room):
    count = 0
    for bot in botlings:
        if bot['paused'] and bot['room'] == room:
            print(bot['nickname'])
            count += 1
    print("%i paused bots in &%s"%(count,room))



for i in range(0,len(sys.argv)):
    if "--help" in sys.argv[i]:
        print("""Flags:
-r prints rooms in order of highest boting occupancy
-l room prints all botlings present in a room
-n prints a list of all botlings in snapshot
-d prints a list of all botlings with more than one instance
-s @botname prints information about a specific bot
-p prints a list of all paused botlings
-pr room prints a list of all paused botlings in &room""")
    elif "-l" in sys.argv[i]:
        try:
            printBotsInRoom(sys.argv[i+1])
        except:
            print("Room not specified.")
    elif "-r" in sys.argv[i]:
        printRoom = True
    elif "-n" in sys.argv[i]:
        printName = True
    elif "-d" in sys.argv[i]:
        printDuplicates = True
    elif "-s" in sys.argv[i]:
        try:
            printStatsForBot(sys.argv[i+1][1:])
        except:
            print("Botling name not specified.")
    elif "-pr" in sys.argv[i]:
        printPausedInRoom(sys.argv[i+1])
    elif "-p" in sys.argv[i]:
        printPaused = True

if printRoom:
    print("Rooms:\n")
    for bot in botlings:
        if rooms.get(bot['room']) is None:
            rooms[bot['room']] = 1
        else:
            rooms[bot['room']] += 1

    sorted_rooms = sorted(rooms.items(), key=operator.itemgetter(1))
    sorted_rooms = sorted_rooms[::-1]
    for room in sorted_rooms:
        print("&%s: %i"%(room[0],room[1]))

    print("\n\n\n")

if printName:
    count = 0
    for bot in botlings:
        names.append(bot['nickname'])
    names = sorted(names)
    for name in names:
        print(name)
        count += 1
    
    print("\n\n%i botlings"%(count))

if printDuplicates:
    inst_count = 0
    dupe_count = 0
    for bot in botlings:
        if duplicates.get(bot['nickname']) is None:
            duplicates[bot['nickname']] = 1
        else:
            duplicates[bot['nickname']] += 1
            inst_count +=1

    sorted_duplicates = sorted(duplicates.items(), key=operator.itemgetter(1))
    sorted_duplicates = sorted_duplicates[::-1]
    for dupe in sorted_duplicates:
        if dupe[1] > 1:
            print("%s: %i"%(dupe[0],dupe[1]))
            dupe_count += 1
    print("%i excessive instances of %i bots."%(dupe_count,inst_count))
    print("\n\n\n")

if printPaused:
    paused = 0
    for bot in botlings:
        if bot['paused']:
            paused += 1
            print("%s (%s)"%(bot['nickname'],bot['room']))
    print("%i paused botlings."%(paused))
