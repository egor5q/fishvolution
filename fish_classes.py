
resttypes=['immobility', 'moving', 'hide', 'lying']
# immobility - неподвижно находится в воде.
# moving - отдыхает в движении.
# hide - прячется куда-то для того, чтобы отдохнуть
# lying - лежит на чём-нибудь

class Fish:
  
    def __init__(self):
        self.speed=1               # Скорость рыбы. Ну тут все и так понятно.
        self.foodstorage=6         # Запас еды
        self.currentfood=6         # Текущая еда.
        self.feed=3                # Сколько надо currentfood, чтобы чувствовать себя сытой
        self.type='vegan'          # vegan/carnivorous/omnivorous (травоядное/плотоядное/всеядное)
        self.stealth=1             # Общая заметность на любой поверхности. Чем выше, тем больше шанс, что другие рыбы вас увидят. 1 = 100%
        self.silence=1             # Общая громкость рыбы. Чем выше, тем больше шанс быть услышанными другими рыбами. 1 = 100%
        self.vision=1              # Зрение. Чем выше, тем больше шанс увидеть других рыб. 1 = 100%
        self.hearing=1             # Слух. Чем выше, тем больше шанс услышать других рыб. 1 = 100%
        self.resttype='immobility' # Тип отдыха рыбы. Все они есть выше.
        self.maxenergy=100         # Силы рыбы. Тратятся постоянно, а иногда - в повышенном объёме.
        self.energy=100            # Если == 0, то рыба либо засыпает (если есть еда), либо умирает.
        self.restspeed=1           # Скорость восстановления сил рыбы во время сна. 1 = 100%
        self.abilities=[]          # Различные способности рыбы. Например: отращивание конечностей, как у морской звезды.
        self.mind=1                # Интеллект рыбы. Поможет выжить в нестандартных ситуациях.
        self.currenttarget=None    # Текущая цель рыбы.
        self.currentloc={          # Текущая локация.
            'place':'grassland',
            'block':1,
            'depth':4
        }         
    
    
    
    def action(self):
        if self.currenttarget==None:
    
    
