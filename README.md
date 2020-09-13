# keremkerem

main.py dosyasını çalıştırdığımda:
(When I run the main.py file:)
*****************************************************************************************************
Traceback (most recent call last):

File "C:/Users/W 8.1/Desktop/PythonApplication1/pythonProject/main.py", line 17, in <module>
app()
    
File "C:/Users/W 8.1/Desktop/PythonApplication1/pythonProject/main.py", line 14, in app
win = myApp()

File "C:/Users/W 8.1/Desktop/PythonApplication1/pythonProject/main.py", line 10, in __init__
self.ui.setupUi(self)
    
TypeError: setupUi() missing 1 required positional argument: 'MainWindow'
******************************************************************************************************

hatası alıyorum.
(I am getting this error.)

masaustu.py dosyası, designer ile oluşturduğum .ui dosyasının .py dosyasına dönüştürülmüş hali. main.py'da ise oluşturduğum pencereyi açmaya çalıştım.
