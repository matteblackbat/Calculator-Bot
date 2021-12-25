import discord
import math
from discord.ext import commands
import math
from keep_alive import keep_alive
from random import *



client=commands.Bot(command_prefix='!', help_command=None)


def command():
    return '''

    HEY THERE, THIS IS THE CALCULATOR BOT :)

    MATHEMATICAL OPERATIONS/FUNCTIONS AND THEIR CALLOUTS

    ->Addition: !mathadd
    ->Subtraction: !mathsub
    ->Multiplication: !mathmul
    ->Division: !mathdiv
    ->Power: !mathpow
    ->Square Root: !mathsqrt
    ->Average: !mathaverage
    ->Log to base 10: !mathlog10
    ->Logarithm: !mathlog
    ->Factorial: !mathfactorial
    ->Sine (in radians): !mathsin
    ->Cosine (in radians): !mathcos
    ->Tangent (in radians): !mathtan
    ->Cotagent (in radians): !mathcot
    ->Secant (in radians): !mathsec
    ->Cosecant (in radians): !mathcosec

    '''

def sub(x:float,y:float):
    return x-y

def add(x:float,y:float):
    return x+y

def multiply(x:float,y:float):
    return x*y

def divide(x:float,y:float):
    try:
        return x/y
    except ZeroDivisionError:
        return "A number cannot be divided by 0"

def power(x:float,y:int):
    return math.pow(x,y)

def sqrt(x:float):
    return math.sqrt(x)

def average(x:list):
    return sum(x)/len(x)

def log10(x:int):
    try:
        return math.log10(x)
    
    except ValueError:
        return "Natural Log of 0 cannot be found"

def logarithm(x:int,y:int):
    try:
        return math.log(x,y)

    except ValueError:
        return "Log of 0 cannot be found"

def factorial(x:int):
    return math.factorial(x)

    
#TRIGNOMETRIC FUNCTIONS

def sin(x:math.radians):
    return math.sin(x)

def cos(x:math.radians):
    return math.cos(x)

def tan(x:math.radians):
    return math.tan(x)

def cot(x:math.radians):
    return math.cot(x)

def cosec(x:math.radians):
    return math.cosec(x)

def sec(x:math.radians):
    return math.sec(x)

#FUNCTIONS DECLARED

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


#BOT COMMANDS


@client.command()
async def mathadd(message,x:float,y:float):
    result=add(x,y)
    await message.send(result)

@client.command()
async def mathsub(message,x:float,y:float):
    result=sub(x,y)
    await message.send(result)

@client.command()
async def mathmul(message,x:float,y:float):
    result=multiply(x,y)
    await message.send(result)

@client.command()
async def mathdiv(message,x:float,y:float):
    result=divide(x,y)
    await message.send(result)

@client.command()
async def mathpow(message,x:float,y:float):
    result=power(x,y)
    await message.send(result)

@client.command()
async def mathsqrt(message,x:float,y:float):
    result=sqrt(x)
    await message.send(result)

@client.command()
async def mathaverage(message,x:float):
    result=average(x)
    await message.send(result)

@client.command()
async def mathlog10(message,x:float):
    result=log10(x)
    await message.send(result)

@client.command()
async def mathlog(message,x:float,y:float):
    result=logarithm(x,y)
    await message.send(result)

@client.command()
async def mathfactorial(message,x:int):
    result=factorial(x)
    await message.send(result)

@client.command()
async def mathsin(message, x:float):
    result=sin(x)
    await message.send(result)

@client.command()
async def mathcos(message, x:float):
    result=cos(x)
    await message.send(result)

@client.command()
async def mathtan(message,x:float):
    result=tan(x)
    await message.send(result)

@client.command()
async def mathcot(message,x:float):
    result=cot(x)
    await message.send(result)

@client.command()
async def mathcosec(message,x:float):
    result=cosec(x)
    await message.send(result)

@client.command()
async def mathsec(message,x:float):
    result=sec(x)
    await message.send(result)

@client.command()
async def mathcommands(message):
    result=command()
    await message.send(result)


keep_alive()
client.run(('OTIwOTIyNTg0NjM4NDMxMjMy.YbrZ_g.lISRbYBCnibHK9CC7WNXIZDKdfs'))