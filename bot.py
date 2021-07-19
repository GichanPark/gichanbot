import discord
from discord.ext import commands
import youtube_dl
import datetime
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
    
@bot.command(aliases=['골라줘', '뭐먹지', '골라봐'])
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
        
@bot.command(aliases=['멈춰'])
async def stop(ctx):
    if bot.voice_clients[0].is_playing():
        bot.voice_clients[0].stop()
    else:
        await ctx.send("일단 재생을 해야 멈출 수 이썽 바보야")

@bot.command(aliases=['아파'])
async def hurt(ctx):
    await ctx.send('여니 아픈 곳 호오호오,,,, 우리 애기 아프지 망,,,,,,,,')

@bot.command(aliases=['편지', '할 말'])
async def letter(ctx, txt):
    letters=['1. 7월 26일',
    '2. 7월 27일',
    '3. 7월 28일',
    '4. 7월 29일',
    '5. 7월 30일',
    '6. 7월 31일']
    
    start=datetime.datetime(2021, 7, 26)
    today=datetime.datetime.today()
    sub=today-start
    start_s=start.strftime('%Y-%m-%d')
    today_s=today.strftime('%Y-%m-%d')
    sub_i=int(sub.days)+1
    await ctx.send(f'입영일:{start_s}, 오늘:{today_s}, 입대: D+{sub_i}')

    if txt=='전체' or txt=='모두':
        for i in range(sub_i):
            await ctx.send(letters[i])
    elif txt=='오늘':
        await ctx.send(letters[sub_i-1])

@bot.command()
async def test(ctx):
    await ctx.send('test')
    now_hour=time.strftime('%H', time.localtime(time.time()))
    now_minute=time.strftime(('%M', time.localtime(time.time())))
    

@bot.command(aliases=['머해', '뭐해', '뭐하고이써', '뭐하고있어', '머해?', '뭐해?', '머행', '뭐행'])
async def what(ctx):
    now_hour=time.localtime(time.time())
    now=int(now_hour.tm_hour)
    await ctx.send(f'지금은 {now}시!')
    if now<=6:
        list=['차니 쿠울쿠울 자는 중',
        '드르렁 푸우푸우 퐈퐈퐈',
        '코오코오..코오...코어ㅓ어ㅓ거ㅓ걱']
        random.seed(a=None)
        selected=list[random.randrange(len(list))]
        await ctx.send(selected)
    elif now<=7:
        list=['아침 점호 중이징!',
        '아침부터 체력단련하는 중~~']
        random.seed(a=None)
        selected=list[random.randrange(len(list))]
        await ctx.send(selected)
    elif now<=8:
        list=['나 어푸어푸 씻는 중!!',
        '슥슥삭삭 청소하는 중이징',
        '냠냠접접 밥 먹는 중이당! 애기도 밥 먹었어?']
        random.seed(a=None)
        selected=list[random.randrange(len(list))]
        await ctx.send(selected)
    elif now<=9:
        list=['차니 학과준비!',
        '차니 출장~']
        random.seed(a=None)
        selected=list[random.randrange(len(list))]
        await ctx.send(selected)
    elif now<=12:
        list=['오전교육 듣는 중....으그극 개노잼 핵 노 잼',
        '교육...시러.....귀차나...쉬마려...',
        '자고싶다 자 고 싶 다']
        random.seed(a=None)
        selected=list[random.randrange(len(list))]
        await ctx.send(selected)
    elif now<=13:
        list=['와구와구 점심 먹는 중',
        '나 점심 먹는 중이징 여니는 밥 뭐 먹엉??',
        '나나ㅏ나 밥 먹고 이따!']
        random.seed(a=None)
        selected=list[random.randrange(len(list))]
        await ctx.send(selected)
    elif now<=16:
        list=['차니 오후교육 듣는 중',
        '나 또 교육 듣는다 노잼이다 차라리 코딩하고 싶다',
        '교육 시러 나 잘 래 ㅜㅜ 여니 안고 잘래']
        random.seed(a=None)
        selected=list[random.randrange(len(list))]
        await ctx.send(selected)
    elif now<=17:
        list=['차니 교보재 반납하는 중',
        '슈르륵 삭삭 청소하는 중이징~',
        '삐까뻔쩍 청소하는 중!!']
        random.seed(a=None)
        selected=list[random.randrange(len(list))]
        await ctx.send(selected)
    elif now<=17:
        list=['운동하는 중이다잇!',
        '체력단련 하는 중!!',
        '나 생활관으로 가는 중이징']
        random.seed(a=None)
        selected=list[random.randrange(len(list))]
        await ctx.send(selected)
    elif now<=19:
        list=['차니 저녁 먹는 중!',
        '정비하는 중이징',
        '지금은 자유시간! 책 읽거나 공부할 듯??']
        random.seed(a=None)
        selected=list[random.randrange(len(list))]
        await ctx.send(selected)
    elif now<=20:
        list=['차니 내무교육 받는 중 ㅜ ㅜ',
        '아니 무슨 자기 전까지 교육을 받냐 넘 싫다!',
        '나 또 교육...여니는 머해??']
        random.seed(a=None)
        selected=list[random.randrange(len(list))]
        await ctx.send(selected)
    elif now<=21:
        list=['차니 수양록 작성 중!',
        '나나나나 점호 준비 중이징',
        '아가가각 저녁점호한다!',
        '기찬 이제 취침준비!']
        random.seed(a=None)
        selected=list[random.randrange(len(list))]
        await ctx.send(selected)
    else:
        list=['차니 쿠울쿠울 자는 중',
        '흠냐흠냐 여니꿈....여니다 흠냐냐ㅑ',
        '코오코오..코오...코어ㅓ어ㅓ거ㅓ걱 드르러어어ㅓ어엉ㅇ']
        random.seed(a=None)
        selected=list[random.randrange(len(list))]
        await ctx.send(selected)


