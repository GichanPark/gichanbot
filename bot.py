import discord
from discord.ext import commands
import youtube_dl
from datetime import datetime
import asyncio
import time
import random
import os

bot = commands.Bot(command_prefix='차니야 ')
 
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="여니 생각"))
    print('logged in as \nname: {}\n  id: {}'.format(bot.user.name, bot.user.id))
    print('='*80)
    ctx.send("차니 접속 완료.")

@bot.command()
async def empty(ctx, *, txt=None):
    if(text!=None):
        await ctx.send(text)

@bot.command(aliases=['안녕', 'hi', '안녕하세요', '안뇽', '하잉', '하이'])
async def hello(ctx):
    await ctx.send('웅 여니 안뇽')

@bot.command(aliases=['반복', '따라해'])
async def repeat(ctx, *, txt):
    await ctx.send(txt)
 
@bot.command(aliases=['사랑해', '사랑', '러브', '조아해', '좋아해', '사랑행', '좋아행', '조아행'])
async def love(ctx):
    love_list=['헤헤 나두 여니 조아해',
    '사랑해 여니야',
    '여니야 사랑해',
    '여니 조아아아아아악ㄱㄱ가ㅏ가각',
    '이뿌니 사랑해~❤',
    '여니 조아아ㅏ❤',
    '사랑햇!!😀❤']

    random.seed(a=None)
    selected=love_list[random.randrange(len(love_list))]
    await ctx.send(selected)
    
@bot.command(aliases=['귀여워', '귀여웡', '기여엉', '겨웡', '겨워', '겹다'])
async def cute(ctx):
    cute_list=['헤헤 여니도 귀여웡',
    '귀여워 여니야',
    '여니야 귀여워',
    '여니 귀여워어어어어어ㅓ억',
    '이뿌니 귀여워잇~❤',
    '여니 고마웡❤',
    '귀여웟!!!😀❤']

    random.seed(a=None)
    selected=cute_list[random.randrange(len(cute_list))]
    await ctx.send(selected)
    
@bot.command(aliases=['골라줘', '뭐먹지'])
async def select(ctx, *txt):
    random.seed(a=None)
    selected=txt[random.randrange(len(txt))]
    await ctx.send(selected+' 어때?')
    
@bot.command(aliases=['전역 언제야?', '전역', '꽃신언제신어?'])
async def discharge(ctx):
    now=datetime.now()
    dis_day=datetime.strptime("20230125", "%Y%m%d")
    remain_day=dis_day-now

    now=now

    embed=discord.Embed(title='전역')
    embed.add_field(name='오늘', value=now.strftime('%Y-%m-%d'), inline=False)
    embed.add_field(name='전역일', value=dis_day.strftime('%Y-%m-%d'), inline=False)
    embed.add_field(name='전역까지 남은 날짜', value=remain_day, inline=False)
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Flag_of_the_Republic_of_Korea_Armed_Forces.svg/300px-Flag_of_the_Republic_of_Korea_Armed_Forces.svg.png')
    embed.set_image(url='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Emblem_of_the_Ministry_of_National_Defense_%28South_Korea%29_%28Korean%29.svg/270px-Emblem_of_the_Ministry_of_National_Defense_%28South_Korea%29_%28Korean%29.svg.png')

    await ctx.send(embed=embed)

@bot.command(aliases=['정보'])
async def info(ctx):
    embed=discord.Embed(title='박기찬', description='1. 세젤예 세젤귀 표경연의 남자친구 .\n2. 나라의 부름을 받고 군대에 끌려간 사람.', color=0x62c1cc)
    embed.add_field(name='키', value='170(사실 169.6인데 반올림은 국룰이지 ㅋㅋ')
    embed.add_field(name='몸무게', value='70초중반 암튼 돼지 맞음 군대 가서 60 후반으로 만들어서 올 예정 암튼 그럼')
    embed.add_field(name='나이', value='입대할 때는 21살 나올 때는 23살 틀딱 ㅋㅋ')
    embed.add_field(name='학교', value='동국대학교 공과대학 컴퓨터정보통신공학부 정보통신공학 전공')
    embed.add_field(name='입대 및 전역', value='입대 2021년 7월 26일\n전역 2023년 1월 25일\n2023년 오기는 하는 거냐...?')
    embed.set_footer(text='아 빨리 전역하고 싶다.....')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/860035519290277911/860692067495182356/20210620_092454448_iOS.jpg')
    
    await ctx.send(embed=embed)

@bot.command(aliases=['들어와'])
async def join(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
    	channel = ctx.author.voice.channel
    	await channel.connect()
    else:
    	await ctx.send("음성채널에 먼저 들어가고 불렁")

@bot.command(aliases=['나가'])
async def leave(ctx):
    await bot.voice_clients[0].disconnect()
    await ctx.send("나 나가떵,,")

@bot.command(aliases=['재생', '틀어', '재생해줘', '틀어줘'])
async def play(ctx, url):
    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))

@bot.command(aliases=['일시정지', '잠깐'])
async def pause(ctx):
    if not bot.voice_clients[0].is_paused():
        bot.voice_clients[0].pause()
    else:
        await ctx.send("일시정지 할 수 업따")

@bot.command(aliases=['다시', '다시 틀어줘', '다시 재생'])
async def resume(ctx):
    if bot.voice_clients[0].is_paused():
        bot.voice_clients[0].resume()
    else:
        await ctx.send("이미 나오는 중인뎅,,,,,")
        
@bot.command()
async def stop(ctx):
    if bot.voice_clients[0].is_playing():
        bot.voice_clients[0].stop()
    else:
        await ctx.send("일단 재생을 해야 멈출 수 이썽 바보야")

@bot.command(aliases=['아파'])
async def hurt(ctx):
    await ctx.send('여니 아픈 곳 호오호오,,,, 우리 애기 아프지 망,,,,,,,,')

@bot.command(aliases=['편지', '할 말'])
async def letter(ctx, num):
    letters=['1. 7월 26일',
    '2. 7월 27일',
    '3. 7월 28일',
    '4. 7월 29일',
    '5. 7월 30일',
    '6. 7월 31일']

    selected=letters[int(num-1)]
    await ctx.send(selected)

@bot.command()
async def test(ctx):
    now_hour=time.strftime('H', time.localtime(time.time()))
    await ctx.send(now_hour)
    if(now_hour>=12):
        await ctx.send('오후')
    if(now_hour<12):
        await ctx.send('오전')

#@bot.command(aliases=['머해', '뭐해', '뭐하고이써', '뭐하고있어', '머해?', '뭐해?', '머행', '뭐행'])
#async def what(ctx):
#    now_hour=time.strftime('H', time.localtime(time.time()))
    #if()

token=os.environ['bot_token']
bot.run(token)
