import tkinter
import time
import random
import datetime
import atexit
#노래의 재생과 종료 관련 함수
import pygame
index = 0 #게임 상황
select =0 #선택
key=""
gauge_width = 1015
re_width = gauge_width  # 게이지 바의 너비 초기값 설정
prev_re_width = re_width # 이전 게이지 바의 너비 설정

pressed = False

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0

cnt = 0
esc = 0
memo = 0
dir = 0
paper = 0
tem = 0
timer = 0
score = 0
motion1 = 0 
motion2 = 0

sound = 0

starttime = datetime.datetime.now()
nowtime = starttime

#캐릭터 위치
x=520
y=580

#마우스 움직일때
def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

#마우스 누를때
def mouse_press(e):
    global mouse_c, index
    if index==0:
        index =1
    mouse_c = 1

#마우스 버튼 놓을때
def mouse_release(e):
    global mouse_c
    mouse_c = 0

#방향키 누를떄
def key_down(e):
    global key
    key = e.keysym

#방향키 놓을때
def key_up(e):
    global key
    key = ""

#ctrl 키
def key_press(e):
    global ch_speed, us_cookie

    cvs.itemconfig(screen1, item1='hidden')
    cvs.itemconfig(screen2, item2='hidden')
    
    if key_press == "Control_L" and not us_cookie:
        us_cookie = True
        ch_speed = 0
        root.after(1000, us_cookie)
        
#키보드 키를 떼자마자 훈장님이 움직인다면 이 코드 삭제
def key_release(e): 
    global ch_speed, us_cookie

    if key_press == "Control_L" and us_cookie:
        us_cookie = False
        ch_speed = 1

def random_item():
    global tem
    tem = random.randrange(1,3)
    if tem == 1:
        cvs.itemconfig(item1, state='normal')
        cvs.itemconfig(item2, state='hidden')
    elif tem == 2:
        cvs.itemconfig(item1, state='hidden')
        cvs.itemconfig(item2, state='normal')

def hunjang():#훈장님
    global elapsed_seconds,timer,motion1,motion2,index
    if index == 2:
        cvs.itemconfig(hun1, state='normal')
        cvs.itemconfig(hun2, state='hidden')
        cvs.itemconfig(hun3, state='hidden')

        i = random.randrange(1,3)
        if i == 1:
            cvs.itemconfig(hun1, state='hidden')
            motion()
        else:
            root.after(400,hunjang)
    

def motion():
    global timer,motion1
    if index == 2:     
        timer = timer + 1
        if timer == 1:
            cvs.itemconfig(hun3, state='hidden')
            cvs.itemconfig(hun2, state='normal')
            cvs.itemconfig(hun1, state='hidden')
            motion1 = 0
        if timer == 3:
            cvs.itemconfig(hun3, state='normal')
            cvs.itemconfig(hun2, state='hidden')
            cvs.itemconfig(hun1, state='hidden')
            motion1 = 1
        if timer == 20:
            cvs.itemconfig(hun1, state='normal')
            cvs.itemconfig(hun2, state='hidden')
            cvs.itemconfig(hun3, state='hidden')
            motion1 = 0
            timer = 0
            root.after(1000,hunjang)
            return
        

        
        root.after(100,motion)

def students():
    global index,re_width,motion1
    if index == 2:
        cvs.itemconfig(student1, state='normal')
        cvs.itemconfig(student2, state='hidden')

        if paper == 1 and motion1 == 1:
            
            cvs.itemconfig(hun1, state='hidden')
            cvs.itemconfig(hun2, state='hidden')
            cvs.itemconfig(hun3, state='hidden')
            cvs.itemconfig(hun4, state='normal')

            cvs.itemconfig(student1, state='hidden')
            cvs.itemconfig(student2, state='normal')
        
            re_width -= 150
            root.after(250, students_end)

        root.after(100, students)
    
def students_end():
    cvs.itemconfig(hun1, state='normal')
    cvs.itemconfig(hun4, state='hidden')
    cvs.itemconfig(student2, state='hidden')
        
        

