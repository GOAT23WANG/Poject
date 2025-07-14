# text.py
# 一个简易的命令行记事本程序

def show_menu():
    print("\n简易记事本")
    print("1. 新建笔记")
    print("2. 查看所有笔记")
    print("3. 退出")

def add_note(notes):
    note = input("请输入你的笔记内容：")
    notes.append(note)
    print("笔记已保存。")

def view_notes(notes):
    if not notes:
        print("暂无笔记。")
    else:
        print("\n所有笔记：")
        for idx, note in enumerate(notes, 1):
            print(f"{idx}. {note}")

def main():
    notes = []
    while True:
        show_menu()
        choice = input("请选择操作（1/2/3）：")
        if choice == '1':
            add_note(notes)
        elif choice == '2':
            view_notes(notes)
        elif choice == '3':
            print("感谢使用，再见！")
            break
        else:
            print("无效选择，请重新输入。")

if __name__ == "__main__":
    main()