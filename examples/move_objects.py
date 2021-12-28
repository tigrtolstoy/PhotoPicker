# example from https://stackoverflow.com/questions/54622239/kivy-move-image-following-mouse-movement-without-kv

import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

class TestLayer(FloatLayout):
    def __init__(self, **kwargs):
        super(TestLayer, self).__init__(**kwargs)
        self.pos_hint = {'top':1, 'x':0}
        self.size_hint_x = 1
        self.size_hint_y = 1

    def build(self):
        # specify your image dir and name
        self.img = Image(source='tests/test_data/images/img.jpeg', size=(100, 100))
        self.add_widget(self.img)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if touch.button == 'left':

                # Hold value of touch downed pos
                pass

        return super(TestLayer, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            if touch.button == 'left':

                # self.img.x = self.img.x + (mouse movements distance)
                # self.img.y = self.img.y + (mouse movements distance)
                pass

        return super(TestLayer, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            if touch.button == 'left':

                # process after movement or something?
                pass

        return super(TestLayer, self).on_touch_up(touch)

class TestScreen(Screen):
    def __init__(self, **kwargs):
        super(TestScreen, self).__init__(**kwargs)
        layer = TestLayer()
        self.add_widget(layer)
        layer.build()

sm = ScreenManager()

class DemoApp(App):
    def build(self):
        sm.add_widget(TestScreen(name='test'))
        return sm

if __name__ == '__main__':
    DemoApp().run()
