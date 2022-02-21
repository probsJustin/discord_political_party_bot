import discord
import json

client = discord.Client()


class politics:
    default_directory = "./data"
    party_file = f'{default_directory}/parties'
    congress_file = f'{default_directory}/congress.json'
    senate_file = f'{default_directory}/senate.json'
    president_file = f'{default_directory}/president.json'
    configure_file = f'{default_directory}/configure.json'
    server_voting_file = f'{default_directory}/server_voting.json'
    server_political_system_file = f'{default_directory}/server_political_systems.json'


@client.event
async def on_ready():
    print('US_POL_SYSTEM is ready!')
    print('We have logged in as {0.user}'.format(client))



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


def startVote(server_id):
    return True


def endVote(vote_id, server_id):
    return True


def appointment(user_id, server_id):
    return True


def removeAppointment(user_id, server_id):
    return True

def castVote(vote_id, user_id, server_id):
    return True


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$pol'):
        content = message.content.split(' ')

        if(content[1] == "show"):
            if(content[2] == "structure"):
                await message.channel.send(await getPoliticalStructure('server-id'))
            if(content[2] == "votes"):
                await message.channel.send(await showOpenVotes('server-id'))
            if(content[2] == "congress"):
                await message.channel.send(await showPoliticalPosition(content[2], 'server-id'))
            if(content[2] == "senate"):
                await message.channel.send(await showPoliticalPosition(content[2], 'server-id'))
            if(content[2] == "president"):
                await message.channel.send(await showPoliticalPosition(content[2], 'server-id'))

        if(content[1] == "debug"):
            if(content[2] == "start"):
                if(content[3] == "vote"):
                    await message.channel.send(await startVote(content[4], 'server-id'))

            if(content[2] == "end"):
                if(content[3] == "vote"):
                    await message.channel.send(await endVote(content[4], 'server-id'))

            if(content[2] == "appoint"):
                if(content[3] == "congress"):
                    await message.channel.send(await appointment(content[4], 'server-id'))
                if (content[3] == "senate"):
                    await message.channel.send(await appointment(content[4], 'server-id'))
                if (content[3] == "president"):
                    await message.channel.send(await appointment(content[4], 'server-id'))

            if(content[2] == "remove"):
                if(content[3] == "congress"):
                    await message.channel.send(await removeAppointment(content[4], 'server-id'))
                if (content[3] == "senate"):
                    await message.channel.send(await removeAppointment(content[4], 'server-id'))
                if (content[3] == "president"):
                    await message.channel.send(await removeAppointment(content[4], 'server-id'))

            if(content[2] == "vote"):
                await message.channel.send(await castVote(content[3], 'fake user', 'server-id'))


client.run('')