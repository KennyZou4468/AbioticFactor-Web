from flask import Flask, render_template, request, url_for, redirect, session
import pymysql
app = Flask(__name__)
authority_global=None
@app.route("/SignUp", methods=['GET', 'POST'])
def SignUp():
    #button_click_for_signup跳转至此，显示页面
    if request.method == 'GET':
        print("show page for sign up--get")
        return render_template("SignUpPage.html")  # Render the signup page
    #注册函数实现，加入数据库新数据
    if request.method == 'POST':
        print("show page for sign up--post")
        username = request.form.get('user')
        password = request.form.get('password')
        sector = request.form.get('sector')
        if(username == "" or password == "" or sector == ""):
            return  render_template("SignUpPage.html");
        # For now, just print out the form data in the console
        print(f"Username: {username}, Password: {password}, Sector: {sector}")
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="12345678", db="AbioticFactor")
        cursor = conn.cursor()
        sql = "insert into staff(name,password,sector) values(%s,%s,%s)"
        cursor.execute(sql, [username, password, sector])
        conn.commit()
        cursor.close()
        conn.close()
        #返回主页面
        return render_template("LoginMainPage.html")
@app.route("/",methods=['GET', 'POST'])
def Login():
    if request.method == 'GET':
        print("show page for main page--get")
        return render_template("LoginMainPage.html")  # Render the signup page
@app.route("/Check",methods=['POST'])
def Check():
    global authority_global
    if request.method == "POST":
        #检查sign in 的时候是否存在于数据库
        print("show page for main page--post")
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="12345678", db="AbioticFactor")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"Username: {username}, Password: {password}")
        cursor.execute("select * from staff where name=%s and password=%s", (username, password))
        data_list = cursor.fetchall()
        if len(data_list) == 0:
            print("no data")
            return render_template("LoginMainPage.html", message="No such staff,or your password is wrong.\nPlease try again.")
        else:
            print("Identity confirmed!")
            authority=data_list[0]
            authority=authority["authorized"]
            print(authority)
            #获取权限等级
            authority_global=authority
        cursor.close()
        conn.close()
        return redirect(url_for("EntityList"))
@app.route("/StaffList", methods=['GET'])
def StaffList():
    page = request.args.get('page', 1, type=int)  # 获取当前页码，默认为1
    per_page = 10  # 每页显示的元素数量
    offset = (page - 1) * per_page  # 计算SQL查询的偏移量

    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="12345678", db="AbioticFactor")
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # 获取staff的总数
    cursor.execute("SELECT COUNT(*) FROM staff")
    total = cursor.fetchone()['COUNT(*)']

    # 获取当前页面的staff数据
    cursor.execute(f"SELECT * FROM staff LIMIT {per_page} OFFSET {offset}")
    data_list = cursor.fetchall()

    cursor.close()
    conn.close()

    total_pages = (total + per_page - 1) // per_page  # 计算总页数

    return render_template("StaffForm.html", data_list=data_list, page=page, total_pages=total_pages)
@app.route("/EntityList",methods=['GET'])
def EntityList():
    page = request.args.get('page', 1, type=int)  # 获取当前页码，默认为1
    per_page = 10  # 每页显示的元素数量
    offset = (page - 1) * per_page  # 计算SQL查询的偏移量

    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="12345678", db="AbioticFactor")
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # 获取staff的总数
    cursor.execute("SELECT COUNT(*) FROM Entity")
    total = cursor.fetchone()['COUNT(*)']

    # 获取当前页面的staff数据
    cursor.execute(f"SELECT * FROM Entity LIMIT {per_page} OFFSET {offset}")
    data_list = cursor.fetchall()

    cursor.close()
    conn.close()

    total_pages = (total + per_page - 1) // per_page  # 计算总页数

    return render_template("EntityContent.html", data_list=data_list, page=page, total_pages=total_pages)
@app.route("/LocationList",methods=['GET'])
def LocationList():
    page = request.args.get('page', 1, type=int)  # 获取当前页码，默认为1
    per_page = 10  # 每页显示的元素数量
    offset = (page - 1) * per_page  # 计算SQL查询的偏移量

    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="12345678", db="AbioticFactor")
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # 获取staff的总数
    cursor.execute("SELECT COUNT(*) FROM Location")
    total = cursor.fetchone()['COUNT(*)']

    # 获取当前页面的staff数据
    cursor.execute(f"SELECT * FROM Location LIMIT {per_page} OFFSET {offset}")
    data_list = cursor.fetchall()

    cursor.close()
    conn.close()

    total_pages = (total + per_page - 1) // per_page  # 计算总页数

    return render_template("LocationContent.html", data_list=data_list, page=page, total_pages=total_pages)
