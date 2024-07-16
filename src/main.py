import asyncio
import os
from datetime import datetime
import discord
from discord.ext import tasks
from selenium import webdriver
from selenium.common import NoSuchElementException
from dotenv import load_dotenv

load_dotenv()

client = discord.Client(intents=discord.Intents.none())


@client.event
async def on_ready():
    channel = await client.fetch_channel(int(os.getenv("CHANNEL")))
    await channel.send("up and running")
    await check_for_ticket.start()


@tasks.loop(seconds=30)
async def check_for_ticket():
    channel = await client.fetch_channel(int(os.getenv("CHANNEL")))
    me = await client.fetch_user(int(os.getenv("ME")))
    opts = webdriver.FirefoxOptions()
    # start in headless mode or will throw exception
    opts.add_argument("--headless")
    browser = webdriver.Firefox(options=opts)
    try:
        browser.get(
            "https://tre.ge/en/search?leavingPlace=56014&enteringPlace=57070&leaveDate=31.07.2024&passengerCount=4")
        #wait for the page to load fully
        await asyncio.sleep(6)
        #if the link contains a buisness class ticket, bingo we found it, if not then we throw NoSuchElementException and handle it.
        browser.find_element(by="xpath", value="//*[contains(text(), 'BusinessClass')]")
        await channel.send("Business Class Ticket Found")
        await me.send("Business Class Ticket Found")
        browser.close()
    except NoSuchElementException:
        print(f"ticket available yet {datetime.now()}")
        browser.close()
    except Exception as e:
        await me.send(e)
        browser.close()


client.run(token=os.getenv("TOKEN"))