#쪽지 보내기
def moving_memo():
    global memo,dir,paper,motion1
    if dir == 1:
        memo = -1
        for i in range(10):
            if motion1 == 0:
                cvs.itemconfig(character3, state='normal')
                cvs.coords(character3, x+i*27*memo,y)
                cvs.update()
                time.sleep(0.08)
                if i == 9:
                    random_item()
            else:
                break
        paper = 0
    elif dir == 2:
        memo = 1
        for i in range(10):
            if motion1 == 0:
                cvs.itemconfig(character3, state='normal')
                cvs.coords(character3, x+i*27*memo,y)
                cvs.update()
                time.sleep(0.08)
                if i == 9:
                    random_item()
            else:
                break
        paper = 0
    memo = 0
    dir = 0
    cvs.coords(character3, x,y)
    cvs.itemconfig(character3, state='hidden')

#약과 먹기
def eat_cookie():
    global ch_speed, tem
    ch_speed = 1
    stop_time()
    cvs.itemconfig(item1, state='hidden')

def stop_time():
    global timer,cnt,motion1
    cnt += 1
    if 0 < cnt < 200:
        motion1 = 0
        cvs.itemconfig(item3, state='normal')
        root.after(10,stop_time)

    elif cnt == 200:
        cvs.itemconfig(item3, state='hidden')
        cnt = 0
    
    
#만화책 사용
def read_book():
    global re_width, tem
    re_width += 200
    cvs.itemconfig(item2, state='hidden')

#글자
def draw_txt(txt, x, y, siz, col, tg):
    fnt = ("궁서체", siz, "bold")
    cvs.create_text(x + 2, y + 2, text=txt, fill="black", font=fnt, tag=tg)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)

# 실시간 키 입력 처리
def main_proc():
    global esc, dir, motion2, re_width, paper

    if key == "Escape":
        cvs.itemconfig(replay2, state='hidden')
        esc = 1
    else:
        esc = 0

    if index == 2:  # 게임 시작 시
        global pressed
        sleep_sound=pygame.mixer.Sound("sleep.wav")

        if key == "Down" and pressed == False:  # 아래키 작동 여부에 따라 그림 변경
            sleep_sound.play()
            pressed = True


        elif key == "Down" and pressed == True:  # 아래키 작동 여부에 따라 그림 변경
            cvs.itemconfig(character1, state='hidden')
            cvs.itemconfig(character2, state='normal')
            if re_width < gauge_width:  # 게이지가 가득 차지 않았다면 계속 채우기
                re_width += 0.9  # 게이지 너비를 증가시킵니다 (조정 가능)
                cvs.coords(gauge, 10, 10, re_width, 30)
            motion2 = 1

        elif key == "Left":
            if key != "Down":
                dir = 1
                paper = 1
                moving_memo()

        elif key == "Right":
            if key != "Down":
                dir = 2
                paper = 1
                moving_memo()

        elif key == "Control_L":
            global tem,motion1
            if motion1 != 1:
                if tem == 1:
                    eat_cookie()
                    tem = 0
                elif tem == 2:
                    read_book()
                    tem = 0

        else:
            pressed = False
            pygame.mixer.stop()
            cvs.itemconfig(character1, state='normal')
            cvs.itemconfig(character2, state='hidden')
            motion2 = 0

    root.after(1, main_proc)

# 시간 및 게이지 업데이트 함수
def update_time_and_gauge():
    global index, gauge_width, starttime, timer, score, elapsed_seconds, re_width, prev_re_width

    if index == 2:  # 게임 진행 중일 때에만 시간 표시 및 게이지 업데이트
        nowtime = datetime.datetime.now()
        timedelta = nowtime - starttime
        elapsed_seconds = timedelta.total_seconds()

        time_text = f"시간: {elapsed_seconds:.1f} 초"
        cvs.delete("TIME")
        cvs.create_text(100, 70, text=time_text, fill="Red", font=("HY견고딕", 20), tag="TIME")

        if key != "Down":  # 아래 방향키를 누르지 않았을 때 게이지 감소
            re_width -= 5  # 게이지 감소 (조정 가능)
            cvs.coords(gauge, 10, 10, re_width, 30)

        # 게임 종료 조건 설정
        if motion1 == 1 and motion2 == 1:
            cvs.itemconfig(hun1, state='hidden')
            cvs.itemconfig(hun2, state='hidden')
            cvs.itemconfig(hun3, state='hidden')
            cvs.itemconfig(hun4, state='normal')

            score = elapsed_seconds * 30
            index = 3  # 게이지가 다 소진되면 게임 종료로 인덱스 변경
            timer = 1  # 타이머 시작
            root.after(10, game_main)

        if re_width <= 9:
            score = elapsed_seconds * 30
            index = 3  # 게이지가 다 소진되면 게임 종료로 인덱스 변경
            timer = 1  # 타이머 시작
            root.after(10, game_main)

    root.after(100, update_time_and_gauge)  # 100ms마다 게이지 및 시간 갱신

