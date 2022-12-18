import discord
from discord import app_commands

from bot import Bot, Module


class Core(Module):
    @app_commands.command()
    async def sync(self, interaction: discord.Interaction):
        self.bot.tree.copy_global_to(guild=interaction.guild)
        await self.bot.tree.sync(guild=interaction.guild)
        await interaction.response.send_message('Commands synchronised!')


async def setup(bot: Bot):
    await bot.add_cog(Core(bot))
