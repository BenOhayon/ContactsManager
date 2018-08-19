import model.contactsDB as DB

try:
    import tkinter as tk
except ImportError:  # if running with python 2.x
    import Tkinter as tk


def filter_list():
    if mode_var.get() == 1:
        contacts_list = DB.get_all_contacts()
    elif mode_var.get() == 2:
        contacts_list = DB.query_by_name(filter_query.get())
    else:
        contacts_list = DB.query_by_email(filter_query.get())

    for row in contacts_list:
        shown_list.insert(tk.END, row)


def add_contact():
    pass


def clear_fields():
    name_val.set("")
    phone_val.set(0)
    email_val.set("")
    # name_textfield.delete(0, 'end')
    # phone_textfield.delete(0, 'end')
    # email_textfield.delete(0, 'end')


def select_callback():
    list_selection = shown_list.get(shown_list.curselection())
    name, phone, email = list_selection
    name_val.set(name)
    phone_val.set(phone)
    email_val.set(email)


if __name__ == "__main__":
    main_window = tk.Tk()
    main_window.title("Contacts Manager")
    main_window.geometry("540x380")
    main_window['padx'] = 12

    tk.Label(main_window, text="Contacts List").grid(row=0, column=0)

    # Configuring the list frame to contain the contacts list
    list_frame = tk.Frame(main_window)
    list_frame.grid(row=1, column=0)
    list_frame.columnconfigure(0, weight=1)

    # Configuring the list to be populated with contacts
    shown_list = tk.Listbox(list_frame, relief="sunken", borderwidth=2)
    shown_list.grid(row=0, column=0, rowspan=7)
    shown_list.config(width=40)
    shown_list.bind('<<ListboxSelect>>', select_callback)

    # Configuring the scrollbar for the list
    list_scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL, command=shown_list.yview)
    list_scrollbar.grid(row=0, column=1, sticky='nsw', rowspan=7)
    shown_list['yscrollcommand'] = list_scrollbar.set

    # Configuring a frame to hold the frames that hold the labels and textfield for name, phone and email
    fields_frame = tk.Frame(main_window)
    fields_frame.grid(row=1, column=2, sticky='nsw')
    fields_frame['padx'] = 25
    fields_frame.rowconfigure(0, weight=1)
    fields_frame.rowconfigure(1, weight=1)
    fields_frame.rowconfigure(2, weight=1)

    # Initializing the value for the variables to bind to the text fields.
    name_val = tk.StringVar()
    phone_val = tk.IntVar()
    email_val = tk.StringVar()

    # Configuring a frame to hold the frames that hold the labels and textfield for name, phone and email
    # Name frame
    name_frame = tk.Frame(fields_frame)
    name_frame.grid(row=0, column=0, sticky='nsw')
    tk.Label(name_frame, text="Name:").grid(row=0, column=0, sticky='sw')
    name_textfield = tk.Entry(name_frame, textvariable=name_val)
    name_textfield.grid(row=1, column=0)

    # Phone frame
    phone_frame = tk.Frame(fields_frame)
    phone_frame.grid(row=1, column=0, sticky='nw')
    tk.Label(phone_frame, text="Phone:").grid(row=0, column=0, sticky='sw')
    phone_textfield = tk.Entry(phone_frame, variable=phone_val)
    phone_textfield.grid(row=1, column=0)

    # Email frame
    email_frame = tk.Frame(fields_frame)
    email_frame.grid(row=2, column=0, sticky='ne')
    email_frame.columnconfigure(0, weight=1)
    tk.Label(email_frame, text="Email:").grid(row=0, column=0, sticky='sw')
    email_textfield = tk.Entry(email_frame, textvariable=email_val)
    email_textfield.grid(row=1, column=0)

    # Configuring the buttons frames for both filtering and adding contacts & clearing fields
    add_clear_frame = tk.Frame(main_window)
    add_clear_frame.grid(row=7, column=2)
    add_clear_frame.columnconfigure(0, weight=1)

    filter_frame = tk.Frame(main_window)
    filter_frame.grid(row=7, column=0)

    # Configuring the filter button
    tk.Button(filter_frame, text="Filter", command=filter_list).grid(row=0, column=0)
    filter_mode_frame = tk.LabelFrame(main_window, text="Mode")
    filter_mode_frame.grid(row=7, column=1)
    filter_mode_frame['padx'] = 8

    # Initializing the value for the selected radio button
    mode_var = tk.IntVar()
    mode_var.set(1)

    # Configuring the radio buttons
    all_filter_mode = tk.Radiobutton(filter_mode_frame, text="All", value=1, variable=mode_var)
    name_filter_mode = tk.Radiobutton(filter_mode_frame, text="Name", value=2, variable=mode_var)
    email_filter_mode = tk.Radiobutton(filter_mode_frame, text="Email", value=3, variable=mode_var)
    all_filter_mode.grid(row=0, column=0, sticky='w')
    name_filter_mode.grid(row=1, column=0, sticky='w')
    email_filter_mode.grid(row=2, column=0, sticky='w')

    # Creating the filter query textfield
    filter_query = tk.Entry(filter_frame)
    filter_query.grid(row=1, column=0)

    # Configuring the add and clear buttons
    tk.Button(add_clear_frame, text="Add Contact", command=add_contact).grid(row=0, column=0)
    tk.Button(add_clear_frame, text="Clear Fields", command=clear_fields).grid(row=0, column=1)

    main_window.mainloop()
