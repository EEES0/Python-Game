import arcade #arcade 라이브러리 임포트
import random #랜덤 라이브러리 임포트
import os #os 라이브러리 임포트
import sys #sys 라이브러리 임포트

def get_path(*paths): #환경에 따라 path(경로) 바꿈
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, *paths)

BASE_PATH = os.path.dirname(__file__)

class GameView(arcade.View): #arcade.View 클래스를 상속받아 GameView 클래스 정의
    
    def __init__(self): #초기화
        super().__init__() 
        self.buttonList = None #버튼 스프라이트 리스트
        self.buttons = {} #버튼들 구분용 딕셔너리
        self.currentLevel = 0 #현재 레벨 
        self.currentGold = 10000 #골드 초기화(시작 10000골드)                                                                              드)
        self.upgradeClicked = False #업그레이드 버튼 클릭 여부 
        self.upgradeRandom = 0 #강화- 랜덤 정수
        self.upgradePercent = 100 #강화 확률
        self.upgradeGold = 0 #강화 소모 골드
        self.sellCost = 0 #강화 판매 골드

    def setup(self): 
        self.buttonList = arcade.SpriteList() #버튼 스프라이트 리스트 생성 - arcade 3.3 이미지 사용법
        self.levelList = arcade.SpriteList() #레벨 이미지 스프라이트 리스트 생성
        self.buttons = {} #버튼들 구분용 딕셔너리
        self.levelText = arcade.Text(f"+{self.currentLevel}", 580, 570, arcade.color.BLACK, 70) #현재 레벨 화면 상단에 표시
        self.goldText = arcade.Text(f"현재 골드: {self.currentGold}", 530, 670, arcade.color.BLACK, 30) #현재 골드 화면 상단에 표시
        self.upgradeGoldText = arcade.Text(f"업그레이드 비용: {self.upgradeGold}", 530, 120, arcade.color.BLACK, 20) #업그레이드 골드 화면 상단에 표시
        self.upgradePercentText = arcade.Text(f"성공 확률: {self.upgradePercent}%", 530, 90, arcade.color.BLACK, 20) #업그레이드 성공 확률 화면 상단에 표시
        self.sellCostText = arcade.Text(f"판매 가격: {self.sellCost}", 530, 150, arcade.color.BLACK, 20) #판매 가격 화면 상단에 표시
        self.maxLevel = arcade.Text("클리어", 100, 600, arcade.color.BLACK, 30) #만렙 달성
        self.levelTexture = [ #레벨별 이미지 스프라이트들
            arcade.load_texture(get_path("Assets","Level1.png")),
            arcade.load_texture(get_path("Assets","Level2.png")),
            arcade.load_texture(get_path("Assets","Level3.png")),
            arcade.load_texture(get_path("Assets","Level4.png")),
            arcade.load_texture(get_path("Assets","Level5.png")),
            arcade.load_texture(get_path("Assets","Level6.png")),
            arcade.load_texture(get_path("Assets","Level7.png")),
            arcade.load_texture(get_path("Assets","Level8.png")),
            arcade.load_texture(get_path("Assets","Level9.png")),
            arcade.load_texture(get_path("Assets","Level10.png")),
            arcade.load_texture(get_path("Assets","Level11.png")),
            arcade.load_texture(get_path("Assets","Level12.png")),
            arcade.load_texture(get_path("Assets","Level13.png")),
            arcade.load_texture(get_path("Assets","Level14.png")),
            arcade.load_texture(get_path("Assets","Level15.png"))            
        ]
        self.levels = arcade.Sprite() #레벨 이미지 스프라이트로 생성
        self.levels.center_x = 640 #레벨 이미지 x좌표
        self.levels.center_y = 380 #레벨 이미지 y좌표
        self.levels.scale = 0.3 #레벨 이미지 크기
        self.levelList.append(self.levels) #레벨 스프라이트 리스트에 스프라이트 추가

        self.upgradeBtn = arcade.Sprite(
            get_path("Assets","Upgrade.png")
        ) #업그레이드 버튼 이미지 스프라이트로 생성
        self.upgradeBtn.scale = 0.3 #버튼 크기
        self.upgradeBtn.center_x = 1100 #버튼 x좌표
        self.upgradeBtn.center_y = 500 #버튼 y좌표
        self.buttons[self.upgradeBtn] = self.upgrade #업그레이드 버튼 딕셔너리에 추가

        self.sellBtn = arcade.Sprite(
            os.path.join(BASE_PATH,"Assets","Sell.png")
        ) #판매 버튼 이미지 스프라이트로 생성
        self.sellBtn.scale = 0.2 #버튼 크기
        self.sellBtn.center_x = 1125 #버튼 x좌표
        self.sellBtn.center_y = 300 #버튼 y좌표

        self.buttonList.append(self.upgradeBtn) #강화 버튼 스프라이트 리스트에 추가
        self.buttonList.append(self.sellBtn) #판매 버튼 스프라이트 리스트에 추가

        self.buttons[self.sellBtn] = self.sell #판매 버튼 딕셔너리에 추가
        

    def on_update(self, delta_time): #프레임마다 업데이트
        self.levelText.text = f"+{self.currentLevel}" #업데이트마다 현재 레벨 텍스트 업데이트
        self.goldText.text = f"현재 골드: {self.currentGold}" #업데이트마다 현재 골드 텍스트 업데이트
        self.upgradeGoldText.text = f"업그레이드 비용: {self.upgradeGold}" #업그레이드 골드 텍스트 업데이트
        self.sellCostText.text = f"판매 가격: {self.sellCost}" #판매 가격 텍스트 업데이트
        if 0 <= self.currentLevel <= 2: #강화 레벨이 올라갈수록 강화 소모 비용 증가
            self.upgradeGold = self.currentLevel * 100 #0~200
        elif 3 <= self.currentLevel <= 5:
            self.upgradeGold = self.currentLevel * 300 #900~1500
        elif 6 <= self.currentLevel <= 8:
            self.upgradeGold = self.currentLevel * 500 #3000~4000
        elif 9 <= self.currentLevel <= 11:
            self.upgradeGold = self.currentLevel * 1000 #9000~11000
        elif 12 <= self.currentLevel <= 13:
            self.upgradeGold = self.currentLevel * 3000 #36000~39000
        self.upgradePercentText.text = f"성공 확률: {self.upgradePercent}%" #업그레이드 성공 확률 텍스트 업데이트
        self.levels.texture = self.levelTexture[self.currentLevel] #currentLevel따라 스프라이트 리스트 인덱스값 변경
        if 0 <= self.currentLevel <= 2: #레벨따라 판매 가격 
            self.sellCost = self.currentLevel * 200 #0~400
        elif 3 <= self.currentLevel <= 5:
            self.sellCost = self.currentLevel * 1000 #3000~5000
        elif 6 <= self.currentLevel <= 8:
            self.sellCost = self.currentLevel * 3000 #18000~24000
        elif 9 <= self.currentLevel <= 11:
            self.sellCost = self.currentLevel * 5000 #45000~55000
        elif 12 <= self.currentLevel <= 13:
            self.sellCost = self.currentLevel * 10000 #120000~130000
        elif self.currentLevel == 14:
            self.sellCost = 500000
        
        

    def on_draw(self): #화면 그리는 arcade 함수
        self.clear(arcade.color.DARK_GRAY) #화면 배경색 dark_gray로 화면 초기화
        self.buttonList.draw() 
        self.levelText.draw()  
        self.goldText.draw() 
        self.upgradeGoldText.draw()
        self.upgradePercentText.draw()
        self.levelList.draw() 
        self.sellCostText.draw() 
        if self.currentLevel == 14:
            self.maxLevel.draw() #만렙 달성
    def on_mouse_press(self, x, y, button, modifiers): #마우스로 버튼 클릭했을 때 호출되는 함수
        if arcade.get_sprites_at_point((x, y), self.buttonList): #클릭한 위치에 버튼이 있는지 확인
            for btn in arcade.get_sprites_at_point((x, y), self.buttonList): #클릭한 위치에 있는 모든 버튼에 대해 반복
                actions = self.buttons.get(btn) #버튼에 해당하는 함수 가져오기
                if actions:
                    actions() #버튼에 해당하는 함수 호출

    def upgrade(self): #업그레이드 함수
          self.upgradeRandom = random.randint(1, 100) #1부터 100까지 무작위 정수 
          self.upgradePercent = max(100 - self.currentLevel * 5, 20) #레벨마다 5씩 확률 줄어듬, 최소 20(추후 레벨 추가 고려)
          if self.currentLevel < 14: #만렙인 14렙보다 레벨 낮아야 강화 가능
            if self.currentGold >= self.upgradeGold: #현재 골드가 업그레이드 비용보다 많거나 같은지 확인
                if self.upgradeRandom <= self.upgradePercent: #1~100까지 랜덤으로 나온 정수가 확률보다 작거나 같아야 강화 성공
                    self.currentLevel += 1 #레벨 증가
                    self.currentGold -= self.upgradeGold #강화 비용 소모
                else: #강화 실패
                    self.currentLevel = 0 #레벨 초기화
                    self.upgradePercent = 100 #강화 확률 초기화
          
              


    def sell(self): #판매 함수
        
        if 0 <= self.currentLevel <= 2: #현재 레벨이 0보다 큰 경우에만 판매 가능, 레벨따라 판매 가격 다름
            self.currentGold += self.currentLevel * 200 #0~400
        elif 3 <= self.currentLevel <= 5:
            self.currentGold += self.currentLevel * 1000 #3000~5000
        elif 6 <= self.currentLevel <= 8:
            self.currentGold += self.currentLevel * 3000 #18000~24000
        elif 9 <= self.currentLevel <= 11:
            self.currentGold += self.currentLevel * 5000 #45000~55000
        elif 12 <= self.currentLevel <= 13:
            self.currentGold += self.currentLevel * 10000 #120000~130000
        elif self.currentLevel == 14: #만렙
            self.currentGold += 500000


        self.currentLevel = 0 #판매 후 레벨 초기화
        self.upgradePercent = 100 #판매 후 업그레이드 성공 확률 초기화

def main(): #메인 함수
    window = arcade.Window(1280, 720, "방패 키우기") #게임 창 속성
    game = GameView() #객체 생성
    game.setup() #게임 설정 함수 호출
    window.show_view(game) #창 띄우기
    arcade.run() #게임 루프 시작
    


if __name__ == "__main__": #이 파일로 직접 실행할 때만 main()함수 호출(다른 파일에서 import시 main()함수 바로 호출 안됨)
    main()