card_list = [{"name": "uzi", "phone": "123456789", "qq": "1234568", "email": "123@qq.com"}]


def show_menu():
    """菜单显示"""
    print("*" * 50)
    print("欢迎使用系统!")
    print("1.新建名片 [1]")
    print("2.显示名片 [2]")
    print("3.查询名片 [3]")
    print("4.退出系统 [0]")
    print("*" * 50)


def new_card():
    """新建card"""
    name = input("请输入姓名:")
    phone = input("请输入电话:")
    qq = input("请输入qq:")
    email = input("请输入邮箱")

    card_dict = {"name": name, "phone": phone, "qq": qq, "email": email}

    card_list.append(card_dict)

    print("新建名片成功!\t\n")


def all_card():
    """显示全部card"""

    if len(card_list) == 0:
        print("不好意思 没有名片!")
    else:
        print("=" * 50)
        print("显示所有名片")
        for mn in ["姓名", "电话", "qq", "邮箱"]:
            print(mn, end="\t\t\t\t")
        print("")
        for io in card_list:
            print("%s\t\t\t\ty%s\t\t\t\t%s\t\t\t\t%s" % (io["name"], io["phone"], io["qq"], io["email"]))
        print("=" * 50)


def card_select():
    """查询card"""
    i1 = input("请输入查询信息(姓名):")
    for i2 in card_list:
        if i2["name"] == i1:
            print("找到了")
            print("=" * 50)
            for mn in ["姓名", "电话", "qq", "邮箱"]:
                print(mn, end="\t\t\t\t")
            print("")
            for io in card_list:
                print("%s\t\t\t\ty%s\t\t\t\t%s\t\t\t\t%s" % (io["name"], io["phone"], io["qq"], io["email"]))
            print("=" * 50)
            deal_card(i2)
            break
    else:
        print("抱歉 没有你想要的信息\n")


def deal_card(tempdict):
    """修改名片"""
    while True:
        action = int(input("输入你想要的进行的操作 修改 [1]; 删除 [2] 返回主页 [3]:"))
        if action in [1, 2, 3]:
            if action == 1:
                tempdict["name"] = input("姓名:")
                tempdict["phone"] = input("电话:")
                tempdict["qq"] = input("qq:")
                tempdict["email"] = input("邮箱:")
                print("修改成功")
                break
            elif action == 2:
                card_list.remove(tempdict)
                print("删除成功")
                break
            else:
                print("你已返回主页面")
                break
        else:
            print("s输入有错重新输入!")
