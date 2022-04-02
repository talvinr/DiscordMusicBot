import discord
from discord.exe import commands
import youtube_dl

class music(commands.Cog);
    def__init__(self, client):
        self.client = client



    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("You are not in a voice channel")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.disconnect()
     
    
    
    @commands.command()
    async def disconnect(self,ctx):
         await ctx.voice_client.disconnect()
    
    

    
     @commands.command()
     async def play(self,ctx,url):
          ctx.voice_client.stop()
          FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 
          -reconnect_delay_max 5', 'options': '-vn'}
          YDL_OPTIONS = {'format':"bestaudio"}
          vc = ctx.voice_client
          
          with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:  
     
                            
    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("paused")

    @commands.command()
    async def resume(self,ctx):
         await ctx.voice_client.resume()
         await ctx.send("resumed")                       
                            
                            
           

def setup(client):
    client.add_cog(music(client))

        
