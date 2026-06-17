import tkinter as tk
students = []

root = tk.Tk()
root.title("Student Management System")
root.geometry("400x450")



def update_list():
    listbox.delete(0, tk.END)
    for s in students:
        listbox.insert(tk.END, f"{s['id']} - {s['name']}")

def clear_entries():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)

def add_student():
    name = name_entry.get()
    sid = id_entry.get()
    
    if name and sid:
        students.append({"id": sid, "name": name})
        clear_entries()
        update_list()

def delete_student():
    selected = listbox.curselection()
    if selected:
        students.pop(selected[0])
        update_list()

def load_selected():
    selected = listbox.curselection()
    if selected:
        s = students[selected[0]]
        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        id_entry.insert(0, s["id"])
        name_entry.insert(0, s["name"])

def update_student():
    selected = listbox.curselection()
    
    if not selected:
        print("No student selected")
        return
    
    index = selected[0]
    
    students[index] = {
        "id": id_entry.get(),
        "name": name_entry.get()
    }
    
    clear_entries()
    update_list()

def search_student():
    sid = id_entry.get()
    listbox.delete(0, tk.END)
    
    for s in students:
        if s["id"] == sid:
            listbox.insert(tk.END, f"{s['id']} - {s['name']}")
            return
    
    listbox.insert(tk.END, "Student not found")



tk.Label(root, text="Student ID").pack()
id_entry = tk.Entry(root)
id_entry.pack()

tk.Label(root, text="Student Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Button(root, text="Add", command=add_student).pack(pady=3)
tk.Button(root, text="Search by ID", command=search_student).pack(pady=3)
tk.Button(root, text="Load Selected", command=load_selected).pack(pady=3)
tk.Button(root, text="Update", command=update_student).pack(pady=3)
tk.Button(root, text="Delete", command=delete_student).pack(pady=3)
tk.Button(root, text="View All", command=update_list).pack(pady=3)

listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)

root.mainloop()