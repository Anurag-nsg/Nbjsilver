import flet as ft
import time
from pymongo import MongoClient
import pdf
from datetime import datetime
current_datetime = datetime.now()

clint=MongoClient('mongodb+srv://Bable:silver_test123@test.ohcmfil.mongodb.net/?retryWrites=true&w=majority&appName=test')
db=clint['db1']
collection=db['silver_test']




def main(page:ft.Page):
    page.window_min_width=71
    page.window_min_height=146

    
    def route1(e):
        global calc_price
        calc_price=0
        global rate
        rate=0
        
        ##### sale report #####
        
        global weight_f
        global netweight_f
        global making_charge_f
        global total_f
        global old_weight_f
        global old_percentage_f
        global old_price_f
        global sale_price_f
        
        
        with open("price.txt","r") as pu:
            p=pu.read()
            rate=int(p)
        
        
        def calc(weight,price,old_weight,old_percentage):
            price=price//10
            net_weight=weight+((weight*5)/100)
            making_charge=net_weight*5
            total=(net_weight*price)+making_charge
            if(old_weight!=0 and old_percentage!=0):
                old_weight_n=(old_weight*old_percentage)/100
                old_price=price-((price*5)//100)
                old_price=old_weight_n*old_price
                total1=old_price
                total=int(total)
                total1=int(total1)
                return [total,total1]
            
            return int(total)
        
        #App bar
        page.appbar=ft.AppBar(
            center_title=True,
            toolbar_height=60,
            title=ft.Text("NBJ",color="red"),  
        )
        
        #home
        
        def c2(e):
            try:
                int(push_price.value)
                push_price.error_style=None
                push_price.error_text=""
                commit.content=ft.Container(ft.Column(
                        controls=[
                                push_price,
                                ft.Container(
                                    ft.Row(
                                        controls=[
                                            ft.ElevatedButton("Reset",on_click=reset,width=100,height=40),
                                            ft.Container(width=80),
                                            ft.ElevatedButton("SALE",bgcolor="#4CAF50",color="#FFFFFF",on_click=sell,width=100,height=40),
                                        ],
                                    ),alignment=ft.alignment.center
                    )
                        ],alignment=ft.CrossAxisAlignment.CENTER
                    ),alignment=ft.alignment.center)
                
                page.update()
            except:
                push_price.error_text="Please Enter Correct Amount"
                page.update()
        
        def change(e):
            commit.content=ft.Container(ft.Column(
                    controls=[
                            push_price,
                            ft.Container(
                                ft.Row(
                                    controls=[
                                        ft.ElevatedButton("Reset",on_click=reset,width=100,height=40),
                                        ft.Container(width=70),
                                        ft.ElevatedButton("Confirm",on_click=c2,width=110,height=40),
                                    ],
                                ),alignment=ft.alignment.center
                )
                    ],alignment=ft.CrossAxisAlignment.CENTER
                ),alignment=ft.alignment.center)
            page.update()
        
        
        def cal(e):
                
                global calc_price
                global rate
                global weight_f
                global netweight_f
                global making_charge_f
                global total_f
                global old_weight_f
                global old_percentage_f
                global old_price_f
                try:
                    if(float(anklet_wight.value)>0):
                        anklet_wight.error_text=""
                        anklet_wight.error_style=None
                        if(old_anklet.value==""):
                            calc_price=round(calc(float(anklet_wight.value),rate,0,0))
                        else:
                            
                            pr=calc(float(anklet_wight.value),rate,float(old_anklet.value),float(old_anklet_percentage.value))
                            calc_price=pr[0]
                            old_price=pr[1]
                    else:
                        
                        anklet_wight.error_text="Enter correct weight"
                        page.update()
                        return
                except:
                    anklet_wight.error_text="Enter correct weight"
                    page.update()
                    return
                if(old_anklet.value==""):
                    
                    old_anklet.height=0
                    old_anklet.width=0
                    old_anklet.opacity=0
                    old_anklet_percentage.height=0
                    old_anklet_percentage.width=0
                    old_anklet_percentage.opacity=0
                    told.height=0
                    total_anklet_price.height=520
                    page.update()
                    commit.content=ft.ElevatedButton("Commit",on_click=change,height=40)
                    
                    
                    
                    weight_f=int(anklet_wight.value)
                    netweight_f=round((float(anklet_wight.value)+float(anklet_wight.value)*5/100),2)
                    making_charge_f=round(float(anklet_wight.value)+(float(anklet_wight.value)*5/100))*5
                    total_f=calc_price
                    old_weight_f=0
                    old_percentage_f=0
                    old_price_f=0
                    
                    total_anklet_price.content=ft.Container(
                            ft.Column(controls=[
                                ft.Divider(thickness=2),
                                ft.Row(
                                    controls=[
                                        ft.Text("10 gram / Silver Price : ",color="blue",weight=ft.FontWeight.W_600,size=15),
                                        ft.Text(rate,color="blue",weight=ft.FontWeight.W_600,size=15),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                ft.Divider(thickness=2),
                                ft.Row(
                                    controls=[
                                        ft.Text("Item weight : "),
                                        ft.Text(anklet_wight.value),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN   
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text("Wastage : "),
                                        ft.Text(float(anklet_wight.value)*5/100),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text("Net Weight : "),
                                        ft.Text("%.2f" %(float(anklet_wight.value)+float(anklet_wight.value)*5/100)),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                    
                                ),
                                ft.Divider(thickness=2),
                                ft.Row(
                                    controls=[
                                        ft.Text("Price : "),
                                        ft.Text(int((float(anklet_wight.value)+(float(anklet_wight.value)*5/100))* int(rate//10))),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN 
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text("Making Charge : "),
                                        ft.Text(f"+ {round(float(anklet_wight.value)+(float(anklet_wight.value)*5/100))*5}"),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                                ft.Divider(thickness=2),
                                ft.Container(
                                    ft.Row(
                                        controls=[
                                            ft.Text("Total  :",color="#FFFFFF",weight=ft.FontWeight.W_600,size=15),
                                            ft.Text(f"{calc_price}  ",color="#FFFFFF",weight=ft.FontWeight.W_600,size=15),
                                        ],
                                        alignment=ft.MainAxisAlignment.END
                                    ),
                                    bgcolor="#4CAF50",
                                    height=35
                                ),
                                ft.Divider(thickness=2),
                                ft.Row(
                                    controls=[
                                        ft.Column(
                                            controls=[
                                                commit
                                            ]
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                                )
                            ],alignment=ft.CrossAxisAlignment.CENTER,expand=True
                                    
                                    
                            ),
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(left=20,right=20),
                            
                        )
                    
                    page.update()
                    
                else:
                    

                    weight_f=int(anklet_wight.value)
                    netweight_f=round((float(anklet_wight.value)+float(anklet_wight.value)*5/100),2)
                    making_charge_f=round(float(anklet_wight.value)+(float(anklet_wight.value)*5/100))*5
                    total_f=calc_price-old_price
                    old_weight_f=int(old_anklet.value)
                    old_percentage_f=int(old_anklet_percentage.value)
                    old_price_f=old_price
                    
                    commit.content=ft.ElevatedButton("Commit",on_click=change,height=40)
                    total_anklet_price.height=770
                    total_anklet_price.content=ft.Container(
                            ft.Column(controls=[
                                ft.Divider(thickness=2),
                                ft.Row(
                                    controls=[
                                        ft.Text("10 gram / Silver Price : ",color="blue",weight=ft.FontWeight.W_600,size=15),
                                        ft.Text(rate,color="blue",weight=ft.FontWeight.W_600,size=15),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                ),
                                ft.Divider(thickness=2),
                                ft.Row(
                                    controls=[
                                        ft.Text("Item weight : "),
                                        ft.Text(anklet_wight.value),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN   
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text("Wastage : "),
                                        ft.Text(float(anklet_wight.value)*5/100),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text("Net Weight : "),
                                        ft.Text("%.2f" %(float(anklet_wight.value)+float(anklet_wight.value)*5/100)),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                    
                                ),
                                ft.Divider(thickness=2),
                                ft.Row(
                                    controls=[
                                        ft.Text("Price : "),
                                        ft.Text(int((float(anklet_wight.value)+(float(anklet_wight.value)*5/100))* int(rate//10))),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN 
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text("Making Charge : "),
                                        ft.Text(f"+ {round(float(anklet_wight.value)+(float(anklet_wight.value)*5/100))*5}"),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                                ft.Divider(thickness=2),
                                ft.Row(
                                    controls=[
                                        ft.Text("Total  :",color="#F0F0F0",weight=ft.FontWeight.W_600,size=15),
                                        ft.Text(calc_price,color="#F0F0F0",weight=ft.FontWeight.W_600,size=15),
                                    ],
                                    alignment=ft.MainAxisAlignment.END
                                ),
                                ft.Divider(thickness=2),
                                ft.Row(
                                    controls=[
                                        ft.Text("Old item weight : "),
                                        ft.Text("%.2f" % float(old_anklet.value)),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text("Old Silver Price : "),
                                        ft.Text((rate-(rate*5//100))//10),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(f"{old_anklet_percentage.value}% Silver wight : "),
                                        ft.Text("%.2f" % ((float(old_anklet.value)*float(old_anklet_percentage.value))/100)),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(f"Old Item Price : "),
                                        ft.Text(f"{old_price}"),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                                ft.Divider(thickness=2),
                                ft.Row(
                                    controls=[
                                        ft.Text("Total Amount  :",color="red",weight=ft.FontWeight.W_600,size=15),
                                        ft.Text(calc_price,color="red",weight=ft.FontWeight.W_600,size=15),
                                    ],
                                    alignment=ft.MainAxisAlignment.END
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text("Old Anklet Amount  :",color="red",weight=ft.FontWeight.W_600,size=15),
                                        ft.Text(f"-{old_price}"   ,color="red",weight=ft.FontWeight.W_600,size=15),
                                    ],
                                    alignment=ft.MainAxisAlignment.END
                                ),

                                
                                ft.Divider(thickness=2),
                                ft.Container(
                                    ft.Row(
                                        controls=[
                                            ft.Text("Final Amount  :",color="#FFFFFF",weight=ft.FontWeight.W_600,size=15),
                                            ft.Text(f"{calc_price-old_price}  ",color="#FFFFFF",weight=ft.FontWeight.W_600,size=15),
                                            
                                        ],
                                        alignment=ft.MainAxisAlignment.END
                                    ),
                                    bgcolor="#4CAF50",
                                    height=35
                                ),
                                ft.Divider(thickness=2),
                                ft.Row(
                                    controls=[
                                        ft.Column(
                                            controls=[
                                                commit
                                            ]
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                                )
                            ],alignment=ft.CrossAxisAlignment.CENTER
                                    
                                    
                            ),
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(left=20,right=20),
                            
                        )
                    page.update()
                anklet_wight.value=""
                old_anklet.value=""
                old_anklet_percentage.value=""
                page.update()
                    
        def old_calc(e):
            old_anklet.height= 70 if old_anklet.height==0 else 0
            old_anklet.width= 170 if old_anklet.width==0 else 0
            old_anklet.opacity=100 if old_anklet.opacity==0 else 0
            old_anklet_percentage.height= 70 if old_anklet_percentage.height==0 else 0
            old_anklet_percentage.width= 170 if old_anklet_percentage.width==0 else 0
            old_anklet_percentage.opacity=100 if old_anklet_percentage.opacity==0 else 0
            told.height= 50 if told.height==0 else 0
            old_anklet.value="" if old_anklet.height==0 else old_anklet.value
            old_anklet_percentage.value="" if old_anklet_percentage.height==0 else old_anklet_percentage.value
            page.update()
            
        def foc(e):
            old_anklet_percentage.focus()
            page.update()
            
        def reset(e):
            anklet_wight.error_style=None
            anklet_wight.error_text=""
            commit.content=ft.ElevatedButton("Commit",on_click=change,height=40)
            old_anklet.value=""
            old_anklet_percentage.value=""
            anklet_wight.value=""
            push_price.error_style=None
            push_price.error_text=""
            old_anklet.height= 0
            old_anklet.width= 0
            old_anklet.opacity= 0
            old_anklet_percentage.height= 0 
            old_anklet_percentage.width= 0 
            old_anklet_percentage.opacity=0
            told.height= 0
            old_anklet.value="" 
            old_anklet_percentage.value="" 
            push_price.value=""
            total_anklet_price.height=0
            page.update()
            
        push_price=ft.TextField(label="Enter Selling price",keyboard_type=ft.KeyboardType.NUMBER,on_submit=c2)
        commit=ft.Container(ft.ElevatedButton("Commit",on_click=change,height=40),alignment=ft.alignment.center)
        
        anklet_wight=ft.TextField(label="Enter Anklet wight",on_submit=cal,keyboard_type=ft.KeyboardType.PHONE)
        old_anklet=ft.TextField(label="Enter Old Anklet wight",height=0,width=0,opacity=0,on_submit=foc,keyboard_type=ft.KeyboardType.NUMBER)
        old_anklet_percentage=ft.TextField(label="Enter Old Anklet %",height=0,width=0,opacity=0,on_submit=cal,keyboard_type=ft.KeyboardType.NUMBER)
        told=ft.Container(ft.Row(controls=[old_anklet,old_anklet_percentage],alignment=ft.MainAxisAlignment.SPACE_AROUND),alignment=ft.alignment.center,height=0)
        total_anklet_price=ft.Container(height=0)
        
        
        pop_up_1=ft.Container(height=0,alignment=ft.alignment.center,opacity=0,animate=ft.animation.Animation(1000, "bounceOut"),bgcolor="green")
        
        Home=ft.Container(ft.Column(
            controls=[
                pop_up_1,
                ft.Container(height=10),
                anklet_wight,
                ft.Container(height=5),
                told,
                ft.Container(
                    ft.Row(
                                controls=[
                                    ft.ElevatedButton("Old Anklet",on_click=old_calc),
                                    ft.ElevatedButton("Calculate",on_click=cal),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY
                            ),alignment=ft.alignment.center
                ),
                total_anklet_price,
                
            ],alignment=ft.CrossAxisAlignment.CENTER,scroll=ft.ScrollMode.AUTO
        ),alignment=ft.alignment.center)
        
        
        def sell(e):
            global rate
            global calc_price
            global weight_f
            global netweight_f
            global making_charge_f
            global total_f
            global old_weight_f
            global old_percentage_f
            global old_price_f
            silver_price_f=round(rate/10)
            sale_price_f=int(push_price.value)
            if(sale_price_f<=total_f-(total_f*5/100)):
                profit_loss="Loss"
            else:
                profit_loss="Profit" 
                
            current_date = current_datetime.day
            current_month = current_datetime.month
            current_year = current_datetime.year    
            
            current_hour = current_datetime.hour
            current_minute = current_datetime.minute
            mongo_push={"time":(f"{current_hour}:{current_minute}"),"day":current_date,"month":current_month,"year":current_year,"silver\nprice":silver_price_f,"item\nweight": weight_f,"item\nnetweight" :netweight_f,"making\ncharge":making_charge_f,"old\nweight":old_weight_f,"old\npercentage":old_percentage_f,"old\nprice":old_price_f,"Total":total_f,"sale_price":sale_price_f,"profit\nloss":profit_loss}
            
            collection.insert_one(mongo_push)
            mongo_push={}
            reset(e)
            push_price.value=""
            pop_up_1.bgcolor="green"
            page.update()
            if(profit_loss=="Loss"):
                pop_up_1.content=ft.Text(f" {weight_f} Grams of Anklet Sold At Loss",text_align="center",color="white")
                pop_up_1.bgcolor="red"
            
            if(profit_loss=="Profit"):
                pop_up_1.content=ft.Text(f" {weight_f} Grams of Anklet Sold ",text_align="center",color="white")
                pop_up_1.bgcolor="green"
            pop_up_1.height=50
            pop_up_1.opacity=100
            page.update()
            time.sleep(10)
            pop_up_1.height=0
            page.update()
            time.sleep(1)
            pop_up_1.opacity=0
            page.update()
        
        page.scroll=True
        
        #Price Update
        def price_updated(e):
            with open("price.txt","w") as pu:
                pu.write(udate_price.value)
                global rate
                rate=int(udate_price.value)
                page.update()
                
            udate_price.value=""
            password.value=""
            update_price.disabled=True
            page.update()
            pop_up_2.content=ft.Text(f"Price Updated Successfully as {rate}",text_align="center")
            pop_up_2.height=50
            pop_up_2.opacity=100
            page.update()
            time.sleep(10)
            pop_up_2.height=0
            page.update()
            time.sleep(1)
            pop_up_2.opacity=0
            page.update()
            
        def check_password(e):
            if(password.value=="Santhosh.nbjsilver#1985"):
                update_price.disabled=False
                
            else:
                update_price.disabled=True
            page.update()
        pop_up_2=ft.Container(height=0,alignment=ft.alignment.center,opacity=0,animate=ft.animation.Animation(1000, "bounceOut"),bgcolor="green")
        udate_price=ft.TextField(label="Enter the Silver Price to be Updated",keyboard_type=ft.KeyboardType.NUMBER,on_submit=price_updated)
        password=ft.TextField(label="Enter password to update",password=True,can_reveal_password=True,on_change=check_password)
        update_price=ft.Container(ft.ElevatedButton("Update",on_click=price_updated,opacity=100),opacity=100,disabled=True,alignment=ft.alignment.center)
        Price_Update=ft.Container(
            ft.Column(controls=[
                pop_up_2,
                ft.Container(height=10),
                udate_price,
                password,
                update_price
            ])
        )
        
        
        # Sale_report
       
        
        global mon
        mon='00'
        def change_date(e):
            global mon
            date=date_picker.value
            date=str(date).split('-')
            date=date[1]
            date = [int(part) if part.isdigit() else part for part in date]
            if(date[0]==0):
                date=date[1]
            else:
                date = ''.join(map(str, date))
            mon=date

            

        import datetime
        day=datetime.datetime.now()
        day=str(day).split(" ")
        day=day[0].split('-')
        day = [int(part) if part.isdigit() else part for part in day]
                    
        date_picker = ft.DatePicker(
            first_date=datetime.datetime(2024, 3 ,13),
            last_date=datetime.datetime(day[0],day[1],day[2]),
            
            on_change=change_date,
            
        )

        page.overlay.append(date_picker)
        

        date_button = ft.IconButton(
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: date_picker.pick_date(),
        )
        
        
        def pop_3(k):
            if(k==1):
                pop_up_3.content=ft.Text("Please Enter a valid Date",color="white")
                pop_up_3.bgcolor="red"
                page.update()
            if(k==2):
                pop_up_3.content=ft.Text("Report Sent to Mail Successfully",color="white")
                pop_up_3.bgcolor="green"
                page.update()
            if(k==0):
                pop_up_3.content=ft.Text("Please wait",color="#333333")
                pop_up_3.bgcolor="#ADD8E6"
                pop_up_3.height=50
                pop_up_3.opacity=100
                page.update()
                return
            pop_up_3.height=50
            pop_up_3.opacity=100
            page.update()
            time.sleep(10)
            pop_up_3.height=0
            page.update()
            time.sleep(1)
            pop_up_3.opacity=0
            page.update()
            
        
        def send_month(e):
            global mon
            if(mon!=0):
                
                try:
                    dat_data=collection.find({'month':mon})
                    lis=[]
                    for i in dat_data:
                        i.pop('_id')
                        lis.append(i)
                    pop_3(0)
                    pdf.pdf(lis,'Month')
                    pop_3(2)
                    page.update()
                    mon='00'
                except:
                    pop_3(1)
                    page.update()
            else:
                pop_3(1)
                page.update()
        
        def send_day(e):
            current_date = current_datetime.day
            dat_data=collection.find({'day':current_date})
            lis=[]
            for i in dat_data:
                i.pop('_id')
                lis.append(i)
            pop_3(0)
            pdf.pdf(lis,'Day')
            pop_3(2)
            

        pop_up_3=ft.Container(height=0,alignment=ft.alignment.center,opacity=0,animate=ft.animation.Animation(1000, "bounceOut"),bgcolor="green")
        Sale_report=ft.Container(
            ft.Column(controls=[
                pop_up_3,
                ft.Container(height=10),
                ft.Container(
                    ft.Row(controls=[ft.Text(" Today Report "),ft.Row(controls=[ft.Container(width=43,height=3),ft.ElevatedButton("Send",on_click=send_day)])],alignment=ft.MainAxisAlignment.SPACE_AROUND),alignment=ft.alignment.center
                ),
                ft.Container(height=10),
                ft.Container(
                    ft.Row(controls=[ft.Text(" Month Report "),ft.Row(controls=[date_button,ft.ElevatedButton("Send",on_click=send_month)])],alignment=ft.MainAxisAlignment.SPACE_AROUND),alignment=ft.alignment.center
                )
                
            ])
            
        )
        
        
        
        # side bar
        def change_nav(e):
            if e.control.selected_index==0:
                page.clean()
                page.add(
                    Home
                )
                page.close_drawer()
                page.update()
            elif e.control.selected_index==1:
                page.clean()
                page.add(
                    Price_Update
                )
                page.close_drawer()
                page.update()

            elif e.control.selected_index==2:
                page.clean()
                page.add(
                    Sale_report
                )
                page.close_drawer()
                page.update()
            elif e.control.selected_index==3:
                page.clean()
                page.clean()
                route2('e')
            page.update()
            
            
        page.drawer = ft.NavigationDrawer(
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    label="Home",
                    icon=ft.icons.HOME_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.HOME_ROUNDED),
                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.MONETIZATION_ON_OUTLINED),
                    label="Silver Price",
                    selected_icon=ft.icons.MONETIZATION_ON_ROUNDED,
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.POINT_OF_SALE_ROUNDED),
                    label="Sale Report",
                    selected_icon=ft.icons.POINT_OF_SALE_OUTLINED,
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.LOGOUT_OUTLINED),
                    label="Log out",
                    selected_icon=ft.icons.LOGOUT,
                ),
            ],
            on_change= lambda e: change_nav(e),  
            
            
        )
        page.add(
            Home
        )
        page.update()

    
    def route2(e):
        page.drawer=False
        page.appbar=False
        def page_change(e):
            page.clean()
            route1('e')
            username.value=""
            password.value=""
            page.update()
        
        
        def check_password2(e):
            username.update()
            password.update()
            if(username.value=="Santhosh.nbj" and password.value=="Santhosh@nbj#1985"):
                log.disabled=False
                log.bgcolor="green"
                log.color="white"
                page.update()
                
            else:
                log.disabled=True
                log.bgcolor="gray"
            page.update()
            
        
        def foc2(e):
            password.focus()
            page.update()
        
        username=ft.TextField(label="Enter Username",on_change=check_password2,on_submit=foc2)
        password=ft.TextField(label="Enter Password",password=True,can_reveal_password=True,on_change=check_password2,on_submit=page_change)
        log=ft.ElevatedButton("Login",on_click=page_change,width=400,height=50,expand=True,bgcolor="gray",style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),disabled=True,)
        login=ft.Container(
            ft.Container(ft.Column(controls=[
                ft.Container(ft.Text("NBJ Login",text_align="center",color="red",weight=ft.FontWeight.W_500,size=25),alignment=ft.alignment.center),
                ft.Container(height=100),
                username,
                ft.Container(height=3),
                password,
                ft.Container(height=5),
                ft.Container(log,width=400,height=50,border_radius=10),
                ft.Container(height=100)
                
            ],alignment=ft.MainAxisAlignment.CENTER,
                
                #bgcolor="#cc2d2b2c",
                ),width=400,opacity=80,expand=True,padding=30,alignment=ft.alignment.center),alignment=ft.alignment.center,padding=ft.padding.only(top=150,bottom=60,left=30,right=30)
        )
        page.update()
        page.add(login)
        page.update()
        
    
    route2('e')
    
ft.app(target=main,view=ft.WEB_BROWSER)