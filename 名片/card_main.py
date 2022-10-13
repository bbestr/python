import card_tools
while True:
    card_tools.show_menu()
    action = int(input("请输入想要的操作:"))
    if action in [1,2,3]:
        if action == 1:
            card_tools.new_card()
        elif action == 2:
            card_tools.all_card()
        else:
            card_tools.card_select()

    elif action == 0:
        print("你已退出")
        break
    else:
        print("输入错误!,重新输入")