@app.route("/TheoryList",methods=['GET'])
def TheoryList():
    page = request.args.get('page', 1, type=int)  # 获取当前页码，默认为1
    per_page = 10  # 每页显示的元素数量
    offset = (page - 1) * per_page  # 计算SQL查询的偏移量

    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="12345678", db="AbioticFactor")
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    # 获取staff的总数
    cursor.execute("SELECT COUNT(*) FROM Theory")
    total = cursor.fetchone()['COUNT(*)']

    # 获取当前页面的staff数据
    cursor.execute(f"SELECT * FROM Theory LIMIT {per_page} OFFSET {offset}")
    data_list = cursor.fetchall()

    cursor.close()
    conn.close()

    total_pages = (total + per_page - 1) // per_page  # 计算总页数

    return render_template("TheoryContent.html", data_list=data_list, page=page, total_pages=total_pages)
@app.route("/button_click_for_signup",methods=['GET'])
def button_click_for_signup():
    #单独跳转到SignUp函数
    print("Opps")
    print(url_for("SignUp"))
    return redirect(url_for("SignUp"))
@app.route("/deleteEntity",methods=['POST'])
def deleteEntity():
    id=request.form.get('id')
    print(id)
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="12345678", db="AbioticFactor")
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql='DELETE FROM Entity WHERE id = %s'
    cursor.execute(sql, [id])
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('EntityList'))
@app.route("/deleteStaff",methods=['POST'])
def deleteStaff():
    id=request.form.get('id')
    print(id)
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="12345678", db="AbioticFactor")
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql='DELETE FROM staff WHERE id = %s'
    cursor.execute(sql, [id])
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('StaffList'))
@app.route("/deleteTheory",methods=['POST'])
def deleteTheory():
    id=request.form.get('id')
    print(id)
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="12345678", db="AbioticFactor")
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql='DELETE FROM Theory WHERE id = %s'
    cursor.execute(sql, [id])
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('TheoryList'))
@app.route("/deleteLocation",methods=['POST'])
def deleteLocation():
    id=request.form.get('id')
    print(id)
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="12345678", db="AbioticFactor")
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql='DELETE FROM Location WHERE id = %s'
    cursor.execute(sql, [id])
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('LocationList'))
@app.route("/addEntity",methods=['GET','POST'])
def addEntity():
    if request.method == "GET":
        print("show page for AddEntity--get")
        return render_template("AddEntityPage.html")  # Render the signup page
    if request.method == 'POST':
        print("show page for Add entity--post")
        CodeName = request.form.get('Codename')
        Name = request.form.get('Name')
        Description = request.form.get('Description')
        if(CodeName == "" or Name == "" or Description == ""):
            return  render_template("AddEntityPage.html");
        # For now, just print out the form data in the console
        print(f"CodeName: {CodeName}, Name: {Name}, Description: {Description}")
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="12345678", db="AbioticFactor")
        cursor = conn.cursor()
        sql = "insert into Entity(codename,name,description) values(%s,%s,%s)"
        cursor.execute(sql, [CodeName, Name, Description])
        conn.commit()
        cursor.close()
        conn.close()
        #返回主页面
        return redirect(url_for('EntityList'))
@app.route("/addTheory",methods=['GET','POST'])
def addTheory():
    if request.method == "GET":
        print("show page for AddTheory--get")
        return render_template("AddTheoryPage.html")  # Render the signup page
    if request.method == 'POST':
        print("show page for Add theory--post")
        Name = request.form.get('Name')
        Description = request.form.get('Description')
        if( Name == "" or Description == ""):
            return  render_template("AddEntityPage.html");
        # For now, just print out the form data in the console
        print(f"Name: {Name}, Description: {Description}")
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="12345678", db="AbioticFactor")
        cursor = conn.cursor()
        sql = "insert into Theory(name,description) values(%s,%s)"
        cursor.execute(sql, [Name, Description])
        conn.commit()
        cursor.close()
        conn.close()
        #返回主页面
        return redirect(url_for('TheoryList'))
@app.route("/addLocation",methods=['GET','POST'])
def addLocation():
    if request.method == "GET":
        print("show page for AddLocation--get")
        return render_template("AddLocationPage.html")  # Render the signup page
    if request.method == 'POST':
        print("show page for addLocation--post")
        Locationname = request.form.get('Location-name')
        Description = request.form.get('Description')
        if(Locationname == "" or Description == ""):
            return  render_template("AddLocationPage.html");
        # For now, just print out the form data in the console
        print(f"CodeName: {Locationname},Description: {Description}")
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="12345678", db="AbioticFactor")
        cursor = conn.cursor()
        sql = "insert into Location(name,description) values(%s,%s)"
        cursor.execute(sql, [Locationname, Description])
        conn.commit()
        cursor.close()
        conn.close()
        #返回主页面
        return redirect(url_for('LocationList'))
