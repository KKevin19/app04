import flet as ft


def calc_suma(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtnum1.value.strip())
        num2=float(txtnum2.value.strip())
        resultado=num1+num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error Ingresa valores correctos" 
        

def calc_resta(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtnum1.value.strip())
        num2=float(txtnum2.value.strip())
        resultado=num1-num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error Ingresa valores correctos" 
        
        
def calc_mult(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtnum1.value.strip())
        num2=float(txtnum2.value.strip())
        resultado=num1*num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error Ingresa valores correctos" 

def calc_div(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtnum1.value.strip())
        num2=float(txtnum2.value.strip())
        resultado=num1/num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error Ingresa valores correctos"         



#funcion de manejo s¿de eventos        

def on_calc_suma=(e):
    calc_suma(txtNum1, txtnum2, lblresultado)
    page.update()

def on_calc_resta=(e):
    calc_resta(txtNum1, txtnum2, lblresultado)
    page.update()

def on_calc_mult=(e):
    calc_mult(txtNum1, txtnum2, lblresultado)
    page.update()

def on_calc_div=(e):
    calc_div(txtNum1, txtnum2, lblresultado)
    page.update()

def limpiar(e):
    txtNum1.value =""
    txtNum2.value =""
    lblResultado.value = "Resultado"
    page.update()


#se crean los botones de la aplicacion
btnSuma=ft.ElevatedButton(text="+",on_click=on_calc_suma)
btnResta=ft.ElevatedButton(text="+",on_click=on_calc_resta)
btnMult=ft.ElevatedButton(text="+",on_click=on_calc_mult)
btnDiv=ft.ElevatedButton(text="+",on_click=on_calc_div)
btnLimpiar=ft.ElevatedButton(text="+",on_click=on_calc_limpiar)

ft.app(main)
