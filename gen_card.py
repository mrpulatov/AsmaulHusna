import sqlite3
con = sqlite3.connect('database.db')
cur = con.cursor()
sql = "SELECT name, id, name_arabic FROM NAMES"
for row in cur.execute(sql):
    modalId = 'modalName' + str(row[1])
    print("""
          <div class="col-xl-4 col-lg-4 col-md-6 col-sm-6 card-block ">
            <div class="info card" data-bs-toggle="modal" data-bs-target="#""" + modalId + """">
              <div class="row text-center">
                  <div class="col cirilic">""" + row[0] + """</div>
                  <div class="col number yellow">""" + str(row[1]) + """</div>
                  <div class="col arabic yellow">""" + row[2] + """</div>
              </div>     
            </div>
          </div>
""")
con.commit()
con.close()
