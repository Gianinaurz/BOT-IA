import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola! soy un bot diseñado para ayudar a detectar medicamentos.{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:        
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await ctx.send(f"El archivo fue guardado en ./{file_name}")
            await attachment.save(f"./{file_name}")

            try:      
                clase = get_class("keras_model.h5", "labels.txt", file_name)                
                if clase[0] == "convencional/comprimido":
                    await ctx.send("Los comprimidos convencionales son pastillas diseñadas para su rapida accion en sus usarios. Una vez ingeridos, se desintegran y se disuelven en el estomago, permitiendo que el fármaco sea absorbido por el cuerpo. Son fáciles de ingerir, y ocultan substancias dificiles de consumir o con mal sabor . Son muy usadas dado a su bajo precio y su fecha de vencimiento es mas extensa. Sin embarg estos comprimibles también tienen algunas desventajas, como el dificil  uso en personas que su cuerpo no puede deglutir o tiene problemas de biodisponibilidad. Existen otros tipos de comprimidos, como los masticables, los efervescentes, los “flash”, los recubiertos, los de capas múltiples, los con cubierta gastrorresistente o entérica, y los bucales. ")
                if clase[0] == "masticable/comprimido":
                    await ctx.send("")
   
   
            except:                
                await ctx.send("Ay, parece que ocurrio un error. Porfavor intentelo de nuevo")
    else:
        await ctx.send("Olvidaste subir una imagen")   

bot.run("tu token ")
