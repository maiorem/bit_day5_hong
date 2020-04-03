
class Quiz:

    def __init__(self,text):
        self.text = text
        self.yes = None
        self.no = None


class QuizManager:

    def __init__(self):
        q1 = Quiz("인싸력 측정하면 난 최소 장원급제다.")
        q2 = Quiz("나만의 고정 Pick! 아는맛 = 인생의 진리")
        q3 = Quiz("인생은 인싸와 아싸. 그 사이에 그럴싸다.")
        q4 = Quiz("진정한 먹리어답터. 새로운 것은 먹어봐야 직성이 풀리는 편.")
        q5 = Quiz("난... ㅈㅏ주 고독을 즐긴다...☆")
        q6 = Quiz("잘 모르겠고, 전 그냥 맥도날드면 다 좋은데요?")
        q7 = Quiz("풍성한 재료의 맛 놓칠세라, 입찢도 불사하고 입에 넣는 편")
        q8 = Quiz("어차피 인생은 고기서 고기다. 고기면 다 좋다.")
        q9 = Quiz("패티는 소고기. 뭐로가도 소고기. 무조건 소고기.")

        q1.yes = q2
        q1.no = q3
        q2.no = q4
        q3.yes = q4
        q5.yes = q6
        q6.yes = q7
        q7.no = q8
        q8.no = q9

        self.start_quiz = q1

    def getFirstQuiz(self):
        return self.start_quiz


class QuizUI:

    def __init__(self):
        manager = QuizManager()
        self.playShow(manager.getFirstQuiz())


    def playShow(self,quiz):

        if quiz == None:
            print("THE END")
            return

        answer = input(quiz.text)

        if answer == 'y':
            self.playShow(quiz.yes)
        elif answer == 'n':
            self.playShow(quiz.no)

ui = QuizUI()

