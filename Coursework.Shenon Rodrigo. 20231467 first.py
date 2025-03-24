from graphics import*
progress = 0
trailer = 0
retriever = 0
excluded = 0
part2=[]
# the main function
def main():
    global progress, trailer, retriever, excluded
    while True:
        # ask the user for valid pass credits and prompt for possible errors
        while True:
            pass_credits = input('Please enter your credits at pass:')
            try:
                pass_credits = int(pass_credits)
            except(ValueError):
                print('Integer required')
                continue
            if pass_credits not in [20*i for i in range(7)]:
                print('Out of range.')
                continue
            else:
                break
        
        # ask the user for valid defer credits and prompt for possible errors
        while True:
            defer_credits = input('Please enter your credit at defer:')
            try:
                defer_credits = int(defer_credits)
            except:
                print('Integer required')
                continue
            if defer_credits not in [20*i for i in  range(7)]:     #59
                print('Out of range')
                continue
            else:
                break
        
        # ask the user for valid fail credits and prompt for possible errors
        while True:
            fail_credits = input('Please enter your credit at fail:')
            try:
                fail_credits = int(fail_credits)
            except :
                print('Integer required')
                continue
            if fail_credits not in [20*i for i in  range(7)]:
                print('Out of range')
                continue
            else:
                break

        if defer_credits + pass_credits + fail_credits != 120:
            print('Total incorrect')
            break
        # display the Progression Outcome
        if pass_credits == 120:
                print("Progress")
                progress += 1
                part2.append([("Progress"),[pass_credits,defer_credits,fail_credits]])
        elif pass_credits == 100:
                print("Progress(module trailer)")
                trailer += 1
                part2.append([("Progress(Module trailer)"),[pass_credits,defer_credits,fail_credits]])
        elif pass_credits<100 and fail_credits<80:
                print("Module retriever")
                retriever  += 1
                part2.append([("Do not progress-module retriver"),[pass_credits,defer_credits,fail_credits]])
        elif fail_credits>=80:
                print("Exclude")
                excluded  += 1
                part2.append([("Excluded"),[pass_credits,defer_credits,fail_credits]])
        
        break


def display_graph():
    global progress, trailer, retriever, excluded
    outcomes = (progress, trailer, retriever, excluded)    

    largest_value = max(outcomes)

    while largest_value !=0:
    
        p = 200 - (progress/largest_value)*100
        t = 200 - (trailer/largest_value)*100
        r = 200 - (retriever/largest_value)*100
        e = 200 - (excluded/largest_value)*100
#win

        win=GraphWin(title="Histogram", width=400, height=300)
        win.setBackground("honeydew1")    

    #window
        label= Text(Point(x=80, y=24), text="Histogram results")
        label.setStyle("bold")
        label.setFace("helvetica")
        label.draw(win)

        aLine=Line(Point(10,203), Point(360,203))
        aLine.setFill("grey")
        aLine.setWidth(4)
        aLine.draw(win)

        tot_outcomes=sum(outcomes)
        total=Text(Point(200,250),f"{tot_outcomes} outcome(s) in total")
        total.setSize(20)
        total.setTextColor("grey")
        total.draw(win)

        box1=Rectangle(Point(x=24, y=p), Point(x=96, y=200))
        box1.setFill("red")
        box1.draw(win)

        bar_heading1=Text(Point(x=((24+96)/2),y=(p-10)), outcomes[0])
        bar_heading1.draw(win)

        bar_label1=Text(Point(x=((24+96)/2),y=(230)), "Progress")
        bar_label1.draw(win)

        box2=Rectangle(Point(x=106, y=t), Point(x=178, y=200))
        box2.setFill("blue")
        box2.draw(win)

        bar_heading2=Text(Point(x=((106+178)/2),y=(t-10)), outcomes[1])
        bar_heading2.draw(win)

        bar_label2=Text(Point(x=((106+178)/2),y=(230)), "Trailer")
        bar_label2.draw(win)

        box3=Rectangle(Point(x=188, y=r), Point(x=260, y=200))
        box3.setFill("green")
        box3.draw(win)

        bar_heading3=Text(Point(x=((188+260)/2),y=(r-10)), outcomes[2])
        bar_heading3.draw(win)

        bar_label3=Text(Point(x=((188+260)/2),y=(230)), "retreiver")
        bar_label3.draw(win)
        
        box4=Rectangle(Point(x=270, y=e), Point(x=342, y=200))
        box4.setFill("orange")
        box4.draw(win)

        bar_heading4=Text(Point(x=((270+342)/2),y=(e-10)), outcomes[3])
        bar_heading4.draw(win)

        bar_label4=Text(Point(x=((270+342)/2),y=(230)), "excluded")
        bar_label4.draw(win)

        try:
            win.getMouse()
        except(GraphicsError):
            print("")
        win.close()
        break

    print("End of session")

def user_input():
    while True:
        print("Would you like to enter another set?")
        get_input = input('Please enter "y" to continue or "q" to quit: ').lower()

        if get_input == "q":
            break
        elif get_input == "y":
            print("")
            main()
        else:
            print('Invalid Input\n')

    display_graph()


            
def part2_function():
    print(part2)
    print("\nPart 2:")
    for i in part2:
        name=i[0]
        marks=i[1]
        print(f"{name} - {marks[0]}, {marks[1]}, {marks[2]}")


def part3_function():
    with open ("Part_3.txt","w") as file:
        for i in part2:
            name=i[0]
            marks=i[1]
            file.write(f"{name} - {marks[0]}, {marks[1]}, {marks[2]}\n")
    with open("Part_3.txt","r") as file:
        part_3_text = file.read()
        print("\nPart 3")
        print(part_3_text)        

    
# call the main method
if __name__ == '__main__':
    main()
    user_input()
    part2_function()
    part3_function()

