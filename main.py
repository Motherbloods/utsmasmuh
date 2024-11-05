from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivymd.app import MDApp
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.video import Video

class ImageButton(ButtonBehavior, Image):
    pass

KV = '''
ScreenManager:
    WelcomeScreen:
    HomeScreen:
    CeritaScreen:
    QuizScreen:
    LevelScreen:
    HattaScreen:
    CutScreen:
    DewantaraScreen:
    DiponegoroScreen:
    KartiniScreen:
    PatimuraScreen:
    SoehartoScreen:
    SoekarnoScreen:
    SudirmanScreen:
    Supriyadi2Screen:

<WelcomeScreen>:
    name: "welcome"
    FloatLayout:
        Video:
            id: video
            source: 'Bgwelcome.png'
            state: 'play'
            options: {'eos': 'loop'}
            allow_stretch: True
            keep_ratio: False
        ImageButton:
            source: 'button_play.png'
            size_hint: (0.9, 0.9)
            pos_hint: {"center_x": 0.5, "center_y": 0.1}
            on_release:
                app.start_app()

<HomeScreen>:
    name: "home"
    FloatLayout:
        Video:
            id: video_home
            source: 'Bgmenu.png'  
            state: 'play'
            options: {'eos': 'loop'}
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            orientation: 'vertical'
            padding: 2
            spacing: 5

            Widget:
                size_hint_y: 0.2

            ImageButton:
                source: 'cerita.png'
                size_hint: (0.5, 0.10)
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                on_release:
                    app.go_to_cerita()

            ImageButton:
                source: 'quiz.png'
                size_hint: (0.5, 0.10)
                pos_hint: {"center_x": 0.5, "center_y": 0.3}
                on_release:
                    app.go_to_quiz()

            ImageButton:
                source: 'kembali.png'
                size_hint: (0.5, 0.10)
                pos_hint: {"center_x": 0.5, "center_y": 0.1}
                on_release:
                    app.go_to_welcome()

            Widget:
                size_hint_y: 0.1

<CeritaScreen>:
    name: "cerita"
    FloatLayout:
        Video:
            id: video_cerita
            source: 'Bgmenu.png'
            state: 'play'
            options: {'eos': 'loop'}
            allow_stretch: True
            keep_ratio: False

        ScrollView:
            size_hint: 1, 0.6
            pos_hint: {"center_x": 0.5, "top": 0.9}
            GridLayout:
                id: grid_heroes
                cols: 2
                row_default_height: 150
                row_force_default: True
                spacing: 10
                padding: 10
                size_hint_y: None
                height: self.minimum_height  
                
                ImageButton:
                    source: 'IMG_hatta.png'
                    size_hint_x: 0.5
                    on_release: app.show_story('Hatta')
                ImageButton:
                    source: 'IMG_cutnyak_dien.png'
                    size_hint_x: 0.5
                    on_release: app.show_story('Cut')
                ImageButton:
                    source: 'IMG_dewantara.png'
                    size_hint_x: 0.5
                    on_release: app.show_story('Dewantara')
                        
                ImageButton:
                    source: 'IMG_diponegoro.png'
                    size_hint_x: 0.5
                    on_release: app.show_story('Diponegoro')
                ImageButton:
                    source: 'IMG_kartini.png'
                    size_hint_x: 0.5
                    on_release: app.show_story('Kartini')
                ImageButton:
                    source: 'IMG_patimura.png'
                    size_hint_x: 0.5
                    on_release: app.show_story('Patimura')
                ImageButton:
                    source: 'IMG_soeharto.png'
                    size_hint_x: 0.5
                    on_release: app.show_story('Soeharto')
                ImageButton:
                    source: 'IMG_soekarno.png'
                    size_hint_x: 0.5
                    on_release: app.show_story('Soekarno')
                ImageButton:
                    source: 'IMG_sudirman.png'
                    size_hint_x: 0.5
                    on_release: app.show_story('Sudirman')
                ImageButton:
                    source: 'IMG_supriyadi2.png'
                    size_hint_x: 0.5
                    on_release: app.show_story('Supriyadi2')

                

    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 5
        MDLabel:
            text: ""
            halign: "center"
            theme_text_color: "Primary"
            font_style: "H4"
        ImageButton:
            source: 'kembali.png'
            size_hint: (0.5, 0.5)
            pos_hint: {"center_x": 0.5}
            on_release:
                app.go_to_home()


<QuizScreen>:
    name: "quiz"
    FloatLayout:
        Video:
            id: video_quiz
            source: 'Bgquiz.png'  
            state: 'play'
            options: {'eos': 'loop'}
            allow_stretch: True
            keep_ratio: False

        ImageButton:
            id: level1
            source: 'button_quiz.png'
            size_hint: (0.3, 0.3)
            pos_hint: {"center_x": 0.35, "center_y": 0.6}
            on_release:
                app.go_to_level(0)

        ImageButton:
            id: level2
            source: 'button_quiz.png'
            size_hint: (0.3, 0.3)
            pos_hint: {"center_x": 0.65, "center_y": 0.6}
            on_release:
                app.go_to_level(1)

        ImageButton:
            id: level3
            source: 'button_quiz.png'
            size_hint: (0.3, 0.3)
            pos_hint: {"center_x": 0.35, "center_y": 0.4}
            on_release:
                app.go_to_level(2)

        ImageButton:
            id: level4
            source: 'button_quiz.png'
            size_hint: (0.3, 0.3)
            pos_hint: {"center_x": 0.65, "center_y": 0.4}
            on_release:
                app.go_to_level(3)

        ImageButton:
            id: level5
            source: 'button_quiz.png'
            size_hint: (0.3, 0.3)
            pos_hint: {"center_x": 0.5, "center_y": 0.2}
            on_release:
                app.go_to_level(4)

        ImageButton:
            source: 'kembali.png'
            size_hint: (0.3, 0.2)
            pos_hint: {"center_x": 0.5, "center_y": 0.1}
            on_release:
                app.go_to_home()

<LevelScreen>:
    name: "level"
    FloatLayout:
        Video:
            id: video_level
            source: 'Bgsoal.png'  
            state: 'play'
            options: {'eos': 'loop'}
            allow_stretch: True
            keep_ratio: False
        
        BoxLayout:
            orientation: 'vertical'
            padding: 20
            spacing: 10
            size_hint: (0.7, 0.7)  
            pos_hint: {"center_x": 0.5, "center_y": 0.4}



            Image:
                id: question_image
                source: ""

            MDRaisedButton:
                id: option1
                text: ""
                on_release:
                    app.check_answer(1)

            MDRaisedButton:
                id: option2
                text: ""
                on_release:
                    app.check_answer(2)

            MDLabel:
                id: result_label
                text: ""
                halign: "center"
                theme_text_color: "Secondary"

        ImageButton:
            source: 'kembali.png'
            size_hint: (0.3, 0.9)
            pos_hint: {"center_x": 0.5, "center_y": 0.1}
            on_release:
                app.go_to_quiz()


<HattaScreen>:
    name: "hatta"
    FloatLayout:
        Video:
            source: 'BgHATTA.png'
            state: 'play'
            options: {'eos': 'loop'}
            allow_stretch: True
            keep_ratio: False
            size_hint: (1, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        ImageButton:
            source: 'kembali.png'
            size_hint: (0.2, 0.1)
            pos_hint: {"center_x": 0.5, "center_y": 0.08}
            on_release:
                app.go_to_cerita()


<CutScreen>:
    name: "cut"
    FloatLayout:
        Video:
            source: 'BgCUTNYAK.png'
            state: 'play'
            options: {'eos': 'loop'}
            allow_stretch: True
            keep_ratio: False
            size_hint: (1, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        ImageButton:
            source: 'kembali.png'
            size_hint: (0.2, 0.1)
            pos_hint: {"center_x": 0.5, "center_y": 0.08}
            on_release:
                app.go_to_cerita()

<DewantaraScreen>:
    name: "dewantara"
    FloatLayout:
        Video:
            source: 'BgDEWANTARA.png'
            state: 'play'
            options: {'eos': 'loop'}
            allow_stretch: True
            keep_ratio: False
            size_hint: (1, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        ImageButton:
            source: 'kembali.png'
            size_hint: (0.2, 0.1)
            pos_hint: {"center_x": 0.5, "center_y": 0.08}
            on_release:
                app.go_to_cerita()

<DiponegoroScreen>:
    name: "diponegoro"
    FloatLayout:
        Video:
            source: 'BgDIPPONEGORO.png'
            state: 'play'
            options: {'eos': 'loop'}
            allow_stretch: True
            keep_ratio: False
            size_hint: (1, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        ImageButton:
            source: 'kembali.png'
            size_hint: (0.2, 0.1)
            pos_hint: {"center_x": 0.5, "center_y": 0.08}
            on_release:
                app.go_to_cerita()

<KartiniScreen>:
    name: "kartini"
    FloatLayout:
        Video:
            source: 'BgRAKARTINI.png'
            state: 'play'
            options: {'eos': 'loop'}
            allow_stretch: True
            keep_ratio: False
            size_hint: (1, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        ImageButton:
            source: 'kembali.png'
            size_hint: (0.2, 0.1)
            pos_hint: {"center_x": 0.5, "center_y": 0.08}
            on_release:
                app.go_to_cerita()

<PatimuraScreen>:
    name: "patimura"
    FloatLayout:
        Video:
            source: 'BgPATIMURA.png'
            state: 'play'
            options: {'eos': 'loop'}
            allow_stretch: True
            keep_ratio: False
            size_hint: (1, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        ImageButton:
            source: 'kembali.png'
            size_hint: (0.2, 0.1)
            pos_hint: {"center_x": 0.5, "center_y": 0.08}
            on_release:
                app.go_to_cerita()

<SoehartoScreen>:
    name: "soeharto"
    FloatLayout:
        Video:
            source: 'BgSOEHARTO.png'
            state: 'play'
            options: {'eos': 'loop'}
            allow_stretch: True
            keep_ratio: False
            size_hint: (1, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        ImageButton:
            source: 'kembali.png'
            size_hint: (0.2, 0.1)
            pos_hint: {"center_x": 0.5, "center_y": 0.08}
            on_release:
                app.go_to_cerita()

<SoekarnoScreen>:
    name: "soekarno"
    FloatLayout:
        Video:
            source: 'BgSOEKARNO.png'
            state: 'play'
            options: {'eos': 'loop'}
            allow_stretch: True
            keep_ratio: False
            size_hint: (1, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        ImageButton:
            source: 'kembali.png'
            size_hint: (0.2, 0.1)
            pos_hint: {"center_x": 0.5, "center_y": 0.08}
            on_release:
                app.go_to_cerita()

                
<SudirmanScreen>:
    name: "sudirman"
    FloatLayout:
        Video:
            source: 'BgSUDIRMAN.png'
            state: 'play'
            options: {'eos': 'loop'}
            allow_stretch: True
            keep_ratio: False
            size_hint: (1, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        ImageButton:
            source: 'kembali.png'
            size_hint: (0.2, 0.1)
            pos_hint: {"center_x": 0.5, "center_y": 0.08}
            on_release:
                app.go_to_cerita()


<Supriyadi2Screen>:
    name: "supriyadi2"
    FloatLayout:
        Video:
            source: 'BgSUPRIYADI.png'
            state: 'play'
            options: {'eos': 'loop'}
            allow_stretch: True
            keep_ratio: False
            size_hint: (1, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        ImageButton:
            source: 'kembali.png'
            size_hint: (0.2, 0.1)
            pos_hint: {"center_x": 0.5, "center_y": 0.08}
            on_release:
                app.go_to_cerita()

'''

