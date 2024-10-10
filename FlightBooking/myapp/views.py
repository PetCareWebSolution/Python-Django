from django.shortcuts import render

# Create your views here.


def indexp(request):
    return render(request,"index.html")

def fetchdata(request):

    name = request.POST.get('fname')
    lname = request.POST.get('last name')
    email = request.POST.get('g email')
    pn = request.POST.get('phone number')

    triptype = request.POST.get('tripType')

    tcd = request.POST.get('tclass')

    con = request.POST.get('tcountry')

    dc = request.POST.get('dcountry')

    dt = request.POST.get('datepick')

    timedept = request.POST.get('tdep')

    rt = request.POST.get('retrundate')

    rettime = request.POST.get('returntime')

    airport = request.POST.get('airselect')

    nuoflaug = request.POST.get('nol')

    airline = request.POST.get('al')

    flightnumber = request.POST.get('fn')

    numfora = request.POST.get('noa')

    numforc = request.POST.get('noc')

    hotelbrand = request.POST.get('phb')

    pu = request.POST.get('pickup')

    passpnumber = request.POST.get('passnum')

    expd = request.POST.get('datepickpass')

    message = request.POST.get('msg')


    print(f"This is Your name=>{name}\nThis is my lname=>{lname}\nThis is email=>{email}\nThis is Phone Number=>{pn}\nTrip Type=>{triptype}\n"
          f"This is your class=>{tcd}\nThis is your country=>{con}\nThis is your destination country=>{dc}\nThis is your Department Date=>{dt}\n"
          f"This is your Time you selected=>{timedept}\nThis is Your return date={rt}\nThis is your return time=>{rettime}\n"
          f"Airport=>{airport}\nNumber of Luggage=>{nuoflaug}\nAirline=>{airline}\nFlight Number=>{flightnumber}\n"
          f"Number of Adults=>{numfora}\nNumber of Children=>{numforc}\nPrefferd Hotel Brand=>{hotelbrand}\nHow you will be pickup=>{pu}\n"
          f"Passport Number=>{passpnumber}\nExpiry Date=>{expd}\nMessage=>{message}\n")

    return render(request,"index.html")

'''
def fetchformdata(request):
    name = request.POST.get('uname')
    email = request.POST.get('uemail')
    phone = request.POST.get('uphone')
    msg = request.POST.get('usmg')

    print(f"=>this is your name {name} \n=>This is my email {email} \n=>This is my Phone Number:{phone} \n=>This is my messasge:{msg}")

    return render(request,"form.html")
'''