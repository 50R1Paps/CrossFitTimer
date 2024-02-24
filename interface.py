from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
import datetime

class MyApp(App):
    def build(self):
        time = int(input("Quanto dura il primo intervallo?"))
        self.target_time = datetime.datetime.now() + datetime.timedelta(seconds=time+3)
        self.countdown_active = False
        self.main_box = BoxLayout(orientation='vertical')
        
        self.button = Button(text='Start Countdown', font_size=100)
        self.main_box.add_widget(self.button)
    
        self.button.bind(on_press=self.start_countdown)
        
        return self.main_box
    
    def start_countdown(self, button):
        self.countdown_active = True
        Clock.schedule_interval(self.timer, 1.0)

    def timer(self, dt):
        if self.countdown_active:
            current_time = datetime.datetime.now()
            remaining_time = self.target_time - current_time
            if remaining_time.total_seconds() <= 0:
                self.button.text = 'Countdown finished!'
                self.countdown_active = False
                self.stop()
            else:
                self.button.text = str(int(remaining_time.total_seconds()))  # Mostra solo la parte intera

if __name__ == '__main__':
    print("Starting the app")
    intervals = int(input("Quanti intervalli sono?"))
    for i in range(intervals):
        MyApp().run()