class WelcomeScreen(Screen):
    def on_enter(self):
        self.sound = SoundLoader.load('opening_sound.mp3')
        if self.sound:
            self.sound.loop = True
            self.sound.play()

    def on_leave(self):
        if self.sound and self.sound.state == 'play':
            self.sound.stop()

class HomeScreen(Screen):
    pass

class HattaScreen(Screen):
    pass
class CutScreen(Screen):
    pass
class DewantaraScreen(Screen):
    pass
class DiponegoroScreen(Screen):
    pass
class KartiniScreen(Screen):
    pass
class PatimuraScreen(Screen):
    pass
class SoehartoScreen(Screen):
    pass
class SoekarnoScreen(Screen):
    pass
class SudirmanScreen(Screen):
    pass
class Supriyadi2Screen(Screen):
    pass

class CeritaScreen(Screen):
    def on_enter(self):
        video = self.ids.video_cerita
        if video:
            video.state = 'play'



class QuizScreen(Screen):
    pass

class LevelScreen(Screen):
    pass

class WelcomeApp(MDApp):
    def build(self):
        # Window.size = (360, 600)
        self.level_data = [
            {"image": "IMG_supriyadi2.png", "options": ["Suryadi", "Supriyadi"], "answer": 2},
            {"image": "IMG_patimura.png", "options": ["Patrimura", "Patimura"], "answer": 2},
            {"image": "IMG_soekarno.png", "options": ["Soekarno", "Soehkarno"], "answer": 1},
            {"image": "IMG_hatta.png", "options": ["Moh halim", "Moh hatta"], "answer": 2},
            {"image": "IMG_sudirman.png", "options": ["Sudirman", "Supirman"], "answer": 1},
            {"image": "IMG_soeharto.png", "options": ["Sriharto", "Soeharto"], "answer": 2},
            {"image": "IMG_kartini.png", "options": ["Kartini", "Krartini"], "answer": 1},
            {"image": "IMG_diponegoro.png", "options": ["Diponegroro", "Diponegoro"], "answer": 2},
            {"image": "IMG_dewantara.png", "options": ["Diwantara", "Dewantra"], "answer": 1},
            {"image": "IMG_cutnyak_dien.png", "options": ["laila", "Cut Nyak Dien"], "answer": 2},
        ]
        self.levels_unlocked = [True, False, False, False, False]  
        self.current_level = 0
        self.current_question = 0
        return Builder.load_string(KV)

    def start_app(self):
        self.root.transition = SlideTransition(direction='left')
        self.root.current = "home"

    def go_to_welcome(self):
        self.root.transition = SlideTransition(direction='right')
        self.root.current = "welcome"

    def show_story(self, story_name):
        if story_name == 'Hatta':
            self.root.current = "hatta"
        if story_name == 'Cut':
            self.root.current = "cut"
        if story_name == 'Dewantara':
            self.root.current = "dewantara"
        if story_name == 'Diponegoro':
            self.root.current = "diponegoro"
        if story_name == 'Kartini':
            self.root.current = "kartini"
        if story_name == 'Patimura':
            self.root.current = "patimura"
        if story_name == 'Soeharto':
            self.root.current = "soeharto"
        if story_name == 'Soekarno':
            self.root.current = "soekarno"
        if story_name == 'Sudirman':
            self.root.current = "sudirman"
        if story_name == 'Supriyadi2':
            self.root.current = "supriyadi2"
         

    def go_to_home(self):
        self.root.transition = SlideTransition(direction='left')
        self.root.current = "home"

  

    def go_to_cerita(self):
        self.root.transition = SlideTransition(direction='left')
        self.root.current = "cerita"


    def go_to_quiz(self):
        self.update_quiz_screen()
        self.root.transition = SlideTransition(direction='left')
        self.root.current = "quiz"

    def update_quiz_screen(self):
        quiz_screen = self.root.get_screen("quiz")
        for i in range(5):
            button = quiz_screen.ids[f'level{i+1}']
            if not self.levels_unlocked[i]:
                button.opacity = 0.5  
                button.disabled = True  
            else:
                button.opacity = 1  
                button.disabled = False  

    def go_to_level(self, level_index):
        if not self.levels_unlocked[level_index]:
            print(f"Level {level_index + 1} terkunci. Selesaikan level sebelumnya dulu!")
            return
        self.current_level = level_index
        self.current_question = 0
        self.load_question()

    def load_question(self):
        screen = self.root.get_screen("level")
        level_data = self.level_data[self.current_level * 2 + self.current_question]  
        screen.ids.question_image.source = level_data["image"]
        screen.ids.option1.text = level_data["options"][0]
        screen.ids.option2.text = level_data["options"][1]
        screen.ids.result_label.text = ""

        self.root.transition = SlideTransition(direction='left')
        self.root.current = "level"

    def check_answer(self, selected_option):
        level_data = self.level_data[self.current_level * 2 + self.current_question]
        screen = self.root.get_screen("level")
        if selected_option == level_data["answer"]:
            screen.ids.result_label.text = "Wihhhh kamu benarr!"
            self.current_question += 1
            if self.current_question == 2:  
                self.unlock_next_level()
            else:
                self.load_question()  
        else:
            screen.ids.result_label.text = "Yahh coba lagi yukk!"

    def unlock_next_level(self):
        if self.current_level + 1 < len(self.levels_unlocked):
            self.levels_unlocked[self.current_level + 1] = True
        self.go_to_quiz()

if __name__ == '__main__':
    WelcomeApp().run()
