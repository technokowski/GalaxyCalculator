from flask import Flask,render_template,request


"""
Code created for Google Colab by:
Aerospace911#9828 with the help of TopThreePlayz#9422 and Fashoomp#9015

Code refactoring and flask implementation by: technokowski

"""

app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    b = 0
    lis1 = []
    lis2 = []
    trade = []
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        sil_b = float(request.form.get('sil_b'))
        car_b = float(request.form.get('car_b'))
        ird_b = float(request.form.get('ird_b'))
        ada_b = float(request.form.get('ada_b'))
        pal_b = float(request.form.get('pal_b'))
        tit_b = float(request.form.get('tit_b'))
        qua_b = float(request.form.get('qua_b'))
        ura_b = float(request.form.get('ura_b'))

        sil_m = float(request.form.get('sil_m'))
        car_m = float(request.form.get('car_m'))
        ird_m = float(request.form.get('ird_m'))
        ada_m = float(request.form.get('ada_m'))
        pal_m = float(request.form.get('pal_m'))
        tit_m = float(request.form.get('tit_m'))
        qua_m = float(request.form.get('qua_m'))
        ura_m = float(request.form.get('ura_m'))

        def convert_mega(r):
            return(round(r - (r * 0.075), 1))

        def profit_check(name,rs1,rs2):
            pr = round(rs1 - rs2, 1)
            if pr > 0.00:
                if pr > 1.00:
                    trade.append(name + ' ' + str(pr) + ' (PROFITABLE +1)-----')
                    lis1.extend([pr,name])
                else:
                    trade.append(name + ' ' +str(pr) + ' (PROFITABLE +0)-----')
                    lis1.extend([pr,name])
            else:
                trade.append(name + ' ' + str(pr) + ' Not Profitable')
                lis2.extend([pr,name])

        ##Convert mega buy to sell
        ##Silicate
        sil_ms = convert_mega(sil_m)
        ##Carbon
        car_ms = convert_mega(car_m)
        ##Iridium
        ird_ms = convert_mega(ird_m)
        ##Adamantite
        ada_ms = convert_mega(ada_m)
        ##Palladium
        pal_ms = convert_mega(pal_m)
        ##Titanium
        tit_ms = convert_mega(tit_m)
        #Quantium
        qua_ms = convert_mega(qua_m)
        ##Uranium
        ura_ms = convert_mega(ura_m)

        ##Profit Check
        profit_checks = [
            ('Silicate',sil_ms, sil_b),('Carbon',car_ms, car_b),
            ('Iridium',ird_ms, ird_b),('Adamantite',ada_ms, ada_b),
            ('Palladium',pal_ms, pal_b),('Titanium',tit_ms, tit_b),
            ('Quantium',qua_ms,qua_b),('Uranium',ura_ms,ura_b)
            ]

        for i in profit_checks:
            profit_check(i[0],i[1],i[2])

        ### Buy from Starbase and sell to Megabase
        form_data_1 = sorted([(i, j) for i, j in zip(lis1[::2], lis1[1::2])], reverse=True)

        if len(lis1) == 0:
          print('N/A   N/A')
        else:
          b = b + 1

        ### Buy from Megabase and sell to Starbase
        form_data_2 = sorted([(abs(i), j) for i, j in zip(lis2[::2], lis2[1::2])], reverse=True)

        if len(lis2) == 0:
          print('N/A   N/A')
        else:
          b = b + 1

        return render_template('data.html',form_data_1 = form_data_1,form_data_2 = form_data_2,
                trade = trade)
    return render_template('form.html')


app.run(host='localhost', port=5002)