@bot.command(aliases=['명령어', '도움'])
async def order(ctx):
    embed=discord.Embed(title='명령어', description='군인기찬 사용법')
    embed.add_field(name='차니야', value='군인기찬이를 부르는 명령어', inline=False)
    embed.add_field(name='hello', value='[\'안녕\', \'hi\', \'안녕하세요\', \'안뇽\', \'하잉\', \'하이\']\n군인기찬과 인사를 할 수 있다.', inline=False)
    embed.add_field(name='love', value='[\'사랑해\', \'사랑\', \'러브\', \'조아해\', \'좋아해\', \'사랑행\', \'좋아행\', \'조아행\']\n군인기찬과 사랑을 나눌 수 있다.', inline=False)
    embed.add_field(name='cute', value='[\'귀여워\', \'귀여웡\', \'기여엉\', \'겨웡\', \'겨워\', \'겹다\']\n군인기찬과 귀엽다는 말을 주고 받는다.', inline=False)
    embed.add_field(name='select', value='[\'골라줘\', \'뭐먹지\', \'골라봐\']\n선택장애 발생시에 군인기찬에게 고르라고 시킬 수 있다.\n여러개도 가능하다.', inline=False)
    embed.add_field(name='discharge', value='[\'전역 언제야?\', \'전역\', \'꽃신언제신어?\']\n군인기찬의 전역날짜를 볼 수 있다.', inline=False)
    embed.add_field(name='info', value='[\'정보\']\n군인기찬의 정보를 볼 수 있다.', inline=False)
    embed.add_field(name='join', value='[\'들어와\']\n여니가 현재 위치한 음성채널로 군인기찬을 소환한다.', inline=False)
    embed.add_field(name='leave', value='[\'나가\']\n군인기찬이 여니의 명령에 의해 음성채널을 나간다,,,,', inline=False)
    embed.add_field(name='play', value='[\'재생\', \'틀어\', \'재생해줘\', \'틀어줘\']\n명령어 뒤에 유튜브 링크를 넣으면 군인기찬이 불러준다.', inline=False)
    embed.add_field(name='pause', value='[\'일시정지\', \'잠깐\']현재 군인기찬이 부르고 있는 노래를 잠시 멈춘다.', inline=False)
    embed.add_field(name='resume', value='[\'다시\', \'다시 틀어줘\', \'다시 재생\']\n일시정지 했던 노래를 군인기찬이가 이어서 부른다.', inline=False)
    embed.add_field(name='stop', value='[\'멈춰\']\n군인기찬이 부르고 있는 노래를 그만 부른다.', inline=False)
    embed.add_field(name='hurt', value='[\'아파\'\]n아픈 여니를 위해 기찬이가 호오호오 해준다.', inline=False)
    embed.add_field(name='what', value='[\'머해\', \'뭐해\', \'뭐하고이써\', \'뭐하고있어\', \'머해?\', \'뭐해?\', \'머행\', \'뭐행\']\n군인기찬이 뭘 하고 있는지 알 수 있다.', inline=False)
    embed.add_field(name='letter', value='???', inline=False)
    embed.add_field(name='개발중', value='개발중', inline=False)
    embed.add_field(name='개발중', value='개발중', inline=False)

    embed.set_image(url='https://opgg-com-image.akamaized.net/attach/images/20200517115437.917026.jpg')
    
    await ctx.send(embed=embed)

token=os.environ['bot_token']
bot.run(token)
