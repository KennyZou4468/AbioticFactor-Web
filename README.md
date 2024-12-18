# AbioticFactor Web
 This is a project about database. The theme is Abiotic Factor
 demo video link: https://www.bilibili.com/video/BV1iQkcYLE1q/?vd_source=8e598f658d074544cf8ad3e4f322a1b2
 
Overall description
Abiotic Factor is a popular video game. I like it very much so I decide to make a project regarding it.
There are several tables within the databases. The main role is staff, which is the key for you to login the web and view different information of different contents, including staff, location, theory, entity. I combine web page and database mysql using pymysql and flask.
This is a background information about this game:

“Home to the world's greatest minds, GATE operates a global network of secretive research laboratories, spanning every field of scientific study - and the realms beyond.

As a GATE employee you extend the bounds of human knowledge, and seek to explain the unexplainable - including anomalies and paranormal entities: from gravity-distorting artifacts to supernatural creatures with an unbridled instinct for violence. Safety, security, and secrecy are of the utmost importance… usually.

After a catastrophic containment breach, your workplace has become a cosmic battle zone: anomalous entities are on the loose, enemies from other dimensions are invading via portals, and an arcane military sect - known as The Order - is targeting personnel and entities indiscriminately, aiming to seize artifacts and put an end to the chaos.

Containment procedures have failed and help isn’t on the way. Stranded miles beneath the surface, it’s up to you and your fellow scientists to band together, plan your escape, and make this underground complex your new home - for now.”




Requirement Analysis & database design
	 The main roles in this project are staffs. There are two kinds of staff, one has authority to add, edit, or delete information within the database, another has no such authority(normal staff can only see the information). 
All of them can view the information of different contents. If you have no account, you can click sign in button in the main login page to register a new staff !
The data in these tables are mostly data from the game, which is based on the game setting. Some of data comes from testing, I think you can easily distinguish.
SQL queries design
	I have some comments in APP.py, you can check it.
	If you want to add new data into database in terminal directly, you can use the followings SQL quries:
Add Entity:
		insert into Entity(codename,name,description) values(“”, “”, “”);
Add Location:
		insert into Location(name,description) values(“”, “”);
Add Staff:
		insert into Staff(name,password,authorized,sector) values(“”, “”, 0/1, “”);
(a)Showing information use sql like 
	"select * from staff"
 	And use some javascript to show data in the form, which enable you to view them in the web page.
(b)Notice that %s are parameters
(c)Achieving login and sign up need to check the database if there are any staff matches. 
	Login check:
	"select * from staff where name=%s and password=%s", (username, password)
		 Sign up:
	insert into staff(name,password,sector) values(%s,%s,%s)
(d)Add new item, delete, edit are as followings(use Entity database as an example):
	"insert into Entity(codename,name,description) values(%s,%s,%s)"
	'DELETE FROM Entity WHERE id = %s'
	"update Entity set name=%s, description=%s where codename=%s"


 
Front and back-end design and implemention
	For front end design, I use flask, html, CSS and javascript to implement. Besides, I use some CSS from fontawesome website and bootstrapt website to modify my website to make it more beautiful. There are many different html file in folder ‘template’, which will show corressponding information in web page. One video from bilibili is quite educational and meaningful and I put it here:	
【MySQL数据库，保姆级web前端数据库精讲视频，99%的新手选择】 https://www.bilibili.com/video/BV1Ns4y1w7sg/?share_source=copy_web&vd_source=ba9569846bdf4f9af33dd437098e8516
It teaches how to implement html web page, how to combine web with mysql database.
 	For back-end design, Please see codes in APP.py, where I implement all functions needed by the project, including adding, deleting, editing new objects(Entity, staff, Location,Theory) and check staff which contains aroud 12 functions.
I also implement function to pagination and display 10 elements per page. You can check it.