#타이틀화면
def title_screen():
    global wav, sound
    pygame.init()
    wav=pygame.mixer.Sound("title.wav")
    sound +=1
    if sound == 1:
        wav.play(-1)
    global index, mouse_c, select
    cvs.itemconfig(screen1, state='normal')
    cvs.itemconfig(screen2, state='hidden')
    cvs.itemconfig(screen3, state='hidden')
    cvs.itemconfig(screen4, state='hidden')
    cvs.itemconfig(replay2, state='hidden')

    
#게임방법표시
def show_tutorial():
    global mouse_c,key,index,esc
    cvs.delete("TITLE")
    cvs.itemconfig(screen1, state = 'hidden')
    cvs.itemconfig(screen2, state = 'hidden')
    cvs.itemconfig(screen3, state = 'normal')
    cvs.itemconfig(screen4, state = 'hidden')
    cvs.create_text(512, 200, text="방향키 ↓ 로 졸기", fill="Black", font=("궁서체", 40), tag="TUTORIAL")
    cvs.create_text(512, 300, text="방향키 ← → 로 쪽지 넘기기", fill="Black", font=("궁서체", 40), tag="TUTORIAL")
    cvs.create_text(512, 400, text="좌측 Ctrl을 눌러 아이템 사용", fill="Black", font=("궁서체", 40), tag="TUTORIAL")
    cvs.create_text(512, 500, text="훈장님의 감시를 피해야 한다", fill="Black", font=("궁서체", 40), tag="TUTORIAL")
    cvs.itemconfig(replay2, state='normal')
    draw_txt("돌아가기(ESC)",512,675,30,"black","TUTORIAL")
    if mouse_c == 1: 
        if 412 < mouse_x and mouse_x < 612 and 650 < mouse_y and mouse_y < 700:
            index=0
            cvs.delete("TUTORIAL")
            cvs.itemconfig(replay2, state='hidden')
            game_main()

    elif esc == 1:
        cvs.itemconfig(replay2, state='hidden')
        index=0
        cvs.delete("TUTORIAL")
        esc =0 
        game_main()
        
    if index == 1:
        root.after(10,show_tutorial)

        

#게임 시작함수
def start_game():
    global index, gauge, starttime, re_width, prev_re_width,sound
    pygame.mixer.stop()
    starttime = datetime.datetime.now()
    index = 2
    sound = 0
    cvs.delete("TITLE")
    cvs.itemconfig(screen1, state='hidden')
    cvs.itemconfig(screen2, state='normal')

    # 게이지 바 초기값 설정
    re_width = gauge_width  # 게이지 바 초기화
    prev_re_width = re_width  # 이전 게이지 바 초기화
    gauge = cvs.create_rectangle(10, 10, re_width, 30, fill="red", state='normal')
    hunjang()
    students()
    root.after(1, game_main)

#게임오버 함수
def game_over():
    global index,gauge,starttime,gamescore
    cvs.delete("TIME")
    
    cvs.itemconfig(screen2, state='hidden')
    cvs.itemconfig(screen4, state='normal')
    
    cvs.itemconfig(character1, state='hidden')
    cvs.itemconfig(character2, state='hidden')
    
    cvs.itemconfig(gauge, state='hidden')
    
    cvs.itemconfig(hun1, state='hidden')
    cvs.itemconfig(hun2, state='hidden')
    cvs.itemconfig(hun3, state='hidden')
    cvs.itemconfig(hun4, state='hidden')

    cvs.itemconfig(student1, state='hidden')
    cvs.itemconfig(student2, state='hidden')

    cvs.itemconfig(item1, state='hidden')
    cvs.itemconfig(item2, state='hidden')



    gamescore = f"점수 : {score:.0f} "
    cvs.create_text(512, 158, text=gamescore, fill="Black", font=("궁서체", 60), tag="OVER")

    cvs.itemconfig(replay1, state='normal')
    draw_txt("다시하기", 850, 685, 30, "Black", "OVER")



