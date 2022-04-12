from re import X
import turtle
import pandas

sc=turtle.Screen()
sc.title("US naming game")
img="blank_states_img.gif"
sc.addshape(img)
turtle.shape(img)
x1=0
y1=0
data = pandas.read_csv("50_states.csv")
li=data["state"].to_list()
def get_coor(x,y):
    x1=x
    y1=y
    print(x,y)
n=0    
turtle.onscreenclick(get_coor)
gs=[]
while n<=50:
    usstate=sc.textinput(title=f"{n} /Guess other states",prompt="What is the another state name").title()
    
    if usstate=="Exit":
        miss=[i for i in li if i not in gs]
        newdata=pandas.DataFrame(miss)
        newdata.to_csv("missing states to learn.csv")
        print(miss)
        break

    if usstate in li:
        gs.append(usstate)
        n+=1
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        ele=data[data["state"]==usstate]
        x1=int(ele.x)
        y1=int(ele.y)
        t.goto(x1-1,y1)
        t.write(ele.state.item())
    
turtle.mainloop()