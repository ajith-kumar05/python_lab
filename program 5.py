#SQL

import pymysql
class Employee:
        def create(self):
                self.db=pymysql.connect(host="172.16.34.105",user="mca109",passwd="mca109",database="mca109")
                self.cur=self.db.cursor()
                #self.cur.execute("create database employee")
                self.cur.execute("Show databases")
                for row in self.cur:
                                print(row)
        def tablecreate(self):
                self.cur.execute("create table emp(name varchar(20),age int(10),slno int(10),mobile int(10),address varchar(20))")
                self.cur.execute("describe emp")
                for row in self.cur:
                        print(row)
        def inserttable(self):
                tab="insert into emp(name,age,slno,mobile,address)values(%s,%s,%s,%s,%s)"
                val=[("Ajith",21,109,7686678,"bangalore"),("Rem",20,108,6546678,"bangalore"),("Yuno gasai",20,110,355875,"bangalore"),("Marin kitagawa",22,111,3465587,"bangalore"),]
                self.cur.executemany(tab,val)
                self.db.commit()
                print("inserted")
        def display(self):
                self.cur.execute("select * from emp")
                rows=self.cur.fetchall()
                for row in rows:
                        print(row)
        def delete(self,slno):
                self.cur.execute("delete from emp where slno='%s'"%(int(slno)))
                self.db.commit()
                print("deleted")
        def drop(self):
                self.cur.execute("drop table emp")
                print("table dropped")
while True:
        print("1.create database\n2.create table\n3.insert table values\n4.display\n5.delete a record\n6.drop table")
        print("Enter your choice:")
        ch=int(input())
        if ch==1:
                print("******************************")
                ob=Employee()
                ob.create()
                print("******************************")
        elif ch==2:
                print("******************************")
                ob.tablecreate()
                print("******************************")
        elif ch==3:
                print("******************************")
                ob.inserttable()
                print("******************************")
        elif ch==4:
                print("******************************")
                ob.display()
                print("******************************")
        elif ch==5:
                print("******************************")
                ob.delete("108")
                print("******************************")
        elif ch==6:
                print("******************************")
                ob.drop()
                print("******************************")
        else:
                break
