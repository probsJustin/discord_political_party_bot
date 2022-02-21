

default_directory = "./data"
party_file = f'{default_directory}/parties'
congress_file = f'{default_directory}/congress.json'
senate_file = f'{default_directory}/senate.json'
president_file = f'{default_directory}/president.json'
configure_file = f'{default_directory}/configure.json'
server_voting_file = f'{default_directory}/server_voting.json'
server_political_system_file = f'{default_directory}/server_political_systems.json'

async def getMembersNames(members):
    returnObject = ""
    for x in members:
        returnObject += f'{x["name"]} \n'
    return returnObject

async def getPoliticalStructure(server_id):
    returnObject = ""

    political_structure = dict()

    congressReader = open(politics.congress_file)
    senateReader = open(politics.senate_file)
    presidentReader = open(politics.president_file)

    political_structure["congress"] = json.load(congressReader)[server_id]
    political_structure["senate"] = json.load(senateReader)[server_id]
    political_structure["president"] = json.load(presidentReader)[server_id]

    returnObject += f'[President][Leader] : {political_structure["president"]["president_name"]} \n'
    returnObject += f'[President][Party] : {political_structure["president"]["presidential_party_name"]} \n'

    returnObject += f'\n'

    returnObject += f'[Congress][Leader] : {political_structure["congress"]["leader"]} \n'
    returnObject += f'[Congress][Majority] : {political_structure["congress"]["party_of_majority"]} \n'
    returnObject += f'[Congress][Minority] : {political_structure["congress"]["party_of_minority"]} \n'
    returnObject += f'[Congress][Members] : \n'
    returnObject += f'{ await getMembersNames(political_structure["congress"]["members"]) }'

    returnObject += f'\n'

    returnObject += f'[Senate][Leader] : {political_structure["senate"]["leader"]} \n'
    returnObject += f'[Senate][Majority] : {political_structure["senate"]["party_of_majority"]} \n'
    returnObject += f'[Senate][Minority] : {political_structure["senate"]["party_of_minority"]} \n'
    returnObject += f'[Senate][Members] : \n'
    returnObject += f'{ await getMembersNames(political_structure["senate"]["members"]) }'

    return returnObject


async def showOpenVotes(server_id):
    returnObject = ""
    votesReader = open(politics.server_voting_file)
    vote_structure = json.load(votesReader)[server_id]
    returnObject += f'Server Name: {server_id}\n'
    for x in vote_structure:
        returnObject += f'Vote: {x}\n'
        returnObject += f'Time Left: {vote_structure[x]["end_date"]}\n'
    return returnObject

async def showPoliticalPosition(position_type, server_id):
    returnObject = ""
    political_structure = dict()

    congressReader = open(politics.congress_file)
    senateReader = open(politics.senate_file)
    presidentReader = open(politics.president_file)

    political_structure["congress"] = json.load(congressReader)[server_id]
    political_structure["senate"] = json.load(senateReader)[server_id]
    political_structure["president"] = json.load(presidentReader)[server_id]

    if(position_type == "president"):
        returnObject += f'[{position_type}]:\n'
        returnObject += f'{ political_structure[position_type]["president_name"] }'
    else:
        returnObject += f'[{position_type}]:\n'
        returnObject += f'{ await getMembersNames(political_structure[position_type]["members"]) }'

    return returnObject

def startVote(summary, server_id):
    return True

def endVote(vote_id, server_id):
    return True

def appointment(user_id, server_id):
    return True

def removeAppointment(user_id, server_id):
    return True

def castVote(vote_id, user_id, server_id):
    return True

def createPartyGroup(party_name, party_group_name, user_id, server_id):
    return True

def createParty(party_name, user_id, server_id):
    return True

def showParty(party_name, user_id, server_id):
    return True

def showParties(server_id):
    return True

def disbandGroup(user_id, server_id):
    return True

def configure(configure_option, configure_value, user_id, server_id):
    return True

def banUser(user_id, server_id):
    return True

def removeUser(user_id, server_id):
    return True

def deleteChannel(channel_id, server_id):
    return True

def addChannel(channel_id, server_id):
    return True

def addVoiceChannel(channel_id, server_id):
    return True

def changeVoteStartDate(vote_id, new_date_time, server_id):
    return True

def changeVoteEndDate(vote_id, new_date_time, server_id):
    return True

def showVoteTime(vote_id, server_id):
    return True

def impeach(server_id):
    return True