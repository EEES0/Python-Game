import arcade #arcade 라이브러리 임포트
import random #랜덤 라이브러리 임포트

class GameView(arcade.View): #arcade.View 클래스를 상속받아 GameView 클래스 정의
    
    def __init__(self): #초기화
        super().__init__() 
        self.buttonList = None #버튼 스프라이트 리스트 초기화
        self.buttons = {} #버튼들 구분용 딕셔너리
        self.currentLevel = 0 #현재 레벨 초기화
        self.currentGold = 10000 #골드 초기화 (시작 5000골드)
        self.upgradeClicked = False #업그레이드 버튼 클릭 여부 변수
        self.upgradeRandom = 0 
        self.upgradePercent = 0 
        self.upgradeGold = 0
        self.sellCost = 0

    def setup(self): 
        self.buttonList = arcade.SpriteList() #버튼 스프라이트 리스트 생성 - arcade 3.3 이미지 사용법
        self.levelList = arcade.SpriteList() #레벨 이미지 스프라이트 리스트 생성
        self.buttons = {} #버튼들 구분용 딕셔너리
        self.levelText = arcade.Text(f"현재 레벨: {self.currentLevel}", 530, 680, arcade.color.BLACK, 30) #현재 레벨 화면 상단에 표시
        self.goldText = arcade.Text(f"현재 골드: {self.currentGold}", 530, 640, arcade.color.BLACK, 30) #현재 골드 화면 상단에 표시
        self.upgradeGoldText = arcade.Text(f"업그레이드 비용: {self.upgradeGold}", 530, 120, arcade.color.BLACK, 20) #업그레이드 골드 화면 상단에 표시
        self.upgradePercentText = arcade.Text(f"성공 확률: {self.upgradePercent}%", 530, 90, arcade.color.BLACK, 20) #업그레이드 성공 확률 화면 상단에 표시
        self.sellCostText = arcade.Text(f"판매 가격: {self.sellCost}", 530, 150, arcade.color.BLACK, 20) #판매 가격 화면 상단에 표시
        self.levelTexture = [
            arcade.load_texture("Assets\\Level1.png"),
            arcade.load_texture("Assets\\Level2.png"),
            arcade.load_texture("Assets\\Level3.png"),
            arcade.load_texture("Assets\\Level4.png"),
            arcade.load_texture("Assets\\Level5.png"),
            arcade.load_texture("Assets\\Level6.png"),
            arcade.load_texture("Assets\\Level7.png"),
            arcade.load_texture("Assets\\Level8.png"),
            arcade.load_texture("Assets\\Level9.png")
            
        ]
        self.levels = arcade.Sprite() #레벨 이미지 스프라이트로 생성
 #현재 레벨에 해당하는 텍스처로 설정
        self.levels.center_x = 640 #레벨 이미지 x좌표
        self.levels.center_y = 380 #레벨 이미지 y좌표
        self.levels.scale = 0.3 #레벨 이미지 크기
        self.levelList.append(self.levels)

        self.upgradeBtn = arcade.Sprite(
            "C:\\Users\\minbh\\OneDrive\\바탕 화면\\파이썬 프로젝트\\Assets\\Upgrade.png"
        ) #업그레이드 버튼 이미지 스프라이트로 생성
        self.upgradeBtn.scale = 0.3 #버튼 크기
        self.upgradeBtn.center_x = 1100 #버튼 x좌표
        self.upgradeBtn.center_y = 500 #버튼 y좌표
        self.buttons[self.upgradeBtn] = self.upgrade #업그레이드 버튼 딕셔너리에 추가

        self.sellBtn = arcade.Sprite(
            "C:\\Users\\minbh\\OneDrive\\바탕 화면\\파이썬 프로젝트\\Assets\\Sell.png"
        ) #판매 버튼 이미지 스프라이트로 생성
        self.sellBtn.scale = 0.2 #버튼 크기
        self.sellBtn.center_x = 1125 #버튼 x좌표
        self.sellBtn.center_y = 300 #버튼 y좌표

        self.buttonList.append(self.upgradeBtn) #버튼 스프라이트 리스트에 버튼 추가
        self.buttonList.append(self.sellBtn) #판매 버튼 스프라이트 리스트에 추가

        self.buttons[self.sellBtn] = self.sell #판매 버튼 딕셔너리에 추가
        

    def on_update(self, delta_time):
        self.levelText.text = f"현재 레벨: {self.currentLevel}" #업데이트마다 현재 레벨 텍스트 업데이트
        self.goldText.text = f"현재 골드: {self.currentGold}" #업데이트마다 현재 골드 텍스트 업데이트
        self.upgradeGoldText.text = f"업그레이드 비용: {self.upgradeGold}" #업그레이드 골드 텍스트 업데이트
        self.sellCostText.text = f"판매 가격: {self.sellCost}" #판매 가격 텍스트 업데이트
        if 0 <= self.currentLevel < 3:
             self.upgradeGold = self.currentLevel * 1000 #업그레이드 비용 계산
        elif 3 <= self.currentLevel < 5:
             self.upgradeGold = self.currentLevel * 2000
        elif 5 <= self.currentLevel < 9:
             self.upgradeGold = self.currentLevel * 3000
        self.upgradePercentText.text = f"성공 확률: {self.upgradePercent}%" #업그레이드 성공 확률 텍스트 업데이트 #현재 레벨이 9보다 작은 경우에만 레벨 이미지 업데이트
        self.levels.texture = self.levelTexture[self.currentLevel]
        if 0 <= self.currentLevel < 2: #현재 레벨이 0보다 큰 경우에만 판매 가능
            self.sellCost = self.currentLevel * 3000
        elif 2 <= self.currentLevel < 4:
            self.sellCost = self.currentLevel * 5000
        elif 4 <= self.currentLevel < 6:
            self.sellCost = self.currentLevel * 10000
        elif 6 <= self.currentLevel < 9:
            self.sellCost = self.currentLevel * 20000
    def on_draw(self): #화면 그리는 arcade 함수
        self.clear(arcade.color.DARK_GRAY) #화면 배경색 흰색으로 화면 초기화
        self.buttonList.draw() #버튼 스프라이트 리스트 그리기
        self.levelText.draw()  #현재 레벨 텍스트 그리기
        self.goldText.draw() #현재 골드 텍스트 그리기
        self.upgradeGoldText.draw()
        self.upgradePercentText.draw()
        self.levelList.draw() #레벨 이미지 그리기
        self.sellCostText.draw()
    def on_mouse_press(self, x, y, button, modifiers): #마우스로 버튼 클릭했을 때 호출되는 함수
        if arcade.get_sprites_at_point((x, y), self.buttonList): #클릭한 위치에 버튼이 있는지 확인
            for btn in arcade.get_sprites_at_point((x, y), self.buttonList): #클릭한 위치에 있는 모든 버튼에 대해 반복
                actions = self.buttons.get(btn) #버튼에 해당하는 함수 가져오기
                if actions:
                    actions() #버튼에 해당하는 함수 호출

    def upgrade(self): #업그레이드 함수
          self.upgradeRandom = random.randint(1, 100)
          self.upgradePercent = 100 - (self.currentLevel * 10)
          if self.currentGold >= self.upgradeGold: #현재 골드가 업그레이드 비용보다 많거나 같은지 확인
            if self.upgradeRandom <= self.upgradePercent:
                self.currentLevel += 1
                self.currentGold -= self.upgradeGold
            else:
                 self.currentLevel = 0
                 self.upgradePercent = 100
          else: pass
              


    def sell(self): #판매 함수
        if 0 <= self.currentLevel < 2: #현재 레벨이 0보다 큰 경우에만 판매 가능
            self.currentGold = self.currentGold + (self.currentLevel * 3000)
        elif 2 <= self.currentLevel < 4:
            self.currentGold = self.currentGold + (self.currentLevel * 5000)
        elif 4 <= self.currentLevel < 6:
            self.currentGold = self.currentGold + (self.currentLevel * 10000)
        elif 6 <= self.currentLevel < 9:
            self.currentGold = self.currentGold + (self.currentLevel * 20000)
        self.currentLevel = 0
        self.upgradePercent = 100

def main(): #메인 함수
    window = arcade.Window(1280, 720, "방패 키우기") #게임 창 속성
    game = GameView() #객체 생성
    game.setup() #게임 설정 함수 호출
    window.show_view(game) #창 띄우기
    arcade.run() #게임 루프 시작
    


if __name__ == "__main__":
    main()