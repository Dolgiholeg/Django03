from django import forms

class Nashaforma(forms.Form):
    name = forms.CharField(label='Ваше имя')
    num = forms.IntegerField(label='Номер', required=False, max_value=100, widget=forms.Textarea, initial=12,help_text='напишите сколько вам лет')

class Nashaforma1(forms.Form):
    name1 = forms.CharField(label='Имя животного',help_text='напишите имя животного')
    breed = forms.CharField(label='Порода животного',help_text='напишите породу животного')
    age = forms.IntegerField(label='Возраст животного',help_text='напишите возраст животного')
    color = forms.CharField(label='Цвет животного',help_text='напишите цвет животного')
    food = forms.CharField(label='Любимая еда животного',help_text='напишите любимую еду животного')
    foto = forms.ImageField(label='Фото животного',help_text='Загрузите фото животного')

class Forma3(forms.Form):
    k1 = forms.DecimalField(label='десятичные цифры')
    k2 = forms.EmailField(label='электронный адрес')
    k3 = forms.BooleanField(label='поставьте галочку')
    k4 = forms.NullBooleanField(label='вы человек')# будет предложен выбор в трёх вариантах ответов
    k5 = forms.URLField(label='адрес в интернете')
    k6 = forms.GenericIPAddressField(label='ip-адрес')
    k7 = forms.FilePathField(label='выберите файл', path='C:\\Users\\dolgi\\Desktop', allow_folders=True, match='.*\.txt')# путь откуда берётся файл - сейчас мой рабочий стол, дальше разрешение на видимость внутренних папок, дальше искать только файлы txt
    k8 = forms.ImageField(label='выберите картинку')
    k9 = forms.FileField(label='файл')
    vibor=(('английский','En'),('русский','Rus'),('французкий','Fr'))
    k10 = forms.TypedChoiceField(label='свои варианты ответов', choices=vibor)#ответом будет первое(сохранится)

class Forma4(forms.Form):
    k1 = forms.CharField(label='Ваше имя')
    k2 = forms.IntegerField(label='Ваш возраст')
    Pol = (('мужской', 'мужской'), ('женский', 'женский'), ('не традиционный', 'не традиционный'))
    k3 = forms.TypedChoiceField(label='Ваш пол', choices=Pol)
    k4 = forms.CharField(label='Место жительство')
    k5 = forms.EmailField(label='электронный адрес')
    Education = (('не оконченное среднее', 'не оконченное среднее'), ('среднее', 'среднее'), ('средне-специальное', 'средне-специальное'),
                 ('средне-техническое', 'средне-техническое'), ('не оконченное высшее', 'не оконченное высшее'), ('высшее', 'высшее'))
    k6 = forms.TypedChoiceField(label='Ваше образование', choices=Education)
    smoke = (('да', 'да'), ('нет', 'нет'), ('неизвестно', 'неизвестно'))
    k7 = forms.TypedChoiceField(label='Вы курите?', choices = smoke)
    Animal = (('кошка', 'кошка'), ('собака', 'собака'), ('рыбки', 'рыбки'), ('кролик', 'кролик'), ('птица', 'птица'))
    k8 = forms.TypedChoiceField(label='Ваше домашнее животное', choices=Animal)
    Status = (('студент', 'студент'), ('рабочий', 'рабочий'), ('инженер', 'инженер'), ('предпринематель', 'предпринематель'),
              ('безработный', 'безработный'))
    k9 = forms.TypedChoiceField(label='Ваш статус', choices=Status)
    k10 = forms.ImageField(label='Ваша аватарка')

