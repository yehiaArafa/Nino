from Tkinter import *
import gradientDescent
import Fletcher_Reeves
import Newton
import Uni_variate
import tkMessageBox


#create a tkinter object
root = Tk()
root.resizable(width=False,height=False)
root.minsize(width=800, height=600)
root.maxsize(width=800, height=600)
root.title("Nino")
root.configure(background='white')



#Labels
def MainEngine():
	controlFrame = Frame(root, bg='white')
	controlFrame.pack(fill=X)
	global inpOutFrame
	inpOutFrame = Frame(root, bg='white')
	inpOutFrame.pack(side=BOTTOM, fill=X)

	#WIDGETS CONTROLFRAME
	methodsLabel = Label(controlFrame, bg='white', width='25', text='Methods', justify=LEFT)
	benchmarksLabel = Label(controlFrame, bg='white', width='30', text='Benchmark Functions', justify=LEFT)
	paramsLabel = Label(controlFrame, bg='white', width='30', text='Parameters Input', justify=LEFT)
	methodsLabel.grid(row=0)
	benchmarksLabel.grid(row=0, column=1)
	paramsLabel.grid(row=0, column=2)

	meth = IntVar()
	rb1 = Radiobutton(controlFrame, text="Fletcher_Reeves", variable=meth, value=1, height=3, bg='white').grid(row=1)
	rb2 = Radiobutton(controlFrame, text="Newton", variable=meth, value=2, height=3, bg='white').grid(row=2)
	rb3 = Radiobutton(controlFrame, text="Uni_variant", variable=meth, value=3, height=3, bg='white').grid(row=3)
	rb4 = Radiobutton(controlFrame, text="Gradient_descent", variable=meth, value=4, height=3, bg='white').grid(row=4)

	bench = IntVar()
	rb5 = Radiobutton(controlFrame, text="De Jong", variable=bench, value=1, height=2, bg='white').grid(row=1, column=1)
	rb6 = Radiobutton(controlFrame, text="Rosenbrock", variable=bench, value=2, height=2, bg='white').grid(row=2, column=1)
	rb7 = Radiobutton(controlFrame, text="Rastrigin", variable=bench, value=3, height=2, bg='white').grid(row=3, column=1)
	rb8 = Radiobutton(controlFrame, text="Easom", variable=bench, value=4, height=2, bg='white').grid(row=4, column=1)	
	rb9 = Radiobutton(controlFrame, text="Branin", variable=bench, value=5, height=2, bg='white').grid(row=5, column=1)	

	startPnt = Label(controlFrame, text="Start Point", height=2, bg='white').grid(row=1,column=2)
	startX = Entry(controlFrame, width=10)
	startX.insert(0,'X')
	startX.grid(row=2,column=2)
	startY = Entry(controlFrame, width=10)
	startY.insert(0,'Y')
	startY.grid(row=2,column=3)
	global startptx
	global startpty
	startptx = startX.get()
	startpty = startY.get()
	#WIDGETS INPOUTFRAME
	inputLabel = Label(inpOutFrame, bg='white', height=2, text="Input Function")
	functionIP = StringVar()
	inputEntry = Entry(inpOutFrame, width=50)
	inputButton = Button(inpOutFrame, text="Execute", command=lambda: callMethod(meth), width=5)
	plotButton = Button(inpOutFrame, text="Plot", width=5)
	inputLabel.grid(row=0)
	inputEntry.grid(row=0, column=1)
	inputButton.grid(row=0, column=2)
	plotButton.grid(row=0, column=3)
	outputLabel = Label(inpOutFrame, bg='white', text='Output', height=20)
	outputLabel.grid(row=1)

	#Continously render screen
	root.mainloop()

def main():
	MainEngine()

def callMethod(methodNum):
	if methodNum.get()==1:
		Fletcher_Reeves.main()
	elif methodNum.get()==2:
		Newton.main()
	elif methodNum.get()==3:
		Uni_variate.main()
	elif methodNum.get()==4:
		res = gradientDescent.main()
		restxt = ""
		for i in range(len(res)):
			restxt += str(res[i])
			restxt += '\n'
		result = Label(inpOutFrame, text=restxt, bg='white', height=20)
		result.grid(row=1, column=1)

#MAIN CALLER
if __name__=="__main__":
	main()