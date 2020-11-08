import tkinter
import re
from encoder import GilbertMoureEncode

window = tkinter.Tk()
window.title('Алгоритм Гильберта-Мура')

window.columnconfigure([0, 1], weight=1, minsize=50)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1, minsize=50)



frm_input1 = tkinter.Frame(master=window)
frm_input1.grid(row=0, column=0)
frm_output1 = tkinter.Frame(master=window)
frm_output1.grid(row=0, column=1)
frm_controller1 = tkinter.Frame(master=window)
frm_controller1.grid(row=1, column=0)

lbl_input1 = tkinter.Label(master=frm_input1, text='Введите строку')
lbl_output1 = tkinter.Label(master=frm_output1, text='Результат')
lbl_input1.pack(padx=5, pady=5)
lbl_output1.pack(padx=5, pady=5)
ent_input1 = tkinter.Entry(master=frm_input1, width=50)
ent_output1 = tkinter.Entry(master=frm_output1, width=50)
ent_input1.pack(padx=5, pady=5)
ent_output1.pack(padx=5, pady=5)

def appEncode(event):
    message = ent_input1.get()
    output = ent_output1
    if not re.fullmatch(r'[\+\*/=-]*', r'%s' % message):
        output.delete(0, tkinter.END)
        output.insert(0,'Ошибка. Неверно введено исходное сообщение.')
    else:
        encoder = GilbertMoureEncode()
        outText = encoder.encode(message)
        output.delete(0, tkinter.END)
        output.insert(0, outText)

btn_encode = tkinter.Button(text='Закодировать', master=frm_controller1)
btn_encode.bind('<Button-1>', appEncode)
btn_encode.pack()



frm_input2 = tkinter.Frame(master=window)
frm_input2.grid(row=2, column=0)
frm_output2 = tkinter.Frame(master=window)
frm_output2.grid(row=2, column=1)
frm_controller2 = tkinter.Frame(master=window)
frm_controller2.grid(row=3, column=0)

lbl_input2 = tkinter.Label(master=frm_input2, text='Введите строку')
lbl_output2 = tkinter.Label(master=frm_output2, text='Результат')
lbl_input2.pack(padx=5, pady=5)
lbl_output2.pack(padx=5, pady=5)
ent_input2 = tkinter.Entry(master=frm_input2, width=50)
ent_output2 = tkinter.Entry(master=frm_output2, width=50)
ent_input2.pack(padx=5, pady=5)
ent_output2.pack(padx=5, pady=5)

def appDecode(event):
    message = ent_input2.get()
    output = ent_output2
    if not re.fullmatch(r'[10]*', r'%s' % message):
        output.delete(0, tkinter.END)
        output.insert(0,'Ошибка. Неверно введено исходное сообщение.')
    else:
        encoder = GilbertMoureEncode()
        outText = encoder.decode(message)
        output.delete(0, tkinter.END)
        output.insert(0, outText)

btn_decode = tkinter.Button(text='Раскодировать', master=frm_controller2)
btn_decode.bind('<Button-1>', appDecode)
btn_decode.pack()





encoder = GilbertMoureEncode()
pre_output = zip(encoder.alphabet, encoder.encodedAlphabet)
output = ''
for i in pre_output:
    output += "'" + str(i[0]) + "' : " + str(i[1]) + '   '

vector_craft = list(map(len, encoder.encodedAlphabet))

craft_num = 0
for i in vector_craft:
    craft_num += 1/(2**i)

frm_alphabet1 = tkinter.Frame(master=window)
frm_alphabet1.grid(row=4, column=0)
lbl_alphabet1 = tkinter.Label(master=frm_alphabet1, text='Алфавит:')
lbl_alphabet1.pack(padx=5, pady=5)
frm_alphabet2 = tkinter.Frame(master=window)
frm_alphabet2.grid(row=4, column=1)
lbl_alphabet2 = tkinter.Label(master=frm_alphabet2, text=output)
lbl_alphabet2.pack(padx=5, pady=5)



frm_avglen1 = tkinter.Frame(master=window)
frm_avglen1.grid(row=5, column=0)
lbl_avglen1 = tkinter.Label(master=frm_avglen1, text='Средняя длина кодового слова:')
lbl_avglen1.pack(padx=5, pady=5)
frm_avglen2 = tkinter.Frame(master=window)
frm_avglen2.grid(row=5, column=1)
lbl_avglen2 = tkinter.Label(master=frm_avglen2, text=str(sum(map(len, encoder.encodedAlphabet)) / len(encoder.encodedAlphabet)))
lbl_avglen2.pack(padx=5, pady=5)



frm_craft1 = tkinter.Frame(master=window)
frm_craft1.grid(row=6, column=0)
lbl_craft1 = tkinter.Label(master=frm_craft1, text='Неравенство Крафта:')
lbl_craft1.pack(padx=5, pady=5)
frm_craft2 = tkinter.Frame(master=window)
frm_craft2.grid(row=6, column=1)
lbl_craft2 = tkinter.Label(master=frm_craft2, text= 'Соблюдается' if craft_num <= 1 else 'Не соблюдается')
lbl_craft2.pack(padx=5, pady=5)

window.mainloop()