import sqlite3
con = sqlite3.connect('database.db')
cur = con.cursor()
sql = "SELECT id, name, description FROM NAMES"
f = open('modals.txt', 'w')
for row in cur.execute(sql):
    modalId = 'modalName' + str(row[0])
    print("""
<div class="modal fade" id='""" + modalId + """' tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-fullscreen-xxl-down">
    <div class="modal-content">
      <div class="modal-header">
        <div class="container">
          <div class="row">
              """ + row[1] + """
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
        </div>
        </div>
      <div class="modal-body">
        <div class="row text-center">
          <div class="col img-fluid"><img src="img/names/""" + str(row[0]) + """.jpg" alt=""></div>
      </div>
        <div class="row">
          <div class="col text-center mt-5">
             <div class="text">
             """ + row[2] + """
             </div>
          </div>
        </div>    
      </div> 
    </div>
  </div>
</div>
""")
    
con.commit()
con.close()
f.close()