@app.route("/editTheory",methods=['GET','POST'])
def editTheory():
    name = request.args.get('name')  # 获取传递的codename
    if request.method == "GET":
        print("show page for editTheory--get")
        return render_template("EditTheoryPage.html",name=name)  # Render the signup page
    if request.method == 'POST':
        print("show page for Add Theory--post")
        Name = request.form.get('Name')
        Description = request.form.get('Description')
        if(Name == "" or Description == ""):
            return  render_template("EditEntityPage.html");
        # For now, just print out the form data in the console
        print(f"Name: {Name}, Description: {Description}")
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="12345678", db="AbioticFactor")
        cursor = conn.cursor()
        sql = "update Theory set description=%s where name=%s"
        cursor.execute(sql, [Description, Name])
        conn.commit()
        cursor.close()
        conn.close()
        #返回主页面
        return redirect(url_for('TheoryList'))
@app.route("/editEntity",methods=['GET','POST'])
def editEntity():
    codename = request.args.get('codename')  # 获取传递的codename
    if request.method == "GET":
        print("show page for editEntity--get")
        return render_template("EditEntityPage.html",codename=codename)  # Render the signup page
    if request.method == 'POST':
        print("show page for Add entity--post")
        CodeName = request.form.get('Codename')
        Name = request.form.get('Name')
        Description = request.form.get('Description')
        if(Name == "" or Description == ""):
            return  render_template("EditEntityPage.html");
        # For now, just print out the form data in the console
        print(f"CodeName: {CodeName}, Name: {Name}, Description: {Description}")
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="12345678", db="AbioticFactor")
        cursor = conn.cursor()
        sql = "update Entity set name=%s, description=%s where codename=%s"
        cursor.execute(sql, [Name, Description, CodeName])
        conn.commit()
        cursor.close()
        conn.close()
        #返回主页面
        return redirect(url_for('EntityList'))
@app.route("/editStaff",methods=['GET','POST'])
def editStaff():
    global authority_global
    name = request.args.get('name')  # 获取传递的name
    print(authority_global)
    if authority_global == 0:
        # 没有权限，返回错误信息，并返回 StaffList 页面
        page = 1  # 假设当前页面是第1页
        total_pages = 1  # 假设总页数为1
        return render_template("StaffForm.html", message="You don't have authority to edit!", page=page,total_pages=total_pages)
    else:
        if request.method == "GET":
            print("show page for editStaff--get")
            return render_template("EditStaffPage.html", name=name)  # Render the signup page
        if request.method == 'POST':
            print("show page for edit staff--post")
            Name = request.form.get('Name')
            password = request.form.get('password')
            Authorized = request.form.get('Authorized')
            Authorized = int(Authorized)
            Sector = request.form.get('Sector')
            if (Name == "" or password == "" or Authorized == "" or Sector == ""):
                return render_template("EditStaffPage.html");
            # For now, just print out the form data in the console
            print(f"CName: {Name}, password: {password},Authorized:{Authorized},Sector:{Sector}")
            conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="12345678", db="AbioticFactor")
            cursor = conn.cursor()
            sql = "update Staff set password=%s, authorized=%s, sector = %s where name=%s"
            cursor.execute(sql, [password, Authorized, Sector, Name])
            conn.commit()
            cursor.close()
            conn.close()
            # 返回主页面
            return redirect(url_for('StaffList'))
@app.route("/editLocation",methods=['GET','POST'])
def editLocation():
    name = request.args.get('name')  # 获取传递的name
    global authority_global
    if (authority_global == 0):
        # 没有权限
        return render_template("LocationContent.html", message="You don't have authority to edit!")
    else:
        if request.method == "GET":
            print("show page for editLocation--get")
            return render_template("EditLocationPage.html",name=name)  # Render the signup page
        if request.method == 'POST':
            print("show page for edit location--post")
            Name = request.form.get('Location-name')
            Description = request.form.get('Description')
            if(Name == "" ):
                return render_template("EditLocationPage.html");
            print(f"Name: {Name}, Description: {Description}")
            conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="12345678", db="AbioticFactor")
            cursor = conn.cursor()
            sql = "update Location set description=%s where name=%s"
            cursor.execute(sql, [Description,Name])
            conn.commit()
            cursor.close()
            conn.close()
            #返回主页面
            return redirect(url_for('LocationList'))

if __name__ == '__main__':
    app.run(debug=True)