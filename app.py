import discord
import json
import jsonHandler as politics

client = discord.Client()

@client.event
async def on_ready():
    print('US_POL_SYSTEM is ready!')
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$pol'):
        content = message.content.split(' ')

        if(content[1] == "vote"):
            if(content[2] == "ban"):
                await message.channel.send(await politics.banUser(content[3], 'server-id'))
            if(content[2] == "remove"):
                await message.channel.send(await politics.removeUser(content[3], 'server-id'))
            if(content[2] == "delete"):
                if (content[3] == "channel"):
                    await message.channel.send(await politics.deleteChannel(content[3], 'server-id'))
                if (content[3] == "voicechannel"):
                    await message.channel.send(await politics.addVoiceChannel(content[3], 'server-id'))
            if(content[2] == "add"):
                if (content[3] == "channel"):
                    await message.channel.send(await politics.addChannel(content[3], 'server-id'))
                if (content[3] == "voicechannel"):
                    await message.channel.send(await politics.addVoiceChannel(content[3], 'server-id'))

        if(content[1] == "show"):
            if(content[2] == "structure"):
                await message.channel.send(await politics.getPoliticalStructure('server-id'))
            if(content[2] == "votes"):
                await message.channel.send(await politics.showOpenVotes('server-id'))
            if(content[2] == "congress"):
                await message.channel.send(await politics.showPoliticalPosition(content[2], 'server-id'))
            if(content[2] == "senate"):
                await message.channel.send(await politics.showPoliticalPosition(content[2], 'server-id'))
            if(content[2] == "president"):
                await message.channel.send(await politics.showPoliticalPosition(content[2], 'server-id'))
            if (content[2] == "parties"):
                await message.channel.send(await politics.showParties( 'server-id'))
            if(content[2] == "party"):
                await message.channel.send(await politics.showParty(content[2], 'fake-user', 'server-id'))
            if(content[2] == "votetime"):
                await message.channel.send(await politics.showVoteTime(content[3], 'server-id'))

        if(content[1] == "impeach"):
            await message.channel.send(await politics.impeach('server-id'))

        if(content[1] == "debug"):
            if(content[2] == "start"):
                if(content[3] == "vote"):
                    await message.channel.send(await politics.startVote(content[4], 'server-id'))

            if(content[2] == "end"):
                if(content[3] == "vote"):
                    await message.channel.send(await politics.endVote(content[4], 'server-id'))

            if(content[2] == "appoint"):
                if(content[3] == "congress"):
                    await message.channel.send(await politics.appointment(content[4], 'server-id'))
                if (content[3] == "senate"):
                    await message.channel.send(await politics.appointment(content[4], 'server-id'))
                if (content[3] == "president"):
                    await message.channel.send(await politics.appointment(content[4], 'server-id'))

            if(content[2] == "remove"):
                if(content[3] == "congress"):
                    await message.channel.send(await politics.removeAppointment(content[4], 'server-id'))
                if (content[3] == "senate"):
                    await message.channel.send(await politics.removeAppointment(content[4], 'server-id'))
                if (content[3] == "president"):
                    await message.channel.send(await politics.removeAppointment(content[4], 'server-id'))

            if(content[2] == "vote"):
                await message.channel.send(await politics.castVote(content[3], 'fake user', 'server-id'))

            if(content[2] == "create"):
                if(content[3] == "group"):
                    await message.channel.send(await politics.createPartyGroup(content[4], content[5], 'fake user', 'server-id'))
                if (content[3] == "party"):
                    await message.channel.send(await politics.createParty(content[3], 'fake user', 'server-id'))

            if(content[2] == "disband"):
                if(content[3] == "party"):
                    await message.channel.send(await politics.disbandGroup('fake user', 'server-id'))

            if(content[2] == "change"):
                if(content[3] == "end_date"):
                    await message.channel.send(await politics.changeVoteStartDate(content[4], content[5], 'server-id'))
                if(content[3] == "start_date"):
                    await message.channel.send(await politics.changeVoteEndDate(content[4], content[5], 'server-id'))

        if(content[1] == "config"):
            if (content[2] == "president_status"):
                await message.channel.send(await politics.configure(content[2], content[3], 'fake user', 'server-id'))
            if (content[2] == "congress_status"):
                await message.channel.send(await politics.configure(content[2], content[3], 'fake user', 'server-id'))
            if (content[2] == "congress_seats"):
                await message.channel.send(await politics.configure(content[2], content[3], 'fake user', 'server-id'))
            if (content[2] == "senate_status"):
                await message.channel.send(await politics.configure(content[2], content[3], 'fake user', 'server-id'))
            if (content[2] == "senate_seats"):
                await message.channel.send(await politics.configure(content[2], content[3], 'fake user', 'server-id'))
            if (content[2] == "activity"):
                await message.channel.send(await politics.configure(content[2], content[3], 'fake user', 'server-id'))




client.run('')