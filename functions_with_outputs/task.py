# def format_name(f_name, l_name):
#     # print(f_name.title())
#     # print(l_name.title())

#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()

#     # print(f"{formatted_f_name} {formatted_l_name}")
#     return f"{formatted_f_name} {formatted_l_name}"

# formatted_string = format_name("suraj","prakash")

# print(formatted_string)

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide any value."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
