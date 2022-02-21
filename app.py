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


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$pol'):
        await message.channel.send(await getPoliticalStructure('server-id'))

client.run('')