from pyee import EventEmitter


class EventManager:
    def __init__(self):
        self.event_emitter = EventEmitter()

    def emit(self, event, *args, **kwargs):
       
        self.event_emitter.emit(event, *args, **kwargs)

    def on(self, event, handler):
      
        self.event_emitter.on(event, handler)

    def off(self, event, handler):
       
        self.event_emitter.remove_listener(event, handler)
