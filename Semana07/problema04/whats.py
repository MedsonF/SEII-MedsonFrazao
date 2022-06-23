BoxLayout:
    orientation:'vertical'
    AppBar:
    Widget:

<AppBar@BoxLayout>:
    padding: '6dp'
    canvas:
        Color:
            rgba: 0,0.3,0.13,3
        Rectangle:
            size:self.size
            post:self.pos
    size_hint_y: None
    height: '50dp'
    Label:
        text: 'HashWhats'
        bold: True
        font_size:'20dp'
        haling: 'left'
        text_size: self.size
        valing:'center'
        padding_x:'10dp'
    Icon:
        background_normal: 'lupa.png'
    Icon:
        background_normal: 'pontos.png'

<Menu@BoxLayout>:
    canvas:
        Color
            rgba: 0,0.3,0.13,1
        REctangle:
            size:self.size
            pos: self.pos
    size_hint_y:None
    heitght:'50sp'
    Icon:
        background_normal: 'camera.png'
    MenuButton:
        text: 'CHATS'
        activate: True
    MenuButton:
        text: 'STATUS'
    MenuButton:
        text: 'CALLS'

<Chat@BoxLayout>:
    size_hint_y: None
    height:'100dp'
    Image:
        source:'logo.png'
        size_hint_x: None
        width:self_height
    BoxLayout:
        orientation:'vertical'
        Label: 
            text:'nome do grupo'
            color: 0,0,0,1
            text_size: self_size
            helign:'left'
        Label:
            text:'will: a ultima mensagem'
            text_size: self.size
            halign:'left'
            color: 0,0,0,1
            valing: 'center'
    BoxLayout:
        size_hint_x: None
        width:'100dp'
        padding:'7dp'
        Label:
            text:'21:01PM'
            color: 0,0,0,0.5
            text_size: self_size
            valign:'top'
            halign: 'right'

<MenuButton@Button>:
    activate: False
    canvas:
        Color:
            rgba:1,1,1,1
        Line: 
            width: 4 if root.activate else 0.1
            points: self.x, self.y, self.x+self.width, self.y

    background_color:0,0,0,0
    bold:True    
    color: (1,1,1,1) if root.activate else (1,1,1,0.5)
    
<Icon@Button>:
    activate: False
    size_hint_x: None
    width: self_height
    border: 0,0,0,0
    background_color: (1,1,1,1) if root.activate else (1,1,1,0.5)
