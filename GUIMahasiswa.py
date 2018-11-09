import sys
from PyQt5.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QRadioButton, QGroupBox, QPushButton,\
                            QFrame, QLabel, QTableWidget, QTableWidgetItem, QTableView, QMessageBox,\
                            QLineEdit, QGridLayout

class AppStimed(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent) #memanggil beberapa fungsi
        
        self.tableModel()
        self.groupBoxOther()
        self.txtAction()
        self.btnAction()
        self.gridLayout1()
        self.gridLayout2()
        self.gridLayout3()
        self.verticalLay()
        
        self.setWindowTitle("Data Mahasiswa STIMED Nusa Palapa")
        self.setGeometry(340, 50, 658, 650)
        self.setWindowIcon(QIcon("folderIcon/memed.png"))
    
    def tableModel(self):
        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels(['Nim', 'Nama', 'Jurusan','Tahun Masuk','Alamat','Agama'])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers) #nonaktifkan untuk edit di tabel
        self.table.setSelectionBehavior(QTableWidget.SelectRows) #agar semua 1 baris terseleksi
    
    def groupBoxOther(self):
        self.groupBoxJrsn = QGroupBox(" [ Pilih Jurusan ] ",self)
        self.groupBoxForm = QGroupBox(" [ Isi Form ] ",self)
        self.groupBoxBtn = QGroupBox(" [ Tekan Tombol Berikut ] ",self)
        self.groupBoxCari = QGroupBox(" [ Search && Order ] ",self)
        
        self.radio1 = QRadioButton("TI (S1)",self.groupBoxJrsn)
        self.radio1.setGeometry(10, 20, 110, 20)
        self.radio2 = QRadioButton("SI (S1)",self.groupBoxJrsn)
        self.radio2.setGeometry(10, 40, 110, 20)
        
        self.radio1.toggled.connect(self.radio1Checked)
        self.radio2.toggled.connect(self.radio2Checked )
        
        self.lineV = QFrame(self.groupBoxJrsn)
        self.lineV.setGeometry(200, 10, 20, 50)
        self.lineV.setFrameShape(QFrame.VLine)
        self.lineV.setFrameShadow(QFrame.Sunken)
        
    def txtAction(self):
        self.lblNim = QLabel("Nim                        :")
        self.txtNim = QLineEdit()
        self.txtNim.setPlaceholderText("ex : 01510002 - tekan tombol help")
        self.txtNim.setMaxLength(8)
        
        self.lblNama = QLabel("Nama                     :")
        self.txtNama = QLineEdit()
        self.txtNama.setPlaceholderText("ex : imo")
        
        self.lblTahun = QLabel("Tahun Masuk         : ")
        self.txtTahun = QLineEdit()
        self.txtTahun.setPlaceholderText("ex : 2015")
        self.txtTahun.setMaxLength(4)
        
        self.lblAlamat = QLabel("Alamat                   :")
        self.txtAlamat = QLineEdit()
        self.txtAlamat.setPlaceholderText("ex : Jl. Budidaya, Antang")
        
        self.lblAgama = QLabel("Agama                   :")
        self.txtAgama = QLineEdit()
        self.txtAgama.setPlaceholderText("ex : Islam")
        
        self.lblCari = QLabel("Cari Nama             :",self.groupBoxCari)
        self.lblCari.setGeometry(10, 20, 100, 10)
        self.txtCari = QLineEdit()
        self.txtCari.setPlaceholderText("ex : Rafika")
        self.lblOrder = QLabel("<u>Urutkan semua data secara Asc :</u>",self.groupBoxCari)
        
        self.lblKeterangan = QLabel("<u>Keterangan Jurusan</u> :",self.groupBoxJrsn)
        self.lblKeterangan.setGeometry(250, 10, 110, 13)
        self.lblJrsan = QLabel("",self.groupBoxJrsn)
        self.lblJrsan.setGeometry(250, 30, 110, 13)
        
    def btnAction(self):
        self.btnSimpan = QPushButton('&Simpan')
        self.btnSimpan.clicked.connect(self.simpanData)
        self.btnSimpan.clicked.connect(self.loadData)

        self.btnUpdate = QPushButton('&Update')
        self.btnUpdate.clicked.connect(self.updateData)
        self.btnUpdate.clicked.connect(self.loadData)
        
        self.btnEdit= QPushButton('&Edit')
        self.btnEdit.clicked.connect(self.editData)
        
        self.btnHapus = QPushButton('&Hapus')
        self.btnHapus.clicked.connect(self.hapusData)
        
        self.btnReset = QPushButton('&Reset')
        self.btnReset.clicked.connect(self.resetTxt)
        self.btnReset.clicked.connect(self.loadData)
        
        self.btnExit = QPushButton('&Exit')
        self.btnExit.clicked.connect(self.close)
        
        self.btnPrint = QPushButton('&Print')
        self.btnPrint.clicked.connect(self.printTable)
        
        self.information = QPushButton('&Help')
        self.information.clicked.connect(self.helpMeWoi)
        
        self.btnCari = QPushButton("Cari",self.groupBoxCari)
        self.btnCari.clicked.connect(self.cariData)
        
        self.btnOrderNamaAsc = QPushButton("Order by nama",self.groupBoxCari)
        self.btnOrderNamaAsc.clicked.connect(self.loadData)
        self.btnOrderNamaAsc.clicked.connect(self.orderNamaAsc)
        
        self.btnOrderThnAsc = QPushButton("Order by tahun masuk",self.groupBoxCari)
        self.btnOrderThnAsc.clicked.connect(self.loadData)
        self.btnOrderThnAsc.clicked.connect(self.orderThnAsc)
        
    def gridLayout1(self): #txt,jrsn,label
        self.grid = QGridLayout(self.groupBoxForm)
        self.grid.setContentsMargins(10, 10, 110, 10)
        self.grid.addWidget(self.lblNim, 0, 0)
        self.grid.addWidget(self.txtNim, 0, 1)
        self.grid.addWidget(self.lblNama, 1, 0)
        self.grid.addWidget(self.txtNama, 1, 1)
        self.grid.addWidget(self.groupBoxJrsn, 2,1,12,1)
        self.grid.addWidget(self.lblTahun, 17, 0)
        self.grid.addWidget(self.txtTahun, 17, 1)
        self.grid.addWidget(self.lblAlamat, 18, 0)
        self.grid.addWidget(self.txtAlamat, 18, 1)
        self.grid.addWidget(self.lblAgama, 19, 0)
        self.grid.addWidget(self.txtAgama, 19, 1)
        
    def gridLayout2(self): #gboxCari
        self.grid2 = QGridLayout(self.groupBoxCari)
        self.grid2.setContentsMargins(110, 5, 110, 5) #margin kiri,atas, kanan, bawah 
        self.grid2.addWidget(self.txtCari, 0, 0, 1, 0) #baris 0 kolom 0 sampai, kolom 1
        self.grid2.addWidget(self.btnCari, 1, 0, 1, 0)
        self.grid2.addWidget(self.lblOrder, 2, 0, 1, 0)
        self.grid2.addWidget(self.btnOrderNamaAsc, 3, 0)
        self.grid2.addWidget(self.btnOrderThnAsc, 3, 1)
               
    def gridLayout3(self): #actionBtn
        self.grid3 = QGridLayout(self.groupBoxBtn)
        self.grid3.addWidget(self.btnSimpan,0,0)
        self.grid3.addWidget(self.btnHapus,1,0)
        self.grid3.addWidget(self.btnEdit,0,1)
        self.grid3.addWidget(self.btnUpdate,1,1)
        self.grid3.addWidget(self.btnPrint,0,2)
        self.grid3.addWidget(self.btnReset,1,2)
        self.grid3.addWidget(self.btnExit,0,3)
        self.grid3.addWidget(self.information,1,3)
        
    def verticalLay(self):
        self.vbx = QVBoxLayout()
        self.vbx.addWidget(self.groupBoxForm)
        self.vbx.addWidget(self.groupBoxCari)
        self.vbx.addWidget(self.groupBoxBtn)
        self.vbx.addWidget(self.table)
    
        self.setLayout(self.vbx) #membuat vbx sebagai Layout utama
        
    def radio1Checked(self, enable):
        if enable:
            self.lblJrsan.setText("Teknik Informatika")
    def radio2Checked(self, enable):
        if enable:
            self.lblJrsan.setText("Sistem Informasi")
            
    def cariData(self):
        print ("ini cari")
        cariNama = self.txtCari.text()
        index = 0
        query = QSqlQuery()
        query.exec_("SELECT * FROM tbl_mahasiswa WHERE nama LIKE '%{0}%'".format(cariNama))

        while query.next():
            nimMhs = query.value(0)
            namaMhs = query.value(1)
            jrsMhs = query.value(2)
            thnMhs = query.value(3)
            alamatMhs = query.value(4)
            agamaMhs = query.value(5)

            self.table.setRowCount(index + 1)
            self.table.setItem(index, 0, QTableWidgetItem(str(nimMhs)))
            self.table.setItem(index, 1, QTableWidgetItem(namaMhs))
            self.table.setItem(index, 2, QTableWidgetItem(jrsMhs))
            self.table.setItem(index, 3, QTableWidgetItem(str(thnMhs)))
            self.table.setItem(index, 4, QTableWidgetItem(alamatMhs))
            self.table.setItem(index, 5, QTableWidgetItem(agamaMhs))
            index += 1
        
    def loadData(self):
        index = 0
        query = QSqlQuery()
        query.exec_("SELECT * FROM tbl_mahasiswa")

        while query.next():
            nimMhs = query.value(0)
            namaMhs = query.value(1)
            jrsMhs = query.value(2)
            thnMhs = query.value(3)
            alamatMhs = query.value(4)
            agamaMhs = query.value(5)

            self.table.setRowCount(index + 1)
            self.table.setItem(index, 0, QTableWidgetItem(str(nimMhs)))
            self.table.setItem(index, 1, QTableWidgetItem(namaMhs))
            self.table.setItem(index, 2, QTableWidgetItem(jrsMhs))
            self.table.setItem(index, 3, QTableWidgetItem(str(thnMhs)))
            self.table.setItem(index, 4, QTableWidgetItem(alamatMhs))
            self.table.setItem(index, 5, QTableWidgetItem(agamaMhs))
            index += 1

    def simpanData(self):
        try:
            nimMhs = self.txtNim.text()
            namaMhs = self.txtNama.text()
            jrsMhs = self.lblJrsan.text()
            thnMhs = int(self.txtTahun.text())
            alamatMhs = self.txtAlamat.text()
            agamaMhs = self.txtAgama.text()
    
            query = QSqlQuery()
            query.exec_("INSERT INTO tbl_mahasiswa VALUES('{0}', '{1}', '{2}', {3}, '{4}', '{5}')".\
                        format(nimMhs, namaMhs, jrsMhs, thnMhs, alamatMhs, agamaMhs))
        except ValueError:
            QMessageBox.critical(self, "Terjadi Error",
                    "Coba periksa data yang anda input.\n"
                    "Mungkin terjadi kesalahan padan penginputan\n\n"
                    "Klik Yes untuk mencoba lagi.", QMessageBox.Yes)
        self.resetTxt()
        
    def editData(self):
        try:
            selected = self.table.currentIndex()
            if not selected.isValid() or len(self.table.selectedItems()) < 1:
                return
            
            print(not selected.isValid())
            self.nimMhs = self.table.selectedItems()[0]
            namaMhs = self.table.selectedItems()[1]
            jrsMhs = self.table.selectedItems()[2]
            thnMhs = self.table.selectedItems()[3]
            alamatMhs = self.table.selectedItems()[4]
            agamaMhs = self.table.selectedItems()[5]
            
            self.txtNim.setText(str(self.nimMhs.text()))
            self.txtNama.setText(str(namaMhs.text()))
            self.lblJrsan.setText(str(jrsMhs.text()))
            self.txtTahun.setText(str(thnMhs.text()))
            self.txtAlamat.setText(str(alamatMhs.text()))
            self.txtAgama.setText(str(agamaMhs.text()))
        except ValueError:
            print(ValueError)
    def updateData(self):
        try:
            namaMhs = self.txtNama.text()
            jrsMhs = self.lblJrsan.text()
            thnMhs = int(self.txtTahun.text())
            alamatMhs = self.txtAlamat.text()
            agamaMhs = self.txtAgama.text()
            
            query = QSqlQuery()
            query.exec_("UPDATE tbl_mahasiswa SET nama='{0}', jurusan='{1}', thn_masuk={2},\
                        alamat='{3}', agama='{4}' WHERE nim='{5}'"\
                        .format(namaMhs, jrsMhs, thnMhs, alamatMhs, agamaMhs,self.nimMhs.text()))
        except ValueError:
            QMessageBox.critical(self, "Update Gagal",
                    "Coba periksa data yang anda input.\n"
                    "Mungkin terjadi kesalahan pada penginputan\n\n"
                    "Klik Yes untuk mencoba lagi.", QMessageBox.Yes)
        self.resetTxt()
    def hapusData(self):
        selected = self.table.currentIndex()
        if not selected.isValid() or len(self.table.selectedItems()) < 1:
            return

        nimMhs = self.table.selectedItems()[0]
        query = QSqlQuery()
        try:
            query.exec_("delete from tbl_mahasiswa where nim = " + nimMhs.text())
        except ValueError:
            QMessageBox.critical(self, "Hapus Gagal",
                    "Coba periksa data Table\n\n"
                    "Klik Yes untuk mencoba lagi.", QMessageBox.Yes)
        self.table.removeRow(selected.row())
        self.table.setCurrentIndex(QModelIndex())
        
    def resetTxt(self):
        self.txtNim.clear()
        self.txtNama.clear()
        self.txtTahun.clear()
        self.txtAlamat.clear()
        self.txtAgama.clear()
        self.txtCari.clear()
        
    def orderNamaAsc(self):
        index = 0
        query = QSqlQuery()
        query.exec_("SELECT * FROM tbl_mahasiswa ORDER BY nama ASC")
        while query.next():
            nimMhs = query.value(0)
            namaMhs = query.value(1)
            jrsMhs = query.value(2)
            thnMhs = query.value(3)
            alamatMhs = query.value(4)
            agamaMhs = query.value(5)

            self.table.setRowCount(index + 1)
            self.table.setItem(index, 0, QTableWidgetItem(str(nimMhs)))
            self.table.setItem(index, 1, QTableWidgetItem(namaMhs))
            self.table.setItem(index, 2, QTableWidgetItem(jrsMhs))
            self.table.setItem(index, 3, QTableWidgetItem(str(thnMhs)))
            self.table.setItem(index, 4, QTableWidgetItem(alamatMhs))
            self.table.setItem(index, 5, QTableWidgetItem(agamaMhs))
            index += 1
            
    def orderThnAsc(self):
        index = 0
        query = QSqlQuery()
        query.exec_("SELECT * FROM tbl_mahasiswa ORDER BY thn_masuk ASC")
        while query.next():
            nimMhs = query.value(0)
            namaMhs = query.value(1)
            jrsMhs = query.value(2)
            thnMhs = query.value(3)
            alamatMhs = query.value(4)
            agamaMhs = query.value(5)

            self.table.setRowCount(index + 1)
            self.table.setItem(index, 0, QTableWidgetItem(str(nimMhs)))
            self.table.setItem(index, 1, QTableWidgetItem(namaMhs))
            self.table.setItem(index, 2, QTableWidgetItem(jrsMhs))
            self.table.setItem(index, 3, QTableWidgetItem(str(thnMhs)))
            self.table.setItem(index, 4, QTableWidgetItem(alamatMhs))
            self.table.setItem(index, 5, QTableWidgetItem(agamaMhs))
            index += 1
        
    def closeEvent(self, event):        
        reply = QMessageBox.question(self, 'Message',"Yakin ingin keluar ? ",
				QMessageBox.Yes |  QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def printTable(self):
        printer = QPrinter(QPrinter.ScreenResolution)
        dlg = QPrintPreviewDialog(printer)
        view = PrintView()
        view.setModel(self.table.model())
        dlg.paintRequested.connect(view.printIni)
        dlg.exec_()
        
    def helpMeWoi(self):
        QMessageBox.information(self,"Butuh Bantuan ka kodong :V","<b>PETUNJUK !  **  <br/>I HAVE NEW RULES CIKA :V</b><br/><br/><br/>"\
                                "<i><b>IKUTI ATURANKU NAH :</b><br/><br/>"
                                "1. Penulisan nim masih belum bisa diawali dengan 0, karena tipe data Int<br/>"
                                "bila diubah ke Varchar maka database pada aplikasi tidak dapat terhapus<br/>"
                                "mungkin ada cara, but we, '<u>not found</u>' -,-<br/><br/>"
                                "2. Untuk update data, pilih terlebih dahulu data pada tabel setelah itu tekan<br/>"
                                "tombol edit dan akan muncul data yang terpilih dan tekan update jika selesai.<br/><br/>"
                                "3. Saat ini nim tidak dapat di update karena nim sebagai PrimaryKey<br/>"
                                "mungkin ada cara tapi kami belum menemukan source cara update PrimaryKey.<br/><br/><br/>"
                                "<i>Create on 08/02/2018,</i><br/>"
                                "<b>Created by: V:<b>")
        
    def db_connect(self, filename, server):
        db = QSqlDatabase.addDatabase(server)
        db.setDatabaseName(filename)
        ok = db.open()
        if not ok:
            QMessageBox.critical(self, "Tidak dapat membuka database","Tidak dapat"
                    "terhubung ke database.\n"
                    "Cari di google tentang SQLite support. Baca tentang QtSQL"
                    "\n\n\nKlik Ok untuk keluar.", QMessageBox.Ok)
            sys.exit()

    def db_create(self):
        query = QSqlQuery()
        query.exec_("CREATE TABLE tbl_mahasiswa(nim VARCHAR(8) PRIMARY KEY,"
                    "nama VARCHAR(20) NOT NULL, jurusan VARCHAR(15) NOT NULL, thn_masuk int, alamat VARCHAR(30) NOT NULL,\
                    agama VARCHAR(20) NOT NULL)")
        query.exec_("insert into tbl_mahasiswa values('01510002', 'Rafika Ramayanti', 'Sistem Informasi', 2015,\
                    'Jl. Budidaya, antang', 'Islam')")
    def init(self, filename, server):
        import os
        if not os.path.exists(filename):
            self.db_connect(filename, server)
            self.db_create()
        else:
            self.db_connect(filename, server)
            
class PrintView(QTableView):
    def __init__(self):
        super(PrintView, self).__init__()
    def printIni(self, printer):
        self.resize(printer.width(), printer.height())
        self.render(printer)

if __name__ == '__main__':
    import os
    app = QApplication(sys.argv)
    mainWin = AppStimed()
    mainWin.init('folderDB/db_mahasiswa-ini.db', 'QSQLITE')
    mainWin.loadData()
    mainWin.show()
    os.system('echo hello')
    sys.exit(app.exec_())