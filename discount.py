from datetime import date
import holidays
def discount(l,d):
    disc_days = []
    today = date.today()
    my_date = today.strftime("%d/%m/%Y")
    y = int(my_date.split('/')[-1])
    '''
    for a in holidays.India(years = y).items():
        disc_days += [[a[0],a[1]]]
        # a[0] is date of the festival and a[1] specifies the festival name
    '''
    disc_days=[['12/03/2022', 'Makar Sankranti / Pongal']] ###################
    for k in disc_days:
        k[0] = k[0]
        if my_date == k[0]:
            for i in l:
                if  d['Phone_number'] == i[1] :
                    if float(i[-1])>5000.0:
                        f=open('discount.txt','w')
                        
                        if float(i[-1])>15000.0:
                            f.write(i[0]+'\n'+d['Phone_number'] +'\n'+ '5'+ '\n'+k[-1])
                            # customer name, phone number, discount percentage, festival name
                            f.close()
                            break

                        elif float(i[-1])>7000.0:
                            f.write(i[0]+'\n'+d['Phone_number'] +'\n'+ '3'+ '\n'+k[-1])
                            f.close()
                            break
                       
                        f.write(i[0]+'\n'+d['Phone_number'] +'\n'+ '2' + '\n'+k[-1])
                        f.close()
                        print('Created')
            break
d={'Username':'sel@a','Password':'sel123.456','Phone_number':'9720325252'}
l=[['sel','9720325252','15','5206']]
          
discount(l,d)
