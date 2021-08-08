from flask import *  
import sqlite3    
app = Flask(__name__)  
  
 
@app.route("/")  
def add():  
    return render_template("add_feedback.html")  
 
@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            department = request.form["department"]  
            feedback_type = request.form["feedback_type"]  
            describe_your_feedback = request.form["describe_your_feedback"]  
            name = request.form["name"] 
            email = request.form["email"] 
            with sqlite3.connect("FEEDBACK.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Feedback (department,feedback_type,describe_your_feedback,name,email) values (?,?,?,?,?)",(department,feedback_type,describe_your_feedback,name,email))  
                con.commit()  
                msg = "feedback successfully Added"  
                return render_template("success.html",msg = msg)  
        except Exception as error:  
            con.rollback()  
            msg = f"We can not add the feedback to the list due to {error}"
            return render_template("success.html", msg=msg)
        finally:
            con.close()  
 
@app.route("/view")  
def view():  
    con = sqlite3.connect("FEEDBACK.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Feedback")  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)  
  
@app.route("/final")
def final():
    return render_template("final.html")
if __name__ == "__main__":  
    app.run(debug = True)  