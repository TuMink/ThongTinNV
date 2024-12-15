import csv
import datetime
import pandas as pd
from tkinter import Tk, StringVar, IntVar, Toplevel, messagebox
from tkinter import ttk
def luu_tt():
    tt = {
        "Mã nv": ma_nv.get(),
        "Tên nv": ten_nv.get(),
        "Đơn vị": don_vi.get(),
        "Chức danh": chuc_danh.get(),
        "Ngày sinh": ngay_sinh.get(),
        "Giới tính": "Nam" if gioi_tinh.get() == 1 else "Nữ",
        "Là": "Là khách hàng" if la_gi.get()==1 else "Là nhà cung cấp",
        "Số CMND": so_cmnd.get(),
        "Ngày cấp": ngay_cap.get(),
        "Nơi cấp": noi_cap.get()
    }
    with open("NHANVIEN.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=thong_tin.keys())
        if file.tell() == 0:  # Nếu file rỗng, ghi header
            writer.writeheader()
        writer.writerow(tt)
    messagebox.showinfo("Thành công", "Đã lưu thông tin nhân viên vào file!")



def sinh_nhat_hom_nay():
    hom_nay = datetime.datetime.now().strftime("%d/%m/%Y").split("/")[0:2]
    if not os.path.exists("NHANVIEN.csv"):
        messagebox.showerror("Lỗi", "File CSV không tồn tại. Hãy nhập dữ liệu trước.")
        return

    with open("NHANVIEN.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip header
        ds_sn_hom_nay = [row for row in reader if row[2].split("/")[:2] == hom_nay]

    if not ds_sn_hom_nay:
        messagebox.showinfo("Kết quả", "Không có nhân viên nào sinh nhật hôm nay.")
    else:
        top = Toplevel()
        top.title("Nhân viên có sinh nhật hôm nay")
        ttk.Label(top, text="Danh sách nhân viên có sinh nhật hôm nay:").pack()
        for nv in ds_sn_hom_nay:
            ttk.Label(top, text=f"{nv[0]} - {nv[1]}").pack()


def xuat_excel():

    if not os.path.exists("nhanvien.csv"):
        messagebox.showerror("Lỗi", "File CSV không tồn tại. Hãy nhập dữ liệu trước.")
        return
    df = pd.read_csv("nhanvien.csv", encoding="utf-8")
    df["Tuoi"] = pd.to_datetime(df["Ngay Sinh"], format="%d/%m/%Y").dt.year
    df["Tuoi"] = datetime.datetime.now().year - df["Tuoi"]
    df = df.sort_values(by="Tuoi", ascending=False)
    df.to_excel("danhsach_nhanvien.xlsx", index=False, engine="openpyxl")
    messagebox.showinfo("Thành công", "Danh sách đã được xuất ra file Excel!")

cua_so = Tk()
cua_so.title("Thông tin nhân viên")
cua_so.geometry("650x200")

ma_nv = StringVar()
ten_nv = StringVar()
don_vi = StringVar()
chuc_danh = StringVar()
ngay_sinh = StringVar()
gioi_tinh = IntVar(value=1)
la_gi=IntVar(value=1)
so_cmnd = StringVar()
ngay_cap = StringVar()
noi_cap = StringVar()

khung = ttk.Frame(cua_so, padding="10")
khung.pack(fill="both", expand=True)

tieu_de = ttk.Label(khung, text="Thông tin nhân viên", font=("Arial", 14, "bold"))
tieu_de.grid(row=0, column=0, columnspan=2, sticky="w")

ttk.Label(khung, text="Mã *").grid(row=1, column=0, sticky="w")
ttk.Entry(khung, textvariable=ma_nv).grid(row=2, column=0)

ttk.Label(khung, text="Tên *").grid(row=1, column=1, sticky="w")
ttk.Entry(khung, textvariable=ten_nv).grid(row=2, column=1)

ttk.Label(khung, text="Đơn vị *").grid(row=3, column=0, sticky="w")
ttk.Entry(khung, textvariable=don_vi).grid(row=4, column=0, columnspan=2, sticky="we")

ttk.Label(khung, text="Chức danh").grid(row=5, column=0, sticky="w")
ttk.Entry(khung, textvariable=chuc_danh).grid(row=6, column=0, columnspan=2, sticky="we")

ttk.Label(khung, text="Ngày sinh").grid(row=1, column=2, sticky="w")
ttk.Entry(khung, textvariable=ngay_sinh).grid(row=2, column=2)

ttk.Label(khung, text="Giới tính").grid(row=1, column=3, sticky="w")
ttk.Radiobutton(khung, text="Nam", variable=gioi_tinh, value=1).grid(row=2, column=3)
ttk.Radiobutton(khung, text="Nữ", variable=gioi_tinh, value=2).grid(row=2, column=4)

ttk.Radiobutton(khung, text="Là khách hàng",variable=la_gi,value=1).grid(row=0,column=2)
ttk.Radiobutton(khung, text="Là nhà cung cấp",variable=la_gi,value=2).grid(row=0,column=3)

ttk.Label(khung, text="Số CMND").grid(row=3, column=2, sticky="w")
ttk.Entry(khung, textvariable=so_cmnd).grid(row=4, column=2)

ttk.Label(khung, text="Ngày cấp").grid(row=3, column=3, sticky="w")
ttk.Entry(khung, textvariable=ngay_cap).grid(row=4, column=3)

ttk.Label(khung, text="Nơi cấp").grid(row=5, column=2, sticky="w")
ttk.Entry(khung, textvariable=noi_cap).grid(row=6, column=2, columnspan=3, sticky="we")

ttk.Button(khung, text="Lưu thông tin", command=luu_tt).grid(row=8, column=0)
ttk.Button(khung, text="Sinh nhật ngày hôm nay", command=sinh_nhat_hom_nay).grid(row=8, column=1)
ttk.Button(khung, text="Xuất toàn bộ danh sách", command=xuat_excel).grid(row=8, column=2)


cua_so.mainloop()

