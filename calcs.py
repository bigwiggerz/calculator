import wx

class MyFrame(wx.Frame): #создаем класс, наследующий свойства класса wx.Frame
def __init__(self, parent, title): #конструктор класса
super().__init__(parent, title=title, size=(400, 600)) #конструктор базового класса (нужно для того, чтобы модифицировать класс Frame)
panel = wx.Panel(self) #делаем панель

font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT) #измененяем размера шрифта
font.SetPointSize(15)
panel.SetFont(font)

vbox = wx.BoxSizer(wx.VERTICAL) #робим вертикальный сайзер
self.txtCtrl = wx.ComboBox(panel) #создаем поле ввода
#добавляем поле ввода в сайзер и указываем параметры для правильного размещения этого поля в окне
vbox.Add(self.txtCtrl, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

gbox = wx.GridSizer(5, 4, 5, 5) #делаем новый сайзер
#создаем кнопки внутри нового сайзера
gbox.AddMany( [(wx.Button(panel, label='C'), wx.ID_ANY, wx.EXPAND),
(wx.StaticText(panel), wx.EXPAND),
(wx.StaticText(panel), wx.EXPAND),
(wx.Button(panel, label='Close'), wx.ID_ANY, wx.EXPAND),
(wx.Button(panel, label='7'), wx.ID_ANY, wx.EXPAND),
(wx.Button(panel, label='8'), wx.ID_ANY, wx.EXPAND),
(wx.Button(panel, label='9'), wx.ID_ANY, wx.EXPAND),
(wx.Button(panel, label='/'), wx.ID_ANY, wx.EXPAND),
(wx.Button(panel, label='4'), wx.ID_ANY, wx.EXPAND),
(wx.Button(panel, label='5'), wx.ID_ANY, wx.EXPAND),
(wx.Button(panel, label='6'), wx.ID_ANY, wx.EXPAND),
(wx.Button(panel, label='*'), wx.ID_ANY, wx.EXPAND),
(wx.Button(panel, label='1'), wx.ID_ANY, wx.EXPAND),
(wx.Button(panel, label='2'), wx.ID_ANY, wx.EXPAND),
(wx.Button(panel, label='3'), wx.ID_ANY, wx.EXPAND),
(wx.Button(panel, label='-'), wx.ID_ANY, wx.EXPAND),
(wx.Button(panel, label='0'), wx.ID_ANY, wx.EXPAND),
(wx.Button(panel, label='.'), wx.ID_ANY, wx.EXPAND),
(wx.Button(panel, label='='), wx.ID_ANY, wx.EXPAND),
(wx.Button(panel, label='+'), wx.ID_ANY, wx.EXPAND)] )
#добавляем новоиспечённый сайзер в вертикальный сайзер vbox
vbox.Add(gbox, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
panel.SetSizer(vbox) #устанавливаем сайзер vbox в нашу панель
self.Bind(wx.EVT_BUTTON, self.OnClicked) #связываем кнопки c функцией (связываем дизайн с логикой)
#делаем функцию, которая будет выполнятся при нажатии на кнопочки
def OnClicked(self, evt):
label = evt.GetEventObject().GetLabel() #создаем нью переменную, чтобы записывать в нее имя нажатых кнопочек

if label == '=': #если имя кнопочки равно "=", то...
compute = self.txtCtrl.GetValue() #берем выражение из поля ввода
#тут игнорируем пустой ввод
if not compute.strip():
return

result = eval(compute) #а тут считаем полученное выражение
self.txtCtrl.Insert(compute, 0) #добавляем в историю наши расчеты
self.txtCtrl.SetValue(str(result)) #показываем

elif label == 'C': #если имя кнопки "C"...
self.txtCtrl.SetValue("") #чистим все
elif label == 'Close': #если имя кнопки "Close"...
frame.Destroy() #уничтожаем окно при нажатии
else: #иначе...
self.txtCtrl.SetValue(self.txtCtrl.GetValue() + label) #добавляем имя кнопки к текущей строке в поле ввода

#дефолтные строчки для создания окна
app = wx.App()
frame = MyFrame(None, 'Лучший калькулятор')
frame.Show()
app.MainLoop()