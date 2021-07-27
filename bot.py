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
    if(txt!=None):
        await ctx.send(txt)

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

@bot.command(aliases=['시러', '싫어', '미워', '미웡', '싫엉'])
async def hate(ctx):
    hate_list=['힝구힝구 미안해 여니야...',
    '사랑해 여니야 미아내....',
    '기찬이 왜 싫아...? 힝 미안해',
    '차니 미워...? 힝구.....잘못해써',
    '이뿌니 미안해~❤',
    '여니 조아아ㅏ 미안행❤',
    '나도 미워!!😀❤']

    random.seed(a=None)
    selected=hate_list[random.randrange(len(hate_list))]
    await ctx.send(selected)


@bot.command(aliases=['편지', '할 말'])
async def letter(ctx, txt):
    letters=['-5. 7월 23일 금요일. 입대 5일 전이다. 아직은 실감 안 난다.',
    '-4. 7월 24일 토요일. 입대 4일 전이다. 아직도 실감 안 난다.',
    '-3. 7월 25일 일요일. 입대 3일 전. 이제 슬슬 쫄린다. 내일 빡빡이가 될 예정이다.',
    '-2. 7월 26일 월요일. 입대 2일 전. 이무래도 큰일난 것 같다. 머리가 빡빡이가 됐다. 오늘이 입대 전 경연이 마지막으로 보는 날이다.',
    '-1. 7월 27일 화요일. ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ입대 하루 전. 지인짜 꽃(flowerㅎㅎ)됐다.....',
    '1. 7월 28일 수요일 1주 1일차. ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ이게 뭐노! 나 왜 훈련소 앞? 여니와 함께하지 못해서 너무 아쉽지만 같이 아가가 군대 가는 거 준비해줘서 너무너무 좋아 사랑해!! 훈련소 5주가 우리 만난 날 중에 진짜 손톱만큼도 안 되지만 왜이렇게 길게 느껴지고 막막한 걸까! ㅜㅜ 아가 밖에서 밥 잘 먹구 잘 자구 너무 무리해서 일하고 공부하지 말고 충분히 쉬고 늦게 자지 말구 잘하고 있어랑 사랑한다 애기야!',
    '2. 7월 29일 목요일 1주 2일차. 우리 여니 오늘 하루도 파이팅해 ㅜㅜ 나는 아직 적응이 안돼서 힘들어ㅜㅜ 훈련소 사람들이랑도 너무 어색어색,,, 빨리 친해지고 싶다.',
    '3. 7월 30일 금요일 1주 3일차. 후.......격리 너무 노잼이야 진짜!! 핸드폰도 안 주고 이게 모야. 마스크도 못 벗고 ㅉㅈㄴ 마스크 훌렁훌렁 벗어던지고 아가랑 뽀갈 하고 싶어. 힝구구구구구',
    '4. 7월 31일 토요일 1주 4일차. 여전히 더운 날씨지만 에어컨 덕분에 살 수 있다......여니야 현실세계도 많이 덥지??ㅜㅜ 더위 조심하구 물 많이 마시구......최대한 밖에 나가지 말구 침대에서 딩굴딩굴만 해용!! 헤헤 귀여워 상상만해도!',
    '5. 8월 1일 일요일 1주 5일차. 오,,,,,,,드디어 8월이 되었다. 전역에 가까워졌어!는 무슨 훈련병따리가 무슨 벌써 집 갈 생각임 ㅋㅋ 그래두 일주일이 지나갔네~ 여니도 여니 일 하고 나도 군생활 열심히 하다보면 이 지루하고 긴 시간도 빠르게 지나갈 거야! 사랑해!',
    '6. 8월 2일 월요일 2주 1일차. 오늘은 뭔가 우울할 것 같은 기분. 여니랑 마지막으로 만난 지 1주일 되는 날이다. 여니랑 같이 밥 먹고 안고 하던 모습들이 생생한데 그런 당연하던 것들을 할 수 없다는 게 너무 답답해. 그치만 나는 견딜 거야 왜냐? 나는 남자고 군인이니까! 남자는 뭐다? 견뎌~!',
    '7. 8월 3일 화요일 2주 2일차. 기찬이에게 무얼 하고 있냐 물으신다면 나는 책 읽고 편지를 쓰고 하루종일 여니 생각을 하는 중이징. 여기 밥도 맛있고 좋아 생각보다! 살 만해 ㅎㅎ 울 여니도 밥 잘 먹구 더운데 돌아다니지 말구 잘 살구 있어랑',
    '8. 8월 4일 수요일 2주 3일차. 오늘은 여니 필기 2트~~ 지난번엔 너무 아쉽게 안됐지만 오늘은 왠지 느낌이 좋다! 내가 아는 여니는 분명 잘할 수 있을 거야. 왜냐? 여니니까! 이뿌잖아 ㅎㅎ 이뿌니까 뭐든지 잘해 여니는 아는 문제 실수하지 않기! 그리고 찍은 문제는 무조건 다 맞기!! 공부하느라 수고했구 잘될 거얌!',
    '9. 8월 5일 목요일 2주 4일차. 어제 필기 보고 오늘은 안전교육....그거 완전 노잼이라 나는 들으면서 코오코오 잤어. 아마 다른 사람들도 다 잤던 것 같은데 ㅋㅋㅋㅋ 여니도 귀엽게 꾸벅꾸벅 졸 것 같아 ㅜ 보고싶다 여니 자는 모습....여니 잘 때 숨소리도 너무너무 그리워',
    '10. 8월 6일 금요일 2주 5일차. 경연아. 잘 먹고 잘 살고 있니? 어떻게 살고 있는지 너무 궁금하다. 인편으로 어떻게 살고 있는지 알려줘. \n1. 오늘 응가는 몇 번이나 했니?\n2. 오늘 치카는?? \n3. 오늘 몇 시에 일어났어?? \n4. 어제 몇 시에 잤어ㅡㅡ \n5. 여니 오늘 밥 뭐 먹었어 언제 몇 번이나 먹었어? 오늘 8끼??? 치킨 피자 족발 종류별로 다 먹었나??? 하앙 귀여워 경여니 응애응애 해바~~ 기찬이 심심하니까 빨리 알려주삼!!',
    '11. 8월 7일 토요일 2주 6일차. 힝 아가야 여름 너무너무 덥지 ㅜㅜ 배라(ㅔ가 아니라 ㅐ임) 배달시켜서 먹고 나중에 나한테 다 청구해! 내가 다 사준다. 이제 슬슬 격리가 끝나간당. 담주부터 애기가 사준 썬크림을 쓸 수 있겠구만!! 내 소중한 피부를 지켜줘서 고마워잉 ㅎㅎ 생활관 에어컨 빵빵해서 조아 여니 엉덩이만큼 빵빵해!! 아 엉덩이 만지고 싶다.... 부들부들 너무너무 느낌 조아 헤헤 여니 궁디 베고 누워 있고 싶어....!! 사랑행 히히 여니 만나러 나가면 여니랑 꼬옥 안고 엉덩이 엄청 만질 거임 수고하셈!!',
    '12. 8월 8일 일요일 2주 7일차. 아마 오늘이 격리 마지막이려나?? 2주차 마지막이니까. 오늘이 마지막이면 아마 pcr 검사 할 텐데 너무너무 싫어 코 쑤시는 느낌.... 코피 났을 때 얼얼한 느낌 또 나자나 ㅜㅜ 우리 애기는 방역 수칙 잘 지키구 내가 기도하고 있으니까 pcr 검사 받을 일 없을 거야!!',
    '13. 8월 9일 월요일 3주 1일차. 여니야 벌써 3주차다. 아니 이제야 3주차인가?? 나 점점 몸에서 군인냄새가 나기 시작했어. 자대배치 받으면 섬유유연제 들이붓고 빨래해야지. 후..... 너무너무 재미 없고 싫지만, 그나마 다행인 것은 내 주변 사람들이 다 빡빡이고 또 엄청 많다는 거! 그게 그나마 위안(¥)이 되네.... ㅋㅋ 개드립 ㅈㅅ... 여니가 평소에 개드립 엄청 싫어하지만 가끔은 그리워하지 않을까 생각해서 넣어봤어 ㅎㅎ 어때?',
    '14. 8월 10일 화요일 3주 2일차. 여니야 너무너무 보고싶다. 손편지 쓸 때 여니 사진 프린트 해서 많이많이 보내주라 기찬이 못 봐서 여니 홀쭉해진 거 아니야~~? 얼굴 궁금하니까 빨리 보내줘 ㅎㅎ 더캠프나 육훈 홈피에 기찬 사진 올라오나?? 내 사진 찾을 수 있어 여니?? 여니 빡빡이는 찾어야지ㅡㅡ',
    '15. 8월 11일 수요일 3주 3일차. 일주일 중 가장 힘들다는 수요일.... 우리 아가도 힘들려나? 나는 이번 주부터 제대로 교육 받고 하는데 너무너무 재미가 없떠! 군인기찬한테 뭐하냐고 물어봐. 오전 오후 두 번씩 교육 받아서 너무 싫고 재미 없다고 할걸? 코딩하고 싶다 악악!! 코딩=(여니) 코 (만지면서) 딩(가딩가 하고 싶다)',
    '16. 8월 12일 목요일 3주 4일차. 우리 아가 오늘 희망강의 추첨 결과 나오는 날이지?? 이미 나왔으려나? 아직 안 나왔으면 꼭 여니 될 거야!! 걱정 노노놉 나 여기서 기도하는 중이징. 아가 만약 됐으면 축하하구 안 됐어도 낙담하지 마 ㅜㅜ 본수강신청 때 잘하면 되니까!',
    '17. 8월 13일 금요일 3주 5일차. 하앙 오늘은 불금 그치만 우리 애기는 스터디도 있고 씨유 알바도 있지.....그래도 지금은 날이 꽤 풀리지 않았나?? 30도 밑으로 떨어지긴 했으려나...ㅎㅎㅎㅎ 더우니까 조심해요 아가!! 사랑행',
    '18. 8월 14일 토요일 3주 6일차. 훈련소에서의 주말은 사막의 오아시스와 같지. 밀린 일이나 교육이 없으면 쉬는 날이거든!! 엄청 자유롭지는 않겠지만 그래두 쉬는 날이니까.... 오늘은 왠지 아가 알바 가서 이거 확인할 것 같은데?? ㅎㅎ 오늘 알바두 파이팅하구 내가 진상 안 오게 열심히 기도할게. 알바 하면서도 밥 잘 챙겨먹고 그래랑. 사랑해!',
    '19. 8월 15일 일요일 3주 7일차. 오늘은 광복절이징,, 광복절에도 여니는 일을 합니다.....광복절에 일하는데 설마 진상까지 나타나서 괴롭히는 거 아니겠지? 진상 진짜 너무 싫어 진상이야 개진상 여니 괴롭히는 놈들이 세상에서 제일 싫어. 우리 이쁜 아가 소중히 다뤄달란 말이야 이자식들아!!',
    '20. 8월 16일 월요일 4주 1일차. 오늘은 대체휴일. 오늘은 여니도 쉬는 날이겠징?? 나도 빨간 날이라서 쉰다! 에어컨쓰 빵빵쓰 시원쓰!! 너무 좋아 아가 낼부터 이번주 일정 엄청 많으니까 푹 쉬어! 애기는 애기답게 침대에 누워서 응애응애 이불 포옥 뒤집어쓰고 말이얌 상상만 해도 너무너무 귀엽다 하얀 얼굴 말랑한 볼 땡그란 눈(눈 감아도 땡글땡글) 하앙 뽀뽀마렵다 휴가 외박 면회 도대체 언제임?',
    '21. 8월 17일 화요일 4주 2일차. 여니 오늘 수강신청하는 날이지?? 이미 했나ㅜㅜ 아침 일찍 하는 거니까 왠지 여니 수강신청 다 하고 편지 볼 듯. 설마 매일매일 안 보는 건 아니겠지?? ㅜㅜ 울 여니 수강신청하느라 수고했구 막 손 엄청 떨면서 했을 텐데 ㅜ,,,,,,,수강신청 때 같이 못 있어줘서 미안해 사랑해!!',
    '22. 8월 18일 수요일 4주 3일차. 오늘은 여니 기능 연습 첫째날! 수강신청에 이어 면허 연습이라니 ㅜㅜ 아가 너무 힘든 거 아니야~? 잘 배워서 기능 시험 이번엔 붙을 수 있기를!! 나 처럼 시동 꺼뜨리지 말구 강사님 말씀 잘 들어용!!',
    '23. 8월 19일 목요일 4주 4일차. 오늘은 여니 기능 연습 둘째날이자 시험보는 날! 어제도 하고 오늘도 하니까 잘할 수 있을 거야. 기능 잘 익혀서 도로주행 때 잘 쓰자! 그리구 기찬 데릴러 와야징 ㅎㅎ 차 끌고 썬글라스까지 뙇뙇뙇 여니누나 나 반해썽.... 아무튼 파이팅이야 사랑해!!',
    '24. 8월 20일 금요일 4주 5일차. 사실 훈련소는 4주차가 진땡이지. 화생방 각개전투 사격 훈련이 있거든!! 울 애기를 위험으로부터 지키려면 이 정도는 잘 해야 하지 않을까? 그리고 애기랑 오래오래 같이 살려면 필수지!! ㅋㅋ 특히 화생방... 아가의 방구를 버터기 위해서! 허업.. 생각만 해도 지독한 뿡가뿡가. 그치만 보고싶다 여니 뿡가뿡가. 손편지 보낼 때 여니 뿡가뿡가도 보내줘! 하앙 뿡뿡이 여니 뿡뿡뿡뿡뿡뿡뿔ㅇㅃ우뿡뿡뿡뿌우뿡뿌우ㅃㅇ뿡뿡뿡뿡뿌ㅃ우ㅃㅇㅇ뿡뿌우ㅃㅇ뿡뿌ㅃ웅뿌',
    '25. 8월 21일 토요일 4주 6일차. 훈련...진땡이라 그런지 너무 힘든 한 주였다. 꿀같은 주말이야 여니야..... 동기들이랑 수다 좀 떨구 쉬어야지. 여니 너무너무 보고싶다!! 힘든 훈련 할 때 가장 먼저 생각나는 게 여니였어. 학교생활 할 때도 여니 덕분에 힘든 공부도 버티고 할 수 있었으니까,, 진짜 여니 얼굴부터 떠오르더랑 히히 귀여운 볼 양손으로 찌부해서 부비부비하고싶어잉 히히 여니 품에 안겨서 도리도리...ㅎㅎㅎㅎ 상상만 해도 귀여운 여니당!!ㅎㅎ',
    '26. 8월 22일 일요일 4주 7일차. 훈련소 수료 D-10이당. 입대 D-10은 엄청 빨랐는데 여기는 왜케 느리징??? 나 빨리 사회로 나가고 싶어 여기 공기가 너무 탁해 아ㅏ가가가가가각 여니 냄새 맡고 싶어 더블유드레스룸 그냄새....... 킁킁킁....',
    '27. 8월 23일 월요일 5주 1일차. 으그극 5주차 시작이야. 내가 군인이 된 지 한 달이나 지나다니! 벌써부터 지겹다 지겨워.... 유튜브도 보고 싶고 치킨도 먹고 싶다! 그치만 가장 하고 싶은 것은 우리 아가 만나기~~><>< 너무너무 보고싶엉 만나서 부비ㅜ비뷔뷔뷔부비ㅜ비ㅜ비부비부비부비부비부비부빕 하고시퍼 힝구구구구....아가 맛있는 거 먹구 재밌는 거 보면서 기다리구 있엉!! 금방 나가니까용',
    '28. 8월 24일 화요일 5주 2일차. 힝 여니야 오늘은 뭐해용?? 잠을 잘 잤나!! ㅎㅎ 자고 일어난 여니 보고싶다 볼 빵빵하고 눈 잘 뜨지도 못하고 부비적부비적.... 아가랑 놀구싶당 힝 딱 기다리구 있엉 볼 챱챱챱 만지겡. 제발 맛있는 거 많이 먹어서 살 많이 찌워놔라!! 배도 빵빵해졌으면 좋게썽 히키히키히키',
    '29. 8월 25일 수요일 5주 3일차. 오늘은 우리 애기 차 끌고 처음으로 도로 주행하는 날이네...! 기능 시험이랑 별로 다른 것도 없어! 다른 차들이 슝슝 달릴 뿐이지. 어차피 다른 차들이 도로주행 연습 차들은 배려해주니까 괜찮을 거야! 나는 우리 아가 차 잘 운전할 거라고 생각행 좌우앞뒤 잘 살피구 호이딩이야!',
    '30. 8월 26일 목요일 5주 4일차. 오늘은 여니 도로주행 둘째날이넹. 어제 해봤으니 오늘은 더 잘할 수 있겠지? 흐므므믐..... 어제 잘했으면 어제만큼만 하구 어제 좀 부족했다 싶으면 그부분만 더 집중해서 해보자! 도로주행 잘 하구 한 번에 도로주행 붙어버리자잉~~',
    '31. 8월 27일 금요일 5주 5일차. 뚜둥뚜둥 오늘은 드디어 찐막 도로주행 시험 보는 날!! 잘할 수 있을 거야. 멋있게 한 방에 붙어서 기찬쓰한테 자랑쓰 하자잇! 기찬이 보러 올 때 여니가 운전해서 오고 기찬이한테 자랑 고고링 ㅎㅎ 수고했고 사랑해 여니야!!',
    '32. 8월 28일 토요일 5주 6일차. 힝구....이쯤에 애기 항상 배 아프고 예민해지는뎅..... 더운데 애기 너무 힘들겠다. 편의점에서 아가 맛있는 거 사먹어. 달달구리 한 거 말이야!! 헹헹헹 ㅜㅜㅜㅜ 내가 대신 아플래 짜증나 여니 아픈 거. 그거 안했으면 좋겠어,,,, 알바 끝나면 집 가서 바로 침대 다이빙해!! 배 따뜻하게 하구... 아가 사랑행.....',
    '33. 8월 29일 일요일 5주 7일차. 훈련소 마지막 주말이다!! 자대 가면 이등병.... 주말이 있을까?? 막 괴롭힘 당하는 거 아니야?? 는 무슨 내가 다 싸워서 이기지 ㅋㅋ 뭐 어쩔건데! 우리아빠 군인이다! 다 일러~~ 우리 애기 기찬이 걱정은 했나?? 훈련소 지나고 자대 가면 나는 그나마 꿀보직이라니까 괜찮을 거야 기찬 걱정해주고 준비해줘서 너무너무 고마워! 여니 덕분에 훈련소 잘 버틸 수 있었고 남들보다 편하게 지낸 것 같아! 사랑해잉~~',
    '34. 8월 30일 월요일 6주 1일차. 훈련소 마지막 주다.....별일 없다면 9월 1일에 수료를 하겠지. 우리 아가는 잘 살구 있나! 나는 여니 보고 싶어서 죽겠엉 ㅜ 후......훈련소 만나서 꽃같아고 다신 만나지 말자. 여니도 이런 곳은 오지 마. 내가 대신 가도 된다고 하면 내가 갈게.. 연약한 여니가 올 곳이 못 돼! 차라리 내가 3년 복무한다.... 띠방....',
    '35. 8월 31일 화요일 6주 2일차. 훈련소 수료 D-1, 시간이 안 간다. 빨리 자대 가고싶다. 빨리 폰 받아서 여니랑 연락하고 싶단 말이야!! 근데 한 편으로는 아쉽기도! 정들었던 훈련소 동기들이랑 뱌뱌라니....그래서 인스타 아이디랑 전화번호도 공유했어! 자대 가서도 연락하구 나중에도 만날 수 있으니깡 ㅎㅎ',
    '36. 9월 1일 수요일 수료일. 아 드디어 때가 왔다. 내가 돌아왔다. 이제는 더이상 훈련병이 아니다!!! 이제 이등병으로 불릴 수 있는 때가 온 것이야~~ 자대배치 결과도 나올 거고(이미 나왔으려나?? 나보다 여니가 먼저 알고 있을 수도.....) 관등성명도 훈련병이 아니라 이병 박 기 찬! 이렇게 하는 거징 ㅋㅋ 곧 자대로 이동하고 폰도 받으면 아가랑 편하게 전화하고 연락 가능할 거야! 좀만 참자잇!! 사랑해! 훈련소 기다려줘서 너무너무 고맙고 사랑한다 이거징!!',
    '',
    
    ]
    
    start=datetime.datetime(2021, 7, 23)
    today=datetime.datetime.today()
    sub=today-start
    start_s=start.strftime('%Y-%m-%d')
    today_s=today.strftime('%Y-%m-%d')
    sub_i=int(sub.days)+1
    await ctx.send(f'입영일:{start_s}, 오늘:{today_s}, 입대: D+{sub_i-5}')

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
    now=int(now_hour.tm_hour)+9
    if now>=24:
        now-=24
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
    embed.add_field(name='letter', value='[\'편지\', \'할 말\'] + [\'오늘\', \'전체\', \'모두\']\n오늘을 입력하면 오늘의 편지! 모두를 입력하면 지금까지의 모든 편지를 볼 수 있다.', inline=False)

    embed.set_image(url='https://opgg-com-image.akamaized.net/attach/images/20200517115437.917026.jpg')
    
    await ctx.send(embed=embed)

token=os.environ['bot_token']
bot.run(token)
