import discord
from discord.ext import commands

TOKEN = 'seu token aqui'  # Substitua pelo token do seu bot

class TestBot(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_bot(self):
        await self.wait_until_ready()
        await self.tree.sync()
        print(f'Logado como: {self.user} [{self.user.id}]')
        await self.setup_hook()


    async def on_ready(self):
        print(f'Bot conectado como {self.user.name}')


async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

bot = TestBot(command_prefix=commands.when_mentioned_or("!"), intents=discord.Intents.all())

@bot.command()
async def apagar(ctx, quantidade: int):
    """Apaga uma quantidade especificada de mensagens no canal atual."""
    await ctx.message.delete()  # Deleta o comando usado pelo usuário

    try:
        deleted = await ctx.channel.purge(limit=quantidade + 1)  # Limita a quantidade de mensagens excluídas
        await ctx.send(f'{len(deleted) - 1} mensagens foram apagadas.', delete_after=5)  # Envia mensagem informando a quantidade de mensagens apagadas (excluindo o comando)
    except discord.Forbidden:
        await ctx.send('Eu não tenho permissão para apagar mensagens neste canal.')
    except discord.HTTPException:
        await ctx.send('Ocorreu um erro ao tentar apagar as mensagens.')

bot.run(TOKEN)
