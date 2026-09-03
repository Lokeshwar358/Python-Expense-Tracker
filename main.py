def add_expense():
  ad={"date":input("Enter date:"),
       "category":input("Enter category:"),
        "Description":input("Enter Description:"),
         "Amount":int(input("Enter amount: "))}
  my_exp.append(ad)
  print("Expense added")
def view_expenses():
  for i in my_exp:
     print(f"Date:{i['date']}\nCategory: {i['category']}\nDescription:{i['Description']}\nAmount:{i['Amount']}")
def search_expenses():
  a=input("Enter the expense to search:")
  b=True
  for i in my_exp:
    if i["category"] == a:
      print(f"Date:{i['date']}\nCategory: {i['category']}\nDescription:{i['Description']}\nAmount:{i['Amount']}")
      b=False
  if b:
      print("No Expense Found")
def calculate_total():
  total=0
  for i in my_exp:
    total+=i["Amount"]
  print("Total Expense:",total)
def category_summary():
 summary={}
 for i in my_exp:
  if i["category"] in summary:
    summary[i["category"]]+=i["Amount"]
  else:
      summary[i["category"]]=i["Amount"]
 for i in summary:
  print(i,summary[i])
my_exp=[]
while True:
  i=int(input("Enter the Choice of Expense: "))
  if(i==1):
    add_expense()
  elif (i==2):
    view_expenses()
  elif (i==3):
    search_expenses()
  elif (i==4):
    calculate_total()
  elif (i==5):
    category_summary()
  elif (i==6):
      break
  else:
    print("Enter Valid Choice!")