#게임 메인    
def game_main():
    global mouse_c,index,timer
    if index == 0: # 타이틀 화면 
        cvs.delete("TUTORIAL")
        title_screen()
    if index == 1:
        if mouse_c == 1:
            if 610 < mouse_x and mouse_x < 950 and 488 < mouse_y and mouse_y < 586:
                start_game()
            if 610 < mouse_x and mouse_x < 950 and 625 < mouse_y and mouse_y < 726:
                show_tutorial()
                
    if index == 3: #게임 종료 화면
        pygame.mixer.stop()
        if timer == 1:
            draw_txt("GAME OVER", 512, 300, 60, "red", "overtext")
        if timer == 400:
            cvs.delete("overtext")
            game_over()
        if timer >= 400:
            if mouse_c == 1:
                if 680 < mouse_x and mouse_x < 1020 and 635 < mouse_y and mouse_y < 735:
                    cvs.itemconfig(replay1, state='hidden')
                    cvs.delete("OVER")
                    timer = 0
                    index = 0

        timer = timer + 1
        

    root.after(10,game_main)
   
root = tkinter.Tk()
root.title("훈장님 몰래 딴짓하기")
root.resizable(False,False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
root.bind("<ButtonRelease>", mouse_release)
root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>", key_up)
cvs = tkinter.Canvas(root, width=1024, height=768)
cvs.pack()

bg = [
tkinter.PhotoImage(file="title.png"),
tkinter.PhotoImage(file="main.png"),
tkinter.PhotoImage(file="tutorial.png"),
tkinter.PhotoImage(file="score.png")
]

#캐릭터 이미지
ch=[
    tkinter.PhotoImage(file="player1.png"),
    tkinter.PhotoImage(file="player2.png"),
    tkinter.PhotoImage(file="paper.png")
]

it=[
    tkinter.PhotoImage(file="snack.png"),
    tkinter.PhotoImage(file="comicbook.png"),
    tkinter.PhotoImage(file="barrier.png")
]

hun=[
    tkinter.PhotoImage(file="hunjang1.png"),
    tkinter.PhotoImage(file="hunjang2.png"),
    tkinter.PhotoImage(file="hunjang3.png"),
    tkinter.PhotoImage(file="hunjang4.png")

]

student = [
    tkinter.PhotoImage(file="student1.png"),
    tkinter.PhotoImage(file="student2.png")
]


screen1 = cvs.create_image(512, 384, image=bg[0], state='normal')
screen2 = cvs.create_image(512, 384, image=bg[1], state='hidden')
screen3 = cvs.create_image(512, 384, image=bg[2], state='hidden')
screen4 = cvs.create_image(512, 384, image=bg[3], state='hidden')
#캐릭터 이미지 준비
character1 = cvs.create_image(x, y-190, image=ch[0], state='hidden')
character2 = cvs.create_image(x, y-190, image=ch[1], state='hidden')
character3 = cvs.create_image(x, y-190, image=ch[2], state='hidden')

student1 = cvs.create_image(x, y-190, image=student[0], state='hidden')
student2 = cvs.create_image(x, y-190, image=student[1], state='hidden')

hun1 = cvs.create_image(x-10, y-205, image=hun[0], state='hidden')
hun2 = cvs.create_image(x-10, y-205, image=hun[1], state='hidden')
hun3 = cvs.create_image(x-10, y-205, image=hun[2], state='hidden')
hun4 = cvs.create_image(x-10, y-205, image=hun[3], state='hidden')

replay = [tkinter.PhotoImage(file="replay.png")]
replay1 = cvs.create_image(850,685, image=replay[0], state='hidden')
replay2 = cvs.create_image(505,675, image=replay[0], state='hidden')

item1 = cvs.create_image(80, 120, image=it[0], state='hidden')
item2 = cvs.create_image(80, 120, image=it[1], state='hidden')
item3 = cvs.create_image(x+10, y, image=it[2], state='hidden')

#게이지 바
gauge= cvs.create_rectangle(10,10,gauge_width,30,fill="red",state='hidden')

game_main()
root.after(100, update_time_and_gauge)  # 게임 시작 후 시간 및 게이지 업데이트 시작
main_proc()
root.mainloop()