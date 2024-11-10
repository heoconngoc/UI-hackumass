import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Thêm import từ Pillow

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Handcut")
window_width = 470
window_height = 500  # Tăng chiều cao để chứa ảnh
root.geometry(f"{window_width}x{window_height}")
root.configure(bg="lightblue")

# Tắt khả năng thay đổi kích thước cửa sổ
root.resizable(False, False)

# Tạo frame để chứa cả ảnh và tiêu đề
header_frame = tk.Frame(root, bg="lightblue")
header_frame.pack(pady=20)

# Thêm ảnh "MLlogo_final.png" vào header_frame
logo_path = "MLlogo_final.png"  # Đảm bảo rằng ảnh "MLlogo_final.png" có sẵn trong thư mục chương trình
try:
    # Mở ảnh và thay đổi kích thước sao cho chiều cao ảnh bằng với chiều cao của tiêu đề
    logo_image = Image.open(logo_path)
    logo_height = 45  # Cỡ ảnh bằng với chiều cao của chữ "Handcut"
    logo_image = logo_image.resize((logo_height * logo_image.width // logo_image.height, logo_height))
    logo_photo = ImageTk.PhotoImage(logo_image)
    
    # Tạo Label cho ảnh và đặt trong header_frame
    logo_label = tk.Label(header_frame, image=logo_photo, bg="lightblue")
    logo_label.grid(row=0, column=0, padx=10, pady=5)  # Đặt ảnh vào cột đầu tiên của frame
    
except Exception as e:
    print(f"Error loading image: {e}")

# Thêm tiêu đề "Handcut" vào header_frame
title_label = tk.Label(header_frame, text="Handcut", font=("Arial", 24, "bold"), bg="lightblue", fg="black")
title_label.grid(row=0, column=1, padx=10, pady=5)  # Đặt chữ vào cột thứ hai của frame

# Tạo canvas để hỗ trợ cuộn toàn màn hình
canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

# Tạo scrollbar cho canvas
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Cấu hình canvas để sử dụng scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Tạo một frame bên trong canvas để chứa các widget
inner_frame = tk.Frame(canvas, bg="lightblue")

# Đặt nội dung frame vào canvas
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Danh sách các giá trị dropdown
dropdown_values1 = ["Option 1A", "Option 1B", "Option 1C", "Option 1D", "Option 1E", "Option 1F", "Option 1G", "Option 1H", "Option 1I", "Option 1J"]
dropdown_values2 = ["Option 2A", "Option 2B", "Option 2C", "Option 2D", "Option 2E", "Option 2F", "Option 2G", "Option 2H", "Option 2I", "Option 2J"]
dropdown_values3 = ["Option 3A", "Option 3B", "Option 3C", "Option 3D", "Option 3E", "Option 3F", "Option 3G", "Option 3H", "Option 3I", "Option 3J"]
dropdown_values4 = ["Option 4A", "Option 4B", "Option 4C", "Option 4D", "Option 4E", "Option 4F", "Option 4G", "Option 4H", "Option 4I", "Option 4J"]
dropdown_values5 = ["Option 5A", "Option 5B", "Option 5C", "Option 5D", "Option 5E", "Option 5F", "Option 5G", "Option 5H", "Option 5I", "Option 5J"]
dropdown_values6 = ["Option 6A", "Option 6B", "Option 6C", "Option 6D", "Option 6E", "Option 6F", "Option 6G", "Option 6H", "Option 6I", "Option 6J"]
dropdown_values7 = ["Option 7A", "Option 7B", "Option 7C", "Option 7D", "Option 7E", "Option 7F", "Option 7G", "Option 7H", "Option 7I", "Option 7J"]
dropdown_values8 = ["Option 8A", "Option 8B", "Option 8C", "Option 8D", "Option 8E", "Option 8F", "Option 8G", "Option 8H", "Option 8I", "Option 8J"]
dropdown_values9 = ["Option 9A", "Option 9B", "Option 9C", "Option 9D", "Option 9E", "Option 9F", "Option 9G", "Option 9H", "Option 9I", "Option 9J"]
dropdown_values10 = ["Option 10A", "Option 10B", "Option 10C", "Option 10D", "Option 10E", "Option 10F", "Option 10G", "Option 10H", "Option 10I", "Option 10J"]

# Tạo 5 legend và dropdowns cho cột 1
for i in range(5):
    legend = tk.Label(inner_frame, text=f"Legend {i+1}", font=("Arial", 14, "bold"), fg="blue", bg="lightblue", bd=1, relief="solid", padx=5, pady=5)
    legend.grid(row=i*2, column=0, padx=10, pady=5, sticky="w")
    dropdown = ttk.Combobox(inner_frame, values=globals()[f"dropdown_values{i+1}"], foreground="black")
    dropdown.grid(row=i*2+1, column=0, padx=10, pady=5, sticky="w")

# Tạo 5 legend và dropdowns cho cột 2
for i in range(5, 10):
    legend = tk.Label(inner_frame, text=f"Legend {i+1}", font=("Arial", 14, "bold"), fg="blue", bg="lightblue", bd=1, relief="solid", padx=5, pady=5)
    legend.grid(row=(i-5)*2, column=1, padx=10, pady=5, sticky="w")
    dropdown = ttk.Combobox(inner_frame, values=globals()[f"dropdown_values{i+1}"], foreground="black")
    dropdown.grid(row=(i-5)*2+1, column=1, padx=10, pady=5, sticky="w")

# Căn giữa cả hai cột
inner_frame.grid_columnconfigure(0, weight=1)
inner_frame.grid_columnconfigure(1, weight=1)

# Cập nhật kích thước của inner_frame để phù hợp với số lượng dropdowns
inner_frame.update_idletasks()

# Cập nhật vùng cuộn của canvas khi nội dung thay đổi
canvas.config(scrollregion=canvas.bbox("all"))

# Thêm sự kiện để cuộn bằng chuột
def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", on_mouse_wheel)



# Chạy ứng dụng
root.mainloop()
