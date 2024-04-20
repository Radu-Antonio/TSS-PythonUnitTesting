from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.anchorlayout import AnchorLayout

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        dropdown = DropDown()
        for word in ['F2L Cases', 'OLLs', 'PLLs']:
            btn = Button(text=word, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        main_button = Button(text='Algorithm sets')
        main_button.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(main_button, 'text', x))
        layout.add_widget(main_button)

        switch_button = Button(text='Timer')
        switch_button.bind(on_press=self.switch_to_timer)
        layout.add_widget(switch_button)

        self.add_widget(layout)

    def switch_to_timer(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'timer_screen'

class TimerScreen(Screen):
    def __init__(self, **kwargs):
        super(TimerScreen, self).__init__(**kwargs)
        self.timer_started = False
        self.time_seconds = 0

        layout = BoxLayout(orientation='vertical', spacing=10)
        
        self.timer_display = Label(text='00:00', font_size=40)
        layout.add_widget(self.timer_display)

        self.start_stop_button = Button(text='Start', size_hint=(1, 0.2))
        self.start_stop_button.bind(on_press=self.start_stop_timer)
        layout.add_widget(self.start_stop_button)

        reset_button = Button(text='Reset', size_hint=(1, 0.2))
        reset_button.bind(on_press=self.reset_timer)
        layout.add_widget(reset_button)

        back_button = Button(text='Back', size_hint=(1, 0.2))
        back_button.bind(on_release=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def start_stop_timer(self, instance):
        if self.timer_started:
            Clock.unschedule(self.update_timer)
            self.start_stop_button.text = 'Start'
        else:
            Clock.schedule_interval(self.update_timer, 1)
            self.start_stop_button.text = 'Stop'
        self.timer_started = not self.timer_started

    def update_timer(self, dt):
        self.time_seconds += 1
        minutes, seconds = divmod(self.time_seconds, 60)
        self.timer_display.text = '{:02d}:{:02d}'.format(minutes, seconds)

    def reset_timer(self, instance):
        if self.timer_started:
            self.start_stop_timer(instance)  
        self.time_seconds = 0
        self.timer_display.text = '00:00'

    def go_back(self, instance):
        self.manager.current = 'main_screen'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(TimerScreen(name='timer_screen'))
        return sm

if __name__ == '__main__':
    MyApp().run()
