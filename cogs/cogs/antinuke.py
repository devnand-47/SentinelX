
import discord
from discord.ext import commands
from datetime import datetime, timedelta

class AntiNuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Threshold: 5 bans in 10 seconds triggers a lockdown
        self.ban_limit = 5 
        self.time_window = 10 
        self.ban_log = {} # Stores timestamp of bans

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        """
        Detects if a user is banning members too fast.
        """
        now = datetime.utcnow()
        
        # Get the audit log to see WHO banned this user
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban):
            attacker = entry.user

        if attacker.id == self.bot.user.id:
            return # Ignore actions done by the bot itself

        # Initialize log for this attacker
        if attacker.id not in self.ban_log:
            self.ban_log[attacker.id] = []

        # Add current ban timestamp
        self.ban_log[attacker.id].append(now)

        # Filter out old bans (older than 10 seconds)
        self.ban_log[attacker.id] = [t for t in self.ban_log[attacker.id] if now - t < timedelta(seconds=self.time_window)]

        # CHECK THRESHOLD
        if len(self.ban_log[attacker.id]) >= self.ban_limit:
            await self.engage_lockdown(guild, attacker)

    async def engage_lockdown(self, guild, attacker):
        """
        Triggers Panic Mode: Bans the attacker and removes permissions.
        """
        print(f"[ALERT] Nuke attempt detected by {attacker} in {guild.name}")
        
        try:
            # 1. Ban the Attacker
            await guild.ban(attacker, reason="SentinelX: Anti-Nuke Triggered (Mass Ban)")
            
            # 2. Alert the Server
            for channel in guild.text_channels:
                if channel.permissions_for(guild.me).send_messages:
                    await channel.send(f"🚨 **SECURITY ALERT** 🚨\nUser `{attacker}` has been banned for attempting to nuke the server.\n**System Status:** Lockdown Active.")
                    break
            
        except discord.Forbidden:
            print(f"[ERROR] Could not ban {attacker}. Check bot hierarchy.")

async def setup(bot):
    await bot.add_cog(AntiNuke(bot))
