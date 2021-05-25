import discord
import os
import requests
import json
import xmltodict
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()


def get_metar_data(IACO, DATA_TYPE):
    AIRPORT_CODE = IACO.strip('$')
    response = requests.get(
        'https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString=krdu&hoursBeforeNow=2')
    # resposne = requests.get('https://aviationweather.gov/metar/data?ids={IACO}&format={DATA_TYPE}&date=&hours=0'.format(IACO=IACO, DATA_TYPE=DATA_TYPE)
    print(response.status_code)

    return response


def xmlToJson(metar_xml):
    metar_dict = xmltodict.parse(metar_xml)
    # metar_json = json.dumps(metar_dict, indent=2)
    return metar_dict


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    print(msg)

    # await message.channel.send('Obtaining Metar for {IACO}'.format(IACO=IACO))

    # metar_response = get_metar_data(IACO, DATA_TYPE)

    # if metar_response.status_code != 200:
    #   await message.channel.send("There was an issue. Please try agin.")
    # else:
    #   print(metar_response.content)
    #   metar_dict = xmltodict.parse(metar_response.content)
    #   print(metar_dict.response)
    #   await message.channel.send('metar_json')

    # if message.content.startswith('$krdu'):
    #   await message.channel.send('obtaining METAR for KRDU')

client.run(os.environ['METAR-TOKEN'])
